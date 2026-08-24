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
├── requirements.txt
└── LICENSE
```

## Zajednička priprema

Sve komande se pokreću iz korena repozitorijuma:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
```

## Pokretanje hemijskog dela

```powershell
.\.venv\Scripts\python -m mkdocs serve -f chemistry-foundations/mkdocs.yml
```

## Pokretanje ML/AI dela

```powershell
.\.venv\Scripts\python -m mkdocs serve -f ml-ai-strategy/mkdocs.yml
```

MkDocs zatim u terminalu prikaže lokalnu adresu sajta, podrazumevano `http://127.0.0.1:8000`. Ako oba dela treba da rade istovremeno, drugom se može zadati drugi port, na primer:

```powershell
.\.venv\Scripts\python -m mkdocs serve -f ml-ai-strategy/mkdocs.yml -a 127.0.0.1:8001
```

Repozitorijum ne sadrži dostavljene fakultetske fajlove, CSD izvoze ni white paper. Jedini verzionisani CIF je ručno napravljen sintetički primer namenjen učenju.
