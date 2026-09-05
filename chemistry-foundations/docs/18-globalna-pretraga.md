# 18. Globalna pretraga: teorijski okvir

**Cilj prve aplikacije:** korisnik učitava jedan CIF, zadaje filtere i dobija rangirane, objašnjene CSD kandidate sa jasno navedenim nivoom sličnosti, kvalitetom i pravima pristupa.

Ovo nije „jedan embedding + vector DB“. Pouzdana pretraga je kaskada hemijskih i kristalografskih prikaza.

## 18.1 Značenje pre modela

Različita značenja pretrage mogu se razložiti kroz sledeća pitanja:

| Pitanje | Primer mogućeg odgovora |
|---|---|
| objekat pretrage | glavni ligand / ceo coordination entity / puna crystal form |
| relevantnost | isti scaffold, sličan metal environment, sličan packing… |
| obavezne razlike | charge, stereo, metal, solid form, disorder |
| filter semantika | element u formuli vs koordinisan metal |
| evidence | matched subgraph, atom mapping, score components |
| granica zaključka | nema pouzdanog grafa; nema 3D; ambiguous disorder |

Odvojena značenja sličnosti su naučno transparentnija od neobjašnjivog univerzalnog pojma „similar“. Ovo je semantičko razlaganje problema, a ne specifikacija korisničkog interfejsa.

## 18.2 Naučna dovoljnost ulaza

Pre pretrage mora biti jasno koji je CIF data block predmet analize; da li su formula, atom sites i komponente konzistentni; da li ćelija, simetrija, occupancy/disorder i dostupne koordinate podržavaju traženi nivo sličnosti; šta je direktno, izvedeno ili dodeljeno; i koje verzije i upozorenja ograničavaju zaključak. Veliki refleksioni ili tekstualni blokovi jesu deo izvora, ali nisu samim tim hemijska reprezentacija niti signal za ML sličnost.

## 18.3 Filter semantika

Filter „metal: Cu“ nema jedno značenje. Može označavati, na primer:

- Cu prisutan u punoj entry formuli;
- Cu u coordination entity;
- Cu direktno koordinisan ciljnom ligandu;
- Cu kao counterion/odvojena komponenta;
- exclude/include solvents and coformers;
- required/forbidden elements u parent graph-u ili punom sastavu;
- kriterijum kvaliteta, 3D dostupnosti, disorder-a ili temperature.

Objašnjiva pretraga zato mora razlikovati scope uslova i učinak svakog uslova na populaciju kandidata. To je zahtev za značenje rezultata, ne predlog konkretnog UI-ja.

## 18.4 Višeslojne reprezentacije

| Sloj informacije | Primer sadržaja | Naučna uloga |
|---|---|---|
| provenance | refcode, release, hash, permission | identitet i audit |
| metadata | elementi, formula, components, quality flags | jeftini exact/range filteri |
| 2D graph | fingerprint + substructure index | širok candidate recall |
| coordination | metal, donor set, CN/geometry features | complexes search |
| 3D molecule | conformer/shape features | geometric rerank |
| crystal | standardizovana ćelija + packing/contact reprezentacija | solid-form search |

Promena standardizacije ili feature pravila menja semantiku reprezentacije. Zato rezultat ima smisla samo uz poznatu verziju pravila, a score-ovi izvedeni pod nekompatibilnim pravilima ne treba da se tumače kao ista veličina.

## 18.5 Candidate generation i reranking

Jedna **ilustrativna, nenormativna** kaskada može sadržati sledeće uloge:

- ograničavanje dozvoljenog korpusa i exact metadata uslova;
- exact ili substructure proveru kada je ona deo pitanja;
- visok-recall candidate generation;
- preciznije graph, coordination, geometry ili packing poređenje kada su potrebni podaci dostupni;
- kalibraciju i objašnjenje rezultata.

Konkretan sistem može ove uloge organizovati drugačije. Bitna teorijska razlika je da jeftino generisanje kandidata, precizno poređenje i konačna procena relevantnosti nisu isti zadatak.

ANN candidate generation i konačni proizvod ne mere se istim recall-om:

- **ANN candidate recall@N prema exhaustive exact oracle-u iste reprezentacije i metrike** meri koliko kandidata iz referentnog skupa, dobijenog nad istim dozvoljenim korpusom, uz iste hard filtere i istu tie/self-match politiku, preživi aproksimativnu fazu. To je test gubitka infrastrukture; exact skup nije samim tim ekspertski ground truth relevantnosti.
- **End-to-end recall@k prema ekspertskoj relevantnosti** meri koliko ekspertski potvrđenih relevantnih zapisa završi u prvih `k` rezultata posle svih filtera, candidate generation-a i reranking-a. To je metrika naučnog/proizvodnog claim-a.

Za obe metrike unapred fiksirati `N`/`k`, korpus, denominator i postupanje sa upitima bez relevantnog zapisa. Brzina bez izmerene propuštenosti nije validacija, ali ni visok ANN candidate recall ne dokazuje da je konačni ranking hemijski relevantan.

## 18.6 Rezultat nije samo lista identifikatora

Stručna interpretacija jednog pogotka zahteva više vrsta konteksta: identitet i sastav, poreklo i dozvoljeni obim, značenje ranga, obim mapiranog grafa, koordinacioni i 3D dokaz kada je primenljiv, packing/interakcione signale, kvalitet ulaza i razloge zbog kojih je neki nivo ostao neocenjen. Ovo su kategorije dokaza, ne fiksna result schema.

Lokalni `dve funkcionalnosti.txt` traži i mogućnost preuzimanja CIF-a pogotka. Naučno i podatkovno mora biti jasno da li se preuzima originalni deponovani CIF ili pojednostavljeni/izvedeni eksport, iz koje verzije izvora i u kom dozvoljenom obimu. Rangirani pogodak ili dostupnost javnog metadata zapisa sami po sebi ne daju pravo redistribucije njegovog CIF-a.

Score bez explanation-a ne omogućava stručnjaku da otkrije da je rezultat visok samo zbog velikog zajedničkog aromatičnog dela, a ključni metal environment različit.

## 18.7 Failure-aware ponašanje

| Problem | Naučna posledica |
|---|---|
| nema ćelije/symmetry | 2D zaključak može ostati moguć, ali packing nema potreban dokaz |
| nepoznate/`un` veze | fingerprint/MCS zavise od low-confidence grafa |
| više komponenti | claim zavisi od izbora komponente i full-crystal konteksta |
| disorder | alternative i occupancies nisu skup nezavisnih punih atoma |
| nepoznata stereo | nema dokaza za exact poklapanje definisane stereokemije |
| metal connectivity ambiguous | postoji kandidat ili neodređenost, ne potvrđen coordinated match |
| out-of-license rezultat | licenca ograničava koji dokaz i sadržaj sme biti vidljiv |

## 18.8 Skaliranje, verzije i poreklo

Na velikom korpusu originalni izvori, standardizovani prikazi, numeričke reprezentacije i indeksi nemaju isti epistemološki status. Indeks je izvedena i potencijalno zastarela projekcija, ne izvor istine. Promena baze, standardizacije ili metrike može promeniti skup kandidata i rang, pa poređenje rezultata zahteva poznato poreklo i kompatibilne verzije. Licencna ograničenja pritom važe i za izvedene reprezentacije i izlaze, ne samo za originalni CIF.

## 18.9 Provera znanja

1. Zašto vector database nije source of truth?
2. Šta znači Cu filter na četiri različita nivoa?
3. Kada se packing reranker mora preskočiti?
4. Kako meriš kvalitet ANN candidate generation-a?
5. Zašto svaki indeks ima representation version?

??? success "Odgovori"
    1. Sadrži izvedene, verzionisane i potencijalno lossy features; original/provenance žive drugde.  
    2. Prisustvo u entry formuli, u entity-ju, direktna koordinacija ligandu ili odvojena komponenta/counterion.  
    3. Kada nema validne ćelije/symmetry/3D ili je quality/representation nedovoljna.  
    4. Recall-om prema exhaustive exact oracle-u iste reprezentacije, metrike, korpusa, hard filtera i tie/self-match politike, ukupno i po slice-ovima.  
    5. Promena hemijskog modela/parametara menja features i score semantiku.

**Kriterijum prolaza:** možeš da odbraniš značenje ulaza, filtera, candidate-generation-a, preciznog poređenja i konačne relevantnosti pred hemičarem, kristalografom, ML inženjerom i licencnim vlasnikom.
