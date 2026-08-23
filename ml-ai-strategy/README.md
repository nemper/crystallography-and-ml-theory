# 2CDC ML/AI Strategy

Privatna, evidence-driven dokumentacija za izbor ML/AI algoritama u dve 2CDC aplikacije:

1. globalna pretraga CSD struktura na osnovu jednog CIF-a;
2. precizno poređenje uploadovanog skupa CIF fajlova, svaki sa svakim.

Ovaj repozitorijum je odvojen od kursa hemije. Ne sadrži fakultetske fajlove, CSD izvode ni white paper.

## Lokalno pokretanje

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m mkdocs serve
```
