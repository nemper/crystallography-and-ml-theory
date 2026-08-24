# Pitanja i odluke za kolege sa fakulteta

**Status:** završni pregled dostupnog korpusa, 24. avgust 2026.
**Namena:** jedna autoritativna lista nepoznanica koje fakultet treba da potvrdi pre specifikacije, evaluacije ili disertacionih tvrdnji. Ovo nije plan implementacije.

## Kako koristiti ovu stranu

Za svako pitanje treba zabeležiti:

| Polje | Šta se upisuje |
|---|---|
| status | `OPEN`, `ANSWERED`, `OUT_OF_SCOPE` ili `SUPERSEDED` |
| vlasnik odgovora | ime i uloga osobe koja ima ovlašćenje da odluči |
| odgovor | kratka, nedvosmislena odluka; po potrebi verzionisana definicija |
| dokaz | ugovor, SOP, screenshot, query manifest, primer, zapisnik ili drugi autoritativni prilog |
| važi od / verzija | datum i verzija odluke |
| uticaj | koji zahtev, skup podataka, evaluacija ili tvrdnja se odgovorom menja |

Prioriteti na ovoj strani znače:

- **BLOKIRA SPECIFIKACIJU** — bez odgovora nije poznato šta se gradi ili šta podaci znače;
- **PRE EVALUACIJE** — teorija može da se uči, ali rezultat ne može pošteno da se proglasi uspešnim;
- **USLOVNO** — pitanje se aktivira samo ako fakultet tu temu izričito uvede u scope.

!!! warning "White paper nije specifikacija dve aplikacije"
    White paper ne pominje 2CDC, DAP, Schiffove baze, `N14`, upload-CIF globalnu pretragu, all-pairs aplikaciju, Pinecone, Neo4j, gold/qrels niti doktorsku disertaciju. Kada pitanje nastaje iz briefa, CQS-a ili lokalnih fajlova, to je ispod eksplicitno označeno kao **nema direktne white-paper specifikacije**. White-paper strana se tada navodi samo ako daje relevantan problemski kontekst, nikada kao izmišljeni izvor zahteva.

## Referentni ključ za fizičke strane white paper-a

Brojevi su fizičke strane dostavljenog PDF-a, ne broj koji bi text extractor mogao da izvede iz nevidljivog sloja.

| Ključ | Fizička strana i tačan deo | Šta taj deo zaista podržava |
|---|---|---|
| `WP-03A` | p. 3, **Overview — Executive Summary**, prvi odlomak | vrednost kurirane interne strukturne baze povezane sa eksperimentalnim svojstvima |
| `WP-03B` | p. 3, drugi odlomak | provenance podataka i odnosi između tipova podataka |
| `WP-03C` | p. 3, četvrti odlomak | kvalitet, metadata, veze i „one source of truth“; svojstvo vezano za konkretnu formu |
| `WP-03D` | p. 3, poslednji odlomak | FL kao opšta mogućnost za saradnju bez centralizacije raw podataka |
| `WP-04A` | p. 4, prvi odlomak | solubility, stability i manufacturability kao mogući property target-i; FL motivacija |
| `WP-04B` | p. 4, drugi i treći odlomak | automatizovani tokovi, standardizacija, konzistentnost i pristup na skali |
| `WP-05` | p. 5, **Background**, sva tri odlomka | FAIR; silosi i legacy izvori; identifikatori, poreklo, metadata i verzije |
| `WP-06` | p. 6, **The Cost of Poor Data Management** | posledice loših podataka za odluke i AI/ML; nema 2CDC troškovnik |
| `WP-07` | p. 7, **Benefits of Adopting FAIR Data Principles**, naročito drugi i treći odlomak | javni CSD, proprietary podaci, solid form i povezivanje strukture sa physical/material property podacima |
| `WP-08A` | p. 8, **What Makes In-House Proprietary Data Useful?**, prvi i drugi odlomak | focused subsets i razlika javnog i internog hemijskog prostora |
| `WP-08B` | p. 8, treći i četvrti odlomak | kuracija, atom/bond typing, functional groups, jedinice/metadata i uporedivost konformacija |
| `WP-09A` | p. 9, prvi odlomak i Figure 2 | „usual/unusual“ geometrija u definisanom referentnom skupu |
| `WP-09B` | p. 9, drugi i treći odlomak | intermolekulske interakcije i prisutni/odsutni obrasci |
| `WP-10A` | p. 10, uvodni odlomak iznad naslova o structure/property odnosima | ConQuest, Mercury i CSD Python API kao vendor alati |
| `WP-10B` | p. 10, **The Importance of Managing Data and Structure/Property Relationships**, sva tri odlomka | crystallisation conditions, melting point, solubility i potreba da se property veže za molekul/formu i uslove |
| `WP-11` | p. 11, završetak istog odeljka | dobro strukturirani property podaci i njihov značaj za distribuirano/federativno modelovanje |
| `WP-12` | p. 12, **Adopting New Solutions and In-House Workflows** | automatizovani in-house tok, WebCSD, early-access i main database koncepti |
| `WP-13` | p. 13, **New Modern Interface for Managing Proprietary Structural Data** | Manage Databases, administracija ingest-a i statusa |
| `WP-14` | p. 14, nastavak istog odeljka | CSD-Editor, review/korekcije i automatska database-ready konverzija |
| `WP-15` | p. 15, **Leveraging Federated Learning to Unlock Insights from Proprietary Data** | IP/confidentiality/regulatory motivacija i osnovni FL mehanizam |
| `WP-16` | p. 16, nastavak FL odeljka | kvalitet i usklađenost lokalnih podataka, governance i full control nad proprietary bazom |
| `WP-17` | p. 17, **Case Study: Using Proprietary Data to Make Polymorph Risk Assessment More Reliable** | javni/proprietary coverage i polymorph-risk problemski okvir |
| `WP-18` | p. 18, nastavak case study-ja | Mogul, packing comparison i hydrogen-bond propensity kao kombinovani indikatori za istragu |
| `WP-19` | p. 19, **Conclusion**, drugi i treći odlomak | centralno upravljanje; web i programmatic pristup; podaci iza firewall-a |
| `WP-20` | p. 20, testimonial i završni odlomak | mišljenje i marketinški zaključak, ne nezavisna specifikacija ili benchmark |

Fizičke strane 1–2 su naslov i sadržaj; p. 21 je bibliografija, a p. 22 kontakt. Nevidljivi docking tekst na p. 1–2 je PDF-ingest incident, ne tema projekta.

## Lokalni izvori

| Ključ | Izvor | Dokazna uloga |
|---|---|---|
| `L-BRIEF-1` | `dve funkcionalnosti.txt`, prva funkcionalnost | upload jednog CIF-a, pretraga dozvoljenog CSD korpusa, filteri, skala i lista rezultata/download |
| `L-BRIEF-2` | isti fajl, druga funkcionalnost | upload skupa, svi neuređeni parovi \(n(n-1)/2\), veća preciznost i detaljnije ose poređenja |
| `L-CQS-1` | `1 - Sifove baze DAP.cqs` | sačuvani 18-atomski povezani DAP-bis(iminski) query motiv |
| `L-CQS-2` | `2 - Kompleksi sa DAP SB.cqs` | isti motiv plus nepovezani `4M` atom; metal presence, ne dokazana koordinacija |
| `L-EXPORT` | `search1/search2` CIF, MOL2, SD i SMILES izvozi | stvarni lokalni rezultat, coverage, format-loss, missingness i selection bias |
| `L-N14` | `cu_n14_a.cif`, `N14.mol`, `N14.mol2` | jedan cross-format primer sa nepotvrđenim poslovnim identitetom i lineage-om |
| `L-AUDIT` | [validacioni audit](validacioni-audit-2026-08-23.md) i [registar tvrdnji](registar-tvrdnji.md) | reprodukovane činjenice, otvorena CQS runtime i DAP-scope neizvesnost |

## Činjenice koje ne treba ponovo postavljati kao otvorena pitanja

Ovo je već dokazano dostupnim bajtovima; fakultet treba da potvrdi **nameru i autoritet**, ne da glasa o reprodukovanoj činjenici:

- `search1` ima 2.110 entry-ja, `search2` 2.038 i `search2` je redosledno očuvan strogi podskup; razlika je 72;
- nepovezani `4M` u drugom CQS-u dokazuje samo metal negde u istom CSD entry-ju, ne DAP–metal koordinaciju;
- sačuvani query tragovi navode ConQuest 2022.2.0 i CSD 5.43 sa March/June 2022 segmentima; 2026 temp/save trag nije CSD release iz 2026;
- u sačuvanom CQS objektu `require_3d` nije uključen, a maksimalni R nije zadat; kompatibilni runtime i dalje treba da potvrdi GUI/default semantiku;
- App2 brief već propisuje broj neuređenih parova \(n(n-1)/2\); otvoreni su limiti i značenje poređenja, ne formula;
- `cu_n14_a.cif` ne sadrži Cu atom; `Cu Kα` je izvor rendgenskog zračenja, ne sastav;
- white paper obrađuje polymorph-risk i FL, ali ih brief ne propisuje kao treću i četvrtu aplikaciju.

---

## I. Autoritet, normativni scope i uloge

### Q01 — Normativni red izvora

**Prioritet:** BLOKIRA SPECIFIKACIJU

Koji je zvanični red autoriteta između briefa, odluka naučnog tima, CQS naziva, stvarnih CQS constraints, CCDC dokumentacije, white paper-a i budućih zapisnika? Da li je `dve funkcionalnosti.txt` jedina trenutna specifikacija dve aplikacije, a white paper samo problemski kontekst? Ko rešava konflikt i kako se odluka verzioniše?

**Zašto:** naziv artefakta, mašinski query i marketinško-strateški dokument mogu opisivati različite stvari.

**White paper:** nema projektnu governance specifikaciju; `WP-03B` i `WP-03C` samo motivišu provenance i jedan izvor istine.
**Lokalno:** `L-BRIEF-1`, `L-BRIEF-2`, `L-CQS-1`, `L-CQS-2`.

### Q02 — Vlasnici odluka i potpis

**Prioritet:** BLOKIRA SPECIFIKACIJU

Ko po imenu i ulozi odobrava: (a) hemijsku/koordinacionu semantiku, (b) kristalografsku semantiku, (c) product scope i acceptance, (d) podatke/licence/bezbednost, (e) gold i evaluaciju i (f) disertacione/publikacione tvrdnje? Ko je zamena ako vlasnik nije dostupan?

**White paper:** nema odgovor; `WP-03C`, `WP-12`, `WP-13` i `WP-14` samo pokazuju zašto kvalitet, review i odgovornost postoje.
**Lokalno:** `L-AUDIT` — sadašnji materijal eksplicitno ne zamenjuje formalni stručni i licencni review.

### Q03 — Odnos dve aplikacije

**Prioritet:** BLOKIRA SPECIFIKACIJU

Da li su ovo dva odvojena proizvoda, dva workflow-a istog sistema ili dve istraživačke funkcije? Ko su korisnici svake, koju odluku donose i koja posledica nastaje ako je rezultat pogrešan? Da li jedna deli ulaz, identitet ili rezultate sa drugom?

**White paper:** nema 2CDC aplikacije niti ovaj product odnos.
**Lokalno:** `L-BRIEF-1`, `L-BRIEF-2`.

### Q04 — Uloga DAP/CQS/search/N14 materijala

**Prioritet:** BLOKIRA SPECIFIKACIJU

Da li su DAP, oba CQS-a, `search1/search2` i N14 samo nastavni/forenzički primeri, regression fixtures, pilot slice, acceptance skup, populacija disertacije ili deo punog domena? Ako imaju različite uloge, navesti svaku posebno. Dostavljeni brief već postavlja App1 kao globalnu pretragu dozvoljenog CSD korpusa: postoji li novija ovlašćena odluka koja to sužava, ili DAP materijal ostaje primer unutar šireg korpusa?

**White paper:** ne sadrži DAP, Schiff base, CQS ili N14; `WP-08A` samo pokazuje da focused subset nije isto što i ceo hemijski prostor.
**Lokalno:** `L-BRIEF-1`, `L-CQS-1`, `L-CQS-2`, `L-EXPORT`, `L-N14`.

### Q05 — Status Pinecone/Neo4j primera

**Status u dostupnom korpusu:** ANSWERED — brief ih navodi kao moguće primere, ne kao obavezujući stack.
**Prioritet:** USLOVNO — pitati samo ako postoji novija odluka koja nam nije dostavljena.

Postoji li novija ovlašćena odluka koja menja sadašnju premisu da su Pinecone i Neo4j samo ilustrativni primeri? Ako ne postoji, zabeležiti da konkretna tehnologija nije unapred propisana.

**White paper:** nema Pinecone, Neo4j niti propisan storage stack.
**Lokalno:** `L-BRIEF-1`.

## II. White-paper teme: required, optional ili out of scope

### Q06 — Proprietary/in-house baza

**Prioritet:** BLOKIRA SPECIFIKACIJU

Da li projekat stvarno uključuje fakultetsku ili partnersku proprietary strukturnu bazu pored CSD-a? Ako da: koji izvori, vlasnici, lokacije, populacije i dozvoljene veze sa javnim/licenciranim CSD podacima ulaze? Ako ne, eksplicitno označiti white-paper in-house scenario kao kontekst van scope-a.

**White paper:** `WP-03A`, `WP-07`, `WP-08A` i `WP-12`.
**Lokalno:** brief pominje CSD eksport, ali ne obećava proprietary in-house bazu.

### Q07 — Vendor lifecycle alati i tokovi

**Prioritet:** BLOKIRA SPECIFIKACIJU

Da li su WebCSD/on-site, early-access/main database, Manage Databases, CSD-Editor i database-ready conversion stvarni zahtevi, mogućnosti koje treba proveriti ili samo vendor primeri? Za svaki odgovoriti `REQUIRED`, `OPTIONAL` ili `OUT_OF_SCOPE`.

**White paper:** `WP-10A`, `WP-12`, `WP-13`, `WP-14`.
**Lokalno:** `L-AUDIT` navodi da institucijska dostupnost ovih mogućnosti nije potvrđena.

### Q08 — Structure–property scope

**Prioritet:** BLOKIRA SPECIFIKACIJU ako je property funkcija zahtev; inače USLOVNO

Da li App1/App2 ili disertacija uključuju melting point, solubility, stability, crystallisation conditions ili drugo svojstvo? Za svaki target tražiti: material/compound, konkretnu solid form/structure version, vrednost, jedinicu, uslove, metod, batch/sample, uncertainty, vreme dostupnosti i autoritet etikete.

**White paper:** `WP-03C`, `WP-04A`, `WP-10B`, `WP-11`.
**Lokalno:** `L-BRIEF-1` neodređeno kaže „prisustvo određenih osobina“, ali ne definiše property model.

### Q09 — Manufacturability

**Prioritet:** USLOVNO

Da li je manufacturability stvarni target ili samo primer iz white paper-a? Ako jeste, koji merljivi ishod, proces/protokol, oprema/site, batch, vremenski horizont, specifikacija i ground truth ga operationalizuju? Odgovor „manufacturable: da/ne“ bez tih uslova nije dovoljan.

**White paper:** `WP-04A`; `WP-04B` daje samo opšti kontekst automatizacije i skale, ne značenje manufacturability target-a.
**Lokalno:** brief ne definiše manufacturability.

### Q10 — Polymorph-risk

**Prioritet:** USLOVNO

Da li je polymorph-risk stvarni deliverable? Ako jeste, definisati material/solid-form identitet, tačan claim i korisničku odluku, vremenski horizont, eksperimentalni/energetski gold i porodice dokaza koje se zahtevaju. Da li je izlaz indikator za istragu ili tvrdnja o neotkrivenoj/stabilnijoj formi? Parametre i granice Mogul, packing ili HBP postupaka tražiti samo ako fakultet te vendor metode izričito izabere.

**White paper:** `WP-17` i `WP-18`.
**Lokalno:** nije zahtev `L-BRIEF-1` ili `L-BRIEF-2`.

### Q11 — Federativno učenje

**Prioritet:** USLOVNO

Da li postoji stvarni multi-site supervised target čiji raw podaci ne mogu zakonito/ugovorno da se centralizuju? Ako da: ko su učesnici, koordinator i trust model; koji zajednički target/schema/jedinice važe; koji update-i i metadata smeju da izađu; koje secure-aggregation, DP, poisoning/leakage, withdrawal i per-site kontrole se traže? Ako ne, FL eksplicitno staviti van osnovnog scope-a.

**White paper:** `WP-03D`, `WP-04A`, `WP-11`, `WP-15`, `WP-16`.
**Lokalno:** brief ne pominje FL.

## III. Aplikacija 1 — globalna pretraga

### Q12 — Tačan korpus „cele Kembridž baze“

**Prioritet:** BLOKIRA SPECIFIKACIJU

Koji tačno CCDC proizvod/release/subset čini pretraživi korpus? Da li ulaze organic, organometallic, polymeric, powder, no-3D, disordered, ionic, early-access, withdrawn/superseded i proprietary/in-house zapisi? Koji release i cadence ažuriranja važe?

**White paper:** `WP-07`, `WP-08A`, `WP-12`, `WP-19`; ne definiše 2CDC korpus.
**Lokalno:** `L-BRIEF-1` kaže „cela Kembridž baza“, ali bez verzije i eligibility pravila.

### Q13 — Search modes i jedinica relevantnosti

**Prioritet:** BLOKIRA SPECIFIKACIJU

Koje odvojene definicije sličnosti App1 podržava: CSD entry/određivanje, puna crystal form, coordination entity, glavna komponenta/ligand, scaffold, koordinaciono okruženje, konformacija/3D shape, packing ili interaction network? Da li postoje odvojeni rangovi ili jedan overall rank, i ko odobrava njegovo značenje?

**White paper:** `WP-08B`, `WP-09A`, `WP-09B`, `WP-18`; to su različite analize, ne App1 ranking specifikacija.
**Lokalno:** `L-BRIEF-1` samo kaže „najsličnija“.

### Q14 — Filter dictionary

**Prioritet:** BLOKIRA SPECIFIKACIJU

Za svaki filter odobriti naziv, nivo, operator, jedinicu, hard/soft status, default i missing/unknown/not-applicable ponašanje. Posebno razdvojiti: element u punoj formuli, komponenti ili coordination entity-ju; metal negde u entry-ju ili direktno koordinisan ciljnom ligandu; solvent/counterion; charge/stereo; formula/stoichiometry; 3D/disorder/quality/temperature; property vezan za formu i uslove.

**White paper:** `WP-08A`, `WP-08B`, `WP-10B`; ne daje konkretan filter dictionary.
**Lokalno:** `L-BRIEF-1`, `L-CQS-2`.

### Q15 — CIF upload ugovor

**Prioritet:** BLOKIRA SPECIFIKACIJU

Koji input-i su podržani: jedan ili više CIF data block-ova, više modela/struktura, više komponenti, disorder/partial occupancy, polymeric/powder/no-3D zapis, reflection/RES/HKL ili veliki text blok? Koje su veličinske granice, dopuštene CIF verzije/rečnici i očekivano ponašanje za syntax/semantic/quality grešku?

**White paper:** nema upload-CIF ugovor; `WP-08B` samo motiviše kuraciju i konzistentno tipiziranje.
**Lokalno:** `L-BRIEF-1`, `L-N14`.

### Q16 — Autoritativni prikaz pri neslaganju formata

**Prioritet:** BLOKIRA SPECIFIKACIJU

Ako CIF, MOL, MOL2, SDF i SMILES daju različite bond order-e, charge, stereo, koordinate ili komponente, koji izvor je autoritativan po polju? Šta je declared, curated, assigned, derived ili unknown? Da li je dozvoljena ljudska korekcija i kako se čuva veza sa originalom?

**White paper:** `WP-03B`, `WP-05`, `WP-08B`, `WP-14`.
**Lokalno:** `L-EXPORT`, `L-N14`.

### Q17 — App1 rezultat

**Prioritet:** BLOKIRA SPECIFIKACIJU

Da li sistem vraća `top-k`, sve iznad praga ili sve pogodke? Koje „osnovne informacije“ su obavezne: identitet/sastav, matched atoms/subgraph, coordination ili packing evidence, score components, coverage, quality, confidence, warnings, provenance/release i licence status? Kako izgledaju zero-hit, unsupported i abstained rezultat?

**White paper:** `WP-19` razlikuje web i programmatic pristup, ali ne definiše rezultat aplikacije.
**Lokalno:** `L-BRIEF-1`.

### Q18 — CIF download i prikaz

**Prioritet:** BLOKIRA SPECIFIKACIJU

Ko sme da vidi strukturu i preuzme CIF: samo licencirani korisnik, član institucije, spoljni saradnik ili javnost? Da li se preuzima originalni/deponovani CCDC CIF, kurirani eksport, sanitizovani derivat ili samo licencirani link, i koji release/version/provenance identifikuje taj artefakt? Da li su dozvoljeni pojedinačni i bulk download, koji metadata/evidence smeju u report, koji rate/volume limit važi i kako se postupa sa proprietary ili out-of-license hitom?

**White paper:** `WP-15`, `WP-16`, `WP-19` motivišu confidentiality/firewall, ali nisu pravna dozvola.
**Lokalno:** `L-BRIEF-1` eksplicitno traži mogućnost preuzimanja CIF-a.

### Q19 — Merljivi operativni zahtevi App1

**Prioritet:** BLOKIRA SPECIFIKACIJU

Koji broj paralelnih korisnika, `top-k`, p50/p95/p99 latencija, throughput, timeout, raspoloživost i prihvatljiva svežina release-a predstavljaju merljive operativne zahteve App1?

**White paper:** `WP-04B` govori o pristupu na skali, ali ne daje SLA ili ANN prag.
**Lokalno:** `L-BRIEF-1` kaže „dovoljno brz i skalabilan“ bez brojki.

### Q20 — Ažuriranje korpusa i rezultata

**Prioritet:** BLOKIRA SPECIFIKACIJU

Šta se očekuje kada CSD dobije novi release ili se entry izmeni, povuče ili superseduje? Da li stari rezultat mora ostati reproduktivan, koliko dugo i sa kojim release/provenance dokazom? Ko odobrava re-evaluaciju claim-a posle promene populacije?

**White paper:** `WP-05`, `WP-12`, `WP-13`, `WP-14`.
**Lokalno:** `L-CQS-1`, `L-CQS-2` trenutno vezuju nalaz za istorijski 2022 snapshot.

## IV. Aplikacija 2 — precizno all-pairs poređenje

### Q21 — Comparison profile i jedinica poređenja

**Prioritet:** BLOKIRA SPECIFIKACIJU

Da li se porede full crystal form, CSD entry/određivanje, coordination entity, parent ligand, svaka komponenta ili više paralelnih nivoa? Kako se tretiraju solventi, counterions, coformers, hidrati/solvati, više independent molecules, disorder i coordination polymers?

**White paper:** `WP-08B`, `WP-09B`, `WP-18` daju različite ose analize, ali ne App2 ugovor.
**Lokalno:** `L-BRIEF-2`.

### Q22 — Obavezne grane App2

**Prioritet:** BLOKIRA SPECIFIKACIJU

Koje su obavezne ose: composition/component relation, exact/subgraph/MCS graf, charge/stereo/tautomer, koordinaciono okruženje, mapped conformation/3D, cell/lattice, packing, simulated/measured PXRD i interaction network? Za svaku definisati target i uslove pod kojima je `not-applicable`.

**White paper:** `WP-08B`, `WP-09A`, `WP-09B`, `WP-18`; ne propisuje App2.
**Lokalno:** `L-BRIEF-2` navodi graf, geometriju, packing i interakcije kao moguće detaljne ose.

### Q23 — Jedan score ili vektor dokaza

**Prioritet:** BLOKIRA SPECIFIKACIJU

Da li rezultat treba da bude vektor odvojenih grana, rang po imenovanoj metrici, overall score ili stručna odluka? Ako overall score postoji, za koji tačno use case, sa kojim labelama i kako sprečava da missing/ambiguous grana izgleda kao nesličnost?

**White paper:** nema overall similarity score.
**Lokalno:** `L-BRIEF-2` koristi „najsličnije“, ali ne definiše agregaciju.

### Q24 — All-pairs granice

**Prioritet:** BLOKIRA SPECIFIKACIJU

Koliki su maksimalni `n`, veličina pojedinačnog i ukupnog ulaza, ukupno vreme/memorija, concurrency i timeout za propisani all-pairs režim?

**White paper:** ne pominje all-pairs ili ove limite.
**Lokalno:** `L-BRIEF-2` potvrđuje formulu, ali ne operativne granice.

### Q25 — Identitet, duplikati i neuspeh

**Prioritet:** BLOKIRA SPECIFIKACIJU

Kako se tretiraju isti fajl dvaput, isto određivanje u drugom encoding-u, redeterminations, polymorphs i invalidan/nepotpun CIF? Da li se neuspeh jedne grane ili jednog fajla prikazuje kao partial failure, izuzima par ili prekida ceo posao? Šta tačno znači `not comparable`?

**White paper:** `WP-05` i `WP-08B` motivišu identitet/verzije/kuraciju; nema App2 failure politike.
**Lokalno:** `L-EXPORT`, `L-N14` pokazuju cross-format razlike.

### Q26 — App2 izlaz i stručni pregled

**Prioritet:** BLOKIRA SPECIFIKACIJU

Da li korisnik dobija matrice po metrici, rang, klastere, long-form tabelu, drill-down do mapiranih atoma/symmetry image-a, confidence i warnings? Šta se izvozi i u kom dozvoljenom nivou detalja? Koji ambiguous slučajevi zahtevaju stručni review?

**White paper:** nema UI/export specifikaciju; `WP-09A`, `WP-09B` i `WP-18` samo ilustruju odvojene ose analize i ne propisuju App2 izlaz.
**Lokalno:** `L-BRIEF-2`.

### Q27 — Značenje „mnogo veća tačnost“

**Prioritet:** PRE EVALUACIJE

Prema kom istom target-u, baseline-u i metrici App2 mora biti „mnogo tačnija“ od App1? Da li se porede ranking relevantnost, atom mapping, relation classification, packing match ili drugo? Koja minimalna praktična razlika ima smisla korisniku?

**White paper:** nema poređenje dve aplikacije.
**Lokalno:** `L-BRIEF-2`.

## V. DAP, CQS i lokalni izvozi

### Q28 — Operational definition DAP-a

**Prioritet:** BLOKIRA SPECIFIKACIJU

Potvrditi da nameravani core odgovara 2,6-diacetilpiridinski izvedenom bis-iminskom motivu i odobriti atom mapping. Koje terminalne supstitucije, mono-/bis-imine, parcijalna kondenzacija, protonacija/tautomerija, E/Z/stereo, charge i decomposition varijante su `positive`, `negative`, `ambiguous` ili `out-of-scope`?

**White paper:** nema DAP, Schiff base ili ovu definiciju.
**Lokalno:** `L-CQS-1`, `L-CQS-2`, otvorena stavka u `L-AUDIT`.

### Q29 — Operational definition „kompleksa sa DAP"

**Prioritet:** BLOKIRA SPECIFIKACIJU

Da li pozitivan slučaj znači metal bilo gde u entry-ju, u istoj komponenti, direktan kontakt ili koordinaciju istom mapiranom DAP N3 donorskom setu? Koje monodentate/bidentate/tridentate, bridging, polimerne, multinuklearne, counterion i ambiguous-neighbor varijante ulaze? Da li oxidation state i geometry imaju obavezna pravila?

**White paper:** nema DAP ili CQS koordinacionu semantiku.
**Lokalno:** `L-CQS-2` dokazuje samo motif + metal presence.

### Q30 — Namera i status oba CQS-a

**Prioritet:** BLOKIRA SPECIFIKACIJU

Šta je autor želeo da svaki CQS znači? Da li su rezultati broad-recall kandidati za review, pozitivne labele ili nešto treće? Da li je nepovezani `4M` u drugom upitu bio nameran broad filter ili nedovršena koordinaciona definicija? Da li naziv „Kompleksi“ treba promeniti ili query pojačati?

**White paper:** nema CQS. `WP-10A` samo pominje ConQuest kao alat.
**Lokalno:** `L-CQS-1`, `L-CQS-2`.

### Q31 — Autoritativna CQS reprodukcija

**Prioritet:** BLOKIRA SPECIFIKACIJU

Dostavljeni tragovi već navode ConQuest 2022.2.0 i CSD 5.43 sa March/June 2022 segmentima. Može li ovlašćeni operater da potvrdi GUI/default/filter semantiku, dostavi screenshot oba vizuelna query-ja, machine-readable constraints/filter manifest, identitet i datum stvarnog run-a, refcode manifest/hash i broj pogodaka? Da li je potreban odvojen run nad aktuelnim release-om?

**White paper:** `WP-10A`; ne opisuje `.cqs`, default-e ili lokalni run.
**Lokalno:** `L-CQS-1`, `L-CQS-2`, `L-AUDIT`.

### Q32 — Uloga i eligibility `search1/search2`

**Prioritet:** BLOKIRA SPECIFIKACIJU

Da li izvozi služe kao regression fixture, kandidatni pool, training data ili gold? Kako se tretiraju 72 razlike, prazni SD zapisi, nedostajući SMILES, `Du`/`un`, matching problemi, disorder, polimeri i zapisi bez 3D? Koji režim sme da koristi koji record i sa kojim coverage izveštajem? Tražiti i potvrđen lineage `CQS run → refcode manifest/hash → CIF/MOL2/SD/SMILES export`, sa operaterom, alatom/verzijom, vremenom i export postavkama za svaki format; ne pretpostavljati da svi potiču iz istog run-a.

**White paper:** `WP-08A`, `WP-08B` motivišu focused subset i kuraciju; ne daju status lokalnom skupu.
**Lokalno:** `L-EXPORT`, `L-AUDIT`.

## VI. N14 identitet i lineage

### Q33 — Autoritativni identitet N14

**Prioritet:** BLOKIRA SPECIFIKACIJU ako N14 nije samo nastavni primer

Koji su puni hemijski naziv, interni ID/refcode, publikacija, uzorak/batch i solid-form/determination identitet? Šta znače `N14`, prefiks `cu_` i sufiks `_a`? Da li postoje druge verzije ili forme?

**White paper:** nema N14.
**Lokalno:** `L-N14`; filename nije hemijski dokaz.

### Q34 — Odnos CIF/MOL/MOL2 verzija

**Prioritet:** BLOKIRA SPECIFIKACIJU ako se primer koristi za validation/gold

Da li sva tri fajla predstavljaju isto eksperimentalno određivanje i isti trenutak izvoza? Koji je autoritet za bond order, formal charge, atom mapping, koordinate, ćeliju, simetriju i komponentni identitet? Koji alat/verzija i transformacija su proizveli MOL/MOL2?

**White paper:** `WP-03B`, `WP-05`, `WP-08B` daju samo opšti provenance/curation kontekst.
**Lokalno:** `L-N14`.

### Q35 — Evidenciona uloga N14 kao pojedinačnog slučaja

**Prioritet:** USLOVNO — samo ako Q04 uvede N14 u validation/gold ili disertacioni dokaz.

Koje su tačno relacije, polja ili očekivani ishodi za N14 stručno potvrđeni, a koji ostaju nepoznati? Da li je to positive, negative ili ambiguous primer za konkretan parser/format, bond-typing, stereo, koordinacioni ili crystal-level claim? Jedan slučaj može ilustrovati ili proveriti usku tvrdnju, ali ne sme neopaženo postati dokaz performansi nad populacijom; opštu ulogu određuje Q04, a disertacione claim-ove Q49.

**White paper:** nema N14 ili single-case validaciju.
**Lokalno:** `L-N14`.

### Q36 — Ugrađeni reflection/RES/HKL sadržaj

**Prioritet:** USLOVNO — samo ako N14 ili drugi CIF sa bogatim ugrađenim payload-om ulazi u scope.

Da li ugrađeni reflection/RES/HKL i drugi veliki text sadržaj sme da se parsira, čuva, prikazuje, šalje modelu, loguje ili izvozi? Da li sadrži poverljiv ili licencno ograničen materijal? Koji njegov deo je potreban za naučni cilj?

**White paper:** nema N14 payload politiku; `WP-03B`, `WP-15` i `WP-19` samo motivišu provenance/confidentiality.
**Lokalno:** `L-N14`.

## VII. Podaci, licence, prava i bezbednost

### Q37 — Owner/controller i klasifikacija svakog izvora

**Prioritet:** BLOKIRA SPECIFIKACIJU

Za brief, white paper, CQS, CSD izvoze, N14, budući CSD snapshot, proprietary podatke i korisničke upload-e navesti owner-a, controller-a, klasifikaciju, dozvoljenu svrhu, lokaciju, primaoce i expiry. Ko je ovlašćen da promeni klasifikaciju?

**White paper:** `WP-03B`, `WP-05`, `WP-15`, `WP-16`.
**Lokalno:** svi lokalni izvori; vlasništvo se ne može zaključiti iz činjenice da su fajlovi poslati.

### Q38 — CCDC product/capability matrica

**Prioritet:** BLOKIRA SPECIFIKACIJU

Koji tačan ugovor, product tier, release i verzije postoje? Da li su instituciji stvarno dostupni i dozvoljeni: puni CSD, ConQuest, Mercury, CSD Python API, Mogul, HBP, packing comparison, WebCSD/on-site, Manage Databases i CSD-Editor? Za svaki navesti desktop/headless/server/API ograničenja i ko može da potvrdi capability test.

**White paper:** `WP-10A`, `WP-12`, `WP-13`, `WP-14`, `WP-18`; pominjanje mogućnosti nije dokaz lokalnog entitlement-a.
**Lokalno:** `L-AUDIT`.

### Q39 — Permission matrica po operaciji i derivatu

**Prioritet:** BLOKIRA SPECIFIKACIJU

Za svaki izvor i procesorsko okruženje tražiti pisani `ALLOW/DENY/UNKNOWN` za: read/search, bulk export, transform/standardize, cache/index, fingerprint/descriptor/embedding, train/evaluate, model weights, lokalni ili cloud hosting/processing, third-party processor i backup. Kako se procenjuje da li je derivat rekonstruktivan? Za App2: kada su cross-owner/cross-project parovi dozvoljeni i kako se prava oba izvora kombinuju za pair evidence, trening i eksport? Prava preuzimanja CIF-a odvojeno su u Q18, a prava otkrivanja i objavljivanja u Q41.

**White paper:** `WP-15`, `WP-16`, `WP-19` daju confidentiality/firewall motivaciju, ne dozvolu.
**Lokalno:** `L-BRIEF-1`, CSD izvozi i budući korisnički upload-i.

### Q40 — Dozvoljeni deployment/data-plane boundary

**Prioritet:** BLOKIRA SPECIFIKACIJU

Gde podaci smeju da se obrađuju: on-site ili cloud, koji region/tenant, koji korisnici i service accounts? Da li Pinecone, Neo4j, hosted LLM/API, telemetrija, error tracking i backup predstavljaju dozvoljene procesore? Da li raw, derived i samo metadata imaju različite granice?

**White paper:** `WP-12`, `WP-15`, `WP-16`, `WP-19`; opis on-site/firewall/FL toka nije konkretno pravno odobrenje.
**Lokalno:** `L-BRIEF-1` navodi moguće baze bez odobrenog deployment rešenja.

### Q41 — Objavljivanje, deljenje i disertacija

**Prioritet:** BLOKIRA SPECIFIKACIJU

Šta sme u private/public GitHub, rad, poster, prezentaciju, disertaciju i odbranu: refcode-ovi, agregirane statistike, screenshot, query, schema, synthetic primer, derived feature, embedding, model, weights ili report? Ko odobrava autorstvo, IP/patent review, embargo i reproduktivni paket?

**White paper:** `WP-15`, `WP-16`, `WP-19`; ne određuje prava ovog projekta.
**Lokalno:** sirovi CSD/fakultetski artefakti namerno nisu u repozitorijumu.

### Q42 — Retention, withdrawal i prestanak licence

**Prioritet:** BLOKIRA SPECIFIKACIJU

Koliko se čuvaju raw upload, canonical view, indeks, cache, log, backup, report, training/evaluation skup, model i publikacioni dokaz? Šta se briše ili invalidira kada korisnik povuče upload, entry bude withdrawn/superseded, ugovor istekne ili licenca bude ukinuta? Šta mora ostati radi naučnog audit traga i pod kojim pravnim osnovom?

**White paper:** `WP-05`, `WP-12`, `WP-13`, `WP-14`, `WP-16` daju samo opšti lifecycle/governance kontekst; ne određuju projektne rokove, povlačenje, brisanje derivata, backup/model posledice ili prestanak licence.
**Lokalno:** budući CSD i korisnički tokovi; trenutni materijali ne daju odgovor.

## VIII. Ground truth, evaluacija i disertacioni dokaz

### Q43 — Label guide po search/comparison mode-u

**Prioritet:** PRE EVALUACIJE

Za svaki mode odobriti `positive`, `negative`, `ambiguous`, `not-applicable`, `insufficient-evidence` i abstention semantiku. Koji atomski/periodični/property dokaz se traži, a šta je samo pomoćni signal? Posebno sprečiti da CQS membership postane lažni gold koordinacije ili relevantnosti.

**White paper:** `WP-03C`, `WP-06`, `WP-08B` motivišu kvalitet; ne daju label guide.
**Lokalno:** `L-CQS-1`, `L-CQS-2`, `L-EXPORT`.

### Q44 — Stručni anotatori i adjudication

**Prioritet:** PRE EVALUACIJE

Koje kvalifikacije i koliko nezavisnih anotatora se traže po temi? Kako se beleže evidence, confidence i razlog; kako se meri agreement; ko adjudikuje neslaganje; koji budžet/vreme postoje; koji već postojeći primeri su autoritativni positive/negative/ambiguous slučajevi? Za App1 dogovoriti i kako nastaje i dopunjuje se judgment pool, da li je ocenjivanje slepo/randomizovano, kako se meri judgment coverage i zašto se `unjudged` ne tretira automatski kao negative.

**White paper:** nema anotacioni protokol; `WP-03C` i `WP-06` samo motivišu kvalitet.
**Lokalno:** `L-AUDIT` ne zamenjuje formalni domain review.

### Q45 — Evaluation korpus i leakage-safe split

**Prioritet:** PRE EVALUACIJE

Koja ciljna populacija, sampling plan i zamrznuti train/development/calibration/test važe? Kako se grupišu base-refcode/redetermination, exact graph/scaffold, compound/solid-form, publication i druge target-relevantne porodice? Da li se traži temporalni/prospective ili nezavisni external/site test? Kako se biraju hard negatives i edge/out-of-scope slučajevi? Ako se razmatra pretrained/learned encoder, tražiti poreklo i cutoff njegovog pretraining korpusa, dedup/group/time overlap proveru i unapred odobrenu klasifikaciju claim-a kao transduktivnog, induktivnog ili prospective.

**White paper:** `WP-08A`, `WP-17`, `WP-18` pokazuju da public i proprietary prostor mogu biti različiti; ne propisuju split.
**Lokalno:** `L-EXPORT` je query-conditioned subset sa duplikatima i missingness-om.

### Q46 — Metrike, pragovi i praktična margina

**Prioritet:** PRE EVALUACIJE

Za App1 odvojiti infrastrukturni ANN candidate recall od ekspertne candidate relevantnosti i finalnog ranking-a; dogovoriti Recall@k/nDCG/precision ili druge metrike, query-macro/micro i latency/freshness. Za App2 dogovoriti metrike po grani, invariance, relation agreement/ranking, coverage/not-comparable i eventualnu calibration. Koji interval poverenja, critical slice i unapred odobren prag/margina određuju uspeh? Koja je nezavisna jedinica i resampling metod: query/family za App1, odnosno odgovarajuća endpoint/family grupa i paired poređenje za App2? Hitovi ili svih \(n(n-1)/2\) međuzavisnih parova ne smeju se prećutno tretirati kao IID uzorci.

**White paper:** nema 2CDC metrike ili brojčane pragove.
**Lokalno:** `L-BRIEF-1`, `L-BRIEF-2` daju samo kvalitativne reči „brzo“, „skalabilno“ i „mnogo većom tačnošću“.

### Q47 — Generalizacija koja se sme tvrditi

**Prioritet:** PRE EVALUACIJE

Da li dokaz treba da važi samo za isti snapshot/DAP slice, nove compound/solid-form porodice, novi CSD release, prospective zapise, proprietary podatke ili drugi hemijski domen? Koja tvrdnja se izričito ne sme izvesti iz lokalnog skupa?

**White paper:** `WP-08A`, `WP-17`, `WP-18`.
**Lokalno:** `L-EXPORT` ne predstavlja ceo CSD.

### Q48 — Missing, failure i abstention politika

**Prioritet:** PRE EVALUACIJE

Kako se u gold-u, metrici i rezultatu odvajaju missing input, parse failure, unsupported representation, ambiguous mapping, quality-blocked, timeout, not-applicable i validno izmeren score nula? Koji slučajevi moraju biti prikazani u denominatoru i coverage-u?

**White paper:** `WP-03C`, `WP-05`, `WP-06`, `WP-08B` daju opštu data-quality motivaciju.
**Lokalno:** `L-EXPORT`, `L-N14`.

### Q49 — Naučni i disertacioni claim-ovi

**Prioritet:** PRE EVALUACIJE

Za svaku aplikaciju i disertaciju navesti: populaciju, korisničku odluku, hipotezu, primarni endpoint, cenu FP/FN, baseline, minimalnu praktičnu dobit, poznata ograničenja i ko zaključava protokol pre finalnog testa. Koji se naučni deliverable-i očekuju? Autorstvo, IP i prava objavljivanja odvojeno su u Q41.

**White paper:** `WP-03C`, `WP-06`, `WP-20`; white paper nije benchmark niti disertaciona specifikacija.
**Lokalno:** `L-BRIEF-1`, `L-BRIEF-2`, `L-AUDIT`.

### Q50 — Formalni sign-off i change control

**Prioritet:** PRE EVALUACIJE

Ko potpisuje finalne scope, data/licence, label guide, split, metrike, rezultate i ograničenja? Šta zahteva novu verziju ili ponovnu evaluaciju kada se promeni query, CSD release, parser, standardization, representation, model, property definicija ili licenca?

**White paper:** `WP-03B`, `WP-05`, `WP-12`, `WP-13`, `WP-14`.
**Lokalno:** `L-AUDIT` i registar tvrdnji već pokazuju potrebu za verzionisanjem dokaza.

## Minimalni izlazi koje treba tražiti od fakulteta

Odgovori u slobodnom tekstu nisu dovoljni za stavke koje određuju semantiku ili prava. Minimalni paket je:

1. potpisan scope/authority zapis za obe aplikacije i status svih white-paper tema;
2. DAP i coordination annotation guide sa atom mapping-om i positive/negative/ambiguous primerima;
3. reprodukovani CQS screenshot-i, query/filter manifest i refcode rezultat za poznatu verziju;
4. source/provenance manifest za sve dostavljene i buduće skupove;
5. CCDC product/capability matrica i odvojena pravna permission matrica;
6. App1 search/filter/result ugovor i App2 comparison/output ugovor na nivou značenja, bez diktiranja tehnologije;
7. gold/qrels, split, metrike, critical slice-ovi i sign-off protokol;
8. publikaciona/disertaciona odluka o podacima, derivatima, IP-u, autorstvu i reproduktivnosti.

Kada fakultet nešto označi `OUT_OF_SCOPE`, to je punovredan odgovor: sprečava da vendor primer ili lokalni fixture neopaženo postane zahtev projekta.
