# Brzi podsetnik za projektovanje dve aplikacije

Ova strana je operativna kontrolna tabla. Koristi je kada primaš novi CIF, definišeš zahtev sa hemičarem, projektuješ pipeline, pregledaš rezultat ili odlučuješ da li je verzija sistema spremna za demonstraciju.

!!! danger "Prvo pitanje nije: koji model?"
    Prvo odredi **koji objekat** porediš i **po kom svojstvu**. Sastav, molekulski graf, koordinaciono okruženje, 3D konformacija, kristalno pakovanje i mreža interakcija nisu ista stvar. Jedan broj bez tih specifikacija nema stabilno naučno značenje.

## Dve aplikacije u jednoj tabeli

| | Aplikacija 1 — globalna CSD pretraga | Aplikacija 2 — precizno poređenje svih parova |
|---|---|---|
| ulaz | jedan korisnički CIF + filteri + izabrani search mode | skup korisničkih CIF-ova + comparison profile |
| glavni cilj | visok odziv relevantnih kandidata pri prihvatljivoj latenciji | stručno verodostojan i rastavljiv izveštaj za svaki potreban par |
| osnovni obrazac | jeftini filteri → candidate generation → skuplji reranking | validacija → component/atom mapping → višeslojno poređenje |
| tipičan rizik | brz indeks tiho propušta relevantne strukture | kvadratni broj parova i prividno precizan, ali neuporediv score |
| obavezan dokaz | recall@k prema exact/ekspertskoj referenci, latency i explanation | evidence po nivou, coverage, status i invariance/metamorphic testovi |
| licencna granica | CSD indeks i raw podaci ostaju u odobrenom licensed data-plane-u | svaki ulaz i izvedeni pair report nasleđuju odgovarajuću politiku pristupa |

Detaljni nacrti su na stranama [Globalna pretraga](../projekat/18-globalna-pretraga.md), [Poređenje parova](../projekat/19-parovi.md) i [Evaluacija](../projekat/20-evaluacija.md).

## Odluka 0: šta tačno znači „slično“?

Pre koda dopuni ovu rečenicu:

> Za objekat **____**, u svrhu odluke **____**, relevantnost znači **____**; obavezno razlikujemo **____**, a rezultat važi samo kada su dostupni **____**.

Izaberi jedan ili više slojeva, ali ih u izlazu ne stapaj prerano:

| Sloj | Pitanje | Minimalan dokaz | Šta ne dokazuje |
|---|---|---|---|
| sastav | isti elementi, broj atoma, naboj i komponente? | formula/component tabela sa ulogama | isti graf ili ista supstanca |
| 2D graf | isti scaffold, podstruktura ili povezanost? | eksplicitni graph policy i atom mapping | ista konformacija ili packing |
| koordinacija | isti metal, donor set, CN i geometrija? | metal–donor mapping, distance/angle model, confidence | isto prisustvo metala u entry-ju |
| 3D konformacija | mapirani atomi imaju sličan raspored? | mapping, alignment, coverage i RMSD | isti periodični kristal |
| ćelija/rešetka | metrike rešetke su kompatibilne? | standardizovana/redukovana ćelija i tolerancije | isti packing |
| packing | isto periodično okruženje molekula? | periodični klaster, matched molecules, RMSD i parametri | isti property ili ista stabilnost |
| interakcije | iste H-veze, koordinacione ili druge kontaktne mreže? | definicije, geometrija, periodična topologija i uncertainty | energiju ili „jačinu“ bez dodatnog modela |
| svojstvo | slično ponašanje za tačno određenu metu? | merena vrednost, jedinica, uslovi i provenance | strukturnu identičnost |

Ako stručnjak ne može da popuni rečenicu, sistem treba da ponudi odvojene modove, ne neobjašnjivo dugme **Similar**.

## Zajednička ingest kapija

Svaki ulaz prolazi istim redosledom. `Parse success` nije dovoljno.

### 1. Registruj izvor pre transformacije

- [ ] sačuvan je netaknut original i SHA-256;
- [ ] zabeleženi su source/owner, datum prijema i nivo poverljivosti;
- [ ] postoji licenca ili eksplicitno stanje `unresolved_block_use`;
- [ ] parser, dictionary/profile i verzija su zabeleženi;
- [ ] raw, canonical i derived prikazi imaju različite identifikatore;
- [ ] nijedan proprietary ulaz nije poslat eksternom servisu bez dozvole.

Zašto: hash potvrđuje koji su bajtovi obrađeni; ne potvrđuje tačnost, vidljivost ni pravo korišćenja. Vidi [Licence, FAIR i poreklo](../projekat/21-licence-fair.md).

### 2. Prepoznaj stvarni format i njegov domet

| Format | Tipično čuva | Kritičan gubitak/odluka |
|---|---|---|
| CIF | ćeliju, simetriju, atom sites, occupancy i eksperimentalne metadata | veze i component roles mogu zahtevati hemijski model |
| MOL | connection table i eventualne koordinate | nema periodični kristalni kontekst |
| MOL2 | atom/bond tipove, substructure i opcione parcijalne naboje | tipovi i naboji su dodela konkretnog softvera |
| SDF | niz MOL zapisa + proizvoljna property polja | schema, jedinice i missing semantika nisu automatski pouzdani |
| SMILES | linijski zapis molekulskog grafa | ne čuva ćeliju, packing, occupancy ni eksperimentalnu 3D strukturu |

- [ ] izabran je pravi CIF data block i razlog je zabeležen;
- [ ] `.` i `?` nisu pretvoreni u nulu;
- [ ] frakcione i kartezijanske koordinate nisu pomešane;
- [ ] veliki HKL, SHELX ili tekstualni blokovi nisu poslati modelu kao hemijski tokeni;
- [ ] svaka konverzija ima loss report.

Vidi [Formati](../podaci/12-formati.md) i [Standardizacija](../podaci/13-standardizacija.md).

### 3. Proveri tri različite konzistentnosti

**Sintaksa i šema**

- [ ] CIF tokenizer/loop struktura i dictionary data names su validni;
- [ ] obavezna polja za traženu analizu postoje;
- [ ] jedinice i tipovi vrednosti su eksplicitni.

**Hemija**

- [ ] formula, atom-site elementi, komponente i formalni ukupni naboj su saglasni;
- [ ] H atomi, protonacija, tautomerija i stereo imaju poznat status;
- [ ] bond/atom typing ima provenance i confidence;
- [ ] metal u formuli je odvojen od direktno koordinisanog metala;
- [ ] solvent, counterion, coformer i parent entity nisu nasumično odbačeni.

**Kristalografija**

- [ ] ćelija, space group/symmetry operacije i frakcione koordinate su upotrebljivi;
- [ ] \(Z\), \(Z'\), site multiplicity i occupancy nisu pomešani;
- [ ] disorder alternative nisu pretvorene u više istovremeno punih atoma;
- [ ] quality vector obuhvata R/wR/GoF, completeness/resolution, temperature, s.u., residual density, restraints, disorder/twinning i checkCIF alerts gde su dostupni;
- [ ] alert je pregledan u kontekstu — ne postoji univerzalni `R < x` ili „zelen checkCIF = istina“ kriterijum.

Vidi [Difrakcija i kvalitet](../kristali/10-difrakcija-kvalitet.md).

### 4. Klasifikuj čvrstu formu pre deduplikacije

- [ ] isto neutralno/jonsko hemijsko jezgro, ali drugačiji crystal arrangement → kandidat za polimorf;
- [ ] proton transfer + counterion → so;
- [ ] voda u kristalnoj strukturi → hidrat;
- [ ] drugi rastvarač u strukturi → solvat;
- [ ] više različitih komponenti u jednoj fazi, uz odgovarajuću stručnu definiciju → kandidat za kokristal;
- [ ] nepoznat položaj H/protonacije → `ambiguous`, ne automatska so ili kokristal;
- [ ] anhydrous/hydrated, salt/free form i polymorph relacije čuvaju se odvojeno.

Termodinamički najstabilnija forma pri jednim uslovima nije nužno forma koja prva nastaje. Zabeleži temperaturu, pritisak, sastav rastvarača, vodenu aktivnost, istoriju uzorka i kinetički kontekst. Vidi [Čvrste forme](../kristali/11-cvrste-forme.md).

## Aplikacija 1: odluke za globalnu pretragu

### A. Ugovor upita

- [ ] objekat je `parent ligand`, `coordination entity`, `full crystal form` ili drugi eksplicitan tip;
- [ ] search mode je composition, exact/substructure, 2D similarity, coordination, 3D, cell, packing ili interaction;
- [ ] hard filters navode scope: puna formula, komponenta, ligand, metal environment ili metadata;
- [ ] korisnik bira include/exclude solvente, counterione i coformers;
- [ ] nepoznat charge/stereo/bond/disorder ima definisano ponašanje;
- [ ] postoje abstention pravila pre kandidata i pre prikaza rezultata.

!!! example "Filter `Cu` ima najmanje četiri značenja"
    1. Cu se pojavljuje u punoj entry formuli.  
    2. Cu pripada izabranoj coordination entity.  
    3. Cu je direktno koordinisan ciljnom ligandu.  
    4. Cu je u odvojenoj komponenti/counterion-u.  
    UI i query manifest moraju reći koje od ovoga važi.

### B. Retrieval kaskada

1. primeni access-control i dozvoljene metadata filtere;
2. uradi exact/substructure proveru kada je to zahtev;
3. generiši širok skup kandidata fingerprint/ANN metodom;
4. ponovo rangiraj exact graph/MCS metodom;
5. uključi koordinacionu i 3D geometriju samo kada su validne;
6. pokreni packing/interactions samo kada obe strane imaju dovoljan kristalni dokaz;
7. kalibriši score za konkretan claim i sastavi explanation.

Za binarne fingerprint skupove \(A\) i \(B\):

\[
T(A,B)=\frac{|A\cap B|}{|A|+|B|-|A\cap B|}.
\]

Obavezno prikaži fingerprint tip, radius, dužinu, stereo/charge policy i verziju standardizacije. `T=0,8` bez toga nije ponovljiv rezultat.

### C. Kartica rezultata

- [ ] entry/refcode, CSD release i dozvoljeni nivo prikaza;
- [ ] composition/components/solid-form status;
- [ ] rank, search mode i verzije representation/metric;
- [ ] matched subgraph i coverage;
- [ ] metal, donor set, CN/geometrija i confidence;
- [ ] 3D mapping/RMSD i packing/interactions samo gde važe;
- [ ] quality compatibility, missing data i warnings;
- [ ] jasno objašnjenje zašto je kandidat rangiran;
- [ ] download/export je vidljiv samo ako policy to dozvoljava.

### D. Pre puštanja

- [ ] candidate recall je izmeren prema exact ili skupljoj referenci;
- [ ] recall@k, precision@k, nDCG/MAP, coverage i abstention su prijavljeni;
- [ ] latency p50/p95 i freshness indeksa su izmereni;
- [ ] rezultati su isečeni po metalima, formama, disorder-u, kvalitetu i missingness-u;
- [ ] skoro duplirani entry/family zapisi nisu procurili između train i test;
- [ ] license test blokira bulk enumeration i nedozvoljeni eksport.

## Aplikacija 2: odluke za poređenje svih parova

### A. Plan poređenja pre score-a

Za \(n\) različitih struktura broj neuređenih parova je:

\[
N_{\text{parova}}=\frac{n(n-1)}{2}.
\]

Primeri: 10 → 45, 100 → 4.950, 1.000 → 499.500, 2.110 → 2.224.995 parova.

- [ ] utvrđena je jedinica: ligand, cela coordination entity, formula unit ili crystal;
- [ ] komponente su klasifikovane i globalno uparene pre atom mapping-a;
- [ ] unmatched solvent/counterion/coformer ostaje u izveštaju;
- [ ] svaka grana može vratiti `valid`, `ambiguous`, `not-applicable`, `missing-input` ili `failed`;
- [ ] `not comparable` nije kodirano kao numerička nula;
- [ ] per-structure features se računaju jednom, a par ima simetričan, verzionisan cache ključ.

### B. Redosled grana

1. component mapping;
2. exact/substructure/MCS i atom mapping;
3. metal/donor/CN/coordination geometry;
4. poravnata 3D konformacija;
5. standardizovana ćelija kao candidate signal;
6. periodični packing;
7. definisane interaction networks;
8. evidence-rich report i, samo ako je opravdano, kalibrisan combined score.

Za \(N\) mapiranih atoma posle definisanog optimalnog poravnanja:

\[
\mathrm{RMSD}=\sqrt{\frac{1}{N}\sum_{i=1}^{N}\|\mathbf{x}_i-\mathbf{y}_i\|^2}.
\]

RMSD mora pratiti: mapping/common core, \(N\), coverage, izbor heavy/all atoms, symmetry-equivalent atom policy, H/stereo/disorder policy, tip poravnanja i poreklo koordinata.

### C. Obavezne invarijanse

Rezultat za isti naučni objekat ne sme se promeniti samo zbog:

- [ ] permutacije redosleda atoma ili komponenti;
- [ ] rigidne rotacije/translacije;
- [ ] periodičnog wrap-a preko granice ćelije;
- [ ] symmetry-equivalent ASU/origin izbora;
- [ ] ekvivalentnog \(P\,2_1/c\leftrightarrow P\,2_1/n\) setting-a;
- [ ] invertibilne promene baze/konvencionalne ćelije;
- [ ] drugog validnog SMILES atom ordering-a.

Namerno negativni testovi moraju razlikovati istu formulu/drugi izomer, isti ligand/drugi metal, isti metal/drugu geometriju, isti molekul/drugi polimorf i metal samo u counterion-u.

### D. Izveštaj jednog para

```yaml
pair: {a: structure-version-A, b: structure-version-B}
comparison_profile: dap-crystal-v1
composition: {status: valid, exact: false, unmatched: ["water in B"]}
graph: {status: valid, mapped_heavy_atoms: 28, coverage: 0.82}
coordination: {status: ambiguous, reason: "two plausible neighbor models"}
geometry: {status: valid, rmsd_angstrom: 0.62, policy: heavy-rigid-v2}
packing: {status: missing-input, reason: "A has no valid unit cell"}
overall: {score: null, decision: human-review}
```

`null` je tačan izlaz kada ključni claim nije ocenjen; 0 bi lažno tvrdila validno izmerenu nepodudarnost.

## Lokalni sanity-check: `cu_n14_a.cif`

Pre nego što aplikacija išta rangira, očekuj sledeći sažetak:

| Polje/dokaz | Vrednost | Ispravno tumačenje |
|---|---:|---|
| formula | `C25 H20 N3 O2 P` | nema Cu u sastavu uprkos imenu fajla |
| zračenje | Cu Kα, \(\lambda=1,54178\) Å | `Cu` ovde opisuje izvor zračenja, ne atom uzorka |
| temperatura | 100 K | geometrija nije automatski reprezentativna za sve temperature |
| space group | \(P\,2_1/c\) | simetrijski tip, ne identitet packing-a ili polimorfa |
| ćelija | \(a=12,7138(3)\), \(b=15,3951(4)\), \(c=10,6106(3)\) Å; \(\beta=93,235(1)^\circ\) | brojevi u zagradi su s.u. poslednjih cifara |
| \(Z\) | 4 | formula units u ćeliji; nije automatski \(Z'\) |
| R(all)/R(gt) | 0,0347 / 0,0322 | različiti skupovi refleksija; nema univerzalnog quality praga |
| wR(ref)/GoF | 0,0838 / 1,095 | druga formula/težine; GoF blizu 1 nije dokaz hemijske istine |
| occupancy/disorder polja | sva navedena mesta 1; grupe prazne | nema eksplicitno modelovanih alternativa; ne dokazuje odsustvo svakog problema |
| sadržaj fajla | uključuje SHELX/HKL blokove | nije bezazlen „mali koordinatni fajl“ za prompt ili eksport |

Ako parser iz naziva `cu_n14_a.cif` proizvede element Cu, ako pretvori `12.7138(3)` u dva broja ili ako učita obe disorder alternative kao pune atome, zaustavi downstream ML.

## Crvene zastavice: odmah zaustavi ili degradiraj claim

| Signal | Akcija |
|---|---|
| licenca/owner nepoznati | karantin; dozvoli samo eksplicitno odobren lokalni QA |
| formula i atom-site elementi se ne slažu | ne koristi composition/graph rezultat dok se ne razjasni |
| nema validne ćelije ili symmetry | dozvoli 2D; packing označi `missing-input` |
| nepoznate veze ili metal connectivity | rezultat coordination/graf grane `ambiguous` ili low-confidence |
| više komponenti bez uloga | traži component selection; ne koristi „najveći fragment“ kao univerzalni default |
| nepoznata stereo/protonacija | ne tvrdi exact stereo/form identity |
| ozbiljan checkCIF alert | pregled stručnjaka i zabeleženo obrazloženje; ne automatsko brisanje |
| train/test dele compound/refcode family | ponovi split i evaluaciju |
| top-k iz ANN-a nema recall baseline | rezultat nije validiran kao retrieval sistem |
| score nema metric/representation verziju | ne poredi ga sa ranijim rezultatom |
| skriveni PDF tekst se ne vidi u renderu | zadrži raw evidence, karantin spornog teksta, vizuelni/OCR QA |
| rezultat krši export policy | fail closed; ne vraćaj strukturu/download |

## Pet pitanja pre svake stručne tvrdnje

1. **Objekat:** entry, crystal, formula unit, coordination entity, ligand ili molecular graph?
2. **Dokaz:** direktno polje/meren podatak, izvedena vrednost ili algoritamska dodela?
3. **Uslovi:** temperatura, sastav, representation/metric verzija i quality status?
4. **Neizvesnost:** s.u., missingness, ambiguity, coverage, calibration ili applicability domain?
5. **Pravo:** sme li se podatak obraditi, keširati, deliti i objaviti u ovom obliku?

Ako ijedan odgovor nedostaje, tvrdnja dobija ograničenje ili status `not assessed`; ne popunjava se nagađanjem.

## Go/no-go kartica za izdanje

### GO samo ako

- [ ] svaki ulaz ima parse status, originalni hash i transformacioni dnevnik;
- [ ] objekat i svi nivoi sličnosti su imenovani;
- [ ] missing/ambiguous/not-applicable se razlikuju od 0 i `false`;
- [ ] quality se čuva kao vektor dokaza, ne kao jedan magični prag;
- [ ] osnovni transparentni baseline-i su implementirani;
- [ ] held-out metrike i slice analiza zadovoljavaju unapred dogovorene kriterijume;
- [ ] svaki score ima evidence, parametre i verziju;
- [ ] metamorphic/invariance testovi prolaze;
- [ ] licence, retention, eksport i brisanje derivata su izvršive politike;
- [ ] hemičar/kristalograf može da ospori rezultat na nivou konkretnog atoma, komponente ili periodičnog suseda.

### NO-GO ako

- „AI kaže da je slično“ zamenjuje operational definition;
- CSD pristup ili ugovor još nisu dostupni, a sistem tvrdi validaciju nad celom bazom;
- random split deli skoro iste structure families;
- lep cluster/heatmap se predstavlja kao naučna validacija;
- privatni repo se predstavlja kao dozvola za CSD redistribuciju;
- model ne ume da kaže „nemam dovoljan dokaz“.

## Jednominutna provera znanja

1. Isti molekulski graf i drugačiji packing — koji slojevi se slažu, a koji ne moraju?
2. Zašto reduced-cell pogodak nije dokaz istog polimorfa?
3. Koja tri podatka uz RMSD sprečavaju najčešću pogrešnu interpretaciju?
4. Šta je ispravan izlaz packing grane kada CIF nema ćeliju?
5. Da li CSD-derived embedding automatski sme u javni repo?

??? success "Odgovori"
    1. Slaže se 2D identitet/graf; konformacija može, ali ne mora; packing i interaction mreža mogu biti različiti.  
    2. Različiti kristali mogu imati sličnu metriku ćelije; potrebno je periodično poređenje mapiranih molekula i eksplicitni parametri.  
    3. Atom mapping/common core, broj i coverage mapiranih atoma, te alignment/symmetry/H/stereo policy; korisno je navesti i poreklo koordinata.  
    4. `missing-input` ili `not assessed` sa razlogom, ne score 0.  
    5. Ne. Proveravaju se konkretni ugovor, derivative pravila, mogućnost rekonstrukcije i potrebno pisano odobrenje.
