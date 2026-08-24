# Klasični ML: baseline-i koji zaista imaju smisla

## Glavni zaključak

Klasični ML nije „zastarela alternativa“ deep modelima. Posebno je primeren kada je input rastavljiva tabela deskriptora, labela ima malo ili srednje mnogo, a rezultat mora biti jeftin i proverljiv.

Relevantne porodice metoda su:

- regularizovana linearna/logistička regresija kao transparentna referenca;
- Random Forest i Extra Trees za nelinearne tabularne odnose;
- gradient-boosted trees, pre svega XGBoost/LightGBM/CatBoost porodica, za složenije tabularne odnose;
- SVM/SVR za male i srednje skupove sa pažljivo definisanim kernelom;
- Gaussian Process Regression za male skupe property skupove gde je važna lokalna prediktivna raspodela;
- kNN kao transparentna locality referenca;
- PLS/PCR samo za odgovarajuće niskorangirane, jako korelisane kontinuirane deskriptore;
- calibration i conformal sloj iznad point modela, uz eksplicitne pretpostavke.

Nijedan od njih nije CIF parser, exact substructure matcher, dokaz packing identiteta niti univerzalna mera sličnosti.

Pre formiranja bilo koje supervised matrice obavezan je centralni [cross-format i lifecycle eligibility ugovor](09-cross-format-eligibility.md): svi pogledi istog entry-ja ostaju u istoj split grupi, missing format se ne briše tihim `inner join`-om, a training/calibration/final-test primaju samo eksplicitno dozvoljena lifecycle stanja i rights scope.

## 2.1 Semantički ugovor pre algoritma

Supervised poređenje nije definisano dok za svaki uzorak nisu poznate sledeće kategorije:

| Kategorija | Naučna svrha |
|---|---|
| identitet i grupe | sprečavaju da isti compound, scaffold, solid-form family ili publikacija pređu granicu split-a |
| reprezentacija i missing status | određuju koje su features stvarno dostupne i pod kojom definicijom |
| target, definicija i adjudikacija | vezuju vrednost za konkretan zadatak, anotatore i stepen pouzdanosti |
| uslovi i provenance | razlikuju merenje, račun i eksperimentalni kontekst |
| rights i dozvoljena namena | određuju da li uzorak sme u trening, kalibraciju i evaluaciju |

Tačan tehnički zapis je implementacioni izbor; ove semantičke kategorije ostaju potrebne nezavisno od njega.

Nasumični row split nije prihvatljiv ako bliske redeterminations, isti compound, scaffold ili polymorph family mogu preći u oba skupa. [MoleculeNet](https://doi.org/10.1039/C7SC02664A) je pokazao da scaffold split predstavlja stroži test molekulske generalizacije od random split-a; [materials OOD benchmark](https://doi.org/10.1038/s41524-024-01316-4) pokazuje isti širi problem redundanse kod kristalnih skupova.

## 2.2 Obavezni dummy i linearni baseline-i

### Dummy

Za regresiju:

- sredina/medijana trening target-a;
- group-aware mean kada je to dozvoljen deployment scenario.

Za klasifikaciju:

- uvek većinska klasa;
- stratified random;
- jednostavno pravilo poput `ECFP Tanimoto >= t`, ali prag se bira samo na validation skupu.

Model koji ne pobeđuje dummy ili jedno stručno pravilo nije pokazao dodatnu prediktivnu vrednost.

### Linearna/logistička regresija

Model:

\[
\hat y=\beta_0+\sum_j\beta_jx_j,
\qquad
P(y=1\mid x)=\sigma(\beta_0+\beta^Tx).
\]

Koristi:

- kalibrisana relevantnost para iz malog broja razumljivih score komponenti;
- property baseline nad standardizovanim deskriptorima;
- interpretable quality-risk model;
- pair preference model kada su features definisane kao razlike.

L1/Lasso bira sparse skup, L2/Ridge stabilizuje korelisane features, a Elastic Net kombinuje oba efekta. Koeficijent nije hemijski uzrok: korelacija, transformacija i interakcije određuju tumačenje.

**Ilustrativni 2CDC primer:** logistički model prima ECFP similarity, common-core coverage, donor-set match, RMSD, packing coverage, quality flags i missing-status indikatore. Output je kalibrisana verovatnoća tačno definisane ekspertske labele, ne „procenat univerzalne sličnosti“.

## 2.3 k-nearest neighbors

kNN predviđa iz lokalnog susedstva u izabranoj metrici. Za regresiju je jednostavan oblik:

\[
\hat y(x)=\frac{\sum_{i\in N_k(x)}w_i y_i}{\sum_{i\in N_k(x)}w_i},
\qquad
w_i=\frac{1}{(d_i+\epsilon)^p}.
\]

### Gde je koristan

- sanity test „slični trening primeri imaju sličan target“;
- mali lokalni property baseline;
- objašnjenje kroz konkretne susede;
- detekcija da query nema bliskih referenci.

### Granice

- rezultat potpuno zavisi od reprezentacije i distance;
- sparse high-dimensional prostor pati od concentration efekata;
- predikcija bez indeksa skenira ceo trening skup;
- velika hemijska rupa se ne pretvara u pouzdanu ekstrapolaciju izborom većeg `k`;
- sused iz iste leaked family daje lažno dobar rezultat.

Za 2CDC kNN je baseline i explanation aid, ne konačni globalni ranking engine.

## 2.4 Random Forest

[Random Forest](https://doi.org/10.1023/A:1010933404324) gradi mnogo stabala nad bootstrap uzorcima i nasumičnim podskupovima features, pa agregira njihove rezultate.

### Zašto odgovara projektu

- uči nelinearne pragove i interakcije bez ručnog zadavanja formule;
- radi sa mešavinom kontinuiranih, binarnih i kodiranih kategorijalnih deskriptora;
- zahteva manje podataka i tuning-a od mnogih dubokih modela;
- inference je lak za lokalno izvršavanje;
- out-of-bag procena je koristan razvojni signal, iako ne zamenjuje grouped test.

### Gde ga probati

1. pair relevance classifier/reranker nad unapred izračunatim evidence features;
2. regression/classification property model za mali/srednji skup;
3. quality-review prioritet, pod uslovom da target označava review odluku;
4. meta-model koji bira da li je skupa packing analiza potrebna — samo ako false-negative rizik ima strogu kontrolu.

### Granice

- stabla loše ekstrapoliraju izvan opsega trening target-a;
- veliki broj sparse fingerprint bitova može biti manje efikasan od odgovarajućeg kernel/linear modela;
- impurity feature importance je pristrasan prema features sa više potencijalnih split-ova i uz korelisane prediktore ([Strobl et al.](https://doi.org/10.1186/1471-2105-8-25));
- sirove vote frakcije nisu automatski kalibrisane verovatnoće;
- RF ne daje atom mapping ni kristalografski dokaz.

Koristi held-out permutation importance po grupama i atomske/substrukturne evidence koje proizvodi deterministički sloj; ne prevodi tree importance u uzročnu hemiju.

## 2.5 Extra Trees

[Extremely Randomized Trees](https://doi.org/10.1007/s10994-006-6226-1) dodatno randomizuju izbor split pragova i tipično koriste ceo razvojni uzorak umesto bootstrap-a. Više randomizacije može smanjiti varijansu i ubrzati trening, uz moguć veći bias.

RF i ExtraTrees čine informativno upareno poređenje na istim outer fold-ovima jer različito menjaju bias i varijansu. ExtraTrees nije „RF upgrade“; relativni rezultat zavisi od target-a i features.

## 2.6 Gradient-boosted trees

Boosting sekvencijalno dodaje slaba stabla koja popravljaju trenutni loss. [XGBoost](https://doi.org/10.1145/2939672.2939785) uvodi regularizovan i sparsity-aware skalabilni sistem. [LightGBM](https://proceedings.neurips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree) koristi histogram-based optimizacije, gradient-based one-side sampling i exclusive feature bundling, dok [CatBoost](https://proceedings.neurips.cc/paper/2018/hash/14491b756b3a51daac41c24863285549-Abstract.html) koristi ordered boosting i poseban tretman kategorija.

| Porodica | Tipična primenljivost | Poseban oprez |
|---|---|---|
| XGBoost | opšti tabularni classifier/regressor | sparse/missing putanja može naučiti source artefakt |
| LightGBM | veliki tabularni skup i LambdaMART ranking | leaf-wise rast može overfit-ovati mali skup |
| CatBoost | stvarne kategorije uz numeričke features | ordered encoding ne sprečava compound/family leakage |

### Gde je najjači kandidat

- heterogeneous tabular deskriptori;
- pairwise relevance sa mnogo nelinearnih interakcija;
- property prediction kada labela nije dovoljno velika za end-to-end GNN;
- LambdaMART/listwise reranking kada postoje query-grupisane graded relevance labele.

Na 30 QSAR skupova je [XGBoost poređen sa RF i neuralnim mrežama](https://doi.org/10.1021/acs.jcim.6b00591), ali rezultat iz bioaktivnosti ne prenosi se automatski na kristalno pakovanje. [MoleculeNet](https://doi.org/10.1039/C7SC02664A) dodatno podržava da kernel SVM i tree ensemble metode ostaju ozbiljni kandidati u data-scarce režimu.

### Rizici

- lakše overfit-uje tuning skup od RF-a;
- native missing handling može naučiti laboratoriju/source umesto hemije;
- class weights menjaju score i kalibraciju;
- SHAP objašnjava model nad datim feature space-om, ne dokazuje fizički mehanizam;
- listwise objective bez stvarnih query grupa optimizuje pogrešan problem.

## 2.7 SVM i SVR

[Support-vector machines](https://doi.org/10.1007/BF00994018) traže marginu u originalnom ili kernel-induced prostoru.

### Dobar režim

- stotine do nekoliko hiljada pouzdanih labela;
- descriptor ili fingerprint input sa smislenim kernelom;
- jasna binarna odluka ili smooth regression target;
- potrebna jaka alternativna metoda za small-data režim.

Linear SVM odgovara veoma sparse visokoj dimenziji. RBF SVM hvata nelinearnost, ali zahteva scaling i pažljiv `C/gamma` nested tuning. Specijalizovan Tanimoto/min-max kernel može biti hemijski smisleniji za nenegativne fingerprint/count features; njegovu kernel upotrebu u hemijskom kontekstu razmatraju [Ralaivola et al.](https://doi.org/10.1016/j.neunet.2005.07.009), ali konkretna implementacija mora potvrditi pozitivnu definitnost i numeričku semantiku izabranog prikaza.

### Granice

- kernel matrica i tuning slabo skaliraju na vrlo velike skupove;
- decision margin nije verovatnoća;
- objašnjenje je teže od malog linearnog ili tree modela;
- kalibracija zahteva izdvojene podatke i grupisanje.

## 2.8 PLS/PCR i latentni linearni modeli

PCA/PCR biraju smerove varijanse u (X), dok PLS komponente koriste i kovarijansu sa target-om. [Klasičan prikaz PCA/PLS veze](https://doi.org/10.1016/0898-5529(89)90004-3) objašnjava matematičku osnovu.

### Koristi

- mali skup sa mnogo korelisanih kontinuiranih deskriptora;
- spektroskopski ili drugi dense measurement vektori;
- linearna, stabilna i pregledna latentna regresija.

### Ne koristiti kao default

- nad heterogenim bitovima, kategorijama i missing statusima bez opravdane transformacije;
- za automatsku tvrdnju da latentna komponenta ima jedno hemijsko značenje;
- za packing identitet ili graph matching.

Broj komponenti bira se unutar inner CV-a; preprocessing se fituje samo na trening fold-u.

## 2.9 Gaussian Process Regression

[Gaussian Processes for Machine Learning](https://gaussianprocess.org/gpml/chapters/) definiše distribuciju nad funkcijama kroz kernel. GPR vraća srednju predikciju i model-based varijansu.

### Gde je koristan

- desetine do niske hiljade skupih, dobro definisanih property labela;
- aktivno učenje ili Bayesian optimization kada je akviziciona odluka deo cilja;
- SOAP/REMatch ili drugi validan kernel nad strukturama;
- scenario gde lokalna smoothness pretpostavka ima hemijski smisao.

### Oprez

- exact trening tipično zahteva (O(n^3)) vreme i (O(n^2)) memoriju;
- predictive variance nije automatski kalibrisana greška pod distribution shift-om;
- loš kernel daje precizno izraženu pogrešnu pretpostavku;
- sparse/variational aproksimacije menjaju metod i zahtevaju posebnu validaciju.

## 2.10 Unsupervised i anomaly metode

| Metod | Dozvoljena uloga | Ne dokazuje |
|---|---|---|
| PCA | linearna eksploracija, collinearity i outlier kandidat | klastere hemijske istine |
| UMAP/t-SNE | vizuelni prikaz lokalnog susedstva | globalne distance i stabilne klase |
| k-means | grubo particionisanje odgovarajućeg Euclidean embedding-a | prirodne kristalne familije |
| agglomerative clustering | dendrogram uz eksplicitnu distance/linkage politiku | jedinstven „tačan“ broj klastera |
| HDBSCAN | promenljiva gustina i noise kandidati | hemijsku nevalidnost |
| Isolation Forest | multivariate anomaly triage | da je zapis pogrešan |
| One-Class SVM/LOF | lokalni OOD signal | pouzdanu naučnu abstention odluku bez kalibracije |

Za pairwise aplikaciju clustering se radi nad jednom validiranom distance komponentom ili eksplicitno naučenim task-specific rastojanjem. Dendrogram nad neobjašnjenim weighted average score-om samo vizuelno skriva problem.

## 2.11 Calibration, intervali i abstention

### Kalibracija klasifikatora

Ako model vraća score, „0,8“ nije verovatnoća dok reliability/Brier/log-loss test to ne podrži. [Niculescu-Mizil i Caruana](https://doi.org/10.1145/1102351.1102430) porede Platt scaling i isotonic regression za različite klasifikatore.

- Platt/logistic calibration je stabilnija kada calibration set nije velik.
- Isotonic je fleksibilniji, ali može overfit-ovati mali calibration set.
- Calibration split mora poštovati iste compound/family granice kao test.
- Promena prevalence-a ili domena može pokvariti kalibraciju.

Za retku pozitivnu klasu obavezni su precision–recall prikaz i AUPRC; [Saito i Rehmsmeier](https://doi.org/10.1371/journal.pone.0118432) objašnjavaju zašto ROC prikaz može biti intuitivno varljiv pod velikim imbalance-om.

### Conformal prediction

[Conformal prediction](https://jmlr.org/papers/v9/shafer08a.html) može nadograditi različite point modele prediction set-om ili intervalom sa marginalnim coverage jamstvom pod exchangeability uslovima.

To znači:

- coverage se proverava empirijski ukupno i po kritičnim grupama;
- porodično, vremensko ili source pomeranje može prekršiti potrebnu pretpostavku;
- `90% interval` ne znači da je svaka hemijska podgrupa pokrivena 90%;
- interval ne popravlja pogrešan target, label noise ili licencni problem.

## 2.12 Režimi količine podataka

Broj nezavisnih grupa utiče na razuman kapacitet modela, ali ne postoji univerzalna numerička granica:

| Režim | Primerene hipoteze | Glavni rizik |
|---|---|---|
| veoma malo nezavisnih label grupa | pravila, deskriptivna analiza, regularizovani linearni modeli; GPR ako kernel ima smisla | nestabilna procena i prevelik tuning prostor |
| mali ili srednji skup | linear/Elastic Net, RF/ExtraTrees, SVM/SVR, GPR i pažljivo regularizovan boosting | family leakage i overfitting izbora modela |
| veći heterogeni skup | linear/sparse reference, tree ensembles i, uz odgovarajuću reprezentaciju, neuralni modeli | source artefakti i neujednačena pokrivenost domena |
| veoma veliki skup sa validnim 3D signalom | end-to-end ili pretrained graph modeli mogu postati opravdani uz tabularne reference | trošak, OOD ponašanje i nedokazana task-specifična korist |

Efektivni (n) je broj nezavisnih compound/scaffold/solid-form grupa, ne broj skoro dupliranih CIF redova. Matbench nalaz o relativnoj prednosti graph modela sa većim skupovima je koristan signal, ali njegovi pretežno inorganic/DFT zadaci nisu direktna granica za 2CDC.

## 2.13 Ilustrativni problemski obrasci

### Pair relevance

**Target:** ekspertna ordinalna ocena za tačno jedan režim pretrage, pri čemu nula označava nerelevantan par, jedan povezan par, a dva snažno podudaranje.

**Primerene porodice:** rastavljivi stručni score, linearni ili ordinalni model i tree ensembles. Query-grupisani learning-to-rank ima smisla samo ako labele zaista predstavljaju rangiranje ili preferencije unutar query-ja.

**Split:** query i compound/solid-form family ne prelaze fold granicu. Strukture se prvo dodeljuju particijama, pa se parovi prave unutar particije; pair-random split bi mogao da ostavi `A–B` u train-u, a `A–C` u testu.

**Metrike:** nDCG@k, recall@k, MAP, kalibracija pair odluke, latencija i worst-slice po metalu/disorder-u/missing 3D.

### Property regression

**Target:** jedna property vrednost sa jedinicom, uslovima i measurement/computation provenance-om.

**Primerene porodice:** dummy i regularizovana linearna referenca, PLS kada su features odgovarajuće, tree ensembles, SVR i GPR kada veličina skupa i kernel to opravdavaju.

**Metrike:** MAE kao primarna, RMSE za velike greške, group bootstrap interval, calibration/coverage intervala i OOD slice.

### Quality review triage

**Target:** da li je u eksplicitno definisanom profilu potreban stručni pregled, ne „CIF je dobar/loš“.

**Primerene porodice:** rule-based alerts, logistički model i tree ensembles.

**Ograničenje:** potreban je visok recall na unapred definisanim high-risk slučajevima; model prioritizuje pregled i ne može automatski proglasiti strukturu naučno validnom.

## 2.14 Matrica primenljivosti

| Posao | Transparentna referenca | Porodice koje vredi porediti | Uslov primenljivosti |
|---|---|---|---|
| 2D retrieval | exact ECFP/count + Tanimoto | optimizovan exact, representation-matched ANN, learned embedding | ANN meri aproksimaciju iste reprezentacije; learned embedding je nova semantička hipoteza |
| tabular pair relevance | logistički model | RF/ExtraTrees, kalibrisan GBDT, LambdaMART | LambdaMART zahteva graded query labele |
| mali property regression | mean + Ridge | RF/ExtraTrees/GBDT, SVR, GPR | izbor zavisi od efektivnog broja grupa, kernela i uncertainty cilja |
| veći property skup sa validnim 3D | descriptor model | tree ensemble ili periodic/geometric GNN | 3D model mora pokazati korist na grouped/OOD evaluaciji |
| review triage | stručna pravila | kalibrisan linearni ili tree model, conformal reject sloj | target je prioritet pregleda, ne naučna validnost |
| OOD signal | distance do trening domena | ensemble, descriptor OOD ili specialized deep OOD metod | signal mora biti validiran prema konkretnom shift-u |

Ako složeniji model nema materijalno bolji grouped/OOD rezultat od jednostavnije reference, podaci ne opravdavaju dodatnu složenost.

## 2.15 Leakage-safe evaluacija

Zavisnosti validne supervised evaluacije su:

1. zamrzni raw/provenance snapshot i target definiciju;
2. deduplikuj i napravi compound/scaffold/solid-form/publication/time grupe;
3. odvoji netaknuti temporalni ili release test;
4. koristi spoljašnji grouped CV za procenu, a unutrašnji grouped CV za preprocessing, features i hyperparameter izbor;
5. calibration radi iz posebnih grupa ili grouped out-of-fold predikcija;
6. fituj imputer, scaler, PCA/PLS i feature selection samo na training delu fold-a;
7. pragove zamrzni pre finalnog testa;
8. bootstrap i interval razlike računaj po query-ju ili compound family-ju, ne po međuzavisnim parovima.

[Varma i Simon](https://doi.org/10.1186/1471-2105-7-91) pokazuju bias kada ista CV procedura i bira model i prijavljuje njegovu grešku. [DataSAIL](https://doi.org/10.1038/s41467-025-58606-8) formalizuje similarity-aware split za one- i two-entity ML probleme. To je neposredno relevantno parovima: veliki broj kombinacija ne proizvodi isti broj nezavisnih dokaza.

Evaluacioni izveštaj obuhvata:

- primarnu metriku i paired interval prema baseline-u;
- macro prosek po query-ju;
- najgori unapred definisan metal/form/disorder/missing-3D slice;
- calibration i coverage–risk krivu;
- latency, memoriju i procenat abstention-a;
- sve neuspele i neuporedive ulaze, ne samo uspešne redove.
