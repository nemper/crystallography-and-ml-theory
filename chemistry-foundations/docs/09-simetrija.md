# 9. Simetrija, prostorne grupe i periodičnost

**Preduslov:** iz [poglavlja 8](08-celija.md) koristiš matricu ćelije, frakcione koordinate, wrap i razliku fizičkog kristala od njegovog koordinatnog opisa. Ovde se uvode simetrijske operacije, ASU i multiplicity.

## Šta treba da umeš posle ovog poglavlja

Posle ovog poglavlja treba da možeš da:

- objasniš šta symmetry operation radi nad frakcionim koordinatama;
- razlikuješ identity, rotation/screw, reflection/glide i inversion;
- iz asimetrične jedinice generišeš sadržaj jedinične ćelije;
- razlikuješ asimetričnu jedinicu, opštu i specijalnu poziciju;
- protumačiš \(Z\), \(Z'\), multiplicity, occupancy i site symmetry bez njihovog mešanja;
- pročitaš osnovno značenje oznake \(P\,2_1/c\), IT broja i Hall simbola;
- objasniš zašto \(P\,2_1/c\) i \(P\,2_1/n\) mogu biti različiti setting-i istog space-group type-a #14;
- transformišeš ćeliju, koordinate i symmetry operations pri promeni basis-a i origin-a;
- dizajniraš poređenje koje je invarijantno na setting, basis, origin, red atoma i red operacija;
- izbegneš i false-negative i false-positive zaključke zasnovane samo na space-group stringu.

## Intuicija: jedna instrukcija proizvodi mnogo ekvivalentnih kopija

Simetrijska operacija je transformacija koja preslikava celu idealizovanu kristalnu strukturu na samu sebe. Ona ne pomera samo jedan atom. Ako se operacija primeni na sve atome asimetrične jedinice, dobija se symmetry-related sadržaj.

~~~mermaid
flowchart LR
    A["ASU N14<br/>51 jedinstvena položaja"]
    S["4 opšte symmetry operations<br/>P 21/c"]
    U["Jedinična ćelija<br/>4 formula units, 204 položaja"]
    T["Translacije n ∈ Z³"]
    C["Beskonačan periodični kristal"]
    A --> S --> U --> T --> C
~~~

Asimetrična jedinica nije nužno ceo molekul, niti je jedinična ćelija nužno „četiri puta kopiran fajl“ bez dodatne logike. Specijalne pozicije, disorder, occupancy i komponente mogu promeniti jednostavno brojanje.

## Simetrijska operacija kao afina transformacija

U frakcionim koordinatama operacija se piše:

\[
\boxed{
\mathbf f'=\mathbf R\mathbf f+\mathbf t
}
\]

gde je:

- \(\mathbf R\) rotacioni/refleksioni deo;
- \(\mathbf t\) translacioni deo u frakcionim jedinicama;
- rezultat se posmatra modulo celobrojne lattice translacije.

Zato su:

\[
\mathbf f'
\quad\text{i}\quad
\mathbf f'+\mathbf n,\qquad\mathbf n\in\mathbb Z^3
\]

isti periodični položaj.

Za kristalografske symmetry operations elementi \(\mathbf R\) u odgovarajućoj frakcionoj bazi tipično su mali celi brojevi. Translacioni deo može sadržati razlomke poput \(1/2\), \(1/3\) ili \(1/4\).

## Osnovni tipovi operacija

| Tip | Geometrijska ideja | Translacioni dodatak |
|---|---|---|
| identity | ništa se ne menja | nema |
| proper rotation | rotacija oko ose | nema netrivijalne translacije duž ose |
| screw axis | rotacija + translacija paralelno osi | da |
| mirror | refleksija kroz ravan | nema glide komponente |
| glide plane | refleksija + translacija paralelno ravni | da |
| inversion | \(\mathbf r\mapsto-\mathbf r\) oko centra | origin određuje zapis |
| rotoinversion | rotacija praćena inverzijom | zavisi od setting-a |

Translation subgroup zatim ponavlja sve dobijene položaje kroz ceo kristal.

!!! info "Za projekat je važnija operacija od imena"
    Naziv screw/glide elementa pomaže razumevanju, ali comparator treba da radi sa punim \((\mathbf R,\mathbf t)\) operacijama i njihovim transformacijama. Sam tekstualni label nije dovoljan za reproduktivno atomsko mapiranje.

## Lokalni P2₁/c primer

<code>cu_n14_a.cif</code> navodi:

- kristalni sistem: monoclinic;
- IT broj: 14;
- Hermann–Mauguin oznaku: <code>P 21/c</code>;
- Hall simbol: <code>-P 2ybc</code>;
- četiri symmetry operations:

\[
\begin{aligned}
1.\quad &(x,\ y,\ z),\\
2.\quad &(-x,\ y+\tfrac12,\ -z+\tfrac12),\\
3.\quad &(-x,\ -y,\ -z),\\
4.\quad &(x,\ -y-\tfrac12,\ z-\tfrac12).
\end{aligned}
\]

Četvrta operacija se može zapisati sa drugim celobrojnim translacionim predstavnikom, na primer dodavanjem celih brojeva komponentama. Time se dobija ista klasa operacija **modulo ćelijske translacije**, pa su wrap-ovani položaji isti. U punom beskonačnom prostoru to ipak jesu različite operacije: mogu dati atome u različitim ćelijama. Pri računu konkretnog kontakta promena predstavnika zato mora biti praćena suprotnom promenom image/translacionog vektora, tako da se sačuva ista fizička kopija atoma.

U standardnoj interpretaciji:

- <code>P</code> označava primitive lattice;
- \(2_1\) označava screw simetriju paralelnu jedinstvenoj osi \(b\);
- <code>c</code> označava glide komponentu u odgovarajućoj ravni;
- point-group tip je \(2/m\).

Ovaj kratki opis nije zamena za punu listu operacija. Položaj osa/ravni zavisi od origin-a i setting-a.

### Simetrija kristala i hiralnost molekula

Inverzija menja hiralni molekul u njegovu suprotnu enantiomernu sliku. Zato uređen kristal koji zaista pripada centrosimetričnoj grupi, kao što je \(P\,2_1/c\), ne može sadržati samo jedan enantiomer hiralnih molekula: ako su oni prisutni, simetrija zahteva i suprotnu sliku. To ne dokazuje da je svaki pojedinačni molekul u takvoj grupi ahiralan.

Uređeni enantiomerno čisti molekulski kristali pripadaju jednoj od 65 **Sohncke** grupa, koje imaju samo translacije, rotacije i screw operacije. Sama Sohncke grupa ipak ne dokazuje enantiomernu čistoću molekulskog sadržaja; treba pregledati sve nezavisne komponente i eksperimentalni dokaz. Hiralnost molekula, hiralnost pakovanja i apsolutna struktura zato su odvojena pitanja. Videti [IUCr: Sohncke grupe](https://dictionary.iucr.org/Sohncke_groups) i [IUCr primeri izbora simetrije kod enantiomerno čistih kristala](https://journals.iucr.org/e/issues/2019/12/00/su5523/index.html); eksperimentalna granica obrađena je u [poglavlju 10](10-difrakcija-kvalitet.md#apsolutna-struktura-i-granica-stereokemijskog-zakljucka).

## Generisanje četiri C1 položaja

C1 u ASU ima:

\[
\mathbf f_{\mathrm{C1}}=
(0.55515,\ 0.54005,\ 0.15800).
\]

Primena četiri operacije i wrap u \([0,1)\) daje:

| Operacija | Pre wrap-a | Posle wrap-a |
|---:|---|---|
| 1 | \((0.55515,0.54005,0.15800)\) | \((0.55515,0.54005,0.15800)\) |
| 2 | \((-0.55515,1.04005,0.34200)\) | \((0.44485,0.04005,0.34200)\) |
| 3 | \((-0.55515,-0.54005,-0.15800)\) | \((0.44485,0.45995,0.84200)\) |
| 4 | \((0.55515,-1.04005,-0.34200)\) | \((0.55515,0.95995,0.65800)\) |

Isti postupak se primenjuje na svih 51 položaj u ASU. Važno je da se molekulske kopije formiraju konzistentno: ako se svaki atom nezavisno wrap-uje, jedna symmetry-generated molekulska kopija može izgledati rascepljeno preko više lica ćelije.

## Asimetrična jedinica

Asimetrična jedinica, ASU, jeste najmanji jedinstveni deo kristalne strukture iz kog se space-group simetrijom dobija sadržaj ćelije, a translacijama ceo kristal.

ASU može sadržati:

- jedan ceo molekul;
- više nezavisnih molekula;
- samo deo molekula ako ostatak generiše specijalna simetrija;
- više komponenti soli, solvata ili kokristala;
- disorder alternative sa parcijalnim occupancy vrednostima;
- deo beskonačne koordinacione ili polimerne mreže.

Zato atom count u ASU nije samostalni hemijski identifikator.

!!! danger "ASU nije sinonim za molekul"
    Molecular RMSD nad ASU koordinatama može porediti različite fragmente ili različit broj nezavisnih molekula. Pre poređenja mora se rekonstruisati hemijska komponenta i definisati da li se poredi molekul, formula unit, local environment ili packing cluster.

## Opšta i specijalna pozicija

Atom je na opštoj poziciji ako ga nijedna netrivijalna operacija ne preslikava na isti položaj modulo lattice translacije. Broj različitih kopija jednak je multiplicity-ju opšte pozicije.

Atom je na specijalnoj poziciji ako ga jedna ili više netrivijalnih operacija ostavljaju na istom periodičnom mestu. Tada:

- site symmetry je viša;
- multiplicity je manji od multiplicity-ja opšte pozicije;
- nezavisni deo molekula može biti frakcija cele hemijske jedinice;
- occupancy i multiplicity moraju se tumačiti zajedno.

Na primer, atom tačno u inversion centru \((0,0,0)\) zadovoljava:

\[
(-x,-y,-z)=(x,y,z)
\]

modulo celobrojnu translaciju. Operacija inverzije ne daje novu kopiju tog atoma.

Pri symmetry expansion-u zato nije ispravno samo proizvesti sve operacije i zadržati duplikate. Duplikati se uklanjaju po periodičnoj geometriji, elementu/species-u, disorder grupi i numeričkoj toleranciji.

## Z, Z′, multiplicity i occupancy

Četiri pojma odgovaraju na različita pitanja:

| Pojam | Pitanje |
|---|---|
| \(Z\) | koliko formula units ima u navedenoj jediničnoj ćeliji? |
| \(Z'\) | koliko kristalografski nezavisnih formula units ima u ASU, u primenljivoj molekulskoj definiciji? |
| multiplicity | koliko ekvivalentnih položaja dato crystallographic site daje u ćeliji? |
| occupancy | koji udeo tih site-ova zauzima navedena vrsta/modelovana alternativa? |

Za jedno atomsko mesto doprinos broju atoma po ćeliji je konceptualno:

\[
N_{\mathrm{cell,site}}
=
m_{\mathrm{site}}\cdot\mathrm{occupancy},
\]

uz pažljiv tretman mešanih vrsta i disorder alternativa.

Za N14:

- četiri su opšte operacije;
- svako navedeno atomsko mesto ima site-symmetry order 1;
- occupancy je 1;
- ASU sadrži jednu kompletnu formulu;
- \(Z=4\).

Zato je \(Z'=1\) i jedna formula iz ASU generiše četiri formula units u ćeliji.

Molekul na inversion centru mogao bi imati samo polovinu svojih atoma nezavisno navedenu i dati \(Z'=0.5\) u uobičajenoj molekulskoj terminologiji. To nije „pola fizičkog molekula“; druga polovina je generisana simetrijom.

## Prostor-na grupa nije samo string

Jedan CIF može pružiti više nivoa identifikacije:

| Zapis | Šta primarno govori |
|---|---|
| crystal system | najšira geometrijska klasa |
| Bravais/lattice centering | translaciona rešetka i centriranje |
| Hermann–Mauguin simbol | čitljiv opis simetrijskih elemenata u setting-u |
| IT broj | tip space group-a, nezavisniji od tekstualne varijante |
| Hall simbol | eksplicitniji opis generatora, ose i origin konvencije |
| puna lista \((R,t)\) | operacije koje se zaista primenjuju u tom zapisu |

Sistem treba da proveri saglasnost tih slojeva. Ne treba tiho „ispraviti“ neslaganje na osnovu samo jednog polja.

## P2₁/c naspram P2₁/n

\(P\,2_1/c\) i \(P\,2_1/n\) mogu biti alternativni setting-i istog space-group type-a sa IT brojem 14. Promenom basis-a, a po potrebi i origin-a, glide komponenta i ćelijski vektori dobijaju drugi zapis, dok fizička struktura može ostati ista.

Lokalni <code>search1</code> audit daje:

- 489 zapisa sa raw stringom <code>P 21/c</code>;
- 380 sa <code>P 21/n</code>;
- ukupno 885 zapisa sa IT brojem 14, jer postoje i druge tekstualne/postavne varijante.

Ako model koristi raw string kao kategoriju, veštački razdvaja veliki broj struktura istog space-group type-a. Ali obrnuta prečica je podjednako pogrešna:

!!! warning "Isti IT broj ne znači isti kristal"
    Dve potpuno različite strukture mogu obe pripadati space group-u #14. IT broj uklanja setting-level false negative; ne dokazuje isti sastav, ćeliju, konformaciju ili packing.

Ispravan comparator traži konkretnu transformaciju ćelije i periodično atomsko mapiranje.

## Promena basis-a i origin-a

Neka je stara cell matrix \(\mathbf A\), a nova:

\[
\mathbf A'=\mathbf A\mathbf P.
\]

Definišimo \(\mathbf o\) kao položaj novog origina izražen u starim frakcionim koordinatama. Tada:

\[
\mathbf f'=\mathbf P^{-1}(\mathbf f-\mathbf o).
\]

Za staru symmetry operation:

\[
\mathbf f_{\mathrm{out}}=
\mathbf R\mathbf f+\mathbf t,
\]

operacija u novom setting-u je:

\[
\boxed{
\mathbf R'=\mathbf P^{-1}\mathbf R\mathbf P
}
\]

i:

\[
\boxed{
\mathbf t'=
\mathbf P^{-1}
\left[
\mathbf t+(\mathbf R-\mathbf I)\mathbf o
\right]
}
\]

modulo celobrojne translacije.

Znak origin člana zavisi od toga kako softver definiše smer transformacije; gornje jednačine važe za eksplicitno navedenu konvenciju \(\mathbf f'=\mathbf P^{-1}(\mathbf f-\mathbf o)\). API poziv bez dokumentovanja konvencije nije reproduktivan.

### Šta sme da se promeni

- brojevi \(a,b,c,\alpha,\beta,\gamma\);
- raw frakcione i Cartesian koordinate;
- Hermann–Mauguin setting string;
- translacioni delovi symmetry operations;
- redosled operacija;
- redosled atoma i način na koji molekul prelazi granicu ćelije;
- \(Z\) i atom count ako se pređe na supercell ili ćeliju druge zapremine.

### Šta fizički ne sme da se promeni

- hemijski sastav i stvarni atomski identitet;
- periodične međuatomske udaljenosti i uglovi;
- koordinaciono i kontaktno okruženje;
- chirality fizičkog objekta, iako koordinatni frame može promeniti handedness;
- gustina;
- apstraktni space-group type za ekvivalentan setting;
- whole-crystal packing, posle ispravnog periodičnog mapiranja.

## Origin invariance

Promena origina za isti vektor svim koordinatama ne menja relativne vektore:

\[
(\mathbf f_i-\mathbf o)
-
(\mathbf f_j-\mathbf o)
=
\mathbf f_i-\mathbf f_j.
\]

Međutim, translacioni delovi symmetry operations se menjaju prema prethodnoj formuli. Zato nije dovoljno pomeriti atome, a ostaviti stare operacije.

Jedan learned model koji direktno koristi apsolutne frakcione koordinate bez periodične/origin invarijantnosti može naučiti proizvoljnu CIF konvenciju umesto strukture.

## Basis i setting invariance kao test, ne obećanje

Pouzdan standardizacioni tok je:

1. sačuvaj originalni CIF i checksum;
2. parsiraj ćeliju, koordinate i punu listu symmetry operations;
3. proveri internu saglasnost space-group tagova i operacija;
4. standardizuj uz eksplicitnu biblioteku, verziju i tolerance;
5. sačuvaj \(\mathbf P\), \(\mathbf o\), determinant i smer transformacije;
6. transformiši koordinate i operacije;
7. symmetry-expand i periodično mapiraj atome nazad na original;
8. proveri element/species, occupancy, maksimalni Cartesian residual i broj mapiranih atoma;
9. tek zatim izračunaj kanonske feature-e.

Metamorphic test treba da napravi ekvivalentne zapise istog kristala:

- promenjen atom order;
- promenjen red operacija;
- celobrojno pomereni atomi;
- drugi origin;
- unimodularna basis promena;
- alternativni \(P\,2_1/c\)/\(P\,2_1/n\) setting;
- primitive/conventional ili validni supercell prikaz.

Skor fizičke sličnosti treba da ostane isti unutar numeričke tolerancije.

## Simetrija i periodični susedi

Sada znaš kako se iz ASU dobijaju fizičke atomske kopije. Pre kontaktnog računa savladaj [zauzeće mesta](10-difrakcija-kvalitet.md#occupancy-koliko-je-kristalografsko-mesto-zauzeto) i [nered modela](10-difrakcija-kvalitet.md#disorder-i-displacement-parametri) u poglavlju 10, pa se vrati na [drugi prolaz poglavlja 7](07-interakcije.md#drugi-prolaz). U [glavnom računu periodičnih suseda](07-interakcije.md#kako-se-stvarno-nalaze-periodicni-susedi) na jednom mestu su formule za simetrijsku sliku, dodatnu ćelijsku translaciju i fizičko rastojanje, uz upozorenje o kosim ćelijama.

U [N14 primeru periodičnog kontakta iz poglavlja 7](07-interakcije.md#lokalni-n14-primer-kontakt-koji-nije-u-atomskom-loop-u), O2 kontakt nije dobijen iz originalnog O2 reda, već iz operacije 2 i translacije \((1,0,0)\):

\[
\mathrm{O2}^{(ii)}
=
(1-x,\ y+\tfrac12,\ -z+\tfrac12).
\]

Promena setting-a može isti fizički kontakt opisati drugim \((R,t,\mathbf n)\) trojcem. Zato contact feature treba da bude kanonizovan po fizičkom atomskom mapiranju i geometriji, dok se originalni trojac čuva kao provenance.

## Specijalne pozicije i ML/graf greške

Na specijalnoj poziciji više operacija može proizvesti isti atom. Ako se duplikati ne uklone:

- koordinacioni broj se lažno povećava;
- contact count se duplira;
- graph degree postaje zavisan od CIF encoding-a;
- formula i gustina se mogu pogrešno izračunati;
- packing comparator kažnjava potpuno ekvivalentne strukture.

Deduplication tolerance mora biti:

- izražena u Cartesian udaljenosti, ne samo frakcionoj razlici;
- manja od hemijski relevantnih razmaka;
- dokumentovana i verzionisana;
- testirana na velikim i malim ćelijama;
- svesna elementa/species-a, occupancy-ja i disorder grupe.

Ne spajaj dva različita disorder atoma samo zato što su blizu, niti zadržavaj dve symmetry-generated kopije istog specijalnog mesta.

## Simetrija je deo eksperimentalnog modela

Space group nije nepogrešiva nalepnica:

- moguća je propuštena viša simetrija;
- pseudosymmetry može izgledati kao prava simetrija;
- twinning i disorder mogu otežati određivanje;
- tolerancije programa mogu dati različite standardizacije;
- CIF tag, Hall simbol i navedene operacije mogu biti nesaglasni.

Zato se originalna dodela ne prepisuje automatski rezultatom biblioteke. Čuvaju se oba sloja:

- reported symmetry;
- computed/standardized symmetry sa alatom, verzijom, tolerancijom i upozorenjima.

[IUCr checkCIF](https://checkcif.iucr.org/) i odgovarajući lokalni alati služe kao dijagnostika. Za poverljive strukture ne šalji CIF javnom servisu bez dozvole.

## Teorijske posledice za dve aplikacije

### Globalna pretraga

- IT number/type, Hall simbol, reported setting i standardized setting nose različite informacije i ne treba ih poistovetiti.
- Koristi space group kao filter ili feature, ne kao dokaz identiteta.
- Cell/packing poređenje zahteva kompatibilnu reprezentaciju ćelije i koordinata uz očuvanu vezu sa originalom i transformacijom.
- Candidate generation može koristiti lattice i symmetry klasu; reranking mora proveriti hemiju i periodično atomsko okruženje.
- Raw <code>P21/c</code>/<code>P21/n</code> kategorije mogu stvoriti lažnu udaljenost ako se setting ne razreši.
- Symmetry-confidence i detected-vs-reported neslaganje treba da utiču na uncertainty.

### Poređenje svih parova

Za tumačenje pairwise poređenja relevantni su:

- da li je nađena validna basis/origin transformacija;
- cell i symmetry residual;
- atom-mapping coverage;
- maksimalnu i RMS periodičnu atomsku razliku;
- odnos primitive/conventional/supercell;
- slaganje komponenti, koordinacije, konformacije i packing-a;
- nejasnoće zbog specijalnih pozicija, disorder-a i tolerancije.

Sledeći redosled izražava algoritamske zavisnosti, ne plan implementacije:

1. proveri sastav i komponente;
2. pronađi kompatibilne lattice/basis transformacije;
3. usaglasi space-group setting i origin;
4. generiši/dedupliciraj periodične položaje;
5. pronađi hemijski validan atom mapping;
6. poredi lokalnu geometriju, konformaciju, packing i kontakte;
7. poveži zaključak sa dokaznom transformacijom i uncertainty-jem.

## Tipične zamke

1. Tretirati ASU kao obavezno ceo molekul.
2. Tretirati svaku symmetry-generated kopiju kao novu hemijsku vrstu.
3. Zaboraviti wrap modulo celobrojnih translacija.
4. Zadržati duplikate specijalne pozicije.
5. Izračunati \(Z'\) prostim deljenjem bez provere occupancy-ja i multiplicity-ja.
6. Tretirati <code>P21/c</code> i <code>P21/n</code> kao nepovezane klase.
7. Zaključiti da su dve strukture iste samo zato što imaju IT broj 14.
8. Promeniti basis koordinata, ali ne i symmetry operations.
9. Pomeriti origin atoma, ali ostaviti stare translacione delove operacija.
10. Koristiti indeks symmetry operation kao globalni feature.
11. Verovati jednoj softverskoj standardizaciji bez čuvanja tolerancije i verzije.
12. Pretvoriti pseudosymmetry u „ispravljenu“ višu simetriju bez kristalografskog pregleda.
13. Koristiti apsolutne frakcione koordinate kao ML feature bez origin invarijantnosti.
14. Dopustiti da izbor supercell-a promeni crystal similarity.

## Mini-vežbe

### 1. Četiri C1 položaja

Primeni sve četiri operacije lokalnog CIF-a na C1 i wrap-uj rezultat.

??? success "Odgovor"
    Dobijaju se \((0.55515,0.54005,0.15800)\), \((0.44485,0.04005,0.34200)\), \((0.44485,0.45995,0.84200)\) i \((0.55515,0.95995,0.65800)\).

### 2. Broj položaja u ćeliji

ASU ima 51 atomsko mesto, sva su opšta i potpuno zauzeta. Koliko symmetry-expanded položaja ima ćelija?

??? success "Odgovor"
    \(51\times4=204\). To je saglasno sa četiri formula units, odnosno \(Z=4\), jer jedna formula ima 51 navedeni atom.

### 3. P2₁/c i P2₁/n

Da li dva CIF-a, jedan označen \(P\,2_1/c\), drugi \(P\,2_1/n\), automatski predstavljaju isti kristal?

??? success "Odgovor"
    Ne. Oznake mogu biti alternativni setting-i istog space-group type-a #14, pa raw string razlika nije dokaz različitosti. Ipak, potrebno je pronaći basis/origin transformaciju i proveriti hemijski sadržaj i periodično atomsko mapiranje.

### 4. Promena origina

Svim atomima oduzmeš isti origin shift. Koje veličine sigurno ostaju iste, a šta još moraš transformisati?

??? success "Odgovor"
    Relativne fizičke udaljenosti, uglovi i packing ostaju isti. Moraju se transformisati i translacioni delovi symmetry operations; raw frakcione koordinate i njihov zapis se menjaju.

### 5. Specijalna pozicija

Atom na \((0,0,0)\) u centrosimetričnoj grupi generisan je identity i inversion operacijom. Da li su to dva atoma?

??? success "Odgovor"
    Ne. Inverzija ga vraća na isto periodično mesto. To je specijalna pozicija sa smanjenim multiplicity-jem; duplikat se uklanja uz odgovarajuću toleranciju i species proveru.

### 6. Metamorphic test

Comparator daje 0,72 za originalni CIF, a 0,41 kada se samo promeni red symmetry operations. Šta je zaključak?

??? success "Odgovor"
    Comparator ima encoding artefakt. Red operacija nema fizičko značenje. Test treba da padne, a feature/mapping sloj mora biti kanonizovan ili permutaciono invarijantan.

### 7. Dve strukture sa IT #14

Koji je minimalni sledeći dokaz posle jednakog IT broja?

??? success "Odgovor"
    Potrebna je kompatibilna transformacija ćelije i origin-a, zatim periodično atomsko mapiranje uz isti hemijski sadržaj. Bez toga IT broj samo kaže da strukture pripadaju istom apstraktnom tipu prostor-ne grupe.

## Kriterijum prolaza

Poglavlje si savladao kada možeš da generišeš četiri N14 C1 položaja, obrazložiš \(Z=4\) i \(Z'=1\), objasniš \(P\,2_1/c\) naspram \(P\,2_1/n\), napišeš basis/origin transformaciju i definišeš metamorphic test kojim se dokazuje da rezultat obe aplikacije ne zavisi od proizvoljnog CIF setting-a.

## Primarni i autoritativni izvori

- [IUCr Core CIF dictionary](https://www.iucr.org/resources/cif/dictionaries/cif_core)
- [IUCr CIF dictionaries browser](https://cif-dictionaries.iucr.org/cifdic/dichtm.php?dic=cif_core_2.4.5)
- [IUCr teaching pamphlet 9: matrices, translations and transformations](https://www.iucr.org/education/pamphlets/9)
- [IUCr teaching pamphlet 13: symmetry](https://www.iucr.org/education/pamphlets/13)
- [IUCr teaching pamphlet 14: space groups](https://www.iucr.org/education/pamphlets/14)
- [IUCr Online Dictionary: \(Z\) and \(Z'\)](https://dictionary.iucr.org/Z_and_Z%27)
- [IUCr checkCIF PLAT128: non-standard \(P\,2_1/n\) setting](https://journals.iucr.org/services/cif/checking/PLAT128.html)
- [IUCr discussion of alternative monoclinic settings](https://journals.iucr.org/a/issues/2007/05/00/sh0188/index.html)
- [spglib: symmetry dataset, transformations and origin shifts](https://spglib.readthedocs.io/en/stable/dataset.html)
- [CCDC Python API: packing similarity](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/packing_similarity.html)
