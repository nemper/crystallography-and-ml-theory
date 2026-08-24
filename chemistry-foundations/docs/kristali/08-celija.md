# 8. Kristal, rešetka i jedinična ćelija

## Šta treba da umeš posle ovog poglavlja

Posle ovog poglavlja treba da možeš da:

- razlikuješ kristalnu strukturu, rešetku, motiv i jediničnu ćeliju;
- protumačiš parametre \(a,b,c,\alpha,\beta,\gamma\) i zapreminu ćelije;
- razlikuješ sedam kristalnih od sedam rešetkastih sistema i mapiraš 14 Bravaisovih tipova bez mešanja trigonal/rhombohedral pojmova;
- pretvaraš frakcione koordinate u Cartesian koordinate i obrnuto;
- računaš fizičke udaljenosti pomoću matrice ćelije ili metric tensor-a;
- pronađeš najkraću periodičnu sliku umesto da veruješ koordinatama unutar jednog nacrtanog okvira;
- objasniš zašto isti kristal može imati više legitimnih ćelija;
- razlikuješ primitive, conventional, reduced i supercell opis;
- protumačiš \(Z\) i, uz odgovarajuće uslove, izvedeš \(Z'\);
- izračunaš gustinu iz formule, ćelije i \(Z\);
- definišeš cell-level feature-e koji su invarijantni na setting, basis i origin.

## Intuicija: ćelija je koordinatni izbor, ne fizička kutija

Kristal možeš zamisliti kao beskonačnu periodičnu sliku. Jedinična ćelija je jedan izabrani paralelopiped čijim celobrojnim translacijama opisujemo celu rešetku. Njene ivice nisu fizički zidovi: atom na \(x=0.99\) može biti bliži atomu u sledećoj ćeliji nego atomu na \(x=0.50\) u istoj nacrtanoj ćeliji.

U najkraćem:

| Pojam | Značenje |
|---|---|
| rešetka | beskonačan skup translaciono ekvivalentnih tačaka |
| motiv/basis | atomski ili molekulski sadržaj pridružen rešetki |
| kristalna struktura | rešetka + motiv + simetrija i hemijski identitet |
| jedinična ćelija | izabrani koordinatni paralelopiped koji generiše rešetku |
| asimetrična jedinica | najmanji jedinstveni sadržaj iz kog space-group simetrija daje ćeliju |

!!! danger "Ista ćelija nije isto što i ista struktura"
    Dva različita atomska rasporeda mogu imati jednake ili veoma slične parametre ćelije. Obrnuto, isti fizički kristal može biti zapisan drugom bazom, origin-om, setting-om ili supercell-om i zato imati veoma drugačije brojeve u CIF-u.

## Rešetka kao celobrojna kombinacija tri vektora

Neka su \(\mathbf a,\mathbf b,\mathbf c\) tri nekoplanarna vektora koji čine primitivni bazis. Tada je translaciona rešetka:

\[
\mathbf T_{\mathbf n}
=
n_1\mathbf a+n_2\mathbf b+n_3\mathbf c,
\qquad n_1,n_2,n_3\in\mathbb Z.
\]

Kod centriranog konvencionalnog bazisa \(\mathbf a_c,\mathbf b_c,\mathbf c_c\), njegove celobrojne kombinacije daju samo podrešetku; preostale tačke daju centrirajući vektori. Na primer, I-centrirana ćelija ima i klasu pomerenu za \(\tfrac12(\mathbf a_c+\mathbf b_c+\mathbf c_c)\).

Vektori nisu nužno međusobno ortogonalni. Šest parametara ćelije su:

- \(a=\lVert\mathbf a\rVert\);
- \(b=\lVert\mathbf b\rVert\);
- \(c=\lVert\mathbf c\rVert\);
- \(\alpha=\angle(\mathbf b,\mathbf c)\);
- \(\beta=\angle(\mathbf a,\mathbf c)\);
- \(\gamma=\angle(\mathbf a,\mathbf b)\).

Sedam kristalnih sistema postavljaju ograničenja na ove parametre. Na primer, u monokliničnom standardnom opisu sa jedinstvenom osom \(b\):

\[
\alpha=\gamma=90^\circ,\qquad
\beta\ne90^\circ\ \text{u opštem slučaju}.
\]

Ne treba memorisati 230 prostornih grupa da bi se koristila ćelija. Treba razumeti da ograničenja dolaze iz simetrije i da zaobljavanje ugla bliskog \(90^\circ\) nije dokaz više simetrije.

## Sedam sistema i 14 Bravaisovih tipova bez taksonomske zamke

Ovde se često pomešaju **crystal system** i **lattice system**. Sedam kristalnih sistema su triclinic, monoclinic, orthorhombic, tetragonal, trigonal, hexagonal i cubic. Sedam rešetkastih sistema imaju istu listu osim što se **rhombohedral** pojavljuje umesto **trigonal**. Trigonalni kristal može imati rhombohedral (`hR`) ili hexagonal (`hP`) tip rešetke; zato `trigonal`, `rhombohedral` i `hexagonal setting` nisu sinonimi.

Sledeća tabela zato klasifikuje svih 14 Bravaisovih tipova po **rešetkastom sistemu**. Ograničenja su za uobičajenu konvencionalnu ćeliju i predstavljaju simetrijski zahtev, ne test koji sam dokazuje space group.

| Rešetkasti sistem | Konvencionalna metrička ograničenja | Bravaisovi tipovi |
|---|---|---|
| triclinic | nema simetrijski nametnutih jednakosti; uglovi su opšti | `aP` |
| monoclinic, unique-\(b\) | \(\alpha=\gamma=90^\circ\); \(\beta\) je opšti ugao | `mP`, `mS` |
| orthorhombic | \(\alpha=\beta=\gamma=90^\circ\); dužine su nezavisne | `oP`, `oS`, `oI`, `oF` |
| tetragonal | \(a=b\), \(c\) nezavisno; svi uglovi \(90^\circ\) | `tP`, `tI` |
| rhombohedral, primitive axes | \(a=b=c\); \(\alpha=\beta=\gamma\), opšti jednaki ugao | `hR` |
| hexagonal axes | \(a=b\), \(c\) nezavisno; \(\alpha=\beta=90^\circ,\ \gamma=120^\circ\) | `hP` |
| cubic | \(a=b=c\); \(\alpha=\beta=\gamma=90^\circ\) | `cP`, `cI`, `cF` |

`P` je primitive, `I` body-centred, `F` all-face-centred, a IUCr oznaka `S` znači single-face-centred nezavisno od konkretnog `A`, `B` ili `C` setting-a. U CIF space-group simbolu ćeš češće videti konkretno slovo centriranja, na primer `C 2/c` ili `F m -3 m`.

!!! warning "Metrika može slučajno imati višu simetriju"
    Monoklinična ili orthorhombic ćelija može slučajno imati dve gotovo jednake ivice. To je **metric specialization**, ne automatski dokaz tetragonalne ili cubic simetrije. Crystal system se određuje iz point/space-group simetrije uz tolerancije i validaciju, ne samo poređenjem šest zaokruženih brojeva.

Lokalni `search2` eksport sadrži svih sedam raw cell-setting etiketa. Pri normalizaciji čuvaj raw vrednost, space-group identifikator i transformaciju. Posebno:

```text
raw_cell_setting = "rhombohedral"
→ lattice_system = "rhombohedral"
→ crystal_system = "trigonal"
→ setting/provenance ostaju eksplicitni
```

Sama hexagonal metrika ne razdvaja trigonalni `hP` od hexagonalnog kristalnog sistema; za to je potreban space group/point group. Standardna lista i nomenklatura su u [IUCr tabeli sedam sistema i 14 rešetki](https://www.iucr.org/education/pamphlets/2/full-text) i [IUCr nomenklaturi Bravaisovih tipova](https://www.iucr.org/resources/commissions/crystallographic-nomenclature/bravais).

## Zapremina jedinične ćelije

Opšta zapremina je apsolutna vrednost skalarnog trostrukog proizvoda:

\[
V=
\left|\mathbf a\cdot(\mathbf b\times\mathbf c)\right|.
\]

Iz šest parametara:

\[
V=abc
\sqrt{
1+2\cos\alpha\cos\beta\cos\gamma
-\cos^2\alpha-\cos^2\beta-\cos^2\gamma
}.
\]

Za monokliničnu ćeliju sa \(\alpha=\gamma=90^\circ\):

\[
V=abc\sin\beta.
\]

Lokalni <code>cu_n14_a.cif</code> navodi:

| Parametar | Vrednost |
|---|---:|
| \(a\) | 12,7138(3) Å |
| \(b\) | 15,3951(4) Å |
| \(c\) | 10,6106(3) Å |
| \(\alpha\) | 90° |
| \(\beta\) | 93,235(1)° |
| \(\gamma\) | 90° |
| prijavljeno \(V\) | 2073,51(9) Å³ |

Račun:

\[
12.7138\cdot15.3951\cdot10.6106\cdot
\sin(93.235^\circ)
\approx2073.51\ \text{Å}^3
\]

reprodukuje CIF vrednost. To proverava internu geometrijsku konzistentnost tih polja, ne hemijski identitet strukture.

## Frakcione koordinate

Frakciona koordinata:

\[
\mathbf f=
\begin{bmatrix}
x\\y\\z
\end{bmatrix}
\]

znači:

\[
\mathbf r=x\mathbf a+y\mathbf b+z\mathbf c.
\]

Vrednost \(x=0.25\) nije 0,25 Å. Ona znači četvrtinu vektora \(\mathbf a\), uz doprinose ostalih koordinata. Frakcione koordinate su prirodne za simetriju i periodičnost; Cartesian koordinate su prirodne za fizičke udaljenosti, uglove i poravnanje.

## Matrica ćelije i fractional → Cartesian

Postavi vektore ćelije kao kolone matrice:

\[
\mathbf A=
\begin{bmatrix}
\vert & \vert & \vert\\
\mathbf a&\mathbf b&\mathbf c\\
\vert & \vert & \vert
\end{bmatrix}.
\]

Tada je:

\[
\boxed{\mathbf r=\mathbf A\mathbf f}.
\]

Jedna uobičajena Cartesian konvencija je:

\[
\mathbf A=
\begin{bmatrix}
a & b\cos\gamma & c\cos\beta\\
0 & b\sin\gamma &
c\frac{\cos\alpha-\cos\beta\cos\gamma}{\sin\gamma}\\
0 & 0 & \frac{V}{ab\sin\gamma}
\end{bmatrix}.
\]

Ovo je izbor frame-a. Drugi softver može rotirati celu Cartesian predstavu, a da fizička struktura ostane ista. Zato se Cartesian koordinate iz dva fajla ne porede direktno bez usaglašavanja frame-a.

### Monoklinični N14 slučaj

Pošto su \(\alpha=\gamma=90^\circ\), matrica se pojednostavljuje:

\[
\mathbf A=
\begin{bmatrix}
a & 0 & c\cos\beta\\
0 & b & 0\\
0 & 0 & c\sin\beta
\end{bmatrix}.
\]

Zato:

\[
\begin{aligned}
X &= ax+cz\cos\beta,\\
Y &= by,\\
Z_{\mathrm{cart}} &= cz\sin\beta.
\end{aligned}
\]

C1 u lokalnom CIF-u ima:

\[
(x,y,z)=(0.55515,\ 0.54005,\ 0.15800).
\]

Za \(\cos93.235^\circ\approx-0.0564314\) i
\(\sin93.235^\circ\approx0.9984065\):

\[
\begin{aligned}
X
&=12.7138(0.55515)
+10.6106(0.15800)\cos93.235^\circ\\
&=7.05807-0.09461
\approx6.96346\ \text{Å},\\
Y&=15.3951(0.54005)\approx8.31412\ \text{Å},\\
Z_{\mathrm{cart}}
&=10.6106(0.15800)\sin93.235^\circ\\
&\approx1.67380\ \text{Å}.
\end{aligned}
\]

<code>N14.mol2</code> navodi C1 kao približno:

\[
(6.9635,\ 8.3141,\ 1.6738)\ \text{Å}.
\]

To je jaka reproduktivna potvrda koordinatne transformacije i veze između lokalnog CIF-a i MOL2 izvoza.

## Cartesian → fractional

Ako je matrica ćelije regularna:

\[
\boxed{\mathbf f=\mathbf A^{-1}\mathbf r}.
\]

Za lokalni monoklinični oblik:

\[
\begin{aligned}
z&=\frac{Z_{\mathrm{cart}}}{c\sin\beta},\\
y&=\frac{Y}{b},\\
x&=\frac{X-cz\cos\beta}{a}.
\end{aligned}
\]

Round-trip test treba da proveri:

\[
\mathbf f
\xrightarrow{\mathbf A}
\mathbf r
\xrightarrow{\mathbf A^{-1}}
\mathbf f'
\]

i da je \(\mathbf f'-\mathbf f\) celobrojni vektor do numeričke tolerancije. Za periodične koordinate razlika od tačno 1 u jednoj komponenti nije fizička greška.

## Periodična ekvivalencija i wrap

Frakcione koordinate:

\[
\mathbf f
\quad\text{i}\quad
\mathbf f+\mathbf n,\qquad\mathbf n\in\mathbb Z^3
\]

opisuju isti položaj u različito označenoj ćeliji.

Uobičajeni wrap u interval \([0,1)\) je:

\[
\mathrm{wrap}(\mathbf f)
=
\mathbf f-\lfloor\mathbf f\rfloor
\]

komponentno. Na primer, \((-0.02,1.03,0.40)\) se prikazuje kao \((0.98,0.03,0.40)\).

!!! warning "Ne gubi unwrapped poreklo"
    Wrap je prikazna/kanonizaciona operacija. Ako se svaka koordinata nezavisno wrap-uje, povezan molekul može vizuelno „pući“ preko granice ćelije. Čuvaj originalne koordinate, image-vektore i transformaciju; za molekulske deskriptore prvo napravi hemijski konzistentnu celu komponentu.

## Metric tensor i fizička udaljenost

Metric tensor ćelije je:

\[
\mathbf G=\mathbf A^\mathsf T\mathbf A.
\]

Za frakcionu razliku \(\Delta\mathbf f\):

\[
d^2=
\Delta\mathbf f^\mathsf T
\mathbf G
\Delta\mathbf f.
\]

Za periodični par traži se:

\[
d_{\min}=
\min_{\mathbf n\in\mathbb Z^3}
\sqrt{
(\Delta\mathbf f+\mathbf n)^\mathsf T
\mathbf G
(\Delta\mathbf f+\mathbf n)
}.
\]

U ortogonalnoj ćeliji često je dovoljno svaku komponentu svesti u približno \([-0.5,0.5)\). U veoma kosoj ćeliji komponentno zaokruživanje ne mora dati najkraći Cartesian vektor. Pouzdan sistem koristi redukovanu ćeliju, neighbor-list algoritam ili eksplicitnu pretragu matematički dovoljnog skupa slika.

### Koliko susednih ćelija treba pretražiti?

Fiksno pravilo „uvek \(-1,0,1\) u svakoj osi“ nije univerzalno:

- može biti dovoljno za mali cutoff i dobro uslovljenu ćeliju;
- može propustiti sliku za veći cutoff, veoma kratke/duge ili kose vektore;
- može nepotrebno duplirati mnogo kandidata.

Opseg treba izvesti iz cut-off radijusa i geometrije ćelije ili prepustiti validiranoj biblioteci. Rezultat treba testirati na transformisanim i supercell ekvivalentima istog kristala.

## Jedinična ćelija nije jedinstvena

Ako su kolone \(\mathbf A\) stara baza, a \(\mathbf P\) matrica promene baze:

\[
\mathbf A'=\mathbf A\mathbf P.
\]

Za isti fizički položaj i isti origin:

\[
\mathbf f'=\mathbf P^{-1}\mathbf f.
\]

Metric tensor se menja kao:

\[
\mathbf G'=\mathbf P^\mathsf T\mathbf G\mathbf P.
\]

Ako je \(\mathbf P\) celobrojna unimodularna matrica, \(|\det\mathbf P|=1\), dobija se druga baza iste rešetke i iste zapremine. Ona je primitivna **ako je i početna baza primitivna**; unimodularna transformacija čuva primitivnost, ali ne pretvara centriranu konvencionalnu ćeliju u primitivnu.

Ako je \(|\det\mathbf P|=m>1\), nova baza razapinje podrešetku indeksa \(m\) i njena ćelija ima \(m\) puta veću zapreminu. Da bi takav supercell predstavljao isti beskonačni kristal, atomski motiv se ne „uvećava“ proizvoljno: generiše se \(m\) translacionih kopija, po jedan coset representative početne rešetke u odnosu na podrešetku, zatim se uklanjaju periodični duplikati.

Ako se origin pomeri za \(\mathbf o\), nove frakcione koordinate su:

\[
\mathbf f'=\mathbf P^{-1}(\mathbf f-\mathbf o).
\]

Udaljenosti, uglovi, periodični kontaktni obrazac i fizički kristal se time ne menjaju. Sirove koordinate, ćelijski parametri i zapisi symmetry operations mogu se promeniti.

### Primitive, conventional, reduced i standardized

| Opis | Svrha | Oprez |
|---|---|---|
| primitive cell | sadrži jednu rešetkastu tačku | ne mora biti najintuitivnija |
| conventional cell | prikazuje simetriju prema konvenciji | može biti veća od primitivne |
| reduced cell | metrički kanonizovaniji opis rešetke | slična reduced cell ne dokazuje isti atomski packing |
| standardized cell | softverski izabrana konvencija | zavisi od standarda, tolerancije i verzije |
| supercell | celobrojno proširenje ćelije | isti kristal dobija više atoma i veću zapreminu |

Reduced-cell search je dobar kandidat-generator za slične rešetke. Nije dovoljan crystal-structure comparator, jer ne proverava hemijski identitet i potpuno atomsko pakovanje.

## Z, Z′ i sadržaj ćelije

\(Z\) je broj formula units u jediničnoj ćeliji. To nije:

- broj atoma;
- atomski broj elementa;
- broj molekula u CIF atomskom loop-u;
- broj redova posle symmetry expansion-a.

\(Z'\), čita se „Z prime“, u jednostavnom molekulskom slučaju označava broj kristalografski nezavisnih formula units u asimetričnoj jedinici.

Ako je multiplicity opšte pozicije \(m\), a sve jedinice su na opštim pozicijama:

\[
Z=mZ'.
\]

Ovo nije univerzalna formula bez provere. Specijalne pozicije, višekomponentne forme, polimerne mreže, disorder i parcijalne occupancy vrednosti zahtevaju račun preko site multiplicity-ja i stehiometrije.

Za N14:

- space group \(P\,2_1/c\) ima četiri opšte pozicije u navedenoj conventional ćeliji;
- ASU sadrži jednu kompletnu formulu \(\mathrm{C_{25}H_{20}N_3O_2P}\);
- sva navedena mesta imaju site-symmetry order 1 i occupancy 1;
- CIF navodi \(Z=4\).

Zato je u ovom urednom slučaju:

\[
Z'=1.
\]

Četiri symmetry-related kopije daju \(4\times51=204\) atomske pozicije po ćeliji kada se računaju i svi navedeni H atomi.

## Gustina kao provera konzistentnosti

Za molarnu masu \(M\), zapreminu \(V\) i \(Z\):

\[
\rho=
\frac{ZM}{N_\mathrm A V}.
\]

Kada je \(V\) u Å³, koristi se:

\[
1\ \text{Å}^3=10^{-24}\ \text{cm}^3.
\]

Za N14:

\[
\rho=
\frac{
4\cdot425.41\ \mathrm{g\,mol^{-1}}
}{
(6.02214076\times10^{23}\ \mathrm{mol^{-1}})
(2073.51\times10^{-24}\ \mathrm{cm^3})
}
\approx1.363\ \mathrm{g\,cm^{-3}}.
\]

To odgovara <code>_exptl_crystal_density_diffrn 1.363</code>. Saglasnost proverava formulu, \(Z\), zapreminu i račun kao paket. Ne dokazuje da je svaki atom ili bond type ispravan.

## Pojmovni slojevi opisa ćelije

Šest normalizovanih brojeva nije dovoljno da se razume poređenje. Naučni opis razlikuje:

- originalne \(a,b,c,\alpha,\beta,\gamma,V\) vrednosti i s.u.;
- originalni Cartesian cell matrix \(\mathbf A\);
- originalni space-group/Hall zapis i symmetry operations;
- standardized/reduced matrix kao izvedeni sloj;
- \(\mathbf P\) i origin shift \(\mathbf o\);
- det(\(\mathbf P\)) i odnos primitive/conventional/supercell;
- originalne i transformisane frakcione koordinate;
- tolerancije i verzije biblioteka;
- round-trip i atom-mapping validaciju;
- \(Z\), izvedeni \(Z'\) samo kada je metod opravdan, i confidence.

Ovo su kategorije potrebne za tumačenje ekvivalentnosti i gubitka informacije, ne propisana record schema ili budući tok skladištenja.

## Posledice za dve aplikacije

### Globalna pretraga

- Originalna ćelija je provenance; reduced/standardized ćelija je indeksni prikaz.
- Cell similarity može brzo pronaći slične rešetke, ali mora biti odvojen od molecular i packing similarity.
- Feature mora biti robustan na permutaciju ekvivalentnih osa, setting i konvencionalnu/primitivnu predstavu.
- Temperatura i pritisak su potrebni jer ćelija fizički varira sa uslovima.
- Korisniku treba objasniti da je pogodak „sličan po metric tensor-u“, ne automatski „isti kristal“.

### Poređenje svih parova

- Pre cell distance-a pokušaj standardizaciju i eksplicitne basis/origin transformacije.
- Poredi zapreminu po uporedivoj formula unit ili primitivnoj ćeliji kada se veličine ćelija razlikuju.
- Supercell par ne sme biti ocenjen kao potpuno različit samo zbog više atoma i veće zapremine.
- Posle lattice match-a obavezno proveri hemijski identitet i periodično atomsko mapiranje.
- Vrati transformaciju koja reprodukuje podudaranje, residual metric error i atom-level coverage.

## Tipične zamke

1. Tumačiti frakcionu koordinatu kao udaljenost u Å.
2. Računati udaljenost običnom normom frakcionih razlika.
3. Ignorisati \(\beta\ne90^\circ\) u N14.
4. Porediti Cartesian koordinate iz dva programa bez poravnanja frame-a.
5. Wrap-ovati svaki atom i tako rascepiti molekul preko granice.
6. Koristiti samo atome unutar \([0,1)^3\) pri neighbor search-u.
7. Verovati da slična ćelija dokazuje isti packing.
8. Verovati da različita ćelija dokazuje različit kristal pre provere setting-a ili supercell-a.
9. Prepisati originalnu ćeliju standardizovanom i izgubiti provenance.
10. Pretpostaviti \(Z'=Z/|\text{symmetry operations}|\) bez provere specijalnih pozicija i stehiometrije.
11. Mešati \(Z\) sa brojem atomskih redova u CIF-u.
12. Zaokružiti ćeliju/koordinate pre računanja i napraviti lažne razlike.

## Mini-vežbe

### 1. Zapremina N14

Zašto se u formuli zapremine pojavljuje \(\sin\beta\), a ne samo proizvod \(abc\)?

??? success "Odgovor"
    Zato što \(\mathbf a\) i \(\mathbf c\) nisu ortogonalni. Proizvod \(abc\) važi za pravougaoni paralelopiped; faktor \(\sin\beta\) uzima komponentu jednog vektora normalnu na drugi.

### 2. C1 fractional → Cartesian

Izračunaj C1 koristeći lokalnu monokliničnu matricu.

??? success "Odgovor"
    Dobija se približno \((6.96346,8.31412,1.67380)\ \text{Å}\), što se slaže sa <code>N14.mol2</code> posle zaokruživanja na četiri decimale.

### 3. Periodična ekvivalencija

Da li \((0.98,0.03,0.40)\) i \((-0.02,1.03,0.40)\) predstavljaju različite frakcione položaje?

??? success "Odgovor"
    Ne. Razlikuju se za celobrojni vektor \((-1,1,0)\), pa su periodično ekvivalentni.

### 4. Supercell

Od ćelije napraviš \(2\times1\times1\) supercell. Šta se događa sa zapreminom, brojem formula units i gustinom?

??? success "Odgovor"
    Zapremina i \(Z\) se udvostručuju, dok gustina ostaje ista. Ako comparator koristi sirovu zapreminu ili atom count bez normalizacije, isti kristal može izgledati različito.

### 5. Z′ za N14

Zašto je opravdano \(Z'=1\), a nije samo slepo deljenje?

??? success "Odgovor"
    ASU sadrži jednu kompletnu formula unit, sva atomska mesta su na opštim pozicijama sa occupancy 1, multiplicity opšte pozicije je četiri i CIF navodi \(Z=4\). Svi delovi dokaza su međusobno saglasni.

### 6. Reduced-cell pogodak

Dve strukture imaju gotovo iste reduced-cell parametre. Šta još moraš proveriti pre tvrdnje da su iste?

??? success "Odgovor"
    Hemijski sastav i komponente, symmetry/setting transformaciju, periodično atomsko mapiranje, konformaciju i packing, kao i temperaturu, pritisak i kvalitet određivanja.

### 7. Raw `rhombohedral` etiketa

Eksport ima `_cell_setting = rhombohedral`. Koja tri odvojena polja treba sačuvati?

??? success "Odgovor"
    Sačuvaj originalnu raw etiketu, normalizuj `lattice_system = rhombohedral` i `crystal_system = trigonal`, pa odvojeno sačuvaj space group, setting i svaku primenjenu transformaciju. Sama metrika nije dovoljna za potpunu klasifikaciju simetrije.

## Kriterijum prolaza

Poglavlje si savladao kada možeš da iz <code>cu_n14_a.cif</code> konstruišeš cell matrix, reprodukuješ zapreminu, C1 Cartesian koordinatu i gustinu, mapiraš svih 14 Bravaisovih tipova na rešetkaste sisteme bez učenja napamet i objasniš kako bi comparator prepoznao isti kristal zapisan drugim origin-om, bazom ili supercell-om.

## Primarni i autoritativni izvori

- [IUPAC Gold Book: unit cell](https://goldbook.iupac.org/terms/view/U06562)
- [IUCr Online Dictionary: unit cell](https://dictionary.iucr.org/Unit_cell)
- [IUCr Online Dictionary: primitive cell](https://dictionary.iucr.org/Primitive_cell)
- [IUCr Online Dictionary: centred lattice](https://dictionary.iucr.org/Centred_lattice)
- [IUCr teaching pamphlet 9: matrices, translations and transformations](https://www.iucr.org/education/pamphlets/9)
- [IUCr teaching pamphlet 10: metric tensor](https://www.iucr.org/education/pamphlets/10)
- [IUCr teaching pamphlet 21: crystal packing](https://www.iucr.org/education/pamphlets/21)
- [CCDC Python API: reduced-cell searching](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/reduced_cell_searching.html)
- [spglib: symmetry dataset and standardized cells](https://spglib.readthedocs.io/en/stable/dataset.html)
- [MIT OpenCourseWare 3.091: Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091-introduction-to-solid-state-chemistry-fall-2018/)
