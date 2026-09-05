# ML/AI od nule: pojmovi, matematika i prvi proračuni

Ovaj modul ne pretpostavlja iskustvo sa treniranjem modela. Dovoljni su osnovni račun sa razlomcima i spremnost da se svaka oznaka poveže sa konkretnim primerom. Cilj je da razumeš sledeća poglavlja i možeš da obrazložiš izbor metode; za to nije potrebno da prvo napišeš neuronsku mrežu.

Hemijske pojmove — atom, veza, ligand, konformer, ćelija i kristalno pakovanje — učiš paralelno u hemijskom kursu. Ovde je dovoljno znati da ista formula ili isti molekul ne moraju značiti isti raspored u kristalu.

## 1. Od pitanja do podatka

**Algoritam** je postupak kojim se ulaz pretvara u rezultat. Mnogi važni algoritmi ništa ne uče: parser čita zapis prema pravilima, a geometrijski algoritam izračunava rastojanje. **Mašinsko učenje (ML)** podešava parametre modela pomoću primera. **AI** je širi naziv; upotreba tog naziva ne govori koji se zadatak zaista rešava.

U projektu postoje dva osnovna pitanja:

- **Pretraga:** za jedan upit pronađi i poređaj korisne strukture iz dozvoljenog korpusa, odnosno skupa zapisa koji se pretražuje.
- **Poređenje parova:** za svaki par iz uploadovanog skupa utvrdi po kojim osobinama se strukture podudaraju ili razlikuju.

Pre izbora modela moraš odrediti šta je **uzorak**. Za predikciju svojstva to može biti jedna čvrsta forma; za poređenje je uzorak par struktura; za rangiranje je važna cela lista kandidata jednog upita. Dva različita reda u tabeli zato nisu nužno dva nezavisna primera.

**Feature/deskriptor** je ulazna osobina, npr. broj atoma, vrsta metala ili izračunata sličnost dva grafa. **Target** je ono što pokušavamo da predvidimo. **Labela/oznaka** je poznata target vrednost konkretnog primera, dobijena merenjem, stručnom procenom ili jasno označenim pravilom.

| Zadatak | Ilustrativni target | Izlaz |
|---|---|---|
| regresija | izmerena osobina sa jedinicom i uslovima | broj, npr. procena gustine |
| klasifikacija | da li par ima isti definisani koordinacioni motiv | klasa ili procena verovatnoće klase |
| ordinalna predikcija | različito / povezano / isto po jednom vodiču | uređene kategorije; razmaci između njih nisu nužno jednaki |
| rangiranje | koji kandidat je relevantniji za dati upit | uređena lista |
| grupisanje | koji objekti su bliski u izabranoj reprezentaciji | klasteri; sami po sebi nisu stručne labele |

U **nadgledanom učenju** postoje ciljne labele. **Nenadgledano učenje** istražuje strukturu ulaza bez takvih labela. **Samonadgledano učenje** stvara trening zadatak iz samih podataka, npr. rekonstrukciju sakrivenog dela. Rekonstrukcija ili isti zapis pod rotacijom ne stvaraju automatski oznaku da su dva različita kristala stručno relevantna jedan drugom.

## 2. Reprezentacija određuje šta može da se vidi

Reprezentacija je način zapisivanja objekta za algoritam. Razlikuj sledeće pojmove:

| Pojam | Značenje | Ograničenje |
|---|---|---|
| molekulski graf | atomi su čvorovi, deklarisane ili kurirane veze su ivice | sam ne sadrži kristalno pakovanje |
| fingerprint | kod prisustva ili broja izabranih grafovskih osobina | sažima graf i može imati sudare kodova |
| 3D koordinate | položaji izabranih atoma | bez ćelije i periodičnog konteksta opisuju samo izdvojeni sklop |
| periodični graf | čvorovi i ivice sa odnosima prema periodičnim slikama | zavisi od pouzdanog kristalnog modela i pravila susedstva |
| embedding | vektor u naučenom ili projektovanom prostoru | blizina važi za definiciju tog prostora, ne za svako značenje sličnosti |

**Bit-vektor** sadrži nule i jedinice. **Count vektor** čuva broj pojavljivanja. **Sparse** zapis čuva pretežno nenulte pozicije; **dense** zapis čuva sve komponente. Hashiranje preslikava osobine u kodove ograničene veličine, pa različite osobine mogu završiti pod istim kodom — to je **collision**.

Primer: dva polimorfa istog molekula mogu imati isti 2D fingerprint. Nijedan model koji dobija samo taj identičan ulaz ne može iz njega rekonstruisati koju od te dve forme posmatra. Bolji algoritam ne vraća informaciju koju je reprezentacija odbacila.

## 3. Kako čitati matematičke oznake

**Skalar** je jedan broj. **Vektor** je uređena lista brojeva, npr. \(x=(3,4)\). **Matrica** je pravougaona tabela; u tabelarnom ML-u red često predstavlja uzorak, a kolona jednu osobinu. U kristalografiji matrica može predstavljati i bazu ćelije: značenje određuje kontekst, ne sama oznaka.

Oznaka \(\sum_{i=1}^{N}a_i\) znači „saberi vrednosti od prve do N-te“. Indeks \(i\) bira primer ili atom, a \(j\) često bira osobinu. \(\hat y\) je predviđeno \(y\). \(\theta\) predstavlja skup parametara koji se uče. \(\mathbb{1}[uslov]\) je 1 kada uslov važi, inače 0.

**Skalarni proizvod** sabira proizvode odgovarajućih komponenti:

\[
x^T y=\sum_j x_jy_j.
\]

**Euklidska norma** je dužina vektora: \(\|x\|_2=\sqrt{\sum_jx_j^2}\), pa je \(\|(3,4)\|_2=5\). **Rastojanje** dva vektora je \(\|x-y\|_2\). **L2 normalizacija** deli nenulti vektor njegovom dužinom, npr. \((3,4)\mapsto(0{,}6,0{,}8)\). Nulti vektor nema takvu normalizaciju i zahteva zaseban status/politiku.

Cosine sličnost je

\[
s_{cos}(x,y)=\frac{x^Ty}{\|x\|_2\|y\|_2}.
\]

Poredi smer, a ne veličinu vektora; za opšte realne vektore ima opseg od −1 do 1. Za L2-normalizovane vektore jednak je skalarnom proizvodu, a kvadrirano euklidsko rastojanje je \(2-2s_{cos}\). Isti poredak pod tim uslovima ne znači da proizvoljni nenormalizovani cosine, L2 i inner-product indeks daju iste susede.

**Sličnost** obično raste sa podudaranjem; **rastojanje** opada. Matematička **metrika** dodatno zadovoljava nenegativnost, simetriju, nulu samo za isti objekat i nejednakost trougla: \(d(A,C)\le d(A,B)+d(B,C)\). U tekstu „evaluaciona metrika“ znači meru uspeha poput recall-a i ne mora biti rastojanje. Ni svaki nazvani „similarity score“ ne definiše matematičku metriku.

**Transponovanje** \(X^T\) zamenjuje redove i kolone. Množenje matricom može predstavljati promenu koordinata. Rotacija čuva dužine; proper rotacija ne pretvara objekat u njegovu ogledalsku sliku. **SVD** razlaže matricu na ortogonalne smerove i nenegativne faktore njihovog skaliranja. U Kabsch algoritmu to pomaže pronalaženju najbolje rotacije već mapiranih tačaka; SVD sam ne utvrđuje koji atom odgovara kojem.

## 4. Šta znači trenirati model

Jednostavan linearni model je

\[
\hat y=\beta_0+\sum_j\beta_jx_j.
\]

\(\beta_0\) je intercept, odnosno predikcija kada su sve ulazne osobine nula, a \(\beta_j\) određuje uticaj osobine uz ostale fiksne. Model ne poznaje hemijski uzrok samo zato što je neka težina velika. Korelisane osobine mogu preuzimati međusobni signal.

**Funkcija gubitka (loss)** određuje koliko je predikcija loša prema labeli. Za regresiju primer je \((y-\hat y)^2\). Za binarnu labelu \(y\in\{0,1\}\) i predviđenu verovatnoću \(p\), binarna cross-entropy je

\[
\ell(y,p)=-y\log p-(1-y)\log(1-p).
\]

Ona snažno kažnjava samouverenu pogrešnu predikciju. Logistička funkcija \(\sigma(t)=1/(1+e^{-t})\) pretvara realni izlaz u broj između 0 i 1. **Broj u tom opsegu još ne dokazuje kalibraciju.**

Treniranje bira parametre koji smanjuju prosečni trening gubitak. **Regularizacija** dodaje cenu prevelike ili nestabilne složenosti:

\[
\min_\theta\;\frac1N\sum_i\ell(y_i,f_\theta(x_i))+\lambda\Omega(\theta).
\]

\(\min\) znači traženje najmanje vrednosti. \(\Omega\) je kazna, a \(\lambda\) kontroliše njenu jačinu. **Gradijent** opisuje lokalni smer i brzinu promene gubitka po parametrima; gradient descent pomera parametre približno u suprotnom smeru. Neuronske mreže računaju gradijente kroz slojeve pomoću backpropagation-a. Tree modeli imaju drugačije postupke učenja; ne koristi svaki ML algoritam backpropagation.

**Parametri** se uče iz trening primera. **Hiperparametri** određuju postupak ili kapacitet, npr. dubinu stabla, broj slojeva ili jačinu regularizacije. Njih biraš pomoću razvojnog/validation skupa, ne finalnog testa. Jedan **epoch** je prolaz kroz trening primere, **batch** je podskup obrađen u jednom koraku, a **inference** je primena već naučenog modela.

Razdvajanje matrice uzoraka, targeta, `fit` i `predict` operacija možeš proveriti i u [zvaničnom uvodu u scikit-learn](https://scikit-learn.org/stable/getting_started.html); kod nije preduslov za nastavak ovog modula.

Ako model dobro pamti trening, a loše radi na novim grupama, to je **overfitting**. Ako je prejednostavan da uhvati bitan odnos i loš je već na treningu, moguć je **underfitting**. **Baseline** je referentni postupak: srednja vrednost, jednostavno pravilo ili proverena jednostavnija metoda. Bez njega ne znaš da li dodatna složenost donosi korist.

## 5. Zašto podaci moraju da se podele

| Skup | Čemu služi | Šta se njime ne radi |
|---|---|---|
| trening | učenje parametara, imputacije i transformacija | ne daje nezavisnu završnu procenu |
| validation / razvoj | izbor modela i hiperparametara | ne proglašava se netaknutim finalnim testom |
| kalibracija | podešavanje verovatnoća i, po protokolu, pragova | ne koristi se za završnu nepristrasnu procenu |
| finalni test | procena zamrznute metode na novim primerima | ne bira model, prag, fingerprint ili najbolji seed |

Za male skupove **cross-validation (CV)** više puta menja koji deo razvoja služi za proveru. **Grouped CV** drži povezane primere u istoj grupi. **Nested CV** razdvaja unutrašnji izbor modela od spoljašnje procene; nije dovoljno više puta ponoviti isti test i prijaviti najbolji rezultat.

**Leakage** nastaje kada model ili odluka o modelu dobije informaciju koja prema izabranoj tvrdnji nije smela biti dostupna. Primer: CIF, MOL i MOL2 istog jedinjenja raspodeljeni između treninga i testa. Drugi primer: par A–B je u treningu, a A–C u testu koji navodno meri sasvim nove strukture. Broj kombinacija raste, ali objekat A je već poznat.

**Generalizacija** znači uspeh na ciljanim novim primerima. Test nad novim upitom i poznatim korpusom meri drugo pitanje od testa u kome su obe strukture nove. **OOD** označava primere van raspodele/domena na kojima je model razvijan, npr. novu metalnu porodicu. Nasumični split ne predstavlja automatski takav test. Detalje i uslove za parove daje [modul o evaluaciji](06-metric-learning-and-evaluation.md).

**Missing podatak** nije nula: neizračunat RMSD nije savršeno poravnanje. Imputacija procenjuje nedostajuću ulaznu feature vrednost prema pravilima fitovanim na treningu; ne sme izmišljeni score prikazati kao izmereni naučni dokaz. Njeno poreklo i status ostaju odvojeni.

## 6. Prvi rešeni primer: fingerprint i tri nivoa pretrage

Sledeći mali skup je **izmišljen radi računanja**; nije rezultat `2CDC` pretrage. Query ima uključene bitove \(Q=\{1,2,3\}\), kandidat A \(\{1,2,4\}\), a B \(\{1,2,3,5\}\). Binarni Tanimoto je presek podeljen unijom:

\[
T(Q,A)=2/4=0{,}5,\qquad T(Q,B)=3/4=0{,}75.
\]

B je bliži po tom fingerprint-u. Još nismo dokazali da ima traženu koordinaciju ili packing. Ako su oba fingerprinta prazna, formula je \(0/0\): konkretna biblioteka/profil mora deklarisati ponašanje, a prazan ili neuspešno napravljen fingerprint ne sme postati dokaz istog molekula.

Pretpostavimo da exact top-3 po toj metrici čine A, B i C, dok približni indeks vrati A, C i D. **Infrastrukturni recall** je \(2/3\): pronađena su dva od tri referentna suseda.

Sada pretpostavimo da je ekspert, po sasvim određenom koordinacionom pitanju, označio B, D i E kao relevantne u potpuno ocenjenom malom skupu. Candidate skup A, C, D sadrži samo D, pa je **ekspertni candidate recall** \(1/3\). Reranker može podići D na prvo mesto, ali ne može vratiti B ili E kojih nema među kandidatima.

Zato exact znači „tačno izračunato po datoj definiciji“, a ne „potpuno naučno ispravno za svako pitanje“. ANN je *approximate nearest-neighbor* pretraga: aproksimira susede, ne daje novu definiciju hemijske relevantnosti.

## 7. Kako merimo uspeh i neizvesnost

Za binarnu odluku definiši pozitivni događaj. **TP** su ispravno pronađeni pozitivni, **FP** pogrešno proglašeni pozitivni, **FN** propušteni pozitivni, a **TN** ispravno odbačeni negativni.

\[
precision=\frac{TP}{TP+FP},\qquad
recall=\frac{TP}{TP+FN},\qquad
F_1=\frac{2TP}{2TP+FP+FN}.
\]

Ako u potpuno ocenjenom malom korpusu postoje tri relevantna kandidata, a top-3 sadrži dva relevantna i jedan nerelevantan, precision@3 i recall@3 su oba \(2/3\). Isti precision pri većem broju postojećih relevantnih rezultata mogao bi imati mnogo manji recall. Nulti denominator zahteva deklarisanu politiku i broj takvih slučajeva; nije prilika da se uspeh veštački uveća.

**Accuracy** je udeo svih ispravnih odluka. Ako je samo 1% parova pozitivan, model „uvek negativno“ ima 99% accuracy i nulti recall pozitivnih. **PR kriva** prati precision/recall pri promeni praga, a **ROC kriva** true-positive prema false-positive stopi. Površina ispod krive zavisi od izbora krive i protokola; average precision i trapezoidna PR-AUC nisu ista numerička definicija.

Rangiranje dodatno meri **gde** su dobri rezultati. Jedna česta nDCG definicija koristi ocenu \(g_r\) na rangu \(r\), dobitak \(2^{g_r}-1\) i umanjenje za nižu poziciju:

\[
DCG@k=\sum_{r=1}^{k}\frac{2^{g_r}-1}{\log_2(r+1)},\qquad
nDCG@k=\frac{DCG@k}{IDCG@k}.
\]

IDCG@k koristi najboljih k poznatih ocena iz celog dozvoljenog evaluacionog korpusa za upit; ne dobija se samo preslaganjem trenutno vraćenog top-k. U zamišljenom korpusu sa ukupno tri kandidata ocenjena kao `2,0,1`, taj redosled daje DCG@3 jednak \(3+0+1/2=3{,}5\); ideal `2,1,0` daje \(3+1/\log_2 3\approx3{,}631\), pa je nDCG@3 približno 0,964. To nije 96,4% verovatnoće relevantnosti. Kada nema poznatih relevantnih rezultata, IDCG je nula i protokol mora odvojeno definisati obradu tog upita. Nepotpuno stručno označavanje ograničava i denominator i zaključak.

**MRR** prosečava recipročni rang prvog relevantnog rezultata. **AP** prosečava precision vrednosti na rangovima relevantnih rezultata prema eksplicitno definisanom skupu poznatih pozitivnih; **MAP** je prosek AP-a po upitima. Za sve navedi cutoff, politiku neocenjenih kandidata i query-ja bez pozitivnih.

Definicije precision/recall, MAP i rangovske evaluacije razrađuje autorski udžbenik [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html). Ovaj mali račun koristi unapred navedenu gain funkciju; druga funkcija može promeniti nDCG.

Za regresiju, \(e_i=\hat y_i-y_i\):

\[
MAE=\frac1N\sum_i|e_i|,\qquad
RMSE=\sqrt{\frac1N\sum_i e_i^2}.
\]

Obe imaju jedinicu target-a; RMSE jače naglašava velike greške. To nisu kristalografski RMSD iste definicije: RMSD meri geometrijsko odstupanje mapiranih tačaka.

**Kalibracija** znači da predviđena verovatnoća odgovara učestalosti događaja: među mnogim nezavisnim slučajevima sa procenom oko 0,8, približno 80% treba da bude pozitivno. To nije tvrdnja o „80% istim atomima“. Brier score prosečava \((p_i-y_i)^2\), a log-loss prosečava cross-entropy; oba proveravaju kvalitet probabilističkih predikcija, ali zavise i od drugih osobina osim same kalibracije.

**Abstention/uzdržavanje** znači da sistem ne donosi traženi zaključak. **Coverage** tada označava udeo slučajeva za koje ga donosi, a **risk** grešku među tim slučajevima. Ako tačnost raste samo zato što sistem odbaci najteže primere, mora se videti cena u coverage-u. Druga značenja coverage-a su udeo mapiranih atoma i raspoloživost reprezentacije; uvek navedi koji denominator koristiš.

**Interval poverenja** opisuje varijabilnost procene po protokolu uzorkovanja. Nije garancija za svaki sledeći kristal. **Bootstrap** ponavlja uzorkovanje nezavisnih jedinica sa vraćanjem, pa ista jedinica može biti izabrana više puta; za međuzavisne parove te jedinice nisu obični redovi. **Slice** je unapred definisana podgrupa, npr. zapisi sa disorder-om. Prosek svih grupa može sakriti loš rezultat na retkoj važnoj grupi. **Ablacija** uklanja jednu komponentu metoda da bi se utvrdilo šta doprinosi. **Non-inferiority** proverava da metoda nije lošija preko unapred prihvatljive margine, npr. kada istovremeno znatno smanjuje trošak.

## 8. Od linearne funkcije do GNN-a i attention-a

Neuronska mreža slaže naučene linearne transformacije i nelinearne funkcije. Bez nelinearnosti bi niz linearnih slojeva ostao jedna linearna transformacija. **Encoder** pretvara ulaz u reprezentaciju; **head** iz nje daje konkretnu predikciju. Isti encoder sa drugim head-om i trening ciljem predstavlja drugo naučno pitanje.

**GNN (graph neural network)** uči nad čvorovima i ivicama. U jednom **message-passing** sloju svaki čvor prikuplja poruke suseda, sabira/prosečava ih ili koristi drugi postupak nezavisan od redosleda, pa ažurira svoje osobine. Posle više lokalnih slojeva informacija može dolaziti sa više grafovskih koraka. To još ne garantuje da model vidi celu strukturu ili očuva svu važnu informaciju.

Formalni okvir poruka i readout-a u hemijskim grafovima daje [Gilmer et al., Neural Message Passing for Quantum Chemistry](https://proceedings.mlr.press/v70/gilmer17a.html); periodične slike zahtevaju dodatnu konstrukciju iz crystal-encoder modula.

**Pooling/readout** sabira ili drugačije agregira čvorove u vektor celog objekta. Suma se menja kada se broj istovetnih kopija poveća; sredina se u tom jednostavnom slučaju ne menja. U periodičnom sistemu mean pooling ipak ne dokazuje supercell invariance jer se pre njega mogu promeniti graf, normalizacija ili globalne osobine.

**Attention** daje različite naučene težine porukama/kandidatima. **Softmax** pretvara logite \(a_j\) u pozitivne težine \(e^{a_j}/\sum_k e^{a_k}\), čiji je zbir 1. Attention kaže šta model koristi u tom računu, ne dokazuje fizičku vezu ili tačno atom mapping uparivanje. Transformer je porodica mreža koja koristi attention; jezički transformer i periodični crystal transformer nemaju isti ulaz ni isti target.

Originalni [Attention Is All You Need](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html) uvodi transformer za jezički zadatak; njegova arhitektura nije sama po sebi dokaz kristalne relevantnosti.

**Invariansa** znači da se izlaz ne promeni pod određenom transformacijom, npr. dužina veze pri rotaciji. **Ekvivarijansa** znači da se izlaz promeni na propisan način, npr. vektor sile se rotira zajedno sa strukturom. **Metamorfni test** menja zapis poznatom transformacijom i proverava očekivani odnos izlaza. Rotacija zapisa i zamena metala nisu ista vrsta promene: druga može promeniti hemijski target.

**Dual encoder** izračunava reprezentaciju svakog objekta zasebno, pa se korpus može unapred kodirati. **Cross-encoder/cross-graph model** zajednički obrađuje oba ulaza i zato se uglavnom računa po paru. **Metric learning** uređuje vektorski prostor pomoću označenih sličnih/različitih parova ili trojki. Nijedna od tih arhitektura sama ne definiše šta „slično“ znači.

## 9. Jezički modeli i računarski resursi

**Token** je jedinica tekstualnog kodiranja: deo reči, reč ili drugi simbol, zavisno od tokenizer-a. Generativni jezički model predviđa raspodelu narednog tokena uslovljenu prethodnim kontekstom. Tečan tekst zato nije dokaz da je model parsirao kristal ili izračunao geometriju. SLM označava relativno mali jezički model; ne postoji jedna univerzalna granica broja parametara koja razdvaja SLM i LLM.

**RAG** prvo pronalazi relevantne odlomke, pa ih daje modelu kao kontekst za odgovor. Time se pri običnom pozivu ne menjaju težine modela. **Fine-tuning** ih menja učenjem na dodatnim primerima. U ovom projektu RAG nad dokumentima i pretraga struktura ostaju odvojena pitanja.

**Latencija** je vreme jednog upita; **throughput** je broj završenih upita u jedinici vremena. p95 latencija znači da je 95% merenih upita završeno do te vrednosti. **RAM/VRAM** su radna memorija računara/GPU-a. **Kvantizacija** koristi manje bitova za brojeve, čime štedi prostor uz moguću promenu rezultata.

Oznaka \(O(n)\) opisuje asimptotsku gornju granicu rasta računskog troška, a ne broj sekundi. Kada je vodeći trošak proporcionalan \(n^2\), udvostručavanje velikog \(n\) približno ga učetvorostručuje, uz iste ostale uslove; sama oznaka \(O(n^2)\) ne tvrdi tačnu proporcionalnost. Za 10 CIF-ova ima \(10\cdot9/2=45\) parova; za 20 ih ima 190. Broj parova znamo tačno, ali trajanje svakog mapping/packing poređenja zavisi od složenosti struktura.

## 10. Rečnik za nastavak i provera razumevanja

| Izraz u narednim poglavljima | Značenje |
|---|---|
| pipeline | lanac koraka obrade |
| contract/profil | eksplicitna definicija ulaza, značenja, pretpostavki i ishoda |
| provenance / lineage | poreklo podatka i lanac transformacija koje vode do rezultata |
| eligibility | da li zapis ispunjava uslove upotrebe za konkretnu svrhu |
| ACL | lista/pravila kontrole pristupa; odvojena od relevantnosti |
| PBC | periodični granični uslovi; eksplicitno računanje odgovarajućih kopija kristalnog motiva |
| hard filter | obavezan egzaktan uslov membership-a, odnosno članstva u skupu |
| candidate / reranker | prvobitno pronađen kandidat / metod koji preuređuje kandidate |
| oracle | referentni rezultat tačno određenog zadatka; nije univerzalni izvor istine |
| gold / qrels | proverene ciljne oznake / ocene relevantnosti po upitu |
| evidence | izračunati i proverljivi dokazi sa poreklom |
| estimand | precizno pitanje o populaciji koje procena treba da odgovori |
| iid / exchangeability | nezavisna identično raspodeljena opažanja / slabiji uslov da zajednička raspodela ne zavisi od permutacije opažanja |
| OOD / shift | primer van poznatog domena / promena raspodele podataka |
| snapshot / seed | zamrznuta verzija podataka ili modela / početno stanje slučajnog generatora |
| fallback | alternativni postupak kada primarni nije dostupan ili primenljiv |

Pre [mape pipeline-a](01-pipeline-decision-map.md) objasni svojim rečima:

1. Zašto isto jedinjenje u tri formata nije tri nezavisna trening primera?
2. Kako ANN može imati visok infrastrukturni recall, a nizak ekspertni recall?
3. Zašto nedostajući RMSD i RMSD jednak nuli imaju suprotno značenje?
4. Zašto se hiperparametri i prag ne biraju na finalnom testu?
5. Koju informaciju moraš dodati identičnom 2D fingerprint-u da bi uopšte mogao razlikovati dva packinga?

**Samoprovera:** (1) formati dele izvorni objekat; (2) verno pronalazi susede pogrešne/nepotpune reprezentacije za stručno pitanje; (3) prvo nema merenje, drugo je nulto odstupanje u završenom poređenju; (4) test bi postao deo izbora i precenio generalizaciju; (5) validan periodični/packing podatak, uz odgovarajući target i proveru.

Dalje prati [plan učenja](11-ml-ai-plan-ucenja.md). Primarne radove o pojedinačnim algoritmima i zvanične implementacione definicije naći ćeš uz odgovarajuća detaljna poglavlja; primeri na ovoj strani su obrazovni proračuni, ne izmereni rezultati projekta.
