# 20. Evaluacija i naučna validacija

**Prioritet: MORAŠ.** Model je validan tek kada je jasno koju naučnu tvrdnju test meri, ko je dao referentni odgovor i na kojim slučajevima sistem sme da kaže „ne znam“.

## 20.1 Počni od claim-a

Primer lošeg cilja:

> Praviti AI koji nalazi slične kristale.

Primer proverljivog cilja:

> Za query CIF sa pouzdano percipiranim ligandnim grafom, sistem vraća najmanje 95% ekspertski potvrđenih DAP scaffold analogues u prvih 100 kandidata na held-out compound-family testu, uz dokumentovanu standardizaciju.

Drugi claim je ograničen, merljiv i navodi populaciju, task, metric i uslove važenja.

## 20.2 Ground truth je višeslojna odluka

Jedan par može biti sličan na jednom, a različit na drugom nivou. Ekspertska odluka zato može razdvojiti dimenzije kao što su:

- composition/component identity;
- molecular graph/scaffold;
- DAP motif;
- metal direktno koordinisan DAP-u;
- donor set i coordination geometry;
- conformation;
- lattice/cell;
- whole-crystal packing;
- interaction network;
- task-specific relevantnost;
- sigurnost, obrazloženje i dokaz na kom se odluka zasniva.

Jedan binary `similar=true` skriva neslaganje i ne omogućava dijagnostiku.

## 20.3 Ekspertska anotacija

Sledeći redosled je obrazovni primer dobro kontrolisane anotacije, ne plan konkretnog produkcionog procesa:

1. napiši rubricu sa pozitivnim, negativnim i ambiguous primerima;
2. sakrij model score i identitet metode od anotatora;
3. najmanje dva stručna anotatora nezavisno pregledaju critical set;
4. meri agreement po label komponenti;
5. neslaganje ide na adjudication, ne na tiho majority preglasavanje;
6. čuvaj obrazloženje, atomski mapping/evidence i confidence;
7. verzioniši rubricu i reanotiraj slučajeve pogođene promenom definicije.

White paper i imena ConQuest upita nisu ground truth. Oni daju kontekst i candidate set; label zahteva operational definition.

## 20.4 Evaluation skup

Koristan evaluacioni skup obično kombinuje više vrsta slučajeva:

- **sanity/self pairs**: isti objekat i ekvivalentni encoding;
- **easy negatives**: potpuno različit sastav/graf;
- **hard negatives**: ista formula ili scaffold, ali drugi metal/geometry/packing;
- **near positives**: isto coordination okruženje uz supstituent/promenu setting-a;
- **edge cases**: salts, solvates, Z′>1, disorder, missing H, unknown bonds, polymers;
- **out-of-scope**: records bez podataka potrebnih za claim;
- **future/temporal**: noviji CSD release ili publikacije, ako licenca dozvoli.

Lokalni `search1/search2` je koristan za DAP-focused stress test, ali nije dovoljan za globalnu validaciju.

## 20.5 Split bez curenja

Nasumičan record split može staviti povezane refcode redeterminations, istu compound family ili istu publikaciju u train i test. Biraj grupisanje prema claim-u:

| Claim | Minimalna split jedinica |
|---|---|
| nov analog istog scaffold-a | compound/entry family |
| novi scaffold | scaffold family |
| nova crystal form | compound + solid-form family |
| buduća literatura | vreme/publication |
| druga institucija/lab | source/laboratory, gde je dostupno i dozvoljeno |

Pre split-a radi dedup/family analysis nad podacima koji su dozvoljeni za taj postupak; ne koristi test labels za tuning.

## 20.6 Baselines pre ML-a

Svaki složeni model se poredi sa transparentnim baseline-ima:

- exact formula/element filter;
- exact/substructure graph search;
- Morgan/ECFP + Tanimoto;
- simple metal + donor-set rule;
- torsion/RMSD baseline na istom mapping-u;
- reduced-cell candidate search;
- licencirani CCDC packing similarity ili peer-reviewed reprodukovan baseline, gde je dozvoljeno.

Ako ML ne popravlja relevantnu metricu uz prihvatljivu cenu/objašnjivost, nije opravdan samo zato što je moderniji.

## 20.7 Metrike po proizvodu

### Global search

- ANN candidate recall@N prema exact/high-cost candidate skupu — koliko je aproksimativna faza propustila pre reranking-a; ovo nije mera ekspertske relevantnosti;
- end-to-end recall@k prema ekspertski potvrđenoj relevantnosti — koliko relevantnih zapisa je u vrhu konačne liste;
- precision@k — koliko prikazanih je relevantno;
- MAP ili nDCG — kvalitet celog rangiranja;
- coverage/abstention rate;
- latency p50/p95 i index freshness;
- error rate po parse/representation statusu.

Za count-based precision/recall prijavi **query-macro** i **pooled-micro** rezultat sa eksplicitnim brojiocem i imeniocem. MAP i nDCG prijavi kao prosek query-level vrednosti; svaki alternativni ponderisani agregat mora imati navedenu formulu i težine, a ne samo oznaku „micro“. Pre otvaranja test skupa definiši politiku za query bez ijednog relevantnog zapisa: recall je tada nedefinisan, pa takve upite ne pretvaraj proizvoljno u nulu ili jedinicu; prijavi njihov broj/udeo odvojeno i oceni false-positive ili abstention ponašanje. Denominator i politika moraju pratiti svaku tabelu rezultata.

### Pair comparator

- agreement sa ekspertskim component labels;
- rank correlation kada eksperti daju poredak;
- classification precision/recall za validirane thresholds;
- calibration error i Brier score **samo** za kalibrisanu predikciju verovatnoće ekspertske relevantnosti za precizno definisan claim; sirovi similarity score i input/evidence confidence nisu verovatnoće i za njih Brier score nema ovu interpretaciju;
- symmetry: \(s(A,B)=s(B,A)\) gde metric to zahteva;
- invariance/metamorphic pass rate;
- coverage i razlog neuporedivosti;
- runtime/memory po pair kategoriji.

Clustering se ocenjuje tek nakon definisanja ciljnih grupa; lepa heatmap nije naučna validacija.

## 20.8 Slice analiza

Ukupni prosek može sakriti ozbiljnu grešku. Prijavi rezultate po:

- metal element/group i coordination number;
- metal-free vs metal-containing;
- single vs multi-component;
- salt/solvate/hydrate/co-crystal;
- ordered vs disordered;
- 3D complete vs incomplete;
- bond-perception confidence;
- molecule size/flexibility;
- space-group/crystal-system, bez pretvaranja kategorije u uzrok;
- data-quality bands i source period.

Missing SMILES/failed conversion je poseban slice, jer lokalni dokazi ne podržavaju nekritičku MCAR pretpostavku; uzrok missingness-a tek treba eksplicitno ispitati.

## 20.9 Calibration i abstention

Sistem treba da razlikuje:

- **similarity score** — vrednost određene metrike;
- **probability of expert relevance** — kalibrisana procena za konkretan claim;
- **confidence in input/representation** — kvalitet dokaza;
- **coverage** — deo objekta koji je uopšte poređen.

Visok fingerprint score uz unknown metal bonds može imati visok 2D score, ali nizak confidence za coordination claim. Ako ključno polje nedostaje, ispravan izlaz može biti `not assessed`.

Kalibrator i prag za abstention uče se na zasebnom **calibration skupu**, odvojenom od testa po istoj compound-family/grouping logici kao ostali split-ovi. Ako validation skup istovremeno služi za kalibraciju, to mora biti unapred navedeno i sve odluke se zamrzavaju pre jednokratne evaluacije na netaknutom testu.

Neizvesnost nikada ne prikazuj kao neoznačen broj `confidence`. Uz procenu navedi etiketu izvora i scope-a, na primer `input/representation uncertainty`, `model/finite-data uncertainty`, `calibration uncertainty` ili `out-of-domain`; interval dodatno označi nivoom, metodom i jedinicom uzorkovanja.

Za svaki abstention prag nacrtaj **coverage–risk krivu**: coverage je udeo slučajeva na koje sistem odgovara, a risk unapred definisana greška među tim odgovorima. Prag izaberi na calibration skupu, zatim na testu prijavi krivu i intervale poverenja ukupno i po kritičnim slice-ovima. Sama coverage bez greške zadržanih odgovora nije dokaz bezbednog abstention-a.

## 20.10 Uncertainty i ponovljivost

Objavljeni rezultat mora biti poveziv sa populacijom i verzijom podataka nad kojima je dobijen, granicom licence, pravilima standardizacije i reprezentacije, verzijom modela/metrike, stohastičkim uslovima i razlozima isključivanja. To su kategorije dokaza potrebne za ponavljanje i tumačenje rezultata, a ne propisana šema artefakata ili okruženja.

Uz svaki primarni rezultat obavezno prijavi **point estimate i unapred definisan interval poverenja**. Pre evaluacije zapiši nivo intervala, metod i nezavisnu jedinicu uzorkovanja. Bootstrap ne radi nad pojedinačnim hitovima ili parovima kada dele isti query ili hemijsku porodicu: resampluj na nivou nezavisnog query-ja, odnosno compound-family grupe koja odgovara claim-u, da korelisani primeri ne glume dodatni uzorak.

Za stohastičke modele/ANN indekse pokreni unapred određen skup ponovljenih seed-ova. Baseline i kandidat koriste iste split-ove i, gde je primenljivo, iste seed-ove; prijavi point estimate razlike i **paired delta** interval poverenja. Varijacija kroz seed-ove opisuje algoritamsku ponovljivost, ali se seed-ovi ne smeju tretirati kao nezavisni hemijski uzorci niti zamenjuju grouped bootstrap.

## 20.11 Ilustrativna evidencija tvrdnji

Sledeća tabela je nenormativan primer kako se činjenica odvaja od scope-a i dokaza; njene kolone nisu projektna schema.

| Tvrdnja | Precizan scope | Dokaz/izvor | Lokalni test | Confidence | Datum/verzija | Izuzeci |
|---|---|---|---|---|---|---|
| `4M` znači svi metali | ConQuest atom group | CCDC vodič | oba `.cqs` | high | query snapshot | ne dokazuje koordinaciju |
| search2 je podskup search1 | lokalni export | refcode set diff | 2038/2110 | high | SHA-256 snapshot | samo dostavljeni fajlovi |

Za interpretativni claim koristi dve nezavisne stručne potvrde gde je moguće. Za ponašanje CCDC alata i licence koristi zvanični, datirani izvor.

## 20.12 Koliko jak claim dokazi podržavaju

Spremnost za naučni claim nije jedna univerzalna kapija. Snaga tvrdnje zavisi od toga da li su populacija i prava poznati, reprezentacija hemijski proverena, poređenje izvedeno na nezavisnim podacima, intervali i kritični slice-ovi prijavljeni, a ograničenja i failure modes jasno opisani. Slabost bilo kog od tih dokaza sužava claim ili zahteva abstention; ovo nije release plan niti lista faza realizacije.

## 20.13 Provera znanja

1. Zašto nije dovoljan jedan binary similarity label?
2. Koji leakage nastaje ako redeterminations završe u train i test?
3. Zašto se retrieval meri recall@k, a ne samo accuracy?
4. Koja je razlika između score-a, probability i evidence confidence-a?
5. Kada model treba da abstain?

??? success "Odgovori"
    1. Meša različite naučne nivoe i skriva razlog/nesigurnost.  
    2. Model može prepoznati gotovo isti family record umesto da generalizuje.  
    3. Search ima rangiranu listu i mnogo neizabranih kandidata; accuracy ne meri da li su relevantni vraćeni u vrhu.  
    4. Metric similarity, kalibrisana relevantnost i pouzdanost ulaza/modela su odvojene veličine.  
    5. Kada claim nema potrebne podatke, representation je ambiguous/out-of-domain ili confidence ispod unapred definisanog praga.

**Kriterijum prolaza:** možeš da napišeš testable claim, formiraš leakage-safe evaluation i objasniš svaki exclusion, threshold i failure slice.
