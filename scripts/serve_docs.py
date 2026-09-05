#!/usr/bin/env python3
"""Build both courses and serve their local, cross-linked documentation."""

from __future__ import annotations

import argparse
from functools import partial
from html import escape, unescape
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import logging
import os
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import quote, unquote, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
COURSES = {
    "chemistry-foundations": "Hemijske osnove",
    "ml-ai-strategy": "ML/AI strategija",
}
MARKER = ".ccdc-generated-site"
GITHUB_PREFIX = "/nemper/crystallography-and-ml-theory/blob/main/"
ANCHOR = re.compile(r"<a\b[^>]*>", re.IGNORECASE)
HREF = re.compile(r"(?<![\w-])href\s*=\s*([\"'])(.*?)\1", re.IGNORECASE)
TARGET = re.compile(r"(?<![\w-])target\s*=\s*([\"'])(.*?)\1", re.IGNORECASE)


def inside(path: Path, parent: Path) -> bool:
    return path == parent or parent in path.parents


def check_output(output: Path) -> None:
    """Refuse source directories and ancestors before any build can clean files."""
    if inside(ROOT, output):
        raise ValueError("Izlaz ne sme biti koren projekta niti njegov nadfolder.")
    protected = [ROOT / name for name in COURSES]
    protected += [ROOT / "scripts", ROOT / "site-assets", ROOT / ".venv"]
    protected += [ROOT.parent / "2CDC"]
    for source in protected:
        source = source.resolve()
        if inside(output, source) or inside(source, output):
            raise ValueError(f"Izlaz se preklapa sa izvornim folderom: {source}")
    if output.exists() and not output.is_dir():
        raise ValueError(f"Izlaz nije folder: {output}")


def check_generated(directory: Path, label: str) -> None:
    """Only an empty directory or this launcher's marked output may be reused."""
    if not directory.exists():
        return
    if not directory.is_dir():
        raise ValueError(f"Očekivan je izlazni folder: {directory}")
    marker = directory / MARKER
    expected = f"{ROOT}\n{label}\n"
    if any(directory.iterdir()) and (
        not marker.is_file() or marker.read_text(encoding="utf-8") != expected
    ):
        raise ValueError(
            f"Folder nije prepoznat kao izlaz ove skripte: {directory}. "
            "Izaberite nov ili prazan --output-dir."
        )
    # A copied/junction-linked subtree must never become a recursive clean target.
    for current, directories, files in os.walk(directory, followlinks=False):
        for name in directories + files:
            item = Path(current) / name
            if item.is_symlink() or item.resolve() != item.absolute():
                raise ValueError(f"Izlaz sadrži simboličku vezu/junction: {item}")


def mark_generated(directory: Path, label: str) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / MARKER).write_text(f"{ROOT}\n{label}\n", encoding="utf-8")


def local_teaching_url(url: str, page: Path, configs: dict) -> str:
    """Map only known course Markdown links; leave all other URLs untouched."""
    from mkdocs.structure.files import File

    parsed = urlsplit(unescape(url))
    if parsed.scheme != "https" or parsed.netloc != "github.com":
        return url
    if not parsed.path.startswith(GITHUB_PREFIX):
        return url
    parts = unquote(parsed.path[len(GITHUB_PREFIX):]).split("/")
    if len(parts) < 3 or parts[0] not in COURSES or parts[1] != "docs":
        return url
    relative = PurePosixPath(*parts[2:])
    if relative.suffix != ".md":
        return url
    if any(part in ("", ".", "..") or "\\" in part for part in parts[2:]):
        raise ValueError(f"Neispravna nastavna putanja: {url}")
    config = configs[parts[0]]
    source = (Path(config.docs_dir) / relative).resolve()
    if not inside(source, Path(config.docs_dir).resolve()) or not source.is_file():
        raise ValueError(f"Nastavni link nema lokalni Markdown cilj: {url}")
    file = File(
        relative.as_posix(), config.docs_dir, config.site_dir, config.use_directory_urls
    )
    target = Path(file.abs_dest_path).resolve()
    if not inside(target, Path(config.site_dir).resolve()) or not target.is_file():
        raise ValueError(f"Nastavni link nema izgrađen HTML cilj: {target}")
    local = quote(Path(os.path.relpath(target, page.parent)).as_posix(), safe="/")
    return escape(urlunsplit(("", "", local, parsed.query, parsed.fragment)), quote=True)


def rewrite_teaching_links(configs: dict) -> int:
    rewritten = 0
    for config in configs.values():
        for page in Path(config.site_dir).rglob("*.html"):
            original = page.read_text(encoding="utf-8")

            def replace_anchor(anchor: re.Match) -> str:
                def replace_href(href: re.Match) -> str:
                    nonlocal rewritten
                    url = href.group(2)
                    local = local_teaching_url(url, page, configs)
                    if local == url:
                        return href.group(0)
                    rewritten += 1
                    return f"href={href.group(1)}{local}{href.group(1)}"

                updated_anchor = HREF.sub(replace_href, anchor.group(0), count=1)
                if updated_anchor != anchor.group(0):
                    # Each course has its own theme state and search index. Material
                    # 9.7.7 skips instant navigation for links with a defined target:
                    # src/templates/assets/javascripts/integrations/instant/index.ts
                    # Use a normal same-tab load when crossing the course boundary.
                    target = TARGET.search(updated_anchor)
                    if target is None:
                        updated_anchor = updated_anchor[:-1] + ' target="_self">'
                    elif not target.group(2):
                        updated_anchor = TARGET.sub('target="_self"', updated_anchor, count=1)
                return updated_anchor

            updated = ANCHOR.sub(replace_anchor, original)
            if updated != original:
                page.write_text(updated, encoding="utf-8")
    return rewritten


def build_courses(output: Path, port: int) -> None:
    from mkdocs.commands.build import build
    from mkdocs.config import load_config

    check_output(output)
    check_generated(output, "shared")
    configs = {}
    # Validate both configurations and both clean targets before building either.
    for course in COURSES:
        destination = output / course
        if destination.resolve() != destination:
            raise ValueError(f"Izlaz kursa je simbolička veza/junction: {destination}")
        check_generated(destination, course)
        configs[course] = load_config(
            str(ROOT / course / "mkdocs.yml"),
            site_dir=str(destination),
            site_url=f"http://127.0.0.1:{port}/{course}/",
        )
    mark_generated(output, "shared")
    for course, config in configs.items():
        destination = Path(config.site_dir)
        mark_generated(destination, course)
        print(f"Izgradnja: {COURSES[course]}", flush=True)
        try:
            # MkDocs cleans only this verified, marked course output, never its parent.
            build(config)
        finally:
            mark_generated(destination, course)
    count = rewrite_teaching_links(configs)
    links = "\n".join(
        f'<li><a href="{course}/">{escape(title)}</a></li>'
        for course, title in COURSES.items()
    )
    (output / "index.html").write_text(
        '<!doctype html>\n<html lang="sr"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>2CDC — dva kursa</title><style>'
        'body{font:1.1rem/1.6 system-ui,sans-serif;max-width:48rem;margin:4rem auto;'
        'padding:0 1.5rem;color:#182540;background:#f7f9fc}'
        'a{color:#264f9e}li{margin:1rem 0}'
        '</style></head><body><main><h1>2CDC — dokumentacija za učenje</h1>'
        '<p>Hemija i ML/AI za razumevanje dve projektne funkcionalnosti.</p>'
        f'<ul>{links}</ul></main></body></html>\n',
        encoding="utf-8",
    )
    print(f"Izgrađeno: {output}\nLokalizovani nastavni linkovi: {count}", flush=True)


def main() -> int:
    # Windows redirected streams can default to an encoding without Serbian letters.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-only", action="store_true", help="Izgradi bez servera.")
    parser.add_argument(
        "--output-dir", type=Path, default=ROOT / ".local-site",
        help="Zajednički izlaz (podrazumevano: .local-site u korenu projekta).",
    )
    parser.add_argument("--port", type=int, default=8000, help="Lokalni port (8000).")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("--port mora biti između 1 i 65535")
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    output = args.output_dir.expanduser().resolve()
    try:
        build_courses(output, args.port)
        if args.build_only:
            return 0
        handler = partial(SimpleHTTPRequestHandler, directory=str(output))
        with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
            print(f"Otvorite http://127.0.0.1:{args.port}/ — Ctrl+C za kraj.", flush=True)
            server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer zaustavljen.")
    except ModuleNotFoundError as error:
        print(
            f"Nedostaje zavisnost: {error.name}. Pratite pripremu u README.md.",
            file=sys.stderr,
        )
        return 1
    except Exception as error:
        print(f"Greška: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
