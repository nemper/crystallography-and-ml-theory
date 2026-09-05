# 20. Evaluacija i naučna validacija

**Prioritet: MORAŠ.** Model je validan tek kada je jasno koju naučnu tvrdnju test meri, ko je dao referentni odgovor i na kojim slučajevima sistem sme da kaže „ne znam“.

**Preduslovi i prvi prolaz:** završi [reprezentacije](14-reprezentacije.md), [sličnost](15-slicnost.md), [parove](19-parovi.md) i osnovni [dohvat kandidata](18-globalna-pretraga.md). Ovde najpre savladaj tvrdnju, stručnu ocenu, split i metrike (§20.1–20.8), pa kalibraciju i grupnu neizvesnost (§20.9–20.10). Neuralne modele nije potrebno prethodno čitati. [Povezani primer Q–B–C–D](povezani-primer.md#evaluacija) daje mali zajednički slučaj za sve te korake.

## 20.1 Počni od claim-a

Primer lošeg cilja:

> Praviti AI koji nalazi slične kristale.

Primer proverljivog cilja:

> Za query CIF sa pouzdano percipiranim ligandnim grafom, sistem vraća najmanje 95% ekspertski potvrđenih DAP scaffold analogues u prvih 100 kandidata na held-out compound-family testu, uz dokumentovanu standardizaciju.

Drugi claim je ograničen, merljiv i navodi populaciju, task, metric i uslove važenja.

Proveri i matematičku ostvarivost cilja: ako upit ima \(R_q\) relevantnih zapisa, najveći mogući recall@100 iznosi \(\min(100,R_q)/R_q\). Sa 200 relevantnih zapisa ni savršeno rangiranje ne može preći 50% recall@100. Primer sa 95% zato zahteva odgovarajuću populaciju i broj relevantnih zapisa; broj 95% ovde nije dokazana performansa niti projektni zahtev iz `2CDC`.

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

Kod učenja iz parova nije dovoljno nasumično podeliti redove `(A, B)`. Ako je `(A, B)` u treningu, a `(A, C)` u testu, model već poznaje strukturu A. Za claim o **novim strukturama ili familijama** najpre podeli osnovne strukture/familije, pa formiraj parove unutar odgovarajućih split-ova. Namerno testiranje novih kombinacija već poznatih struktura jeste drugi legitiman cilj, ali ga tako i nazovi. Milion parova nastalih od malog broja struktura ne predstavlja milion nezavisnih hemijskih opažanja.

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

- ANN candidate recall@N prema exhaustive exact oracle-u iste reprezentacije i metrike, nad istim korpusom, hard filterima i tie/self-match politikom — koliko je aproksimativna faza propustila pre reranking-a; ovo nije mera ekspertske relevantnosti;
- end-to-end recall@k prema ekspertski potvrđenoj relevantnosti — koliko relevantnih zapisa je u vrhu konačne liste;
- precision@k — koliko prikazanih je relevantno;
- MAP ili nDCG — kvalitet celog rangiranja;
- coverage/abstention rate;
- latency p50/p95 i index freshness;
- error rate po parse/representation statusu.

Za jedan upit sa \(R_q>0\) relevantnih zapisa u dozvoljenom korpusu, ako je među prvih \(k\) rezultata \(h_q\) relevantno, onda su \(\mathrm{recall@k}=h_q/R_q\) i, kada postoji \(k\) rangiranih mesta, \(\mathrm{precision@k}=h_q/k\). Na primer, 4 relevantna pogotka u prvih 10 uz ukupno 8 relevantnih daju recall 0,50 i precision 0,40. Ako se vraća manje od \(k\) rezultata, unapred odredi da li prazna mesta računaju kao promašaji ili koristiš imenilac broja vraćenih; te dve konvencije nisu ista metrika. Neocenjen kandidat nije automatski negativan: nepotpuna ekspertska anotacija ograničava i procenu ukupnog \(R_q\), pa prijavi obuhvat anotacije.

Za count-based precision/recall prijavi **query-macro** i **pooled-micro** rezultat sa eksplicitnim brojiocem i imeniocem. MAP i nDCG prijavi kao prosek query-level vrednosti; svaki alternativni ponderisani agregat mora imati navedenu formulu i težine, a ne samo oznaku „micro“. Pre otvaranja test skupa definiši politiku za query bez ijednog relevantnog zapisa: recall je tada nedefinisan, pa takve upite ne pretvaraj proizvoljno u nulu ili jedinicu; prijavi njihov broj/udeo odvojeno i oceni false-positive ili abstention ponašanje. Denominator i politika moraju pratiti svaku tabelu rezultata.

### Pair comparator

- agreement sa ekspertskim component labels;
- rank correlation kada eksperti daju poredak;
- classification precision/recall za validirane thresholds;
- calibration error i Brier score za **predikciju verovatnoće** ekspertske relevantnosti za precizno definisan claim; prethodna kalibracija nije uslov da se ove metrike izračunaju — njima se mogu oceniti i nekalibrisane verovatnosne prognoze. Sirovi similarity score i input/evidence confidence nisu automatski verovatnoće;
- symmetry: \(s(A,B)=s(B,A)\) gde metric to zahteva;
- invariance/metamorphic pass rate;
- coverage i razlog neuporedivosti;
- runtime/memory po pair kategoriji.

Clustering se ocenjuje tek nakon definisanja ciljnih grupa; lepa heatmap nije naučna validacija.

Za binarni ishod \(y_i\in\{0,1\}\) i predikciju \(p_i=P(y_i=1)\), uobičajeni binarni Brier score je \(\frac{1}{m}\sum_{i=1}^{m}(p_i-y_i)^2\); manja vrednost je bolja. Ako sistem predvidi 0,8 za jedan stvarno relevantan par, doprinos je \((0,8-1)^2=0,04\). To ocenjuje verovatnosnu prognozu, a ne samo kalibraciju: na rezultat utiče i koliko model razlikuje relevantne od nerelevantnih slučajeva. Za proveru kalibracije zato posmatraj i slaganje predviđenih verovatnoća sa opaženim učestalostima, uz dovoljno nezavisnih primera ([scikit-learn: Brier score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html), [kalibracija verovatnoća](https://scikit-learn.org/stable/modules/calibration.html)).

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
- **probability of expert relevance** — modelom iskazana procena verovatnoće za konkretan claim, čija se kalibracija posebno proverava;
- **confidence in input/representation** — kvalitet dokaza;
- **coverage** — deo objekta koji je uopšte poređen.

Visok fingerprint score uz unknown metal bonds može imati visok 2D score, ali nizak confidence za coordination claim. Ako ključno polje nedostaje, ispravan izlaz može biti `not assessed`.

Kalibrator i prag za abstention uče se na zasebnom **calibration skupu**, odvojenom od testa po istoj compound-family/grouping logici kao ostali split-ovi. Ako validation skup istovremeno služi za kalibraciju, to mora biti unapred navedeno i sve odluke se zamrzavaju pre jednokratne evaluacije na netaknutom testu.

Neizvesnost nikada ne prikazuj kao neoznačen broj `confidence`. Uz procenu navedi etiketu izvora i scope-a, na primer `input/representation uncertainty`, `model/finite-data uncertainty`, `calibration uncertainty` ili `out-of-domain`; interval dodatno označi nivoom, metodom i jedinicom uzorkovanja.

Za svaki abstention prag nacrtaj **coverage–risk krivu**: coverage je udeo slučajeva na koje sistem odgovara, a risk unapred definisana greška među tim odgovorima. Prag izaberi na calibration skupu, zatim na testu prijavi krivu i intervale poverenja ukupno i po kritičnim slice-ovima. Sama coverage bez greške zadržanih odgovora nije dokaz bezbednog abstention-a.

## 20.10 Uncertainty i ponovljivost

### Tri grupe i upareni bootstrap {#grupno-resamplovanje}

**Pitanje:** da li uočena razlika metoda zavisi od toga koje smo hemijske grupe uzorkovali? *Bootstrap* ponovo bira grupe iz opaženog skupa **sa vraćanjem**. U nastavnoj tabeli svaka nezavisna familija ima jedan evaluacioni upit. Metrika je query-level nDCG, veće je bolje, a svaka familija dobija jednaku težinu:

| Nezavisna grupa | Referentna metoda R | Nova metoda N | Razlika N−R |
|---|---:|---:|---:|
| F₁ | 0,6 | 0,8 | +0,2 |
| F₂ | 0,8 | 0,7 | −0,1 |
| F₃ | 0,4 | 0,6 | +0,2 |
| prosek | 0,6 | 0,7 | +0,1 |

U svakoj replici biramo tri grupe, i **iste izabrane grupe** koristimo za obe metode:

| Izbor sa vraćanjem | Prosek R | Prosek N | Uparena razlika |
|---|---:|---:|---:|
| F₁, F₁, F₃ | 1,6/3 = 0,5333 | 2,2/3 = 0,7333 | +0,2 |
| F₂, F₂, F₃ | 2,0/3 = 0,6667 | 2,0/3 = 0,6667 | 0 |
| F₁, F₂, F₃ | 0,6 | 0,7 | +0,1 |
| F₂, F₂, F₂ | 0,8 | 0,7 | −0,1 |

Ponovljena F₁ ulazi dva puta sa svim svojim pripadajućim ocenama; ne proglašava se novom nezavisnom familijom. Raspodela ovih razlika približava varijabilnost procene dobitka usled uzorkovanja grupa iz ciljne populacije, uslovno na fiksirane modele i evaluacioni protokol. **Četiri prikazane replike i tri grupe nisu pouzdana procena intervala.** Ako familije imaju različit broj upita, unapred odredi da li cilj daje jednaku težinu familijama ili upitima i u svakoj replici ponovo izračunaj baš taj agregat. Promena težina menja veličinu koju procenjujemo.

### Zašto parovi nisu nezavisni redovi

Za App 2 razmotri parove (A,B), (C,B), (C,D):

```text
A —— B —— C —— D
  AB   CB   CD
```

Grupisanje samo po prvom članu odvaja AB od CB/CD, iako AB i CB dele B. Za tvrdnju o oba nova endpointa najpre odvoji osnovne strukture/familije, pa formiraj parove. U ovom malom grafu svi parovi su povezani preko endpointa i čine samo jednu povezanu grupu zavisnosti, ne tri nezavisna opažanja. Ako stvarni graf ima jednu veliku povezanu komponentu, običan bootstrap komponenti ne može stvoriti nezavisne podatke; potrebna je evaluaciona konstrukcija ili postupak koji odgovara dyadic zavisnosti. *Dyadic* znači da opažanje pripada paru objekata. Detalji istog principa su u [ML evaluaciji](https://github.com/nemper/crystallography-and-ml-theory/blob/main/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md).

### Kako čitati interval razlike

Neka je \(\Delta=\mathrm{metrika}(N)-\mathrm{metrika}(R)\), uz veću bolju metriku. Sledeći intervali su zasebne nastavne ilustracije, nisu izračunati iz četiri replike iznad:

| Nalaz | Dopušteno tumačenje |
|---|---|
| tačkasta razlika +0,10 | opažena prednost; sama nema iskaz o neizvesnosti |
| unapred definisan interval [0,02; 0,18] | podržava pozitivnu razliku na izabranom nivou pod pretpostavkama postupka; praktični značaj se proverava zasebno |
| interval [−0,02; 0,08], unapred zadana margina neinferiornosti 0,03 | donja granica je iznad −0,03: podrška neinferiornosti, uz odgovarajući unapred izabran nivo i jednostrani/dvostrani protokol; nema dokaza superiornosti |
| interval [−0,20; 0,30] | preširok za zaključak o superiornosti ili neinferiornosti sa marginom 0,03 |

Margina se ne bira nakon gledanja rezultata. Interval evaluacione metrike odnosi se na populacioni učinak, a [conformal interval](https://github.com/nemper/crystallography-and-ml-theory/blob/main/ml-ai-strategy/docs/02-classical-ml.md#split-conformal) na novi cilj pod drugim pretpostavkama. Pokrivenost predikcije i udeo slučajeva na koje sistem odgovara takođe su različite veličine.

### Referentni sloj: reproduktivnost i seed-ovi

Objavljeni rezultat mora biti poveziv sa populacijom i verzijom podataka nad kojima je dobijen, granicom licence, pravilima standardizacije i reprezentacije, verzijom modela/metrike, stohastičkim uslovima i razlozima isključivanja. [Granica teorijskih primera](kako-koristiti.md#teorijski-i-referentni-sloj) važi i za ove kategorije dokaza.

Uz svaki primarni rezultat obavezno prijavi **point estimate i unapred definisan interval poverenja**. Pre evaluacije zapiši nivo intervala, metod i nezavisnu jedinicu uzorkovanja. Bootstrap ne radi nad pojedinačnim hitovima ili parovima kada dele isti query ili hemijsku porodicu: resampluj na nivou nezavisnog query-ja, odnosno compound-family grupe koja odgovara claim-u, da korelisani primeri ne glume dodatni uzorak.

Za stohastičke modele/ANN indekse pokreni unapred određen skup ponovljenih seed-ova. Baseline i kandidat koriste iste split-ove i, gde je primenljivo, iste seed-ove; prijavi point estimate razlike i **paired delta** interval poverenja. Varijacija kroz seed-ove opisuje algoritamsku ponovljivost, ali se seed-ovi ne smeju tretirati kao nezavisni hemijski uzorci niti zamenjuju grouped bootstrap.

## 20.11 Ilustrativna evidencija tvrdnji

Sledeća tabela je nenormativan primer kako se činjenica odvaja od scope-a i dokaza; njene kolone nisu projektna schema.

| Tvrdnja | Precizan scope | Dokaz/izvor | Lokalni test | Confidence | Datum/verzija | Izuzeci |
|---|---|---|---|---|---|---|
| `4M` je ConQuest grupa „svih metala“ | softverska grupa uključuje i Ge/Sb | CCDC vodič | oba `.cqs` | high | query snapshot | ne dokazuje koordinaciju niti univerzalnu taksonomiju |
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
