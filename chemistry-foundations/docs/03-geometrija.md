# 3. Molekulska geometrija i konformacija

**Prioritet: MORAŠ.** Kristalni podaci su trodimenzionalni. Graf kaže ko je povezan; geometrija kaže kako su atomi raspoređeni.

**Preduslov:** iz [poglavlja 2](02-veze.md) razlikuješ vezne i slobodne elektronske parove, red veze i povezanost atoma. Za koordinatne račune potrebni su vektor, norma i skalarni proizvod iz osnovnog matematičkog uvoda; ćelija i kristalna simetrija još nisu potrebne.

## 3.1 Od Lewisovog crteža do 3D

Elektronski parovi se prostorno raspoređuju. Jednostavan VSEPR model predviđa osnovne geometrije glavne grupe:

| Broj elektronskih domena | Idealni raspored | Tipičan ugao |
|---:|---|---:|
| 2 | linearan | 180° |
| 3 | trigonalno planaran | 120° |
| 4 | tetraedarski | 109,5° |

**Elektronski domen** je jedan pravac vezivanja ili jedan nevezani par oko centralnog atoma; jednostruka, dvostruka i trostruka veza prema jednom susedu računaju se svaka kao jedan domen. Tabela opisuje raspored domena. Oblik molekula opisuje samo položaje atoma: CH₄ ima tetraedarski oblik, NH₃ trigonalno-piramidalni, a H₂O savijeni, iako u sva tri primera centralni atom ima četiri domena. Zato broj domena nije isto što i broj vezanih atoma.

Lone pairs odbijaju drugačije od bonding pairs, pa stvarni uglovi odstupaju. Hibridizacije `sp`, `sp2`, `sp3` su koristan model lokalne geometrije i vezivanja, ali nisu dovoljne za sve metale ili delokalizovane sisteme. [OpenStax: molekulska struktura i polaritet](https://openstax.org/books/chemistry-2e/pages/7-6-molecular-structure-and-polarity) daje vizuelne primere.

## 3.2 Tri osnovne geometrijske veličine

Za kartezijanske koordinate \(\mathbf r_i=(x_i,y_i,z_i)\):

### Dužina

\[
d_{ij}=\lVert\mathbf r_j-\mathbf r_i\rVert_2.
\]

U lokalnom N14 primeru C1-C2 je približno 1,386 Å, dok je C1-N1 približno 1,468 Å. Broj sam nema značenje bez elemenata, bond tipa, hemijskog okruženja, temperature i neizvesnosti.

### Ugao

Za A-B-C, vrh je B. Ako su \(\mathbf u=\mathbf r_A-\mathbf r_B\) i \(\mathbf v=\mathbf r_C-\mathbf r_B\):

\[
\theta=\arccos\left(\frac{\mathbf u\cdot\mathbf v}{\lVert\mathbf u\rVert\lVert\mathbf v\rVert}\right).
\]

Promena redosleda atoma može promeniti koji je atom vrh; naziv ugla zato mora čuvati atom mapping.

### Torzioni (dihedral) ugao

Za A-B-C-D porede se ravni ABC i BCD. Potpisani ugao je tipično u opsegu \((-180^\circ,180^\circ]\). On opisuje rotaciju oko centralne veze B-C i presudan je za konformaciju. Zbog kružne prirode, prosečna vrednost uglova +179° i -179° nije 0°; potrebna je circular statistics.

Za račun iz koordinata postavi \(\mathbf b_1=\mathbf r_B-\mathbf r_A\), \(\mathbf b_2=\mathbf r_C-\mathbf r_B\), \(\mathbf b_3=\mathbf r_D-\mathbf r_C\) i normale \(\mathbf n_1=\mathbf b_1\times\mathbf b_2\), \(\mathbf n_2=\mathbf b_2\times\mathbf b_3\). Jedna eksplicitna konvencija je:

\[
\phi=\operatorname{atan2}\!\left(
\frac{\mathbf b_2}{\lVert\mathbf b_2\rVert}\cdot(\mathbf n_1\times\mathbf n_2),
\mathbf n_1\cdot\mathbf n_2
\right).
\]

`atan2(y,x)` čuva kvadrant i znak; rezultat u radijanima pretvara se u stepene množenjem sa \(180/\pi\). Ako su A–B–C ili B–C–D kolinearni, odgovarajuća normala je nula i torzija nije definisana. Na primer, za A=(0,1,0), B=(0,0,0), C=(1,0,0), D=(1,0,1) gornja konvencija daje +90°. Red atoma i konvenciju znaka treba zabeležiti pre poređenja sa drugim alatom.

## 3.3 Konstitucija, konfiguracija i konformacija

| Pojam | Šta se razlikuje | Da li obična rotacija oko single veze pomaže? |
|---|---|---|
| konstitucioni izomer | povezanost atoma | ne |
| konfiguracioni stereoizomer | prostorni raspored koji se ne menja običnom slobodnom rotacijom; interkonverzija zahteva prolazak kroz dovoljno visoku barijeru | ne |
| konformer | 3D oblik istog grafa/konfiguracije | često da; u prstenu su promene torzija međusobno povezane |

„Zahteva kidanje veze“ korisna je intuicija za neke konfiguracione promene,
ali nije univerzalna definicija. Na primer, inverzija piramidalnog N može
promeniti prostorni raspored bez raskida sigma veze, dok ograničena rotacija
može dati izolabilne atropizomere. Razlika konfiguracija–konformacija zato
zavisi i od mehanizma, energetske barijere i vremenske skale posmatranja.

### Hirnost

Objekat je hiralan ako se ne može poklopiti sa sopstvenom slikom u ogledalu. Par takvih stereoizomera su enantiomeri. Za poređenje je važno da algoritam ne dopusti refleksiju ako apsolutna konfiguracija treba da ostane različita.

### E/Z i cis/trans

Ograničena rotacija oko double veze može dati različite konfiguracije. SMILES, MOL/SDF i CIF ne čuvaju stereokemiju na isti način; prazna stereo oznaka ne mora značiti da je molekul ahiralan, već da informacija nije određena ili nije preneta.

Za alken čija oba C atoma nose po dva različita supstituenta, E/Z oznaka se dobija poređenjem prioriteta po Cahn–Ingold–Prelog (CIP) pravilima na svakom kraju dvostruke veze. Viši atomski broj neposredno vezanog atoma daje viši prioritet; izjednačenje zahteva poređenje sledećih suseda po tim pravilima. Dve grupe višeg prioriteta na istoj strani daju **Z**, a na suprotnim stranama **E**. Prioritet nije isto što i prostorna veličina grupe. Cis/trans opisuje odnos izabranih grupa i nije univerzalna zamena za E/Z. [OpenStax: E/Z označavanje](https://openstax.org/books/organic-chemistry/pages/7-5-alkene-stereochemistry-and-the-e-z-designation) daje postupak i primere.

## 3.4 Konformaciona energija nije kristalna stabilnost

Rotacija menja steričke sudare, konjugaciju, intramolekulske H-veze i energiju izolovanog molekula. U kristalu molekul može prihvatiti više-energy konformer ako time dobija povoljnije intermolekulske kontakte i pakovanje.

Zato:

\[
\text{niža energija konformera} \not\Rightarrow \text{stabilniji kristal bez dodatne analize}.
\]

CCDC-ov [Molecular Geometry Analysis](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/molecular_geometry_analysis.html) poredi bond lengths, valence angles, torsions i ring conformations sa hemijski klasifikovanim CSD distribucijama. "Unusual" geometrija je signal za proveru, ne dokaz greške ili metastabilnosti.

## 3.5 Poravnanje i RMSD

Za dva već mapirana skupa od \(N\) atoma, nakon optimalne rotacije/translacije:

\[
\mathrm{RMSD}=\sqrt{\frac{1}{N}\sum_{i=1}^{N}\lVert \mathbf x_i-\mathbf y_i\rVert^2}.
\]

Ali RMSD nije definisan dok ne odgovoriš:

- koji atomi ulaze - svi ili heavy atoms;
- kako je pronađeno atom mapping kod simetričnih atoma;
- da li se dozvoljava refleksija;
- kako se tretiraju nedostajući atomi, disorder i više komponenti;
- da li se poredi jedan molekul ili periodični packing cluster;
- da li su koordinate iz iste jedinice i frame-a.

Ista struktura prevedena/rotirana u prostoru treba da ima RMSD blizu nule posle poravnanja. Bez poravnanja, koordinatni frame dominira i mera je besmislena.

## 3.6 Invarijantnost koju ML reprezentacija mora imati

Za molekul ili kristal obično želimo:

- **translacionu invarijantnost** skora;
- **rotacionu invarijantnost** skora ili ekvivarijantne interne reprezentacije;
- **permutacionu invarijantnost** na redosled ekvivalentnih atoma;
- za kristal, **periodičnu invarijantnost** na izbor ekvivalentne ćelije/origina.

Međutim, ne želimo nužno invarijantnost na refleksiju, promenu stereokemije, protonaciju ili zamenu elementa. Invarijantnost je naučna odluka, ne samo arhitektonsko svojstvo mreže.

## 3.7 Posledice za aplikacije

<div class="project-link" markdown="1">
**Globalna pretraga:** 2D graf je brz i robustan prema koordinatnom frame-u; 3D deskriptori daju oblik/konformaciju, ali zahtevaju definisanu protonaciju, atom mapping i tretman conformer ensemble-a.

**Poređenje parova:** vrati odvojeno molecular RMSD, torsion differences i packing match. Nikada ne nazivaj jedan RMSD "crystal similarity" ako je izračunat samo na asymmetric-unit molekulu.
</div>

## 3.8 Mini-laboratorija na N14

1. Iz `N14.mol2` uzmi koordinate N1, O1 i O2.
2. Izračunaj obe N-O dužine.
3. Objasni zašto skoro identične dužine nose više informacije nego dva formalna MOL2 `1` bond tipa.
4. Transliraj sve koordinate vektorom (100, -50, 3). Proveri da se dužine ne menjaju.
5. Promeni samo red atoma u fajlu. Objasni zašto se hemijska sličnost ne sme promeniti.

??? success "Očekivani zaključak"
    Obe dužine su približno 1,2273 Å. Translacija ne menja razlike koordinata, pa ni dužine. Red linija nije hemijsko svojstvo; stabilan sistem mora mapirati atome po identitetu/grafu, ne po poziciji u fajlu.

**Kriterijum prolaza:** iz koordinata ručno ili kodom izračunaj dužinu, ugao i torziju, pa objasni sve izbore potrebne da bi RMSD bio reproduktivan.
