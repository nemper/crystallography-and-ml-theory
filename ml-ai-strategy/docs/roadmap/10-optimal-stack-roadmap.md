# Uporedna mapa algoritamskih porodica i uslova primene

## Kako čitati ovu mapu

Ova strana poredi porodice metoda relevantne za dva 2CDC problema: globalno pronalaženje srodnih struktura i precizno poređenje skupa struktura svaki-sa-svakim. Ne predstavlja izbor konkretnog sistema niti redosled realizacije.

„Napredniji“ algoritam nije univerzalno bolji. Izbor zavisi od:

- objekta: molekul, komponenta, coordination entity, crystal structure, solid form ili dokument;
- tvrdnje: identitet, containment, lokalna sličnost, packing odnos, relevantnost ili property;
- raspoložive reprezentacije i njihove provenance;
- targeta, gold/qrels semantike i nezavisnih grupa;
- traženih invarijansi i dozvoljenih transformacija;
- prava za čitanje, izvođenje feature-a, embedding, trening i distribuciju;
- potrebe za objašnjenjem, kalibracijom i uzdržavanjem;
- skale, memorije, latencije i troška ažuriranja.

Jedan sistem može koristiti više komplementarnih porodica, ali njihovi skorovi nisu automatski uporedivi niti sabirljivi. Svaka metoda mora ostati vezana za pitanje koje zaista meri.

## Pre algoritma: objekat, target i eligibility

| Pitanje | Zašto menja izbor metode |
|---|---|
| Šta je jedinica poređenja? | isti entry, isti parent graph, isti konformer i ista čvrsta forma nisu ista relacija |
| Koji view je dostupan? | 2D graf, isolated 3D i periodic crystal zahtevaju različite algoritme |
| Koja transformacija čuva značenje? | atom permutation, rotacija, translacija, PBC wrap, setting/basis i refleksija nisu univerzalno ekvivalentne |
| Koji je gold? | ekspertna relevantnost, exact odnos, property merenje i vendor search grupa nisu ista labela |
| Koja je ciljna populacija? | complete-case ili judged podskup može sistematski izostaviti teške primere |
| Koja prava važe? | dozvola za lokalno čitanje ne mora obuhvatiti embedding, trening, API egress ili objavu |
| Koje je as-of vreme? | post-review ili post-measurement informacija može proizvesti leakage |

[Cross-format i eligibility modul](../data/09-cross-format-eligibility.md) detaljnije obrađuje ove uslove.

## Determinističke porodice za reprezentaciju i poređenje

### Standardizacija i identitet

| Porodica | Odgovara na | Prednost | Granica |
|---|---|---|---|
| parser + loss-aware reconciliation | šta je izvor deklarisao i koji su konflikti među formatima | provenance i vidljiva nepoznanica | parser uspeh nije hemijska validnost |
| ruleset standardizacija | kako normalizovati charge, aromatičnost, tautomeriju, komponente i stereo za imenovanu svrhu | reproducibilna semantika | različite svrhe mogu zahtevati različit view |
| canonical hash/identifier | da li su dva već standardizovana objekta identično kodirana | veoma brzo prefiltriranje | collision, toolkit i policy zavisnost; nije dovoljan za sve relacije |
| exact graph isomorphism | postoji li bijekcija čvorova i grana pod zadatim pravilima | objašnjiv mapping | trošak raste uz simetriju i neodređene veze |

### Graph containment i zajedničko jezgro

VF2-like algoritmi traže exact ili subgraph mapping pod eksplicitnim node/edge/stereo ograničenjima. Maximum Common Substructure (MCS) traži najveće zajedničko jezgro kada potpun mapping ne postoji.

| Metoda | Kada je prikladna | Šta mora ostati vidljivo |
|---|---|---|
| exact/subgraph isomorphism | identitet ili usmereni containment | smer, atom mapping i pravila podudaranja |
| MCS | parcijalno zajedničko jezgro | coverage obe strane, timeout i više jednako dobrih mapiranja |
| fingerprint bound pre MCS-a | jeftina granica ili pruning | bound nije konačan mapping dokaz |

Timeout, ambiguity ili nepoznat bond order nisu similarity nula.

### Komponente i assignment

Kod multikomponentnih struktura treba razlikovati ligand, coordination entity, counterion, solvent, coformer i polymeric/network slučaj. Porodice bipartitnog assignment-a, uključujući Hungarian ili min-cost formulacije, mogu upariti komponente uz unmatched opciju.

Korisne su kada postoji eksplicitna cost semantika. Ne rešavaju automatski pitanje „koja je glavna komponenta“, a jedno optimalno uparivanje može prikriti bliske alternative; ambiguity i coverage zato pripadaju rezultatu.

### Mapirano molekulsko 3D poređenje

Kabsch algoritam nalazi optimalnu rigidnu rotaciju posle atom mapping-a. RMSD bez mapiranja nema stabilno hemijsko značenje.

Primenljivost zavisi od:

- dozvoljenih mapiranja i automorfizama;
- coverage-a mapiranih atoma;
- odluke o refleksiji i stereohemiji;
- toga da li se poredi isolated molekul ili periodični objekat;
- treatment-a disorder-a i više konformacija.

Kabsch ne dokazuje crystal packing sličnost.

### Koordinaciona geometrija

Distance/radii, Voronoi, bond-valence i chemistry-aware heuristike daju kandidat-susede; coordination number, donor identitet i continuous shape measures opisuju različite aspekte okruženja. ChemEnv-like pristupi predstavljaju jednu porodicu strukturisanog određivanja lokalne geometrije.

Prisustvo metala u entry-ju nije isto što i direktna koordinacija mapiranog donor seta. Više razumnih neighbor politika može dati sensitivity/ambiguity informaciju umesto jedne skrivene odluke.

### Periodična ekvivalencija i packing

| Porodica | Objekat | Šta može podržati | Ograničenje |
|---|---|---|---|
| cell/symmetry transform search | periodični zapis | ekvivalenciju pod origin/setting/basis/lattice promenama | redukovana ćelija sama nije packing dokaz |
| COMPACK/Packing Similarity | klaster molekula u kristalu | lokalnu packing sličnost pod parametrima metode | dostupnost/licenca i definicija molekulske jedinice |
| PAC | packing alignment/cluster odnos | nezavisan packing signal prema objavljenoj metodi | primenljivost i nezavisna validacija metode |
| CrystalCMP | odabrana molekulska vrsta u kristalu | species-specific crystal poređenje | nije automatski primenljiv na coordination networks |
| SOAP–REMatch | lokalna okruženja i agregaciju sličnosti | soft geometrijski signal | species, cutoff, kernel i stereo/reflection semantika |
| simulated PXRD | difrakcioni obrazac izveden iz strukture | komplementaran signal o periodičnom rasporedu | simulacija iz istog CIF-a nije nezavisan eksperimentalni dokaz |
| interaction network | tipizirane intermolekulske veze/motivi | odnos mreža interakcija | zavisi od pravila detekcije, mapiranja i coverage-a |

Packing, PXRD, SOAP i interaction-network rezultat mere različite relacije. Bez ciljnih labela nema opravdanja za univerzalnu ponderisanu sumu.

## Porodice za globalno pronalaženje kandidata

### Hard filteri

Hard filter predstavlja semantičko ograničenje populacije, ne approximate similarity. Može obuhvatiti elemente, charge, komponente, metal/donor uslov, kvalitet ili prava, ali samo ako je značenje polja definisano.

Relevantna provera je skupovna: optimized filter i referentna exact evaluacija treba da daju isti eligible skup. Brzina ili rang ne nadoknađuju pogrešan membership.

### 2D fingerprint i Tanimoto

Za binarne fingerprint-e Tanimoto je:

\[
T(A,B)=\frac{|A\cap B|}{|A\cup B|}.
\]

ECFP-like fingerprint-i dobro skaliraju i hvataju lokalne 2D podstrukture. Zavise od standardizacije, radius-a, dužine, bit/count varijante i collision-a. Visok 2D score ne dokazuje isti konformer, koordinaciju ili packing.

Exact scan daje referentno susedstvo za istu reprezentaciju i metriku. Inverted/bounded algoritmi mogu ubrzati pretragu uz očuvanu exact semantiku; approximate metode menjaju recall/latency odnos.

### Dense deskriptori i ANN

Dense vector može biti ručno projektovan deskriptor ili learned embedding. Porodice indeksa imaju različite osobine:

| Porodica | Osnovna ideja | Tipična prednost | Rizik |
|---|---|---|---|
| exact Flat | poređenje sa svim vektorima | oracle za isti prostor i metriku | linearni trošak |
| HNSW | navigacija kroz višeslojni proximity graf | dobar latency/recall odnos | memorija i filter-aware ponašanje |
| IVF | pretraga samo relevantnih coarse particija | kontrola broja probanih ćelija | training/distribution drift i missed cells |
| PQ | kompresija vektora codebook-om | manja memorija | dodatna aproksimaciona greška |
| LSH | hashiranje prema izabranoj metrici | teorijski vezano za određene sličnosti | recall i memorija zavise od konstrukcije |

ANN tačnost se definiše prema exact susedima u istom embedding prostoru. To meri infrastrukturnu aproksimaciju, ne stručnu relevantnost embedding-a. Za nju su potrebni qrels i odvojena semantic-recall evaluacija.

### Višekanalni retrieval i rangiranje

2D, koordinacioni, shape/3D i periodični kanali mogu biti komplementarni. Njihova unija povećava pokrivenost samo ako svaki kanal ima jasan objekat i eligibility.

Score fuzija zahteva kalibraciju ili metod koji ne pretpostavlja direktno uporedive skale. Reciprocal Rank Fusion je primer rank-based kombinovanja; rule score, linear/logistic, Random Forest, ExtraTrees, GBDT i learning-to-rank modeli predstavljaju različite porodice rerankera.

Reranker može preurediti postojeće kandidate, ali ne može povratiti relevantan objekat koji candidate generation nije pronašao. Zato candidate recall i kvalitet finalnog ranga odgovaraju na različita pitanja.

Više detalja je u [retrieval/ANN/ranking modulu](../retrieval/03-global-retrieval-ann-ranking.md).

## Porodice za all-pairs poređenje

Za \(n\) ulaza postoji \(n(n-1)/2\) neuređenih parova pre stručnih ograničenja scope-a. Svaki par može imati više grana dokaza:

- component assignment;
- exact/subgraph/MCS odnos;
- mapped molecular 3D;
- koordinacionu geometriju;
- periodic equivalence i packing;
- PXRD, SOAP ili interaction-network signal.

Neke grane su simetrične, druge usmerene. `A contains B` nije isto što i `B contains A`, dok rigidni RMSD pod istim mapiranjem treba da bude simetričan. Availability i ambiguity pripadaju rezultatu; neocenjena grana ne postaje negativna klasa.

Naučni izlaz je prirodno vektor evidence-a, ne nužno jedan scalar. Ako ekspertski target zahteva objedinjenu odluku, linearni/ordinalni modeli, tree ensemble-i ili pair modeli mogu naučiti target-specific kombinaciju. Takav model ne menja značenje pojedinačnih dokaza.

Detalji su u [preciznom pairwise modulu](../pairs/04-precise-pairwise.md).

## Klasične supervised porodice

| Porodica | Pogodna kada | Prednosti | Ograničenja |
|---|---|---|---|
| linear/logistic/ordinal | broj nezavisnih grupa je mali ili se traži objašnjiva referenca | stabilnost, regularizacija, čitljivi koeficijenti | slabe nelinearne interakcije |
| Ridge/Elastic Net | mnogo korelisanih deskriptora | kontrola kompleksnosti i sparsity | zavisi od skaliranja i linearnosti |
| Random Forest/ExtraTrees | tabularni nelinearni signali i interakcije | robusna jaka referenca, malo pretpostavki | kalibracija i ekstrapolacija |
| GBDT | strukturisani feature-i i dovoljno grupa | snažan tabularni model | tuning/overfit i slab OOD dokaz |
| SVM/SVR | srednji skup i smislen kernel | jaka margin metoda | skaliranje sa brojem primera i kalibracija |
| GPR | mali regression skup sa smislenim kernelom | prediktivna uncertainty pod pretpostavkama | kubni trošak i kernel misspecification |
| PLS | mali, visoko korelisan hemometrijski prostor | latentne linearne komponente | ograničena nelinearnost |
| shallow MLP | dovoljno podataka za nelinearnu tabularnu mapu | fleksibilnost | često ne pobeđuje tree/linear reference na malom skupu |

Efektivni uzorak nije broj redova kada parovi dele endpoint-e, strukture imaju više verzija ili query-ji potiču iz iste familije. Model selection zato treba da prati group/time/prospective estimand, ne slučajni row split.

[Klasični ML modul](../classical/02-classical-ml.md) daje detalje o učenju, kalibraciji i evaluaciji.

## Periodični i geometrijski neuronski modeli

| Porodica | Glavna reprezentaciona ideja | Kada je relevantna | Šta ne rešava sama |
|---|---|---|---|
| CGCNN | message passing na crystal grafu | jaka referenca za periodic property zadatke | projektni similarity target i gold |
| SchNet | kontinuirani distance filteri | distance-based 3D/periodic signal | ugaona/stereo semantika bez dodataka |
| ALIGNN | atom graph + line graph uglova | lokalna geometrija i koordinacija | prava, label quality i invariance dokaz |
| Matformer | periodic-aware transformer konstrukcija | duži/strukturni periodic kontekst | automatsku generalizaciju na CSD-like similarity |
| equivariant GNN | kontrolisano ponašanje pod rotacijama/refleksijama | target zahteva vektorske/geometrijske odnose | pogrešno definisan parity/stereo target |
| dual encoder | zaseban embedding svakog objekta | scalable retrieval i simetrične pair funkcije | fine cross-object interakcije |
| cross-graph comparator | zajednička obrada dva grafa | kompleksna pair interakcija | računarski trošak i potrebu za jakim gold-om |

Periodični model zavisi od graph builder-a, cell/symmetry/image informacija, occupancy/disorder politike i invarijansi. Atom-order, translation, wrap, origin, basis/setting i supercell transformacije moraju imati target-specifično očekivanje.

Ovi modeli su uglavnom validirani na objavljenim property zadacima. To ne dokazuje da njihov embedding meri 2CDC stručnu sličnost. [Periodic encoder modul](../deep/05-periodic-crystal-encoders.md) razdvaja te tvrdnje.

## Metric learning i pair modeli

Contrastive, triplet i InfoNCE loss pretpostavljaju strukturu pozitivnih i negativnih primera. Primenljivi su kada relacija može smisleno da se predstavi globalnim prostorom udaljenosti.

Netranzitivna ili query-conditioned relevantnost često bolje odgovara pair/listwise rankeru nego globalnom metric prostoru. Supervised contrastive pristup može pogrešno gurati validne „related“ primere ako pozitivne klase nisu tranzitivne, a false negatives su česti u nepotpuno ocenjenom korpusu.

Dual encoder je pogodan za pretragu jer se embedding može računati po objektu; cross-encoder/cross-graph model daje bogatiju interakciju uz veći trošak. Simetrični target zahteva komutativnu pair funkciju, dok usmereni target mora sačuvati smer.

Više o loss-evima, splitovima i kalibraciji nalazi se u [metric learning i evaluacionom modulu](../deep/06-metric-learning-and-evaluation.md).

## Jezički i dokumentacioni algoritmi

| Porodica | Objekat | Uloga | Granica |
|---|---|---|---|
| formular/rečnik/rules | korisnička namera | kontrolisan unos i razjašnjenje | manja jezička fleksibilnost |
| lokalni SLM | tekst | predlog kontrolisane interpretacije ili objašnjenje | nije hemijski/policy autoritet |
| BM25 | dokument | lexical retrieval tačnih oznaka i termina | slabija semantička parafraza |
| dense bi-encoder | dokument | semantički i višejezični retrieval | retki identifikatori i model drift |
| RRF | rang-liste | kombinovanje komplementarnih kanala | ne vraća kandidata koji nigde nije pronađen |
| cross-encoder/late interaction | query–dokument par | precizniji reranking | veći trošak i zavisnost od candidate recall-a |
| LoRA/QLoRA | model adapter | parameter-efficient prilagođavanje | prava, leakage i memorisanje ostaju |

Dokumentacioni RAG i crystal similarity imaju različite korpuse, embedding-e, metrike i qrels. [Lokalni SLM/RAG modul](../language/07-local-slm-rag.md) detaljno objašnjava tu granicu.

Spoljni API je samo drugi izvršni kontekst za jezički model. Retention, processor, region, feature state i source prava ostaju posebna pitanja; provider/model naziv nije algoritamski dokaz. Pogledati [API/security modul](../language/08-api-llm-security.md).

## Structure–property porodice

Property prediction je zaseban target. Svaka labela treba da bude vezana za material i solid form, strukturu/verziju, jedinicu, uslove, metod, sample/batch, uncertainty i vreme kada je postala poznata.

Klasični deskriptor modeli i periodični GNN/transformer modeli nude različit bias. Slična property vrednost ne dokazuje sličnu strukturu, niti structural similarity automatski daje property jednakost.

Manufacturability nije prirodno jedan scalar. Filtracija, flowability, tableting ili drugi procesni ishodi zavise od formulacije, protokola, opreme, site-a, batch-a i vremena. Bez operativne definicije i dovoljno nezavisnih process grupa model bi uglavnom učio selection i site proxy-je.

## Polymorph-risk — samo uslovna oblast

Mogul/geometrijske raspodele, packing comparison, hydrogen-bond propensity, interaction networks i analog retrieval mogu dati **indikatore za istragu**. Ne daju automatsku dijagnozu neotkrivenog polimorfa, stabilnosti ili termodinamičkog poretka.

Jača tvrdnja zahteva jasno definisan estimand, reprezentativan referentni skup, validirane metode i nezavisne eksperimentalne ili energetske dokaze. White paper motiviše polymorph-risk temu na visokom nivou; ne daje projektnu labelu, prag ili potvrđeni model.

## Federativno učenje — uslovna porodica

Federativno učenje (FL) koordinira učenje bez centralizovanja raw podataka. Ono nije potrebno svojstvo retrieval-a ili determinističkog poređenja i nije automatska zaštita privatnosti.

FL ima smisla samo kada postoji:

- zajednički supervised target na više institucija;
- pravni ili poslovni razlog da se raw podaci ne centralizuju;
- usaglašena semantika podataka i labela, jedinice i quality politika;
- dovoljno heterogenih site-ova za smislen globalni i worst-site rezultat;
- threat model za update/gradient leakage, malicious client, coordinator i finalni model;
- odgovarajuće secure aggregation, diferencijalna privatnost ili robust aggregation kontrole;
- prava za lokalni trening, slanje update-a, agregaciju i distribuciju modela.

FedAvg, FedProx, SCAFFOLD i druge FL porodice rešavaju različite optimizacione probleme pod non-IID podacima. Secure aggregation skriva pojedinačni update od koordinatora u definisanom protokolu; diferencijalna privatnost ograničava informaciju uz cenu korisnosti; robust aggregation cilja kvarove ili zlonamerne klijente. Nijedna kontrola sama ne daje licencu.

## Zajedničke evaluacione ose

| Osa | Pitanje za svaku porodicu |
|---|---|
| semantika | da li score/label meri imenovanu relaciju |
| coverage | nad kojim denominatorom metoda uopšte daje rezultat |
| reference | koji exact, rule, classical ili stručni gold služi kao poređenje |
| leakage | da li identitet, vreme, review ili pretraining overlap daju prečicu |
| invarijanse | šta mora ostati isto pod fizički ekvivalentnim transformacijama |
| calibration | može li score da podrži rizik, prag ili abstention tvrdnju |
| uncertainty | da li nepoznato, neprimenljivo i failure ostaju odvojeni |
| fairness of comparison | isti target, split, corpus, tuning budžet i nezavisan test |
| prava | da li je svaka operacija nad izvorom i derivatom dozvoljena |
| resursi | latency, memorija, throughput, update i održavanje |
| objašnjivost | koji mapping, evidence ili source locator podržava rezultat |

Nema univerzalnog praga ili pobednika izvan konkretne populacije i claim-a. Prosek treba dopuniti unapred definisanim critical slice-ovima, intervalima po nezavisnim grupama i vidljivim failure accounting-om.

## Sažeta mapa uslova

| Ako je glavno pitanje... | Relevantne porodice | Nisu dovoljne same po sebi |
|---|---|---|
| exact 2D identitet/containment | canonicalizacija, VF2-like isomorphism, MCS | fingerprint score |
| brza 2D sličnost | ECFP/count fingerprint, Tanimoto, exact/inverted/LSH | packing ili coordination tvrdnja |
| mapirana molekulska 3D razlika | atom mapping + Kabsch | cell parametri ili raw coordinate redosled |
| koordinacioni odnos | neighbor kandidati, donor mapping, CN/CSM | samo prisustvo metala |
| periodic/packing odnos | symmetry transforms, COMPACK/PAC, SOAP, PXRD, interaction graph | izolovani molekulski RMSD |
| corpus-scale dense retrieval | validan descriptor/encoder + exact/ANN indeks | stručna relevantnost bez qrels-a |
| tabularni target sa ograničenim labelama | regularizovani linearni modeli, RF/ExtraTrees, GBDT, SVM/GPR po režimu | random row split |
| periodic property ili learned similarity | CGCNN/SchNet/ALIGNN/Matformer/equivariant porodice | validan target, graph contract i leakage audit |
| dokumentno pitanje | BM25, dense retrieval, RRF, reranker, grounded generator | crystal similarity embedding |
| cross-site supervised target | FL porodice uz privacy/security kontrole | sama zabrana centralizacije ili marketinška oznaka „federated“ |

## Gde su detalji i izvori

Ova mapa povezuje postojeće teorijske module i ne zamenjuje njihove definicije ili primarne izvore:

- [scope i pravila odlučivanja](../00-scope.md);
- [mapa pipeline funkcija](../01-pipeline-decision-map.md);
- [klasični ML](../classical/02-classical-ml.md);
- [globalni retrieval, ANN i ranking](../retrieval/03-global-retrieval-ann-ranking.md);
- [precizno pairwise poređenje](../pairs/04-precise-pairwise.md);
- [periodični encoderi](../deep/05-periodic-crystal-encoders.md);
- [metric learning i evaluacija](../deep/06-metric-learning-and-evaluation.md);
- [lokalni SLM i RAG](../language/07-local-slm-rag.md);
- [spoljni API i security](../language/08-api-llm-security.md);
- [cross-format i eligibility podataka](../data/09-cross-format-eligibility.md).

Potpuna tematska mapa 22-stranog CCDC white paper-a ostaje u glavnom hemijskom kursu `chemistry-foundations/docs/projekat/22-whitepaper-tokovi-fl.md`. White paper motiviše vendor tokove, lifecycle, structure–property, polymorph-risk i federativne teme. Ne propisuje 2CDC algoritam, DAP/CQS semantiku, gold standard, stack ili realizacioni redosled.
