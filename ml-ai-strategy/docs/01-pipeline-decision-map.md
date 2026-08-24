# Mapa pipeline-a i algoritamskih odluka

## Zašto se problem rastavlja na poslove

Jedan CIF prolazi kroz zadatke koji nemaju isti output ni istu definiciju greške. Parser može biti sintaksno tačan, retrieval može imati visok recall, a konačni ranking ipak biti hemijski pogrešan. Isto tako, dobar property regressor ne mora davati koristan similarity embedding.

Zato se „optimalan AI“ bira **po čvoru pipeline-a**, ne za problem u celini.

| Čvor | Stvarni zadatak | Referentna porodica metoda | Složenija alternativa i uslov primenljivosti | Glavna metrika |
|---|---|---|---|---|
| ingest | bezbedno i verno pročitati CIF | dictionary-aware deterministički parser | nema ML zamene | fixture pass rate, tačnost polja, failure coverage |
| standardizacija | napraviti verzionisane hemijske/kristalne prikaze | eksplicitna pravila + provenance | ML samo kao označen predlog za review | invariance i round-trip/loss testovi |
| hard filter | sprovesti element/formula/quality/licence uslove | inverted/relational index | nema razloga za generativni model | tačna jednakost sa nezavisnim expected skupom: FP = 0 i FN = 0 |
| candidate retrieval | brzo sačuvati relevantne kandidate | ECFP/count fingerprint + exact Tanimoto | validirani learned embedding + ANN | candidate recall@N, latency, memory |
| reranking | poređati mali candidate set po izabranom značenju sličnosti | rastavljivi ručno definisani score-ovi | supervised learning-to-rank kada postoje odgovarajući labeli | nDCG@k, MAP, recall@k, slice rezultati |
| precizno poređenje | dokazati gde su dva CIF-a ista/različita | graph mapping, RMSD, packing i interaction algoritmi | metric/deep model samo kao dodatni signal | ekspertna pair odluka + evidence coverage |
| property/quality | predvideti eksplicitno definisan target | mean/dummy + linear/RF/boosting | GNN ili ensemble kada podaci opravdaju | MAE/RMSE ili AUROC/AUPRC + calibration/OOD |
| jezički sloj | prevesti nameru i objasniti već izračunate dokaze | forme, template-i i rule-based tekst | lokalni SLM ili API LLM sa alatima | schema validity, task success, factuality, leakage |

## Čvorovi u kojima ML nije optimalan

### CIF parsing

CIF je strukturisani format sa dictionary semantikom, loop-ovima, missing tokenima i numeričkim neizvesnostima. Parser mora deterministički vratiti vrednost, poreklo i status ili eksplicitnu grešku. LLM može kasnije objasniti parserov nalaz, ali ne sme biti parser niti autoritet za atomsku petlju.

Diferencijalno poređenje dva nezavisna parsera može da otkrije nekompatibilnosti. Svaka evaluirana interpretacija mora imati deklarisano poreklo i zabeleženo neslaganje, dok se reflection i proizvoljni tekstualni blokovi ne smeju automatski pretvarati u prompt.

### Standardizacija

Normalizacija komponenti, naboja, tautomerije, aromatičnosti, disorder-a, setting-a i periodičnih slika menja ono što svaki kasniji algoritam vidi. Zato su pravila, verzije i loss report primarni. Klasifikator eventualno može označiti sumnjiv slučaj za pregled, ali ne sme nevidljivo prepisati source of truth.

### Hard filteri

Upit „Cu direktno koordinisan mapiranom DAP N3 mestu“ je graph predicate, ne verovatnoća koju treba približno pogađati. Inverted indeksi, range indeksi i exact graph provera imaju prednost kada je uslov egzaktan. ML služi tek kada je cilj fuzzy ranking ili kada stručni label zaista opisuje verovatnoću.

Sam `precision = 1` nije dovoljan: neispravan filter koji vrati prazan skup nema false positive, ali može izgubiti sve validne rezultate. Filter evaluator zato pre retrieval testa poredi **ceo skup ID-jeva** sa nezavisno anotiranim očekivanim skupom: `actual_eligible_ids == expected_eligible_ids`, odnosno FP = 0 i FN = 0. Fixture-i obavezno pokrivaju najmanje jedan stvarni positive, legitimni zero-hit upit, granične vrednosti i missing/unknown/invalid/failure statuse. Tek posle ovog gate-a exact-after-filter oracle ocenjuje ANN nad dokazano ispravnim filtriranim skupom.

## Visok-recall candidate retrieval

[ECFP](https://doi.org/10.1021/ci100050t) je brz i interpretabilan prikaz lokalnih molekulskih okruženja. Exact Tanimoto nad verzionisanim sparse/count ili bit fingerprintom zato daje transparentnu 2D referencu. On ne vidi kristalno pakovanje i zavisi od standardizacije, radijusa, bit dužine, count/binary i stereo politike.

Ako korpus ili broj upita zahteva aproksimaciju, [HNSW](https://doi.org/10.1109/TPAMI.2018.2889473) je kandidat za ANN indeks nad kompatibilnim dense vektorom. ANN je infrastrukturna optimizacija: meri se koliko rezultata exact pretrage preživi u candidate set-u. Ne dokazuje da je embedding hemijski ispravan.

**Algoritamske zavisnosti:**

1. exact pretraga nad istom reprezentacijom definiše oracle prema kome se meri ANN;
2. HNSW ili drugi ANN ima smisla tek kada se može izmeriti kriva `recall–latency–memory` prema tom oracle-u;
3. learned embedding predstavlja zasebnu hipotezu o sličnosti i ne sme se pomešati sa infrastrukturnom aproksimacijom;
4. ligand, coordination environment i crystal/packing modovi nisu ista metrika i zahtevaju odvojeno definisanu reprezentaciju i evaluaciju.

## Reranking kao supervised problem

Reranker dobija mali candidate set i rastavljive features, na primer:

```text
ECFP Tanimoto + common-core coverage + charge/stereo flags
+ metal/donor/CN/geometry agreement
+ mapped RMSD/torsion features
+ packing/contact evidence kada je primenljivo
+ quality compatibility i missing-status indikatori
```

Za mali ili srednji tabelarni skup relevantnih ekspertskih parova, linearni/logistički model, Random Forest i gradient-boosted trees su ozbiljne referentne porodice. [XGBoost](https://doi.org/10.1145/2939672.2939785) je dizajniran za skalabilni tree boosting i sparse input, ali njegova prednost mora biti izmerena na **grouped** split-u i uz jednak tuning budžet.

Learning-to-rank optimizuje grupisane query liste, ali zahteva query-level labele ili preferencije. Nezavisni `similar/not similar` parovi odgovaraju kalibrisanom pair classifier-u; iz njih se ne može pretpostaviti ranking label koji nije anotiran.

## Precizni pairwise dokaz

Validno poređenje dva kristala ima sledeću zavisnost provera:

1. component assignment;
2. exact/substructure/MCS atom mapping;
3. coordination-environment poređenje;
4. rigidno poravnanje mapiranih atoma i RMSD/coverage;
5. periodično packing poređenje;
6. interaction-network poređenje;
7. odvojena quality compatibility procena.

[COMPACK](https://doi.org/10.1107/S0021889804027074) pokazuje kako se molecular packing može porediti preko relativnih položaja/orijentacija bez oslanjanja na identičan space-group ili cell zapis. Noviji [PAC rad](https://doi.org/10.1107/S1600576722009670) dodatno naglašava reproducibilnost i oblik poređenih klastera. To su referentni precizni algoritmi; learned metric može ubrzati candidate pruning ili dati dodatni signal, ali mora dokazati invariance i ne sme sakriti atom/molecule correspondence.

## Property modeli nisu similarity modeli

Property model ima smisla samo uz definisan target, jedinicu, uslove, measurement/computation provenance i validan split. [Matbench](https://doi.org/10.1038/s41524-020-00406-3) je na svojim materials-property zadacima pokazao da descriptor/AutoML pristupi mogu biti vrlo konkurentni na manjim skupovima, dok su crystal GNN modeli dobijali relativnu prednost sa više podataka; to nije univerzalna granica niti direktan benchmark za organske CSD kristale.

[OOD benchmark iz 2024](https://doi.org/10.1038/s41524-024-01316-4) pokazuje da slučajni split može preceniti generalizaciju i da savremeni GNN modeli mogu znatno oslabiti na strukturno out-of-distribution testovima. Zato se nijedan property predictor ne koristi kao similarity oracle, a svaki model dobija compound/scaffold/family/time split prema claim-u.

## SLM/LLM kao kontrolisan interfejs

Dozvoljene uloge su:

- natural-language zahtev → strogo validiran interni query DSL;
- RAG nad odobrenom dokumentacijom i data dictionary-jima;
- objašnjenje strukturisanog evidence objekta;
- draft izveštaja sa citiranim field/atom/result identifikatorima;
- predlog naredne provere koji korisnik ili deterministički alat odobrava.

Zabranjene podrazumevane uloge su:

- parsiranje neproverenog CIF-a „iz teksta“;
- računanje geometrije ili simetrije bez alata;
- izmišljanje missing polja, veza, oxidation state-a ili reference;
- konačna ekspertska labela bez evidence-a;
- slanje restricted strukture eksternom API-ju bez permission gate-a.

## Worked primer: jedan DAP/Zn upit

Korisnik traži strukture slične Zn kompleksu sa N3 donorskim džepom.

1. Parser deterministički izdvaja komponente, koordinate i provenance.
2. Hard filter zahteva Zn u coordination entity-ju; „Zn negde u formuli“ nije dovoljno.
3. ECFP/Tanimoto vraća visok-recall ligand kandidate.
4. Exact graph mapping proverava centralni pyridine N i dva imine N.
5. Coordination reranker poredi da li ista tri mapirana N koordiniraju isti Zn, donor set, CN i geometriju.
6. Packing grana radi samo za validne periodične modele i ostaje zaseban score.
7. LTR model može naučiti query-mode-specific ordering tek iz ekspertskih preferencija.
8. SLM/LLM sastavlja objašnjenje iz strukturisanih rezultata; ne menja score niti izmišlja vezu.

Rezultat je lista sa razlogom za svaki rang, a ne rečenica „AI kaže 92% slično“.

## Kriterijumi fer poređenja složenijeg modela

Složeniji metod može se smatrati opravdanim samo ako:

1. pobeđuje zamrznuti baseline na unapred definisanoj primarnoj metrici;
2. ne pogoršava kritični worst-slice preko dogovorene margine;
3. paired interval razlike isključuje praktično beznačajnu korist;
4. calibration/OOD i abstention testovi prolaze;
5. latencija, memorija i operativni trošak staju u budžet;
6. rezultat zadržava potreban atomski/periodični evidence;
7. model, embedding i data flow prolaze license/privacy review.

Ako uslov nije ispunjen, jednostavniji metod nije „privremeno lošiji“ — on ostaje primereniji za dokazani scope.
