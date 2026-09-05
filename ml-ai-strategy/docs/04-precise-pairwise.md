# Precizno poređenje parova: algoritmi, dokazi i granice

## Glavni zaključak

Za precizno poređenje parova naučno jezgro nije jedan neuralni score, već deterministička mreža zavisnih dokaza:

```mermaid
flowchart TD
    A[CIF A] --> P[Validirani pogledi i comparison plan]
    B[CIF B] --> P
    P --> C[Component assignment]
    C --> G[Exact graph / subgraph / MCS mapping]
    G --> K[Kabsch + mapped 3D]
    G --> M[Metal/donor coordination]
    P --> L[Lattice i periodic equivalence]
    L --> PK[COMPACK / PAC / crystal comparator]
    P --> I[Typed interaction networks]
    P --> X[Simulated PXRD / powder signal]
    PK --> R[Multi-output evidence paket]
    I --> R
    X --> R
    K --> R
    M --> R
    R --> S[Opcioni target-specific ML sloj]
```

Relevantne algoritamske porodice su:

- globalni component assignment: deterministički candidate pairing + Hungarian algoritam;
- exact graph/subgraph: VF2-like matcher sa hemijskim constraint-ima;
- partial graph: bounded MCS sa timeout-om i dvostranom coverage vrednošću;
- rigidno 3D poravnanje: Kabsch tek posle atom mapping-a;
- coordination: više candidate neighbor setova + donor mapping + continuous shape measures;
- packing: validirana COMPACK/Packing Similarity implementacija kao moguća referenca kada je dostupna/licencirana; PAC kao nezavisna metoda poređenja;
- soft local/crystal similarity: SOAP sa eksplicitno izabranom globalnom agregacijom — REMatch ili zaseban chemically constrained average kernel — kada domen primenljivosti prolazi;
- powder signal: jasno parametrizovan simulated-PXRD/VC-PWDF-like komplement, ne jedini dokaz;
- interaction networks: exact motif/fingerprint referenca i složenije WL/graph/optimal-transport alternative;
- ML meta-model: logistic/RF/GBDT tek uz ciljane ekspertske labele i odvojene indikatore ishoda svake grane.

Rezultat je vektor dokaza sa statusima, ne jedan „84% isto“ broj.

## 4.1 Šta je jedinica poređenja

Pre algoritma definiše se profil poređenja:

| Profil | Objekat A/B | Primarne grane |
|---|---|---|
| parent scaffold | standardizovani parent graph | graph, MCS, optional 3D core |
| koordinacioni motiv | metal + mapirani donor atoms/ligands | graph, donor mapping, CN, shape |
| molekulski konformer | jedan eksplicitni molekulski conformer | exact mapping, torsions, RMSD/shape |
| čvrsta forma | puni kristalni sastav i periodični raspored | components, packing, interactions, PXRD |
| ponovno kristalografsko određivanje | pojedinačno kristalografsko određivanje | cell/model/quality/provenance + packing |

Jedan CIF može imati više nezavisnih molekula, counterions, solvente, disorder alternative ili coordination polymer. Zato „najveći fragment“ nije bezbedan implicitni objekat.

Minimalni plan konceptualno određuje:

| Kategorija | Šta razjašnjava |
|---|---|
| profil i objekti A/B | da li se porede parent graph, coordination entity, conformer, crystal form ili redetermination |
| component i graph politika | sastav/uloge, naboj, stereo i bond semantiku |
| H i disorder politika | razdvaja observed/modelled H i međusobno isključive alternative |
| periodic politika | definiše symmetry-expanded multigraph i tretman lattice slika |
| tražene grane | composition, graph, coordination, geometry, packing, interactions i/ili PXRD |

Tačan zapis ovog plana pripada implementaciji; semantičke odluke moraju biti deklarisane pre poređenja.

## 4.2 State machine svake grane

Svaka grana vraća jedan od statusa:

| Status | Značenje |
|---|---|
| ocenjeno (assessed) | metod je završen nad dovoljnim inputom i evidence je raspoloživ |
| dvosmisleno (ambiguous) | više legitimnih mapiranja/neighbor modela menja zaključak |
| nije primenljivo (not applicable) | grana nema smisla za izabrani objekat |
| nedostaje ulaz (missing input) | potreban CIF podatak ne postoji |
| blokirano kvalitetom | podatak postoji, ali ne podržava claim |
| istek vremena | tačno definisan compute limit je istekao |
| neuspeh (failure) | implementaciona/numerička greška |

Ove kategorije opisuju ishod izvršenja grane, ne naučnu klasu relacije. Naučna labela postoji samo kada je grana ocenjena; packing relacija, na primer, može biti ista, povezana ili različita. Dvosmislenost, neprimenljivost, nedostajući ulaz, blokada kvalitetom, istek vremena i neuspeh ostaju bez naučne labele. Parcijalnost takođe nije packing klasa: opisuje se coverage-om obe strane, brojem poklopljenih molekula, RMSD-om i evidence-om o ograničenju ili upozorenju.

Nedostajući ulaz, istek vremena i neuspeh nisu score 0. Nula tvrdi da je završeno validno poređenje našlo minimalnu sličnost; neocenjen ishod tvrdi da merenje nije dobijeno. Prikaz sme objediniti više takvih ishoda kao „nije ocenjeno“, ali izvorne kategorije i odsustvo naučne labele moraju ostati razlučivi.

## 4.3 All-pairs računanje

Za \(n\) struktura ima:

\[
N_{pairs}=\binom n2=\frac{n(n-1)}2
\]

neuređenih parova. Za 2.110 struktura to je 2.224.995 parova.

### Dva eksplicitno različita moda

**Full all-pairs:** svaka primenljiva tražena grana računa se za svaki par. Dozvoljeno je preskočiti samo granu koja po unapred definisanim uslovima nije primenljiva ili nema potreban input.

**Candidate-pruned:** jeftin prefilter bira parove za skupu granu. To je aproksimacija; UI i export prikazuju da neke kombinacije nisu analizirane, a prefilter mora imati recall benchmark prema full referenci.

Ne nazivati candidate-pruned matricu „svim precizno upoređenim parovima“.

Izvorni `dve funkcionalnosti.txt` zahteva poređenje svakog ulaznog CIF-a sa svakim drugim. Zato tom zahtevu odgovara full all-pairs režim. Candidate-pruned režim je ovde samo zasebna moguća proširena upotreba; ne ispunjava taj zahtev umesto punog poređenja. Manji broj ulaza omogućava više računanja po paru, ali veća tačnost mora biti izmerena, ne sledi automatski iz manjeg skupa.

### Računske posledice

Per-structure podatke i skupe mapping rezultate moguće je ponovo koristiti, a svaki neuređeni par treba matematički računati jednom. Način raspodele posla i čuvanja rezultata zavisi od obima i hardvera i nije deo algoritamske specifikacije.

### Pair-order symmetry

Neuređeni par može interno dobiti kanonsku orijentaciju radi izbegavanja duplog računanja, ali component/atom map mora imati provereni inverse, a asimetričan subgraph containment mora čuvati oba smera.

Zamena \(A \leftrightarrow B\) mora dati iste simetrične score-ove i statuse, dok se usmereni coverage i skupovi neuparenih objekata samo zamene između dve strane. Za simetričan target model koristi symmetric pair transforms/set architecture ili eksplicitno prosečava/vezuje \(f(A,B)\) i \(f(B,A)\). Kanonski ID redosled je eventualna tehnička optimizacija, ne simetrija modela: left/right slot ne sme dozvoliti različite težine koje uče hronologiju/source kroz ID redosled. Zamena A/B i ID-relabel/reingest su nužni metamorphic testovi.

## 4.4 Component assignment

Ako A ima komponente \(A_1,\ldots,A_m\), a B komponente \(B_1,\ldots,B_k\), prvo se grade dozvoljeni candidate parovi po:

- elementnom sastavu i formalnom naboju;
- grafu/fingerprintu;
- ulozi: coordination entity, counterion, solvent, coformer;
- stoichiometric multiplicity;
- metal/donor sadržaju;
- task-specific parent/crystal politici.

### Cost matrica

Ilustrativno:

\[
c_{ij}=
w_f d_{formula}(A_i,B_j)
+w_g d_{graph}(A_i,B_j)
+w_r\mathbb{1}[role_i\ne role_j]
+w_q\mathbb{1}[charge_i\ne charge_j].
\]

Težine nisu univerzalna hemijska istina. Pre labela je sigurniji lexicographic policy: prvo zabrani hemijski nedozvoljena uparivanja, zatim optimizuj rastavljive troškove.

[Hungarian metod](https://doi.org/10.1002/nav.3800020109) pronalazi globalno optimalan one-to-one assignment za zadatu cost matricu. Dummy `unmatched` čvorovi sa eksplicitnim troškom dozvoljeni su i kada je `m = k`: dve jednako duge liste ne znače da svaka komponenta ima legitimnog partnera. Standardne implementacije kvadratnog problema tipično su kubne u broju komponenti, što je malo u odnosu na atom/packing grane.

Stoichiometric multiplicities se ili razvijaju u eksplicitne instance ili rešavaju capacity-aware min-cost-flow formulacijom. Jedan Hungarian run vraća samo jedno optimalno rešenje; za ambiguity se enumerišu svi optima/[k-best assignments](https://doi.org/10.1287/opre.16.3.682) unutar definisanog delta-a, uz deterministic ordering.

Izveštaj o enumeraciji navodi da li je pretraga kompletna ili prekinuta, koliko je rešenja vraćeno, poznate donje i gornje granice troška i korišćenu toleranciju delta. Permutacije kopija smeju se quotient-ovati u istu equivalence klasu **samo** kada su dokazano ekvivalentne po svim atributima relevantnim za izabrani profil i kada svaka takva permutacija garantovano daje isti downstream rezultat. Sama jednakost hemijskog grafa ili formule nije dovoljna: kod \(Z' > 1\) hemijski iste komponente mogu biti kristalografski nezavisne, imati različite konformacije, koordinaciona okruženja ili packing uloge. Za njih se čuvaju assignment orbite/permutacije i ocenjuju njihove posledice. Ovo ograničenje sprečava i factorial duplikate i lažno uklanjanje stvarne mapping neizvesnosti; kontekst daju [Desirajuova analiza struktura sa \(Z' > 1\)](https://doi.org/10.1039/B614933B) i [CCDC ConQuest vodič](https://www.ccdc.cam.ac.uk/media/Documentation/2F0D7443-9739-46EB-BE9F-69E62E531FB7/2f0d7443973946ebbe9f69e62e531fb7.pdf).

### Šta Hungarian ne rešava

- ne zna da li je cost hemijski ispravno definisan;
- ne rešava polymeric/infinite entity kao konačan molekul;
- jedna optimalna suma može sakriti više jednako dobrih assignments;
- stoichiometric duplicates zahtevaju multiplicity-aware mapu;
- „solvent“ klasifikacija može biti neizvesna.

Izveštaj zato čuva najbolji assignment, cost po komponenti, unmatched delove i sve alternative unutar definisanog ambiguity delta-a.

## 4.5 Exact graph, subgraph i MCS

### Exact graph isomorphism

Dva označena grafa su exact match ako postoji bijekcija čvorova koja čuva izabrane node/edge atribute. [VF2](https://doi.org/10.1109/TPAMI.2004.75) je praktičan state-space algoritam za graph i subgraph isomorphism.

2CDC node constraints mogu uključiti:

- element i isotope;
- formal charge;
- aromaticity model;
- stereo provenance/tag kao ulaz u mapping-aware proveru;
- ligand/component membership;
- donor/metal role;
- disorder alternative.

Edge constraints mogu uključiti bond type/order, aromaticity i coordination-edge status. Periodic image/gain vector se čuva kao provenance, ali njegova raw integer trojka nije invariantna na basis, origin, wrapping, izbor predstavnika čvora ili supercell promenu. Poredi se tek posle transformacije oba grafa u zajednički lattice mapping i gauge ili preko kanonizovanog periodic quotient/gain odnosa; literalna equality image trojki nije VF2 constraint. Koordinaciona ivica nije automatski ekvivalentna organskoj single vezi.

Promena periodičnog predstavnika jednog čvora dodaje/oduzima njegov integer gauge shift labelama incidentnih ivica. Dve reprezentacije su zato ekvivalentne tek ako postoji zajednička basis transformacija **i vertex-wise gauge transform**; invariantni cycle/path-sum odnosi se zatim mogu porediti. Samo basis transformacija ne rešava wrapping razliku.

Stereo nije običan lokalni string atribut: tetrahedral parity zavisi od permutacije mapiranih suseda. Exact matcher posle candidate bijekcije proverava tetrahedral parity, double-bond `E/Z`, relevantne enhanced stereo groups i unknown/unspecified stanje prema verzionisanoj politici. Nepodržana metalna ili koordinaciona stereokemija ne postaje „ista“ zato što toolkit nema tag; rezultat ostaje dvosmislen i bez naučne relacione labele. Korisne formalne reference su [OpenSMILES stereochemistry pravila](http://opensmiles.org/opensmiles.html#stereochemistry) i [RDKit stereochemistry dokumentacija](https://www.rdkit.org/docs/RDKit_Book.html#stereochemistry).

### Subgraph relation

Substructure pitanje je asimetrično: query motif može biti sadržan u većem target-u, dok obrnuto ne važi. Izveštaj zato navodi smer, query coverage i target coverage.

### Maximum Common Subgraph

MCS traži najveći zajednički deo pod zadatim pravilima. Umesto jednog procenta čuvaju se najmanje atom i bond coverage u oba smera:

\[
coverage^{atom}_A=\frac{N_{mapped\ atoms}}{N_{eligible\ atoms,A}},\qquad
coverage^{bond}_A=\frac{N_{mapped\ bonds}}{N_{eligible\ bonds,A}},
\]

uz analogne vrednosti za B.

MCS/subgraph search može imati eksponencijalan worst case. Definicija metode zato navodi:

- maksimalno vreme i broj states;
- minimalni atom/bond coverage;
- complete-rings/ring-fusion policy;
- induced naspram non-induced i connected naspram disconnected MCS;
- objective/tie-break, na primer prvo broj mapiranih heavy atoma, zatim broj veza i ring completeness;
- stereo/charge/metal pravila;
- status isteka vremena, nikada lažnu nulu;
- svi optimalni non-automorphic mappings ili unapred ograničen k-best/ambiguity set;
- deterministic tie-break i hash svakog prihvaćenog atom mapping-a.

MCS rezultat dodatno navodi da li je optimalnost dokazana, najbolji pronađeni incumbent, poznatu gornju granicu i razlog završetka. Ako istek vremena prekine dokaz optimalnosti, prijavljeni mapping/coverage je lower-bound kandidat, ne „the maximum common subgraph“. Enumeracija optimuma isto razlikuje kompletan od prekinutog ishoda kao component assignment.

### Automorphisms

Simetričan molekul može imati više hemijski ekvivalentnih atom maps. Ne bira se prvi toolkit rezultat. Dozvoljene ekvivalentne mape se enumerišu ili implicitno optimizuju, zatim se prijavljuju:

- broj/tip ekvivalentnih mappinga;
- odabrana mapa i razlog;
- minimalni i raspon RMSD-a, označen kao potpun samo ako je enumeration complete;
- da li zaključak zavisi od tie-a.

Ne smeju se isprobavati hemijski neekvivalentne mape samo da bi RMSD izgledao manji.

## 4.6 Kabsch i mapped 3D

[Kabsch algoritam](https://doi.org/10.1107/S0567739476001873) SVD postupkom nalazi optimalnu rigidnu rotaciju koja minimizuje sum of squared deviations između **već korespondentnih** tačaka. On ne pronalazi atom mapping.

Za \(N\) mapiranih atoma, posle centriranja i orientation-preserving poravnanja:

\[
RMSD=\sqrt{\frac{1}{N}\sum_{i=1}^{N}
\|R\mathbf{x}_i+\mathbf{t}-\mathbf{y}_i\|^2}.
\]

Default su uniformne težine. Ako profil opravdano koristi \(w_i\), centroids, rotacija i prijavljena vrednost moraju pratiti isti weighted contract:

\[
RMSD_w=\sqrt{\frac{\sum_i w_i\|R\mathbf{x}_i+\mathbf t-\mathbf y_i\|^2}{\sum_i w_i}}.
\]

Reproduktivna definicija poređenja navodi:

- mapping hash i broj mapiranih/eligible atoma;
- heavy-only ili eksplicitnu H policy;
- rigid/flexible policy;
- da li je refleksija zabranjena;
- symmetry-equivalent atom treatment;
- experimental/generated coordinate provenance;
- weights i jedinicu;
- RMSD, median, maximum i ključne torsion razlike.

Pre poravnanja finite molekulska komponenta se rekonstruše kontinuirano preko periodic boundary-ja. Frakcione koordinate iz različitih ćelija ne porede se direktno; za molecular RMSD koriste se odgovarajuće unwrapped kartezijanske koordinate. U suprotnom ista veza koja prelazi granicu ćelije može izgledati kao ogromno geometrijsko odstupanje.

Unwrap koristi cycle-consistent propagation symmetry-operation/image labels kroz covalent graph, uključujući symmetry-generated i special-position atome. Za konačan molekul svi graph cycle sums moraju biti konzistentni sa zatvaranjem; nenulti periodic translation ukazuje na polymeric/infinite komponentu ili pogrešnu connectivity pretpostavku i blokira finite-molecule Kabsch profil. Više symmetry-equivalent realizacija se quotient-uju uz očuvan provenance.

### Chirality

Default koristi proper rotation sa determinant-om `+1`; mirror reflection nije dozvoljen. Enantiomorph/mirror odnos se prijavljuje zasebno. Ako neki search mode namerno ignoriše chirality, to je nova verzija profila, ne skrivena numerička opcija.

### Degenerate point sets

Jedinstvena 3D rotacija nije identifikovana sa manje od tri nekolinearne mapirane tačke. Izlaz čuva rank i singular values centriranog koordinatnog skupa i izričito navodi da li je rotacija identifikovana. Za jednu, dve ili kolinearne tačke može se prijaviti ograničen distance residual, ali ne jedinstvena orientation, torsion ili geometry tvrdnja; takav zaključak ostaje dvosmislen.

### Coverage pre lepog RMSD-a

RMSD 0,05 Å nad tri atoma nije snažniji dokaz od 0,60 Å nad 35/37 heavy atoma. Kartica uvek prikazuje RMSD zajedno sa dvostranom coverage vrednošću i unmatched funkcionalnim grupama.

### Neizvesnost

Ako su standard uncertainties/covariance dostupni i uporedivi, mogu se računati uncertainty-aware residuals. U suprotnom se nominalni RMSD ne predstavlja kao statistički significance test. Nizak RMSD dva slaba ili korelisano izvedena modela nije automatski snažan dokaz.

## 4.7 Coordination environment

Najrizičniji korak je odluka ko je zaista sused/koordinisan metalu.

### Candidate neighbor sets

Ne koristi se jedan globalni distance cutoff. Generišu se candidate setovi koristeći kombinaciju:

- periodic distance i element-pair/radii pravila;
- eksplicitnu connectivity evidenciju, uz provenance;
- Voronoi/solid-angle signal;
- charge/valence i donor chemistry kao pomoćni signal;
- occupancy/disorder/H uncertainty;
- sensitivity sweep parametara.

[ChemEnv](https://doi.org/10.1107/S2052520620007994) kombinuje modifikovanu Voronoi analizu, distance/solid-angle parametre i continuous symmetry measures, pri čemu može vratiti jedinstveno ili mešano okruženje. To je snažan kandidat za automatic baseline, ali njegov benchmark nad pretežno inorganic/materials okruženjima ne dokazuje optimalnost za organometalne CSD/DAP komplekse; potreban je poseban 2CDC expert audit.

### Continuous shape measure

Za lokalno okruženje \(Q\) i idealni polyhedron \(P\) sa istim brojem vertices, tipičan normalized CSM oblik je:

\[
S_P[Q]=100\min\frac{\sum_k\|\mathbf q_k-\mathbf p_k\|^2}
{\sum_k\|\mathbf q_k-\bar{\mathbf q}\|^2},
\]

uz optimizaciju skale, rotacije i dozvoljenih vertex permutacija. Manje znači bliže idealnom obliku. [Pregled continuous shape pristupa](https://doi.org/10.1016/j.ccr.2005.03.031) pokazuje zašto diskretne etikete poput „octahedral“ mogu sakriti kontinuirane distortion puteve.

Ne čuvati samo najbolju etiketu. Čuvaju se CSM vrednosti prema svim relevantnim idealnim oblicima, neighbor set, CN i gap između najboljih kandidata.

### DAP-specifičan exact dokaz

Za svaki metal i mapirani DAP motif proverava se:

```text
centralni pyridine N              → isti metal?
levi terminalni N u C=N grani     → isti metal?
desni terminalni N u C=N grani    → isti metal?
tri veze direct / ambiguous / absent?
metal je u istoj komponenti ili samo counterion?
```

Tvrdnje „entry sadrži Cu“ i „Cu koordinira sva tri DAP N atoma“ ostaju odvojene. Oxidation state se ne izmišlja iz formule; navode se način njegovog utvrđivanja i prateći evidence.

### Pair comparison

Nakon donor assignment-a porede se:

- metal element/oxidation evidence;
- CN i alternative;
- donor element/type/ligand membership;
- denticity, bridging/hapticity status;
- M–donor distance vektor i angle/torsion set;
- CSM vector i geometry label mixture;
- coverage i ambiguity.

Hungarian assignment može upariti isto-tipne donore po minimalnom geometrijskom trošku, ali samo unutar chemijski dozvoljene equivalence klase.

## 4.8 Periodični model pre crystal poređenja

Kristal nije samo asimetrična jedinica. Periodična ivica konceptualno povezuje source i target atom i navodi symmetry operation, lattice image, rastojanje, fizičku ulogu kontakta i provenance pravila kojim je izvedena. Tačan tehnički format nije deo teorijske specifikacije.

Crystal branch mora biti invariant/equivariant prema:

- atom/component permutation;
- rigid translation/rotation;
- boundary wrapping;
- origin i symmetry-equivalent ASU opisu;
- ekvivalentnom space-group setting-u, npr. \(P2_1/c\leftrightarrow P2_1/n\);
- unimodularnoj primitive-basis promeni;
- primitive/conventional/supercell reprezentaciji, u granicama profila.

Dve primitive baze iste rešetke povezane su celobrojnom unimodularnom matricom \(U\in GL(3,\mathbb Z)\), \(|\det U|=1\). Supercell je zaseban slučaj sa celobrojnom matricom \(|\det U|>1\): motiv se mora odgovarajuće replicirati i ponovo mapirati, ne samo transformisati lattice vektore. Ova razlika i višestruke coordinate reprezentacije istog kristala razmatraju se u [IUCrJ radu o definicijama kristalne strukture](https://doi.org/10.1107/S2052252524004056).

Reduced/Niggli cell i space group su candidate/signature signali. Ista ćelija ili ista space group ne dokazuju isto packing; ekvivalentni kristal može imati drugačiji zapis ćelije.

### Special positions posle symmetry expansion-a

Atom sa nenultom site symmetry može kroz više symmetry operacija generisati isto fizičko mesto. Ekspanzija zato:

1. svodi fractional positions modulo lattice translation;
2. koalescira isti species/site/disorder state unutar verzionisane coordinate tolerance;
3. čuva listu svih symmetry-operation provenance putanja;
4. proverava dobijenu multiplicity prema CIF/Wyckoff/site-symmetry podatku;
5. ne spaja različite disorder alternative, species ili occupancy modele.

Bez toga se dupliraju susedi, coordination number, kontakti i occupancy doprinos. Formalna polazna tačka je [IUCr Core CIF dictionary](https://www.iucr.org/resources/cif/dictionaries/browse/cif_core), koji razlikuje multiplicity generisanih mesta i site-symmetry red.

### Lattice candidate algoritam

Deterministički lattice branch:

1. validira ćeliju i gradi metric tensor;
2. pravi standardizovanu/reduced reprezentaciju uz deklarisanu toleranciju;
3. po potrebi enumeriše dozvoljene unimodularne integer basis/setting transformacije;
4. poredi lengths/angles, volume i volume po formula unit-u;
5. vraća candidate mappings, ne packing presudu;
6. svaki kandidat proverava atomskim/periodičnim ili packing comparatorom.

Niggli/reduced-cell rezultat blizu degenerate granice može biti numerički nestabilan, pa se originalna ćelija i sve transformacije čuvaju. Supercell mappings se obrađuju zasebno sa multiplicity/motif replikacijom. Space-group label se ne koristi kao jedini gate jer pogrešno/alternativno setting dodeljivanje ne sme sakriti geometrijski match.

## 4.9 COMPACK, PAC i CrystalCMP

### COMPACK / CCDC Packing Similarity

[COMPACK](https://doi.org/10.1107/S0021889804027074) opisuje molecular packing okruženje relativnim položajima/orijentacijama molekula kroz interatomske distance, bez oslanjanja na identične cell/space-group zapise. CCDC-ov [Packing Similarity API](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/packing_similarity.html) tipično vraća broj matched molecules i RMSD za definisan cluster/tolerances.

Parametri koji definišu poređenje:

- referentna komponenta/molecule matching;
- shell/cluster veličina;
- distance/angle tolerancije;
- H atom policy;
- conformational flexibility;
- minimalan broj matched molecules;
- višekomponentni/disorder/polimer policy.

Method paper ne daje automatski pravo korišćenja CCDC implementacije ili podataka. Primenljivost konkretne implementacije zavisi od odgovarajućih prava i ugovora.

### PAC

[Progressive Alignment of Crystals](https://doi.org/10.1107/S1600576722009670) progresivno poravnava clusters i koristi coordinate \(RMSD_N\); uvodi radius of gyration/shape informaciju da razlikuje geometriju superimposed clustera. Rad prijavljuje slaganje sa COMPACK-om na small-molecule testovima i bolju brzinu u analiziranom setup-u, ali to nije univerzalna garancija za metalne komplekse, co-crystals ili disorder.

### CrystalCMP

[CrystalCMP](https://doi.org/10.1107/S1600576720003787) automatski bira fragmente i poredi molecular packing; representative clusters u objavljenoj metodologiji sadrže jedan izabrani tip molekula. Zato rezultat mora navesti izabranu molekulsku vrstu i njeno mapiranje fragmenata i nazvati se species-specific packing comparison, ne automatski poređenjem cele soli/solvata/co-crystal forme. Bez legitimnog izbora rezultat je dvosmislen ili metod nije primenljiv; za beskonačni coordination polymer finite-molecule metod može biti neprimenljiv. Objavljeni threshold-i zavise od settings-a i evaluiranog skupa, pa je metod istraživačka alternativa/cross-check, ne izvor univerzalnog „identical packing“ praga.

### Poređenje uloga

Kada prava i domen primenljivosti to dopuštaju, COMPACK/Packing Similarity može biti referentna metoda zbog direktne veze sa CSD praksom. PAC pruža nezavisno poređenje sa drugačijim cluster-shape informacijama. Njihova neslaganja su informativan skup za slepo stručno ocenjivanje, ali objavljeni threshold-i nisu univerzalni i ne prenose se bez target-specifične kalibracije. Svaki metod treba da prijavi matched \(N\), RMSD, cluster shape/coverage, parametre i failure reason.

## 4.10 SOAP, REMatch i hemijski ograničena agregacija

[SOAP](https://doi.org/10.1103/PhysRevB.87.184115) predstavlja lokalno atomsko okruženje glatkom atomskom gustinom i standardnim power-spectrum kernelom invariantnim na rotaciju i refleksiju. [REMatch](https://doi.org/10.1039/C6CP00415F) kombinuje matricu lokalnih sličnosti u globalni kernel kroz entropy-regularized matching; srodan computational princip je [Sinkhorn regularizovani optimal transport](https://papers.nips.cc/paper/2013/hash/af21d0c97db2e27e13572cbf59eb343d-Abstract.html).

### Parametri koji menjaju značenje

- cutoff radius i periodic neighbor construction;
- Gaussian width;
- radial/angular basis truncation;
- chemical species/alchemical kernel;
- normalization i kernel exponent;
- REMatch regularization;
- izbor centara i pondera;
- full crystal, selected molecule ili local environment nivo.

SOAP sa izabranom agregacijom daje soft similarity za eksploraciju i poređenje. Za GPR ili kernel metode treba dodatno opravdati pozitivnu semidefinitnost baš te globalne konstrukcije: za svaku konačnu listu struktura i realni vektor težina \(c\), matrica sličnosti \(K\) mora zadovoljiti \(c^T K c\ge0\). Proizvoljan best-match maksimum ili hemijsko ograničavanje matching-a ne nasleđuje taj uslov samo zato što lokalni SOAP kernel jeste validan.

Standardni SOAP je reflection-invariant, pa sam ne razlikuje enantiomerna/ogledalska lokalna okruženja; REMatch ne može povratiti odbačenu chirality informaciju. Stereo-sensitive profil zato zadržava exact stereochemical gate ili posebno validiran parity/chirality-sensitive deskriptor.

Običan globalni assignment može upariti lokalna okruženja hemijski neekvivalentnih atoma. [Martin, Ceriotti i Day (2025)](https://doi.org/10.1021/acs.cgd.5c01220) zato uvode **adapted average SOAP kernel**, zasebnu konstrukciju u odnosu na REMatch: prosečavaju samo poređenja analognih atoma istog osnovnog molekula i dozvoljenih molekulskih simetrijskih mapiranja. Taj rad nije definicija „chemically constrained REMatch-a“. Validiran je na užem skupu organskih molekulskih kristala. Autori ograničavaju konstrukciju na skupove sa istim \(Z'\) ili asimetričnim osnovnim molekulom; kombinacija promenljivog \(Z'\) i simetričnog molekula ne zadržava njihovo PSD jamstvo. Primeri sa simetričnim molekulima tretiraju ih kao rigidne; opšti fleksibilni simetrični slučaj nije razrađen.

Pre upotrebe se zato proveravaju chemical identity, konačnost molekula, \(Z'\), molekulska simetrija i pravila agregacije. Salts, co-crystals, metalni kompleksi i coordination networks zahtevaju zasebnu validaciju. SOAP score nije packing identitet bez nezavisnog packing/ekspertnog poređenja. Ako se uvede hemijski ograničen REMatch, to je dodatno definisana metoda sa sopstvenom validacijom, a ne automatska primena navedenog adapted-average rada.

## 4.11 PXRD kao komplementarna grana

Simulirani powder pattern iz CIF-a može se porediti preko:

- peak matching-a uz definisanu tolerance;
- normalized cross-correlation;
- cosine sličnosti nad isto binovanim patternima;
- variable-cell/pattern metodologije koja modeluje lattice deviation.

[VC-PWDF studija](https://doi.org/10.1039/D2CE01080A) poredi powder-based metod sa COMPACK-om na desetinama hiljada parova i nalazi komplementarne failure modes; metod ne pretvara PXRD u jedinstven dokaz atomskog packinga.

Reproduktivna definicija poređenja navodi najmanje:

- vrstu probe — X-ray, neutron ili electron — i geometriju eksperimenta/simulacije;
- sve radiation komponente sa wavelength vrednostima i težinama, ne samo jednu nominalnu talasnu dužinu;
- izvor/verziju scattering factor-a ili scattering length-a i anomalous-scattering politiku;
- politike za occupancy, disorder alternative, H atome i ADP/Debye–Waller faktor;
- Lorentz–polarization, multiplicity i ostale uključene corrections;
- \(2\theta/q/d\) osu, range, step/binning, peak profile, intensity/background normalization i temperaturu;
- simulator, verziju, numeričke tolerancije i razliku između simuliranog i izmerenog obrasca;
- za measured pattern: instrument geometry, kalibraciju/zero shift i poznate sample corrections.

Bez ovih informacija intensity-based cosine/correlation score nije nužno reproduktivan: različite probe i korekcije daju različite intenzitete i kada je strukturni model isti. Kategorije se oslanjaju na zvanične [IUCr pdCIF definicije](https://www.iucr.org/resources/cif/dictionaries/cif_pd) i [IUCr Core CIF scattering kategorije](https://www.iucr.org/resources/cif/dictionaries/browse/cif_core1); svaka reprodukcija mora navesti korišćeni simulator i fizički model.

Važne granice:

- dva CIF-derived simulirana patterna daju izvedenu sličnost, ne nezavisan eksperimentalni dokaz;
- mala promena ćelije/temperature pomera peaks;
- preferred orientation, mixture, noise i instrument menjaju measured pattern;
- sličan powder pattern može sakriti različite strukture/polytypes;
- previše fleksibilan alignment može izravnati stvarnu razliku.

PXRD je dobar disagreement resolver/candidate signal uz packing comparator, ne jedini finalni kriterijum.

## 4.12 Interaction networks

Za svaki crystal gradi se typed periodic multigraph:

- node: atom, donor/acceptor/metal type, component, occupancy/disorder;
- edge: H-bond candidate, coordination, halogen/π ili drugi eksplicitno definisan kontakt;
- atribut: distance, angle, periodic image, rule version, confidence;
- higher motif: chain, ring, layer, 3D network i solvent-mediated put.

### Periodična topologija motiva

Običan cycle detector nad jednom ćelijom nije dovoljan. Za orijentisanu putanju sabiraju se integer translation/gain labels, uz prethodno usaglašenu basis/gauge transformaciju:

- **ring:** zatvorena putanja sa nultim ukupnim translation vektorom;
- **periodic chain:** komponenta čiji nezavisni cycle-sum translation vektori imaju rang 1;
- **layer:** rang 2;
- **3D network:** rang 3.

Ciklus u finite quotient grafu sa nenultim translation sum-om u beskonačnom lift-u nije prsten već nastavlja periodični put. Ova definicija čini dimensionality nezavisnom od proizvoljne supercell veličine; formalni okvir daju [periodic labelled quotient graphs](https://doi.org/10.1107/S2053273325008253) i [quotient-graph dimensionality algoritam](https://doi.org/10.1038/s41524-020-00409-0).

### Transparentne reference

Relevantne su:

- exact motif presence;
- count fingerprint typed edges/motifs;
- Jaccard/min–max similarity;
- donor/acceptor/metal coverage;
- dimensionality/topology flags.

### Složenije alternative

[Weisfeiler–Lehman subtree kernel](https://www.jmlr.org/papers/v12/shervashidze11a.html) je efikasan način poređenja discrete-labeled graph neighborhoods, ali nije potpuni graph-isomorphism dokaz i može imati collisions/ograničenu diskriminaciju. Graph edit distance je intuitivan, ali exact račun može biti nepraktičan; svaka aproksimacija mora čuvati edit-cost semantiku. Optimal transport nad motif/local-environment features može dati soft poređenje, ali regularization i cost matrica postaju deo metode.

H-bond rezultat je posebno osetljiv na H positions, protonation, disorder i temperature. Ishod u kojem veza nije detektovana nije isto što i dokaz da interakcija fizički ne postoji.

## 4.13 Disorder, occupancy i multiple models

Alternative occupancy 0,6/0,4 nisu dva istovremena puna atoma. Dozvoljene strategije:

- poredi svaku kompatibilnu disorder realizaciju i vrati range/best/worst uz probability caveat;
- marginalizuj/ponderi local features occupancy-jem ako metod to matematički podržava;
- blokiraj granu kada alternative nisu rekonstruisane;
- nikad ne dupliraj obe alternative kao pune atomske susede.

Ako CIF ima više models/data blocks, comparison plan beleži koji je izabran i zašto. Model selection nije posao Kabsch-a ili GNN-a.

## 4.14 Da li je potreban ML meta-model

### Bez ekspertskih labela

Ne. Prikazuje se evidence vector i eventualno unapred definisana lexicographic odluka:

```text
graph exact?
→ coordination exact/ambiguous?
→ geometry coverage + RMSD
→ packing matched N + RMSD
→ interaction agreement
→ quality limitations
```

### Sa labelama za jedan use case

Target, na primer relacija koordinacionih okruženja, može dobiti:

- logistički ili ordinalni transparentni model;
- RF/ExtraTrees ili drugi tree ensemble za nelinearne odnose;
- GBDT kada kapacitet i tuning odgovaraju količini nezavisnih grupa;
- calibrated/conformal abstention sloj uz odgovarajuće pretpostavke.

Features su isključivo rastavljivi branch output-i i statusi. Model ne dobija raw ID/source proxy. Strukture se dodeljuju foldovima pre pravljenja parova.

Model/preprocessing/hyperparameter izbor radi se u inner grouped CV-u, a procena u netaknutom outer structure-family/temporal testu ([DataSAIL](https://doi.org/10.1038/s41467-025-58606-8)). Efektivni \(n\) je broj nezavisnih compound/scaffold/solid-form grupa, ne \(n(n-1)/2\) međuzavisnih parova. Calibration/conformal skup poštuje iste granice; standardni marginalni conformal coverage zahteva exchangeability, a shift zahteva drugačije pretpostavke/metod i ne dobija distribution-free garanciju prostim slice izveštajem ([Barber et al.](https://doi.org/10.1214/23-AOS2276)). Coverage se ipak empirijski proverava ukupno i po kritičnim grupama kao deployment dijagnostika.

### Multi-output je bolji od univerzalnog score-a

Moguće target porodice uključuju:

| Target | Primer relacije | Dodatna informacija |
|---|---|---|
| parent graph | same / different | exact graph evidence |
| coordination | same / related / different | donor mapping, CN i geometry evidence |
| conformer | same-like / different | mapped coverage i RMSD |
| packing | same / related / different | complete/partial/none evidence coverage |
| molecular stereo i crystal handedness | same / mismatch | odgovarajući stereo ili enantiomorph dokaz |
| interaction odnos | target-specific kategorije relacije | typed-edge/motif/network evidence |
| korisnost za profil | graded relevance | samo uz eksplicitan label guide |

Svaki od ovih target-a ostaje odvojen od ishoda izvršenja grane: ocenjeno, dvosmisleno, neprimenljivo, nedostaje ulaz, blokirano kvalitetom, istekao je vremenski limit ili je metod neuspešan. Tačan tehnički zapis nije deo konceptualnog modela.

Svaki target ima sopstveni label guide, calibrator i slice metrike. Relation loss se računa samo za ocenjene slučajeve sa poznatom gold relacionom labelom; neocenjeni slučajevi ulaze u coverage, failure i abstention metrike, ne postaju dodatna klasa. Agregatna odluka izostaje ako ključna grana nije ocenjena i semantika targeta ne dopušta zaključak.

## 4.15 Četiri ilustrativna para

### A — isti molekul, drugačiji atom ordering

- component assignment: exact;
- VF2: exact graph sa više mogućih automorphisms;
- Kabsch: isti rezultat posle izbora ekvivalentne mape;
- očekivanje: atom permutation test ne menja evidence.

Ako RMSD zavisi od reda redova u CIF-u, implementacija je pogrešna.

### B — isti parent ligand, dodatna voda

- parent graph: exact;
- full composition: različit;
- component assignment: voda je `unmatched` ili mapirana na vodu;
- packing/interactions: moraju uključiti/eksplicitno izuzeti vodu prema profilu;
- overall: scaffold mode može biti jak match; solid-form mode nije exact composition match.

### C — Cu postoji, ali je counterion/odvojena vrsta

- entry element filter: Cu=true;
- DAP graph: možda exact;
- coordination donor mapping: sva tri N→isti Cu=false/ambiguous;
- CSM: nije primenljiv za traženi DAP–Cu centar;
- zaključak: nije pozitivan coordination-motif primer samo zato što formula sadrži Cu.

### D — isti molekul, dva polymorph-a

- 2D graph: exact;
- molecular conformation: može biti bliska ili različita;
- reduced cell/space group: može biti ista ili različita;
- COMPACK/PAC: treba da odluči packing odnos pod parametrima;
- interaction network: može otkriti drugi H-bond motif;
- conclusion: molecular identity ne implicira crystal-form identity.

## 4.16 Evaluacioni skup

### Evaluacioni slojevi

1. **metamorphic gold:** ista struktura drugačije kodirana, očekivana invariance poznata;
2. **synthetic negative:** kontrolisano promenjen metal, stereo, donor ili periodic edge;
3. **representative grouped test:** random ili unapred design-weighted uzorak iz ciljane all-pairs populacije za prevalence, calibration i risk;
4. **expert pair labels:** slepo ocenjeni stvarni parovi po jednom profilu;
5. **method challenge:** posebno označen COMPACK/PAC/CrystalCMP/SOAP/PXRD disagreement/candidate-enriched pool;
6. **authorized CSD evaluation:** primenljiva samo kada ugovor dozvoli pristup i evaluaciju.

Disagreement pool je odličan za nalaženje failure modes, ali nije reprezentativan za punu populaciju i ne procenjuje prevalence, calibration ni prosečni risk. Aktivno biranje test primera uvodi selection bias; koristi se poznat design/importance-weighted estimator ili odvojeni representative test ([Active Testing](https://proceedings.mlr.press/v139/kossen21a.html)). Neoznačeni parovi nisu automatski negativni.

### Split

Strukture/compound/scaffold/solid-form/publication/time grupe se dele pre generisanja parova. `A–B` u train-u i `A–C` u testu nije nezavisna procena. Za metamorphic varijante svi derivati originala ostaju u istoj particiji.

**2D cold/cold** estimand koristi disjunktne endpoint grupe: ako su particije struktura (T,V,E), train sadrži samo (T\times T), validation samo (V\times V), a test samo (E\times E). Cross-partition parovi poput (T\times E) se iz ovog estimanda izostavljaju. Ako je cilj „nov query naspram poznatog korpusa“, (T\times E) se meri kao zasebno imenovan **1D warm/cold** režim, sa sopstvenim metrikama; nikad se ne meša u cold/cold test. [DataSAIL](https://doi.org/10.1038/s41467-025-58606-8) daje formalni okvir za razlikovanje 1D i 2D splitova. Evaluaciona definicija navodi ciljnu distribuciju, pravilo za cross-partition parove i tačan estimand pre model-selection rada.

### Metrike po grani

| Grana | Primarne metrike |
|---|---|
| component assignment | exact/tie-aware assignment accuracy, unmatched precision/recall |
| atom mapping | mapped-pair precision/recall, coverage, exact graph decision |
| 3D | numerical invariance tolerance, RMSD error prema reference mapi |
| coordination | donor-edge precision/recall, CN accuracy, CSM/label agreement |
| packing | confusion za klase isto/povezano/različito, zasebno slaganje matched-N/coverage/RMSD i neslaganje eksperata |
| interactions | typed-edge/motif precision/recall, topology agreement |
| meta-model | grouped ROC/PR, calibration, coverage–risk, worst slice |
| sistem | p50/p95, peak RAM i stopa svake kategorije neocenjenog ishoda |

Continuous threshold-i se biraju samo na training/calibration grupama. Test izveštaj čuva paired interval po structure-family grupi i sve neuporedive parove.

## 4.17 Metamorphic i adversarial suite

### Mora ostati isto

- permutacija atoma i komponenti;
- rigid translation/rotation;
- periodic wrap;
- origin shift i symmetry-equivalent ASU;
- \(P2_1/c\leftrightarrow P2_1/n\) ekvivalentan setting;
- unimodularna primitive-basis promena;
- primitive/conventional opis i zasebno validiran supercell + replicated-motif opis kada profil poredi isti beskonačni kristal;
- zamena \(A \leftrightarrow B\) uz zamenu usmerenog evidence-a;
- relabel/reingest struktura novim immutable ID-jevima bez promene sadržaja;
- validan drugačiji SMILES atom ordering;
- različit red loop kolona/rows u CIF-u.

### Mora pokazati ciljanu razliku

- isti ligand, drugi metal;
- isti metal/donor set, druga geometry;
- isti formula, constitutional isomer;
- enantiomer/enantiomorph pod stereo-sensitive profilom;
- isti molekul, drugi polymorph;
- metal samo u counterion-u;
- direct naspram solvent-mediated H-bond;
- disorder alternative naspram duplih punih atoma;
- nedostajuća symmetry/ćelija;
- hemijski neekvivalentna mapa sa veštački manjim RMSD-om.

Svaki test navodi očekivane branch statuse i brojeve/tolerance, ne samo overall pass.

## 4.18 Računska složenost i capacity trade-off

All-pairs broj raste kvadratno, a graph i packing poređenja imaju veoma neujednačenu cenu. Blokovska dekompozicija, ponovno korišćenje per-structure rezultata i ograničenje vremena/memorije po grani predstavljaju opšte načine kontrole tog troška. Nepotpuno računanje mora ostati vidljivo u statusima i coverage-u.

Capacity procena treba da koristi rep distribucije vremena i memorije, ne samo prosek. Queue sistem, broj worker-a, cache i export format nisu algoritamski zahtevi ovog poglavlja.

## 4.19 Matrica algoritamskih uloga

| Pitanje | Transparentna referenca | Preciznija ili skuplja alternativa | Uslov ili ograničenje |
|---|---|---|---|
| component pairing | ručno/lexicographic | constrained Hungarian + ambiguity set | learned cost zahteva labele |
| exact molecular identity | canonical hash + exact graph | VF2-like exact matcher ili drugi toolkit cross-check | hemijska semantika grafa mora biti ista |
| partial common core | fingerprint prefilter | bounded MCS + timeout | istek vremena ostaje status, ne score |
| rigid conformation | fixed mapping RMSD | Kabsch po svim ekvivalentnim mapama | mapping mora prethoditi RMSD-u; flexible alignment je drugi target |
| metal neighbor set | distance/radii candidates | multi-policy sensitivity, expert-calibrated ili ChemEnv-like pravilo | cutoff i oxidation/donor pretpostavke moraju biti eksplicitne |
| geometry label | angles/distances | CSM vector + ambiguity ili supervised classifier | classifier zahteva ciljane labele |
| packing | cell candidate signal | licenciran/validiran COMPACK, PAC ili CrystalCMP | finite-molecule/domain i rights uslovi se razlikuju |
| soft crystal metric | simple periodic descriptors | SOAP–REMatch, zaseban adapted-average SOAP ili periodic GNN | agregacija i domen su eksplicitni; score nije packing identitet, a GPR zahteva validan kernel |
| powder signal | fixed-bin cosine/correlation | validiran VC-PWDF-like ili learned model | fizička simulaciona definicija i odgovarajući podaci su obavezni |
| interactions | typed motif fingerprint | exact mapping + motif/network, WL/OT ili graph model | tipovi ivica i protonation/disorder politika menjaju značenje |
| combined decision | branch report | target-specific kalibrisan tree ili deep pair model | zahteva ekspertske labele i ne sme sakriti branch statuse |

## 4.20 Anti-patterni

- RMSD pre atom mapping-a;
- „largest fragment“ kao skriven component policy;
- Hungarian cost predstavljen kao hemijska istina;
- MCS timeout pretvoren u score 0;
- najniži RMSD iz hemijski nedozvoljenih atom permutations;
- reflection dozvoljen bez stereo profile-a;
- jedan distance cutoff za sve metal–donor parove;
- poistovećivanje prisustva metala u zapisu sa dokazom da metal koordiniše DAP;
- ista cell/space group proglašena istim packingom;
- simulated PXRD iz CIF-a predstavljen kao nezavisna potvrda tog CIF-a;
- SOAP score preimenovan u packing identity;
- bilo koji neocenjen ishod grane zamenjen nulom ili naučnom klasom;
- all-pairs label za candidate-pruned posao;
- pair-random split;
- canonical ID ordering korišćen kao zamena za simetričnu pair-model arhitekturu;
- overall score bez target-a i expert label guide-a.

## 4.21 Kriterijumi validnosti

Pairwise tvrdnja je validna kada:

1. svaka grana ima definisane ulaze, odvojen ishod izvršenja, target-specific naučnu labelu samo kada je ocenjiva, evidence coverage i verziju metode;
2. component/atom mapping su reproduktivni i čuvaju alternative;
3. Kabsch rezultat je invariant na order/rigid transform i ne koristi reflection po default-u;
4. DAP coordination tvrdnja navodi isti konkretan metal i sva tri mapirana donor atoma;
5. periodic testovi prolaze za origin/wrap/setting/basis/supercell profile;
6. packing output čuva matched coverage, RMSD, cluster parametre i failure reason;
7. COMPACK/PAC/SOAP/PXRD disagreement set je stručno pregledan pre threshold claim-a;
8. full i candidate-pruned režimi su jasno razdvojeni i potonji ima recall gate;
9. structure-family split prethodi pair generation-u;
10. svi statusi i evidence ostaju dostupni za proveru;
11. relevantni repovi latency distribucije, timeout i peak-memory ulaze u deklarisani computational scope;
12. nijedan overall model ne može sakriti dvosmislenu ključnu granu, nedostajući ulaz ili zaključak blokiran kvalitetom.
