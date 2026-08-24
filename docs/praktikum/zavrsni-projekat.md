# Završna projektantska analiza — bez implementacije

## Zadatak

Ovo je završna provera teorijskog razumevanja, ne prototip, backlog niti plan izrade stvarnog projekta. Nije potrebno pisati kod, praviti baze, trenirati modele, definisati produkcione šeme ili izvršavati budući 2CDC tok.

Na jednom hipotetičkom primeru treba usmeno ili u belešci objasniti:

- šta dve aplikacije pokušavaju da odgovore;
- koje hemijske i kristalografske nivoe ne smeju da pomešaju;
- koje porodice algoritama mogu biti relevantne i pod kojim uslovima;
- koje informacije nedostaju i moraju se potvrditi sa fakultetom;
- kakav dokaz bi jednog dana bio potreban da se rezultat smatra validnim.

Poenta nije broj feature-a. Poenta je da svaki ulaz, score, izuzetak i claim imaju precizno značenje i dokaz.

## Deo A — Konceptualna analiza globalne pretrage

Za hipotetički query CIF objasni, bez realizacije:

1. zašto se original, provenance i izvedeni prikazi moraju razlikovati;
2. kako syntax, chemistry i crystal-quality problemi menjaju dostupne search modes;
3. zašto ligand, coordination entity i puna crystal form nisu isti objekat pretrage;
4. koje značenje mogu imati formula, element, component, coordination i quality filteri;
5. ulogu širokog candidate retrieval-a i skupljeg reranking-a;
6. razliku između 2D, coordination, molecular-3D i packing sličnosti;
7. zašto rezultat mora pokazati coverage, evidence, warning i abstention;
8. zašto licence određuju šta korisnik sme da vidi ili preuzme;
9. koju vrstu stručnog gold-a bi zahtevao imenovani search claim;
10. koje odluke iz [liste za fakultet](../referenca/pitanja-za-fakultet.md) još blokiraju tačno značenje aplikacije.

Ovaj redosled je samo redosled objašnjavanja znanja, ne redosled buduće implementacije.

## Deo B — Konceptualna analiza all-pairs poređenja

Za hipotetički skup od \(n\) CIF-ova:

1. izvedi broj neuređenih parova \(n(n-1)/2\);
2. objasni zašto se composition, graph, coordination, conformation, cell, packing i interaction rezultati drže odvojeno;
3. objasni component mapping pre atom mapping-a i atom mapping pre RMSD-a;
4. razlikuj `not comparable` od validno izmerenog score-a 0;
5. navedi encoding promene na koje rezultat treba da bude invarijantan;
6. objasni zašto jedna overall cifra bez target-specific labela može biti obmanjujuća;
7. opiši kakav atomski/periodični evidence stručnjaku omogućava proveru;
8. izdvoji najmanje pet failure ili ambiguous klasa;
9. objasni koje dodatne informacije zahteva tvrdnja o packing-u ili polimorfnosti;
10. navedi koje App2 odluke mora da potvrdi fakultet pre evaluacije.

## Deo C — Nacrt naučnog dokaza

Ne pravi se stvarni gold skup. Umesto toga treba obrazložiti kako bi valjan evaluation design razlikovao:

- self/equivalent encoding slučajeve;
- lake negative primere;
- hard negatives koji dele veliki deo grafa, ali ne ciljnu relaciju;
- near positives;
- edge, ambiguous i insufficient-evidence slučajeve.

Treba objasniti ulogu nezavisne anotacije, agreement-a, adjudication-a, family/group split-a, hard-negative pokrivenosti, intervala poverenja i unapred definisanog primarnog claim-a. Brojevi, pragovi i veličina budućeg skupa ostaju odluka stakeholdera, a ne zadatak ove vežbe.

## Claim analiza

Za jednu zamišljenu tvrdnju popuni pojmovni okvir:

| Pitanje | Odgovor koji mora biti poznat |
|---|---|
| korisnička odluka | šta će stručnjak uraditi drugačije zbog rezultata? |
| populacija / scope | na koje strukture i uslove tvrdnja važi? |
| objekat | entry, komponenta, ligand, coordination entity ili solid form? |
| relevantnost / label | šta tačno znači pozitivan, negativan i ambiguous slučaj? |
| reprezentacija | koji hemijski/kristalografski nivo nosi signal? |
| algoritamska porodica | koji tip metoda odgovara pitanju i koje su mu granice? |
| evaluation evidence | koji gold, split i metrika mogu proveriti tvrdnju? |
| failure i abstention | kada se odgovor ne sme dati? |
| licence/provenance | koje pravo i poreklo moraju biti vidljivi? |
| otvorena odluka | ko na fakultetu mora da je potvrdi? |

Ovo je okvir za razmišljanje, ne buduća schema ili acceptance specifikacija.

## Similarity analiza

Za jedan hipotetički par razmotri:

| Osa | Pitanje |
|---|---|
| objekat A/B | da li se porede ista vrsta hemijskog/kristalografskog entiteta? |
| komponente | kako solventi, counterions i coformers menjaju značenje? |
| graf | koje odluke o charge-u, H, stereo, tautomeriji i metalnim vezama utiču na rezultat? |
| geometrija | koji mapping, alignment, symmetry i coordinate-origin uslovi važe? |
| periodičnost | kako cell setting, image i shell/tolerance menjaju poređenje? |
| metrika | šta formula meri, a šta ne meri? |
| coverage/status | koliko je objekta stvarno upoređeno i da li je analiza primenljiva? |
| dokaz | šta bi stručnjak morao da vidi da proveri zaključak? |

## Studije slučaja za usmeno objašnjenje

Za svaki scenario navedi najjaču dozvoljenu tvrdnju, najmanje jednu zabranjenu prečicu i dodatni dokaz koji nedostaje:

1. `cu_n14_a.cif` — filename `cu` ne postaje Cu filter;
2. MOL/MOL2 bond-typing neslaganje;
3. DAP motiv bez metala;
4. DAP motiv + metal u entry-ju, bez dokazane koordinacije;
5. kandidat kod koga mapirani DAP donori geometrijski podržavaju koordinaciju;
6. zapis bez 3D;
7. multi-component solvate ili salt;
8. `Du`, `un` ili neuspešan molekulski graf;
9. isti kristal u ekvivalentnom cell/atom encoding-u;
10. isti molekulski graf sa različitim packing-om;
11. Mogul/HBP outlier signal bez nezavisnog dokaza stabilnosti;
12. simulated PXRD koji se poredi sa source CIF-om, bez measured bulk obrasca.

## Rubrika razumevanja

| Oblast | Šta pokazuje prolaz |
|---|---|
| hemijska semantika | razlikuje sastav, komponentu, graf, koordinaciju i čvrstu formu |
| kristalografija | razume ćeliju, simetriju, periodičnost, packing i kvalitet |
| loss/provenance | ume da objasni šta formati čuvaju/gube i šta je source of truth |
| algoritmi | bira porodicu metoda prema pitanju, bez proglašavanja unapred pobednika |
| evaluacija | razlikuje gold, split, metriku, coverage, uncertainty i generalizaciju |
| failure handling | missing/ambiguous/not-applicable ne pretvara u score 0 |
| licence i FAIR | razlikuje tehničku mogućnost, dostupnost i dozvoljenu operaciju |
| granica izvora | ne pripisuje DAP ili dve aplikacije white paper-u |
| pitanja za fakultet | prepoznaje odluke koje dostupni fajlovi ne mogu dati |

## Automatski pad

- tvrditi da CIF filename određuje sastav;
- proglasiti svaki `4M` rezultat koordinisanim DAP kompleksom;
- mešati SMILES/molekulski graf sa crystal packing-om;
- prikriti problematične zapise iz denominatora;
- koristiti nasumični split uz očigledne family duplikate;
- tretirati licencirane raw CSD izvoze kao slobodno objavljive;
- prikazati predicted/assigned vrednost kao eksperimentalno izmerenu;
- dati overall score kada ključni sloj nije validno procenjen;
- tvrditi da white paper propisuje DAP, App1, App2, Pinecone ili Neo4j;
- predstaviti ovu analizu kao redosled buduće izrade.

## Usmena odbrana

Prolaz znači da možeš bez koda i bez prototipa da:

1. objasniš pet nivoa strukture;
2. protumačiš jedan forenzički nalaz uz provenance ograničenje;
3. odbraniš jedan informativan i jedan varljiv search hit;
4. rastaviš jedan pair zaključak do atoma i periodičnog evidence-a;
5. objasniš failed/abstained slučaj;
6. odbraniš zamišljeni split, metric i granicu generalizacije;
7. navedeš šta se ne može odlučiti bez fakulteta i licenciranog CSD pristupa.

**Kriterijum prolaza:** tačne i dosledne veze između hemije, kristalografije, algoritama, dokaza i otvorenih odluka — bez realizacije pravog projekta.
