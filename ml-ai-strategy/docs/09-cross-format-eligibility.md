# Cross-format reconciliation i eligibility podataka

## Svrha modula

CIF, MOL, MOL2, SDF i SMILES nisu zamenljive ambalaže za istu informaciju. Svaki format čuva, gubi ili pretpostavlja drugačiji deo hemijskog i kristalografskog objekta. Zato fingerprint, graf, crystal embedding, indeks, trening primer ili evaluacioni denominator ne treba posmatrati kao neposredan proizvod jednog fajla.

Teorijski bezbedan pogled polazi od inventara svih dostupnih verzija i reprezentacija, čuva konflikte i gubitke, a zatim bira view primeren tačnoj svrsi. Ovo poglavlje objašnjava principe; ne propisuje tehnički dizajn ili razvojni raspored.

Povezano je sa:

- [globalnim retrieval-om](03-global-retrieval-ann-ranking.md);
- [preciznim pairwise poređenjem](04-precise-pairwise.md);
- [periodičnim encoderima](05-periodic-crystal-encoders.md);
- [metric learning-om i evaluacijom](06-metric-learning-and-evaluation.md);
- [lokalnim RAG/SLM slojem](07-local-slm-rag.md);
- [granicama spoljnog API-ja](08-api-llm-security.md).

!!! info "Granica dokaza"
    Brojevi navedeni ispod reprodukuju dostavljeni lokalni snapshot. Nisu statistika aktuelnog punog CSD-a. Raw fakultetski i CSD-derived fajlovi ostaju u licenciranom data-plane-u; privatni repozitorijum sam po sebi ne daje pravo distribucije. Svaka šira tvrdnja zahteva odobren, reprezentativan corpus i zabeleženu odluku o pravima.

## Zašto je cross-format pitanje relevantno za ML

| Gubitak ili konflikt | Posledica za algoritam |
|---|---|
| odsutan ili nepouzdan bond order | menja ECFP, exact graph, MCS i message-passing edges |
| odsutan SMILES | SMILES-only skup menja ciljnu populaciju |
| nema mapiranih 3D koordinata | mapped alignment nije moguće ili ima manju pokrivenost |
| postoje Cartesian koordinate, ali nema ćelije/simetrije | isolated molecular 3D može biti moguć; packing i periodic tvrdnje nisu |
| disorder, dummy ili suppressed atom | broj atoma, komponente i susedi nisu obična potpuna činjenica |
| charge/aromaticity/stereo konflikt | menja standardizaciju, mapping, similarity i značenje labele |
| parser ili matching problem | rezultat je neodređen, ne automatski negativan |
| zastareo lifecycle pogled | izvedeni skup može sadržati povučenu ili nereviewed verziju |

Complete-case analiza zato ne meri automatski populaciju proizvoda. Pored kvaliteta na dostupnim reprezentacijama treba pokazati representation coverage, razloge nedostupnosti i ponašanje uz uzdržavanje.

## Lokalni nalazi kao ilustracije

### N14: isti entry, nejednaki pogledi

Dostavljeni eksperimentalni N14 CIF, MOL i MOL2 odnose se na isti primer, ali ne prenose istu informaciju:

- svi imaju 51 atom i 54 bond record-a;
- MOL označava svih 54 veza kao `single`;
- MOL2 ima 34 `single` i 20 `un` veza;
- CIF sadrži ćeliju, simetriju i širi eksperimentalni/geometrijski kontekst, uključujući velike tekstualne blokove;
- ime `cu_n14_a.cif` nije composition label: deklarisana formula nema Cu.

Zaključak nije da jedna ekstenzija uvek pobeđuje. Bogati eksperimentalni CIF u ovom primeru ima eksplicitne bond zapise, dok pojednostavljen CSD CIF iz lokalnog skupa može biti bez bond loop-a. Autoritet se procenjuje po polju, view-u, provenance-u i svrsi, ne po ekstenziji.

### Lokalni CSD export: missingness nije slučajna

U dostavljenom `search2` snapshot-u:

- postoji 2.038 entry-ja;
- 1.954 ima upotrebljiv coordinate/atom model, a 84 nema;
- 1.805 ima SMILES, a 233 nema;
- istih 233 nedostaje i u `search1`, koncentrisano u složenijim metalnim zapisima;
- MOL2 sadrži 7.805 `Du` atoma u 627 record-a;
- 176 SD record-a nosi matching problem uz „No disordered atoms“, a 84 uz unknown disorder.

Ove brojke ilustruju selection mehanizam: denominator ograničen na redove sa SMILES-om ili potpunim koordinatama može sistematski izbaciti teže metalne strukture i dati optimističan rezultat.

## Temeljni principi

1. **Izvor postoji pre derivata.** Vlasnik, prava, release/verzija, vreme i byte-level identitet pripadaju provenance-u.
2. **Nema tihog prepisivanja.** Canonical činjenica mora ostati povezana sa source pogledima, konfliktima i transformacijama.
3. **Lossy pogled nije automatski autoritet.** Može biti fallback ili dopunski evidence.
4. **Union prethodi izboru.** Odsutan pogled dobija eksplicitno stanje; `inner join` ne sme nevidljivo promeniti populaciju.
5. **Eligibility prethodi reprezentaciji.** Prava, svrha, lifecycle i quality određuju da li se view sme koristiti.
6. **Promena izvora menja izvedene tvrdnje.** Nova verzija, korekcija ili promena prava zahteva ponovno razmatranje pogođenih derivata.

## Inventar više pogleda

Za objašnjiv cross-format sistem važno je rekonstruisati:

| Oblast | Teorijski sadržaj |
|---|---|
| identitet | stabilna veza entry-ja, verzija, derivata i poznatih compound/solid-form porodica |
| izvor | baza ili fajl, release/verzija i vreme izvoza/ingest-a |
| prava | dozvoljene svrhe, ograničenja i status odluke |
| lifecycle | stanje zapisa i kontekst u kojem to stanje važi |
| reprezentacije | dostupni formati, parser/revizija, gubici i konflikti |
| koordinate | coordinate system, jedinica, cell/symmetry i mapiranje kada postoje |
| odluke | koji view je korišćen za koju svrhu i na osnovu čega |

Tehnologija čuvanja nije teorijski zaključak. Bitno je da se različiti pogledi ne sliju u jednu neproverljivu vrednost.

### Availability ima više značenja

Potrebno je razlikovati bar: prisutno, odsutno, nepoznato, neprimenljivo, neuspešno parsirano, konfliktno, quarantined i uskraćeno politikom. Nula, prazan string, CIF `?`, CIF `.`, odsutno polje i zabranjeno polje nisu ista vrednost.

Algoritam dobija vrednost zajedno sa statusom i poreklom ili se uzdržava od grane koja nije ocenljiva. Missing nije negativna labela i ne treba ga kodirati kao similarity nula.

### Crystal system i setting nisu isto

Lokalni `search2` sadrži 12 doslovnih `_symmetry_cell_setting = rhombohedral` vrednosti. `Rhombohedral` u tom kontekstu nije osmi crystal system; pripada trigonalnom sistemu, dok reported lattice setting i coordinate axes setting ostaju odvojeni pojmovi.

Normalizovana kategorija služi modelima i stratifikaciji, a raw label ostaje provenance. Sama etiketa ne dokazuje da su koordinate zapisane u rhombohedral umesto hexagonal axes setting-u.

## Reconciliation nije izbor „najboljeg fajla“

Jedan univerzalni graf može sakriti poreklo. Korisno je konceptualno razlikovati:

| Pogled | Šta predstavlja | Koju tvrdnju podržava |
|---|---|---|
| deklarisani graf | eksplicitne atom/bond/stereo/charge zapise imenovanog izvora | „izvor je deklarisao“ |
| kurirani graf | stručno ili pravilima odobrenu interpretaciju sa vidljivom razlikom | namenska 2D/mapping analiza |
| geometrijski kandidat-susedi | veze predložene iz distance/Voronoi/chemistry kriterijuma | kandidat za proveru koordinacije, ne bond-order istinu |

Dva lossy eksporta nisu dva nezavisna glasa protiv bogatijeg originala ako su nastala iz istog upstream zapisa. Consensus zato nije prosto glasanje formata.

Konflikt se ne popunjava najpogodnijom vrednošću samo zato što biblioteka traži potpun input. Moguće su različite teorijski ispravne reakcije: koristiti drugi odobren view, zadržati unknown edge, ograničiti analizu na primenljivu reprezentaciju ili vratiti neodređen status.

## Koordinatni ugovor

CIF nije samo još jedan 3D format:

- CIF tipično daje frakcione koordinate u odnosu na konkretnu ćeliju; Cartesian položaj zavisi od matrice ćelije, konvencije osa i jedinica;
- MOL/MOL2/SDF tipično daju Cartesian koordinate izolovanog molekula ili odabranog sklopa, bez kompletnog kristalnog packinga;
- isti kristal može imati drugi origin, setting, basis ili celobrojni lattice pomeraj;
- ASU site, symmetry-expanded site i atom izdvojenog molekula nisu isti identitet;
- fractional/Cartesian konverzija, change-of-basis, origin transform i wrapping moraju imati proverljiv transformacioni lanac.

Dva mapirana izolovana Cartesian molekula mogu se Kabsch-poravnati i bez ćelije. Taj rezultat govori o mapiranoj molekulskoj konformaciji, ne o packingu, periodic equivalence ili PXRD-u. Obrnuto, periodično poređenje mora uključiti cell, symmetry i image provenance.

## Purpose-specific view

„Canonical“ ima smisla samo u odnosu na pitanje:

| Svrha | Potrebna informacija | Ako nedostaje |
|---|---|---|
| 2D fingerprint | validan molekulski graf pod imenovanom standardizacijom | kanal nije ocenljiv; entry može ostati u drugim kanalima |
| exact/subgraph/MCS | node/edge/stereo politika i dozvoljen mapping | konflikt ili timeout ostaje vidljiv |
| mapped molecular 3D | koordinatni sistem i atom mapping | nema RMSD tvrdnje |
| coordination | metal/donor kandidati, distance/radii politika i ambiguity | vraća evidence o ograničenju, ne izmišljenu vezu |
| periodic encoder/packing | validna ćelija, simetrija, site i image podaci | periodična grana nije primenljiva |
| dokumentni RAG | odobren tekst, verzija i locator | dokument ne ulazi u corpus |
| property model | target vezan za material/solid form, metod, uslove i vreme | nema pouzdane supervised labele |

Odsustvo jednog view-a nije razlog da entry nestane iz svih analiza.

## Coverage i denominatori

### Globalna pretraga

Potrebno je razlikovati:

- ukupan source corpus;
- populaciju dozvoljenu pravima i svrhom;
- populaciju koja prolazi semantički hard filter;
- raspoloživost svake reprezentacije;
- broj kandidata koji svaki kanal može da oceni;
- broj neocenjenih ili nepoznatih slučajeva.

Recall nad complete-case podskupom odgovara na drugo pitanje od recall-a nad celom ciljnom populacijom. Rezultate treba prikazati uz denominator i coverage, posebno po source-format i missingness grupama.

### All-pairs poređenje

Kod skupa od \(n\) ulaza postoji \(n(n-1)/2\) neuređenih parova pre stručnih ograničenja scope-a. Neuspeh jedne reprezentacije ne treba da izbriše par: svaka grana može biti ocenjena, neprimenljiva, neodređena ili neuspešna, uz očuvanje para i razloga.

Usmerene veličine, kao coverage A→B i B→A, treba razlikovati od simetričnih veličina. Zamena redosleda ulaza ne sme slučajno menjati simetričan rezultat.

## Lifecycle, prava i kvalitet su odvojene ose

Lifecycle opisuje gde se zapis nalazi u procesu prijema, provere, kuracije, objave, korekcije ili povlačenja. Prava opisuju dozvoljenu upotrebu. Quality opisuje pouzdanost i raspoloživost modela. Jedna osa ne sme da glumi drugu:

- released ne znači da je svaka projektna upotreba licencno dozvoljena;
- early-access ili needs-review ne znači automatski naučno netačno;
- povučeno ne znači da se istorijski zapis briše bez traga;
- visok quality score ne daje pravo za embedding, trening ili egress.

White paper opisuje early-access/main tok i alate za review/curation na visokom nivou. Ne definiše projektnu state machine, DAP semantiku, tačne inclusion politike ili aplikacione statuse. Te odluke zahtevaju vlasnika i domenskog autoriteta.

Promena lifecycle-a ili prava može uticati na indeks, embedding, trening red ili report. Teorijski zahtev je da se zna koji derivati zavise od koje verzije i odluke, a ne da se ovde propiše format događaja ili mehanizam invalidacije.

## Point-in-time i post-review leakage

Za vremenski osetljivu tvrdnju treba razlikovati:

- **effective time** — kada je činjenica važila u domenu;
- **recorded time** — kada je sistem saznao ili zabeležio činjenicu;
- **as-of vreme** — šta je bilo dostupno modelu ili korisniku u trenutku predikcije;
- **outcome vreme** — kada je target meren ili odlučen.

Prognostička feature slika mora prethoditi target događaju prema unapred definisanoj semantici. Kasniji review status, korekcija, kurirani graf ili property rezultat ne smeju retroaktivno ući u raniji feature red.

Primer: model za `expert_review_needed` ne sme kao ulaz dobiti činjenicu da je zapis kasnije odobren ili ispravljen. Property predikcija ne sme koristiti vrednost ili metadata nastao posle merenja. Deskriptivna retrospektivna analiza može imati drugačiji vremenski odnos, ali se ne sme predstavljati kao predikcija budućeg ishoda.

## Identity pre split-a

Pre train/development/calibration/test podele treba povezati:

- sve formate i verzije istog stabilnog entry-ja;
- derivacione i redetermination veze;
- exact graph ili canonical SMILES klaster kada je relevantan;
- compound, scaffold, material ili solid-form porodicu prema target-u;
- source/publication/batch porodicu kada može proizvesti leakage.

Tek posle identity povezivanja bira se split koji odgovara estimand-u: random row split često deli gotovo isti objekat na obe strane. Learned imputer, scaler, vocabulary, PCA, feature selection i hard-negative mining uče se samo na trening delu.

## Missingness i shortcut learning

Availability, source i lifecycle informacije potrebne su za routing, primenljivost, coverage i abstention. U naučnom relevance/property modelu mogu biti opasna prečica jer format, release i judgment pool nisu slučajni.

Korisne provere uključuju:

- baseline koji koristi samo availability/source/status informacije;
- ablation bez tih polja i njihovih proxy-ja;
- leave-source/release/time-out ili prospective shift;
- metrike po zajedničkim availability × source × lifecycle grupama;
- poređenje nad istom union populacijom, ne samo complete-case redovima.

Dobitak koji nestaje kada se ukloni source/missingness signal nije dokaz bolje hemijske reprezentacije. Takav signal eventualno može opisati rizik ili potrebu za uzdržavanjem, ali ne treba ga nevidljivo ugrađivati u naučni similarity score.

## Veza sa izvornim materijalom

- `chemistry-foundations/docs/17-lokalni-skup.md`: cross-format gubici, 84 zapisa bez coordinate model-a, 233 bez SMILES-a, `Du`, matching problem, N14 i leakage.
- `chemistry-foundations/docs/22-whitepaper-tokovi-fl.md`: early-access/main lifecycle, review/curation, structure–property veza i uslovni FL pojmovi.
- dostavljeni CCDC white paper, **vizuelno/fizički strane 12–14**, odlomci o early-access naspram main baze, Manage Databases, Review Structures/CSD-Editor i database-ready toku.
- `dve funkcionalnosti.txt`: globalni candidate/ranking problem i all-pairs poređenje, što motiviše coverage i denominator razmatranja.

White paper je vendor problemski okvir. Ne daje 2CDC dataset identitet, DAP pravilo, gold standard, konkretne inclusion pragove, strukturu projektnih podataka ili dokaz performansi algoritma. Lokalni nalazi ilustruju rizike, ali ne zamenjuju ovlašćen corpus, stručnu semantiku i point-in-time evaluaciju.
