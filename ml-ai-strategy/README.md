# 2CDC ML/AI Strategy

Privatna, evidence-driven dokumentacija o algoritamskim porodicama relevantnim za dva 2CDC problema:

1. globalna pretraga CSD struktura na osnovu jednog CIF-a;
2. precizno poređenje uploadovanog skupa CIF fajlova, svaki sa svakim.

Ovaj poddirektorijum je poseban dokumentacioni deo istog repozitorijuma u kojem se nalazi i kurs hemije. Ne sadrži fakultetske fajlove, CSD izvode ni white paper.

## Lokalno pokretanje

Iz korena repozitorijuma, nakon zajedničke instalacije zavisnosti:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m mkdocs serve -f ml-ai-strategy/mkdocs.yml
```
