# Kako se koristi ova knjiga

## Ne čitaj pasivno

Hemijski pojmovi postaju korisni tek kada ih povežeš sa reprezentacijom podataka. Za svaku lekciju radi sledeći ciklus:

1. pročitaj intuitivni deo bez memorisanja;
2. zatvori stranicu i sopstvenim rečima objasni pojam u dve rečenice;
3. pronađi taj pojam u lokalnom CIF/MOL/MOL2 primeru;
4. uradi proveru bez gledanja rešenja;
5. zapiši jednu posledicu za dizajn aplikacije.

Ako ne možeš da odgovoriš na pitanje "koju grešku bi ovaj pojam sprečio u modelu?", gradivo još nije postalo operativno.

## Oznake prioriteta

| Oznaka | Značenje |
|---|---|
| **MORAŠ** | potrebno pre prve ozbiljne odluke o reprezentaciji ili metrici |
| **TREBA** | potrebno pre evaluacije prototipa i razgovora sa hemičarima/kristalografima |
| **KASNIJE** | korisno za istraživački rad, ali nije blokator prvog validnog sistema |

Knjiga je već poređana tako da se pojmovi uvode pre upotrebe. Nemoj preskakati module 1-3 i 7-10. Modul preskoči samo ako položiš njegovu ulaznu proveru.

## Kriterijum za prelazak

Prelazak na sledeću celinu zasniva se na izlaznim sposobnostima, ne na broju pročitanih stranica. Pređi dalje kada možeš samostalno da demonstriraš navedeni ishod, tačno uradiš odgovarajuću proveru ili laboratorijsku vežbu i objasniš ključne zamke. Ako neki ishod nije stabilan, vrati se na njegov preduslov u [planu učenja](plan-ucenja.md#zavisnosti-modula).

## Kako se koriste spoljni linkovi

Postoje tri vrste izvora:

- **normativni** - IUCr CIF rečnici i IUPAC terminologija; njima verujemo za definicije;
- **primarni naučni** - originalni radovi za algoritme poput COMPACK-a ili ECFP-a;
- **didaktički** - recenzirani otvoreni udžbenici za dodatne primere i vežbu.

Ne moraš čitati svaki izvor od početka do kraja. Link "produbi" označava deo koji vredi otvoriti samo ako objašnjenje u knjizi nije dovoljno ili kada donosiš produkcionu odluku.

## Lokalni fajlovi

Vežbe pretpostavljaju ovu strukturu na računaru:

```text
2CDC/
├── CCDC_white_paper_sharpen.pdf
├── cu_n14_a.cif
├── N14.mol
├── N14.mol2
├── dve funkcionalnosti.txt
├── Pretrage CSD/
│   ├── search1.*
│   └── search2.*
└── crystallography-and-ml-theory/
```

Originale tretiraj kao **read-only**. Za eksperimente pravi kopije u sopstvenom privremenom direktorijumu. Ne uploaduj CSD izvoze u javne servise za vizuelizaciju ili validaciju dok se ne proveri licenca i poverljivost.

## Pravilo za pojednostavljenja

U uvodnoj hemiji modeli su namerno uprošćeni. Lewisova struktura, hibridizacija, parcijalno naelektrisanje i "tip veze" nisu fotografije elektronske gustine; to su korisne reprezentacije sa granicama. Svako poglavlje zato razdvaja:

- **posmatrano** - eksperimentalni podaci;
- **izvedeno** - vrednost izračunata iz podataka;
- **dodeljeno** - hemijska interpretacija softvera ili kustosa;
- **pretpostavljeno** - radna hipoteza modela.

Ta razlika je jedna od najvažnijih navika za ovaj projekat.
