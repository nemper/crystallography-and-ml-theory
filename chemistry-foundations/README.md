# 2CDC - hemijske osnove za strukturnu pretragu

Privatna, projektno usmerena knjiga za ML inženjera koji kreće od nule i treba da projektuje dve aplikacije nad malim molekulskim kristalnim strukturama:

1. brzu pretragu velike strukturne baze po sličnosti sa ulaznim CIF-om;
2. precizno poređenje svih parova u manjem skupu CIF fajlova.

Knjiga objašnjava samo hemiju, kristalografiju i cheminformatiku koje utiču na te zadatke. Svaka celina sadrži intuitivni model, formalnu definiciju, primer vezan za dostavljene fajlove, tipičnu zamku, praktičnu vežbu i proveru znanja.

Plan je uređen prema preduslovima i proverljivim ishodima znanja. Posebno razdvaja sastav, molekulski graf, koordinaciono okruženje, konformaciju, kristalno pakovanje i intermolekulske interakcije, jer ne postoji jedna univerzalna strukturna sličnost.

## Lokalno pokretanje

Iz korena repozitorijuma:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m mkdocs serve -f chemistry-foundations/mkdocs.yml
```

Zatim otvoriti adresu koju prikaže MkDocs, podrazumevano `http://127.0.0.1:8000`.

## Važno o izvornim podacima

Repozitorijum namerno ne sadrži white paper, CSD izvoze, ConQuest `.cqs` upite niti dostavljene CIF/MOL/MOL2 fajlove. Jedini verzionisani `.cif` je ručno napisan, sintetički teaching fixture u `chemistry-foundations/docs/assets/open/tutorial-minimal.cif`; ne sadrži eksperimentalne ni CSD podatke. CSD Portfolio i iz njega izvedeni podskupovi podležu CCDC licenci i ne smeju se redistribuirati bez odgovarajućeg odobrenja. Dostavljene lokalne kopije tretiraju se kao restricted dok se sa fakultetom ne potvrde owner/controller, dozvoljene operacije i odobreni data plane.

## Status validacije

Sadržaj je izveden iz lokalnih projektnih artefakata i proveravan prvenstveno prema IUCr, IUPAC i CCDC dokumentaciji, standardima i originalnim radovima. [Validacioni audit](docs/referenca/validacioni-audit-2026-08-23.md) beleži tri nezavisna pregleda, anonimizovano glasanje, jedinu brojčanu korekciju, zatvorene rupe i preostale neizvesnosti. Stranica `Izvori i metod validacije` razdvaja normativne izvore, primarne radove i didaktičke udžbenike.
