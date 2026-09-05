# 2CDC dokumentacija za učenje

Ovaj repozitorijum sadrži dva odvojena, ali međusobno usklađena dokumentaciona dela:

- [Hemijske osnove](chemistry-foundations/docs/index.md) — hemija, kristalografija i cheminformatika relevantne za 2CDC;
- [ML/AI strategija](ml-ai-strategy/docs/index.md) — algoritamske porodice, reprezentacije, evaluacija i ML/AI preduslovi relevantni za ista dva problema.

Oba dela ostaju u istom repozitorijumu i imaju zasebne MkDocs konfiguracije. Svi nastavni fajlovi leže neposredno u odgovarajućem `docs/` folderu, bez tematskih podfoldera. Zajedničke Python zavisnosti, virtuelno okruženje i statički runtime resursi nalaze se u korenu repozitorijuma.

## Struktura

```text
crystallography-and-ml-theory/
├── chemistry-foundations/
│   ├── docs/
│   └── mkdocs.yml
├── ml-ai-strategy/
│   ├── docs/
│   └── mkdocs.yml
├── site-assets/
├── scripts/
│   └── serve_docs.py
├── requirements.txt
└── LICENSE
```

## Zajednička priprema

Sve komande se pokreću iz korena repozitorijuma:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
```

## Zajedničko lokalno pokretanje — preporučeno

```powershell
.\.venv\Scripts\python scripts/serve_docs.py
```

Otvorite `http://127.0.0.1:8000/` i izaberite kurs. Skripta izgradi oba dela u `.local-site/chemistry-foundations/` i `.local-site/ml-ai-strategy/`, pa pokrene server dostupan samo na ovom računaru. Nastavni linkovi između dva kursa tada vode na upravo izgrađenu lokalnu teoriju i učitavaju drugi kurs u istom tabu, sa njegovom navigacijom i pretragom. Ostali spoljni linkovi, uključujući naučne izvore i poreklo sadržaja, ostaju nepromenjeni. Izvorni Markdown fajlovi se ne menjaju.

Server se zaustavlja sa `Ctrl+C`. Izgradnja se obavlja pri pokretanju; posle izmene teorije zaustavite i ponovo pokrenite skriptu. Drugi port ili samo izgradnja bez servera:

```powershell
.\.venv\Scripts\python scripts/serve_docs.py --port 8001
.\.venv\Scripts\python scripts/serve_docs.py --build-only
.\.venv\Scripts\python scripts/serve_docs.py --build-only --output-dir .local-site --port 8000
```

`--output-dir` može biti nov ili prazan folder, odnosno izlaz prethodno napravljen ovom skriptom. Skripta odbija izvorne foldere i njihove nadfoldere; osvežava samo svoja označena izlazna podstabla kurseva. `.local-site/` je izuzet iz verzionisanja. Ako izaberete drugi izlaz, sami obezbedite da se generisani fajlovi ne dodaju među izvorne fajlove projekta. Skripta ne instalira pakete i ne objavljuje sajt.

Izgrađene fajlove pregledajte preko HTTP servera na portu zadatom pri izgradnji; `site_url` oba kursa koristi taj port i njihov podfolder. Za naknadno posluživanje rezultata `--build-only` komande na podrazumevanom portu:

```powershell
.\.venv\Scripts\python -m http.server 8000 --bind 127.0.0.1 --directory .local-site
```

## Pojedinačno pokretanje hemijskog dela

```powershell
.\.venv\Scripts\python -m mkdocs serve -f chemistry-foundations/mkdocs.yml
```

## Pojedinačno pokretanje ML/AI dela

```powershell
.\.venv\Scripts\python -m mkdocs serve -f ml-ai-strategy/mkdocs.yml
```

MkDocs zatim u terminalu prikaže lokalnu adresu sajta, podrazumevano `http://127.0.0.1:8000`. Ako oba dela treba da rade istovremeno, drugom se može zadati drugi port, na primer:

```powershell
.\.venv\Scripts\python -m mkdocs serve -f ml-ai-strategy/mkdocs.yml -a 127.0.0.1:8001
```

Pojedinačni `mkdocs serve` automatski obnavlja taj kurs pri izmenama, ali ne obrađuje međukursne nastavne linkove: oni otvaraju GitHub kopiju drugog kursa, koja može biti starija od lokalnih izmena. Za čitanje oba konačna lokalna kursa koristite zajednički pokretač iznad.

Repozitorijum ne sadrži dostavljene fakultetske fajlove, CSD izvoze ni white paper. Jedini verzionisani CIF je ručno napravljen sintetički primer namenjen učenju.
