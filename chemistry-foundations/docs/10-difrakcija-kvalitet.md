# 10. Difrakcija, refiniranje i kvalitet

## Šta treba da umeš posle ovog poglavlja

Posle ovog poglavlja treba da možeš da:

- objasniš kako od difrakcionih intenziteta nastaje atomski model;
- povežeš Millerove indekse, reciprocal lattice, \(d(hkl)\) i položaj pika \(2\theta\);
- razlikuješ simulirani powder pattern izveden iz CIF modela od izmerenog PXRD bulk uzorka;
- razlikuješ merenje, izračunati model i deskriptore slaganja između njih;
- protumačiš R, wR, goodness of fit, occupancy, disorder i standardnu neizvesnost;
- pročitaš ključna polja iz <code>cu_n14_a.cif</code> bez proglašavanja jednog broja za presudu o kvalitetu;
- koristiš checkCIF kao dijagnostički sistem, a ne kao automatski sertifikat;
- prevedeš kvalitet i neizvesnost u zahteve za obe 2CDC aplikacije.

## Intuicija: CIF nije fotografija kristala

Kristal rasipa rendgensko zračenje. Detektor ne vidi atome direktno; meri položaje i intenzitete difrakcionih refleksija. Iz tih merenja, uz pretpostavljenu simetriju i hemijsko znanje, kristalograf gradi model atomskih položaja i zatim ga iterativno podešava.

Zato postoje tri različita objekta:

| Sloj | Primer | Šta može biti pogrešno |
|---|---|---|
| eksperiment | refleksija sa indeksima \(h,k,l\), intenzitetom \(I\) i neizvesnošću \(\sigma(I)\) | slab kristal, apsorpcija, preklapanje, zračenjem oštećen uzorak |
| model | atomi, koordinate, occupancy, displacement parametri, simetrija | pogrešan element, propušten solvent, pogrešna space group, loše modelovan disorder |
| izvedena geometrija | dužina veze, ugao, torzija, kontakt | zavisi od modela i njegove kovarijanse |

!!! danger "Najvažnija rečenica"
    Eksperimentalna kristalna struktura je najbolje podržan model za data merenja pod navedenim uslovima. Nije savršeno poznata i nije isto što i izolovani molekul bez kristalnog okruženja.

## Od Braggovog pika do modela

Za familiju ravni sa razmakom \(d\), konstruktivna interferencija nastaje kada važi Braggov zakon:

\[
n\lambda = 2d\sin\theta
\]

Položaji pikova prvenstveno nose informaciju o jediničnoj ćeliji i simetriji. Intenzitet refleksije je, u idealizovanom obliku, proporcionalan kvadratu modula strukturnog faktora:

\[
I(hkl) \propto |F(hkl)|^2
\]

\[
F(hkl)=\sum_j f_j
\exp\left[2\pi i(hx_j+ky_j+lz_j)\right]
\]

Ovde je \(f_j\) faktor rasipanja atoma \(j\), a \(x_j,y_j,z_j\) njegove frakcione koordinate. Detektor meri intenzitet, ali ne i fazu kompleksnog \(F\); to je suština faznog problema. Rešenje strukture daje početni model, a refiniranje podešava njegove parametre da bi izračunati podaci bolje odgovarali merenim.

U ovoj pojednostavljenoj sumi \(j\) obuhvata sve atome jedinične ćelije, uključujući simetrijske kopije, uz puno zauzeće i zanemareno atomsko pomeranje. U stvarnom računu svaki doprinos nosi occupancy i displacement faktor, a atomski faktor rasipanja zavisi od ugla/rezolucije i zračenja. Suma samo preko redova ASU bez simetrijskog proširenja nije isti račun.

U <code>cu_n14_a.cif</code> piše:

- Cu K\(\alpha\) zračenje, \(\lambda=1.54178\ \text{Å}\);
- merenje na \(100\ \text{K}\);
- monoklinična ćelija, \(P\,2_1/c\);
- refiniranje na \(F^2\), označeno poljem <code>_refine_ls_structure_factor_coef Fsqd</code>;
- 87.254 izmerene refleksije, svedene na 4.237 jedinstvenih refleksija za refiniranje;
- 3.891 refleksija zadovoljava \(I>2\sigma(I)\);
- izmerena frakcija do navedenog ugla je 1.000;
- 284 parametra i nijedan geometrijski restraint.

Odnos 4.237 refleksija prema 284 parametra je približno 14,9. To je korisna informacija o količini podataka u odnosu na složenost modela, ali ni taj odnos sam ne dokazuje da je model hemijski ispravan.

Za širi uvod vidi [IUCr definiciju refiniranja](https://dictionary.iucr.org/Refinement), a za formalna značenja CIF polja [IUCr Core CIF dictionary](https://www.iucr.org/resources/cif/dictionaries).

### Constraint i restraint nisu isto

**Constraint** nameće tačnu vezu između parametara ili fiksira vrednost, pa smanjuje broj nezavisnih parametara. U riding modelu položaj H prati geometriju roditeljskog atoma. **Restraint** uvodi ciljnu geometriju sa težinom/neizvesnošću: odstupanje je dozvoljeno, ali doprinosi funkciji koja se minimizuje. Zato lokalnih `0 restraints` ne znači da su svi položaji nezavisno određeni — N14 istovremeno ima riding H atome i slobodnije refiniran H2N. Ovo razlikovanje objašnjava i broj parametara i neizvesnost geometrije. [IUCr rečnik restraints/constraints](https://www.iucr.org/resources/cif/dictionaries/browse/cif_core_restraints) daje formalnu razliku.

## Reciprocal space: operativni most \(hkl\rightarrow d\rightarrow2\theta\)

Millerovi indeksi \((hkl)\) su celi brojevi koji opisuju orijentaciju i period ravni u odnosu na ćeliju. U frakcionim koordinatama ravni zadovoljavaju \(hx+ky+lz=m\), gde je \(m\) ceo broj. Ako je neki indeks nula, ravni su paralelne toj osi; \((000)\) ne definiše familiju sa konačnim razmakom. Na primer, \((200)\) daje ravni \(x=m/2\), pa u kubnoj ćeliji imaju razmak \(a/2\). U difrakciji indekse ne svodiš automatski na najmanji odnos: `(100)` i `(200)` su različite refleksije duž istog recipročnog pravca. [IUCr: Millerovi indeksi](https://dictionary.iucr.org/Miller_indices).

Real-space ćeliju opisuju \(\mathbf a,\mathbf b,\mathbf c\). Za desnoruku bazu, sa \(V=\mathbf a\cdot(\mathbf b\times\mathbf c)>0\), i konvenciju bez faktora \(2\pi\), recipročna baza je:

\[
\mathbf a^*=\frac{\mathbf b\times\mathbf c}{V},\qquad
\mathbf b^*=\frac{\mathbf c\times\mathbf a}{V},\qquad
\mathbf c^*=\frac{\mathbf a\times\mathbf b}{V}.
\]

Refleksiju označenu celobrojnim Millerovim indeksima \((hkl)\) predstavlja reciprocal-lattice vektor:

\[
\mathbf g_{hkl}=h\mathbf a^*+k\mathbf b^*+l\mathbf c^*,
\qquad
d(hkl)=\frac{1}{\lVert\mathbf g_{hkl}\rVert}.
\]

Za cubic ćeliju ivice \(a\):

\[
d(hkl)=\frac{a}{\sqrt{h^2+k^2+l^2}}.
\]

Sintetički CIF iz lekcije 12A ima cubic NaCl teaching ćeliju \(a=5.6400\ \text{Å}\). Za refleksiju \((200)\):

\[
d(200)=\frac{5.6400}{2}=2.8200\ \text{Å}.
\]

Ako se simulira Cu K\(\alpha\) obrazac sa \(\lambda=1.5406\ \text{Å}\) i uzme prvi red \(n=1\):

\[
2\theta
=2\arcsin\left(\frac{\lambda}{2d}\right)
\approx31.7^\circ.
\]

To je deterministički položaj idealizovanog pika za zadatu ćeliju i talasnu dužinu. Promena ćelije pomera \(d\) i \(2\theta\); promena atomskih položaja/vrsta pre svega menja structure factor i intenzitet.

U single-crystal radu „rezolucija“ se često prijavljuje najmanjim dosegnutim razmakom:

\[
d_{\min}=\frac{\lambda}{2\sin\theta_{\max}}.
\]

Veći \(\theta_{\max}\) daje manji \(d_{\min}\), odnosno višu prostornu rezoluciju. Nemoj pomešati „viša rezolucija“ sa numerički većim \(d_{\min}\): smer je obrnut.

## Sistematska odsustva: nedostajući pik može biti zahtev simetrije

Translacioni deo space group-a može učiniti da se doprinosi refleksiji tačno ponište. To daje **systematic absence** ili extinction. Primer je `F` centriranje sintetičke `F m -3 m` ćelije. Doprinos četiri rešetkaste tačke sadrži faktor:

\[
1+e^{\pi i(k+l)}+e^{\pi i(h+l)}+e^{\pi i(h+k)}.
\]

On je nenula samo kada su \(h,k,l\) svi parni ili svi neparni. Zato su `100` i `110` zabranjeni samim `F` centriranjem, dok su `111` i `200` dozvoljeni. Njihovi stvarni intenziteti i dalje zavise od Na/Cl basis-a, atomskih scattering faktora, occupancy-ja, displacement parametara i eksperimentalnih efekata.

!!! warning "Odsustvo nije isto što i slab pik"
    Systematic absence je tačno selection rule svojstvo idealne simetrije. Dozvoljena refleksija može biti veoma slaba ili se slučajno poništiti zbog konkretnog motiva. Izmereni pik može izostati zbog limita detekcije, preferred orientation-a ili preklapanja. Zato se space group ne određuje jednim „ima/nema“ pravilom.

## Measured, unique, merged i refined nisu isti brojevi

| Broj | Šta broji |
|---|---|
| measured reflections | sva zabeležena opažanja, uključujući ponavljanja i symmetry-equivalent merenja |
| unique reflections | ekvivalentna opažanja svedena na jedinstvene \(hkl\) indekse pod usvojenom simetrijom |
| merged data | agregirane intenzitete i neizvesnosti posle skaliranja/kombinovanja ekvivalenata |
| reflections used in refinement | konkretan skup koji ulazi u least-squares model; kriterijum mora biti naveden |

Lokalnih 87.254 measured i 4.237 unique/refinement refleksija zato nisu konflikt. Redundancy, simetrija i merging objašnjavaju razliku; \(R_\mathrm{int}\) opisuje slaganje ekvivalentnih opažanja pre finalnog modela.

## Simulirani naspram izmerenog PXRD-a

| Pitanje | Simulirani pattern iz CIF-a | Izmereni PXRD |
|---|---|---|
| ulaz | ćelija, space group, atomski model, wavelength i simulation settings | bulk uzorak, instrument i eksperimentalni protokol |
| šta daje | očekivane položaje i relativne intenzitete idealizovanog modela | stvarne counts/intensity kroz \(2\theta\), \(q\) ili \(d\) osu |
| šta utiče | radiation, range, profile broadening, occupancy/ADP tretman, software/version | kalibracija, pozadina, K\(\alpha_1/\alpha_2\), veličina/strain, texture, mešavine, amorfni sadržaj, priprema i temperatura |
| epistemološka uloga | koristan fingerprint i predikcija onoga što bi model trebalo da daje | bulk-phase evidence i mogući dokaz mešavine/fazne promene |
| granica | izveden je iz istog CIF-a, pa nije nezavisna potvrda tog modela | dobro slaganje podržava fazni identitet, ali samo ne potvrđuje svaki atom ili refinement detalj SCXRD modela |

Ako se pattern-i porede, interpretacija zahteva poznate kategorije eksperimentalnog/simulacionog konteksta:

- `pattern_type = simulated | measured` i izvorni fajl/hash;
- probe/radiation; wavelength(s) gde je primenljivo; tip i kalibraciju ose (\(2\theta\), \(q\) ili \(d\));
- opseg, korak/binning, intensity scale i background/preprocessing;
- instrument/profile parametrizaciju, temperaturu, pritisak i sample preparation;
- preferred-orientation, mixture/phase i amorphous-status anotacije kada su poznate;
- software/verziju i sve simulation settings;
- comparison metric, peak-matching toleranciju i razlog svake isključene regije.

To nije propisana manifest schema, već spisak promenljivih koje mogu promeniti značenje poređenja.

!!! danger "Ne pravi kružni dokaz"
    „Simulirao sam PXRD iz CIF-a i simulacija se slaže sa istim CIF-om“ proverava implementaciju, ne fazni identitet uzorka. Nezavisan evidence nastaje tek poređenjem sa stvarno izmerenim bulk podatkom, uz unapred definisan protokol i granice zaključka.

## R faktor: koliko se amplitude ne slažu

Konvencionalni R faktor se najčešće piše:

\[
R =
\frac{\sum_{hkl}\left||F_o|-|F_c|\right|}
     {\sum_{hkl}|F_o|}
\]

Za isti skup podataka i refleksija, manja suma apsolutnih razlika između \(|F_o|\) i \(|F_c|\) daje manji R. Ipak, R zavisi od kvaliteta i rezolucije podataka, hemijskog sastava, twinning-a, disorder-a, apsorpcije, skupa uključenih refleksija i samog modela.

Lokalni CIF daje dve vrednosti:

| CIF polje | Vrednost | Skup |
|---|---:|---|
| <code>_refine_ls_R_factor_all</code> | 0,0347 | sve refleksije uključene u refiniranje |
| <code>_refine_ls_R_factor_gt</code> | 0,0322 | refleksije iznad kriterijuma \(I>2\sigma(I)\) |

Očekivano je da je R za jači podskup nešto manji. Poređenje modela A preko <code>R_gt</code> sa modelom B preko <code>R_all</code> nije čisto poređenje.

!!! warning "Ne pravi univerzalni prag"
    Pravilo tipa „R < 0,05 je dobar CIF, ostalo odbaci“ je naučno neodbranjivo. Metalni kompleks sa disorder-om, struktura merena pri visokoj temperaturi i jednostavna uredna organska struktura nemaju isti očekivani profil. R može biti nizak i za pogrešan, previše fleksibilan ili nepotpun model.

## wR: težinski ostatak, često na F²

Za refiniranje na \(F^2\), težinski faktor se može zapisati kao:

\[
wR(F^2)=
\left[
\frac{\sum w\left(F_o^2-F_c^2\right)^2}
     {\sum w\left(F_o^2\right)^2}
\right]^{1/2}
\]

Težine \(w\) određuju koliko pojedina refleksija utiče na optimizaciju. U lokalnom CIF-u:

- <code>_refine_ls_wR_factor_ref = 0.0838</code>;
- <code>_refine_ls_wR_factor_gt = 0.0820</code>;
- fajl beleži i konkretnu SHELXL formulu za težine.

wR je često numerički veći od konvencionalnog R jer nije ista formula ni ista skala. Ne upoređuj ih kao da su dve procene iste veličine. Formalne definicije su u [IUCr CIF rečniku](https://www.iucr.org/__data/iucr/cif/dictionaries/cif_core_2.4.2.dic.pdf).

## Goodness of fit: da li su ostaci saglasni sa težinama

Za least-squares refiniranje bez restraints, kao u lokalnom N14 primeru:

\[
S =
\left[
\frac{\sum w(Y_o-Y_c)^2}
     {N_{\text{ref}}-N_{\text{param}}}
\right]^{1/2}
\]

Ovde je \(Y=F^2\) za ovaj CIF. Vrednost bliska 1 često je poželjna samo ako su procenjene neizvesnosti i težine realistične.

<code>cu_n14_a.cif</code> ima:

\[
S = 1.095
\]

To je kompatibilno sa razumno podešenim težinama, ali nije dokaz da su hemijski identitet, space group, svi solventi i svaki disorder ispravno modelovani. GoF značajno iznad ili ispod 1 može ukazivati na loše težine, potcenjene ili precenjene neizvesnosti, model defect ili druge probleme; tumačenje mora biti kontekstualno.

## Standardna neizvesnost: brojevi u zagradama nisu dekoracija

IUCr danas koristi izraz standard uncertainty, skraćeno s.u. Starija literatura često kaže e.s.d. Kada CIF navede:

- \(a=12.7138(3)\ \text{Å}\) znači procenu 12.7138 Å sa \(u(a)=0.0003\ \text{Å}\);
- \(\beta=93.235(1)^\circ\) znači \(u(\beta)=0.001^\circ\);
- \(V=2073.51(9)\ \text{Å}^3\) znači \(u(V)=0.09\ \text{Å}^3\);
- \(d(\mathrm{N2-N3})=1.3608(14)\ \text{Å}\) znači \(u(d)=0.0014\ \text{Å}\).

Zagrade se odnose na poslednje prikazane cifre. Zapis \(x\pm u(x)\) je
skraćen način da se navedu procena i njena standardna neizvesnost; nije tvrd
interval u kome „prava vrednost mora ležati“, niti je automatski confidence
interval sa zadatim nivoom pokrivenosti. Takvo verovatnosno tumačenje zahteva
dodatne pretpostavke o modelu i raspodeli, a interval pokrivenosti mora navesti
odgovarajući faktor/nivo. Standardna neizvesnost takođe nije garancija ukupne
tačnosti: sistematska greška, pogrešan model ili pogrešan element mogu ostati
van nje. Lokalni CIF navodi da su s.u. geometrije uglavnom izračunate iz pune
kovarijansne matrice i da su s.u. ćelije uključene u račun.

Za poređenje dve dužine, gruba neizvesnost razlike nezavisnih veličina je:

\[
u_{\Delta}=\sqrt{u_1^2+u_2^2}
\]

Ako je razlika manja od nekoliko \(u_{\Delta}\), aplikacija ne bi smela samouvereno da je proglasi hemijski značajnom. Korelisani parametri zahtevaju punu kovarijansu, pa je ova formula samo minimum, ne univerzalno rešenje.

Autoritativna polazna tačka je IUCr pregled [Statistical descriptors in crystallography](https://dictionary.iucr.org/Statistical_descriptors).

## Occupancy: koliko je kristalografsko mesto zauzeto

Occupancy opisuje udeo jediničnih ćelija u prosečnom kristalu u kojima dato mesto zauzima navedeni atom ili modelovana alternativa. Nije:

- verovatnoća da je softver „pogodio atom“;
- confidence score;
- količina elementa u molovima;
- automatski znak lošeg kvaliteta kada je manja od 1.

Occupancy ispod 1 može predstavljati vakanciju, dve alternativne pozicije, mešanu populaciju elemenata ili disorder. Alternative koje opisuju isto fizičko mesto obično moraju imati hemijski i simetrijski smislen zbir. Posebna kristalografska pozicija dodatno zahteva pažljivo razlikovanje occupancy od site multiplicity; [IUCr checkCIF primer PLAT076](https://journals.iucr.org/services/cif/checking/PLAT076.html) pokazuje tipičnu zabunu.

U atomskom loop-u <code>cu_n14_a.cif</code> sva navedena mesta imaju occupancy 1, a polja za disorder assembly/group su prazna. To znači da autor nije eksplicitno modelovao parcijalno zauzeće ili alternativne disorder grupe. Ne znači da je opštim pregledom dokazano da nikakav nered ili sistematski problem ne postoji.

## Disorder i displacement parametri

Kristalografski model je prostorni i vremenski prosek ogromnog broja ćelija. Ako atom ili grupa zauzimaju više položaja, moguć je:

- statički disorder: različite ćelije biraju različite konfiguracije;
- dinamički disorder: atom se tokom merenja kreće između položaja;
- occupational disorder: različite vrste ili vakancije dele mesto;
- positional disorder: ista vrsta ima više položaja.

Model može koristiti alternativne atomske pozicije, parcijalne occupancy vrednosti i grupe koje se međusobno isključuju. Atomic displacement parameters, Uiso ili Uani, opisuju prostornu raspodelu rasipanja oko srednjeg položaja. Velika ili izrazito anizotropna vrednost može biti stvarno kretanje, disorder, loš tip atoma ili drugi model problem; nije samostalna dijagnoza.

U lokalnom fajlu većina nevodonikovih atoma ima anizotropne U parametre. Većina H atoma je geometrijski postavljena riding modelom, dok je H2N naveden sa eksperimentalno refiniranim položajem. Zato ni svi atomi unutar istog CIF-a nemaju istu epistemološku težinu.

## Apsolutna struktura i granica stereokemijskog zaključka {#apsolutna-struktura-i-granica-stereokemijskog-zakljucka}

3D koordinate omogućavaju da se nekoj nacrtanoj molekulskoj konfiguraciji dodeli stereooznaka, ali same ne dokazuju da je odabrana pravilna enantiomerna slika eksperimentalnog uzorka. Za necentrosimetričan kristal **apsolutna struktura** razlikuje model od njegove inverzne slike. Rendgenski dokaz može koristiti razlike intenziteta Friedelovih parova \((h,k,l)\) i \((-h,-k,-l)\) usled anomalnog rasipanja, uz odgovarajuću analizu, na primer Flack parametar sa njegovom s.u. Kada je signal nedovoljan, zaključak ostaje neodređen ili se oslanja na nezavisan hemijski dokaz.

Apsolutna konfiguracija odnosi se na molekul, a apsolutna struktura na kristal. Lokalni N14 ima centrosimetričnu grupu \(P\,2_1/c\), za koju takav izbor apsolutne strukture nije primenljiv; to nije manjkavost CIF-a. Skor poravnanja ne sme prikriti nedostajuću ili neprimenljivu stereoinformaciju. [IUCr: absolute structure](https://dictionary.iucr.org/Absolute_structure).

## Još četiri broja koja treba čuvati

### Rint

<code>_diffrn_reflns_av_R_equivalents = 0.0470</code> meri međusobnu saglasnost simetrijski ekvivalentnih merenja pre finalnog strukturnog modela. Nizak Rint je dobar znak konzistentnosti redukcije, ali ne potvrđuje hemijsku ispravnost modela.

### Completeness

Merena frakcija 1.000 znači da su, za navedeni opseg i definiciju, prikupljene sve očekivane refleksije. Potpun skup može i dalje biti slab ili sistematski pogrešan.

### Residualna elektronska gustina

Lokalni CIF navodi:

- maksimum \(+0.327\ e\,\text{Å}^{-3}\);
- minimum \(-0.349\ e\,\text{Å}^{-3}\);
- RMS \(0.043\ e\,\text{Å}^{-3}\).

Veliki rezidualni pik pored teškog atoma, neobjašnjen solvent ili pogrešna absorpciona korekcija imaju različita značenja. Prostorni položaj reziduala je važniji od samog maksimuma.

### Shift/s.u.

Maksimalni i srednji shift/s.u. su u ovom fajlu 0.000. To pokazuje numeričku konvergenciju poslednjih ciklusa, ali algoritam može konvergirati i ka pogrešnom lokalnom modelu.

## checkCIF: linter i naučni dijagnostičar, ne semafor istine

[IUCr checkCIF](https://checkcif.iucr.org/) proverava CIF sintaksu, ćeliju i geometriju, simetriju, displacement parametre, structure factors i neke obrasce mogućih duplikata. Alert znači „pregledaj i, ako treba, objasni“.

Logika stručne provere je:

1. pokreni validaciju odgovarajućeg nivoa;
2. sačuvaj kompletan izveštaj i verziju alata;
3. za svaki alert utvrdi da li je greška, opravdani izuzetak ili nedostajući podatak;
4. zabeleži odluku i dokaz;
5. ne skrivaj alert samo da bi status postao zelen.

[IUCr FAQ](https://journals.iucr.org/services/cif/checking/checkfaq.html) naglašava da se anomalije rangiraju po ozbiljnosti i da opravdani izuzeci mogu dobiti Validation Response Form. Čak i objavljeni pragovi pojedinačnih testova služe kao screening pravila tog testa, ne kao univerzalni zakon za sve strukture.

!!! warning "Poverljivi fajlovi"
    Online checkCIF podrazumeva slanje fajla eksternom servisu. Za proprietary CIF prvo proveri licencu, ugovor i politiku poverljivosti. Ako slanje nije odobreno, koristi lokalno odobrenu validaciju ili testiraj samo javni/sintetički primer.

## Profil kvaliteta, ne jedna etiketa

Kvalitet se može razmatrati kao vektor više pokazatelja:

\[
q = [
R_{\text{all}}, R_{\text{gt}}, wR, S, R_{\text{int}},
\text{completeness}, d_{\min},
\rho_{\min}, \rho_{\max},
N_{\text{refl}}, N_{\text{param}},
\text{restraints}, \text{disorder}, \text{occupancy flags}
]
\]

Svaka komponenta je tumačiva samo uz poznat:

- izvorno CIF polje i originalni tekst;
- status nedostaje/neprimenljivo/izmereno/izvedeno;
- verziju parsera i checkCIF-a;
- temperaturu, talasnu dužinu i tip eksperimenta;
- upozorenja i ljudsko obrazloženje.

Jedinstven „quality score“ može postojati samo kao verzionisan, dokumentovan i kalibrisan pomoćni skor. Nikada ne sme zameniti sirove pokazatelje.

## Teorijske posledice za dve aplikacije

### Globalna pretraga

- Sintaksa, simetrija, hemijska konzistentnost i quality profile određuju koje su analize uopšte podržane.
- Teška greška ili disorder ne znače automatski istu odluku za svaki search mode; mora biti vidljivo koja je reprezentacija nepouzdana.
- Quality filter ima kontekst i ne predstavlja univerzalni skriveni prag.
- R i srodna polja mogu biti feature za re-ranking ili uncertainty, ne zamena za hemijsku sličnost.
- Nedostajuća vrednost mora ostati „nepoznato“, a ne nula.

### Poređenje svih parova

- Geometrijska razlika mora se posmatrati uz s.u. i način tretmana H atoma.
- Disorder alternative ne smeju se mapirati kao dva istovremeno prisutna atoma.
- Zaključak treba tumačiti zajedno sa kvalitetom atomskog mapiranja i pokrivenošću upoređenog dela.
- Nizak RMSD između dva slaba modela nije snažan dokaz.
- „Strukturno različito“ i „nema dovoljno pouzdanih podataka“ jesu različita stanja znanja.

Validnost se ne može proceniti samo na urednim primerima: disorder, nepotpunost, redeterminations i kontrolisani oštećeni primeri otkrivaju drugačije failure mode-ove. Tačan budući testni skup i pragove mora da odobri stakeholder.

## Tipične zamke

1. Tretirati R kao accuracy.
2. Uporediti R na \(F\) sa wR na \(F^2\).
3. Pretvoriti svaki checkCIF alert u automatsko odbacivanje.
4. Tumačiti occupancy 0,5 kao „atom je polovično tačan“.
5. Ignorisati da su mnogi H atomi konstrainovani, ne nezavisno opaženi.
6. Zaokružiti koordinate pre računanja geometrije i izgubiti preciznost.
7. Koristiti s.u. kao potpunu meru tačnosti i ignorisati sistematsku grešku.
8. Sabiti missing, unknown i not applicable u istu numeričku nulu.
9. Verovati da numerička konvergencija dokazuje hemijski ispravan model.
10. Poslati poverljiv CIF javnom validatoru bez dozvole.

## Mini-vežbe

### 1. Čitanje zagrada

Šta znači \(1.2825(16)\ \text{Å}\)?

??? success "Odgovor"
    Nominalna dužina je \(1.2825\ \text{Å}\), a standardna neizvesnost \(0.0016\ \text{Å}\). Zagrade se odnose na poslednje prikazane cifre.

### 2. Dva R faktora

Zašto su 0,0322 i 0,0347 oba legitimna za isti model?

??? success "Odgovor"
    Prva vrednost koristi samo refleksije iznad kriterijuma \(I>2\sigma(I)\), a druga sve refleksije uključene u refiniranje. Slabije refleksije obično povećavaju ostatak.

### 3. Da li je GoF 1,095 dokaz?

Možeš li samo iz \(S=1.095\) zaključiti da je struktura tačna?

??? success "Odgovor"
    Ne. To pokazuje razumno slaganje normalizovanih ostataka sa korišćenim težinama. Pogrešan hemijski model, propušten solvent ili druga sistematska greška i dalje su mogući.

### 4. Occupancy alternativa

Dve alternativne pozicije istog atoma imaju occupancy 0,62 i 0,38. Kako ih aplikacija treba tretirati?

??? success "Odgovor"
    Kao međusobno isključive alternative čiji zbir iznosi 1, a ne kao dva istovremeno prisutna atoma. Potrebno je sačuvati disorder grupu i propagirati neizvesnost u deskriptore.

### 5. Projektantska odluka

Globalni indeks dobija CIF sa R = 0,09, occupancy disorder-om i validnim checkCIF obrazloženjem. Da li ga automatski odbacuješ?

??? success "Odgovor"
    Ne na osnovu tih podataka. Struktura ide kroz kontekstualnu validaciju. Može biti legitimna, ali geometrijski i packing deskriptori treba da nose quality/uncertainty oznaku, a korisnik može zahtevati stroži filter.

### 6. Jedan cubic pik

Za cubic ćeliju \(a=5.6400\ \text{Å}\) i Cu K\(\alpha\), \(\lambda=1.5406\ \text{Å}\), izračunaj \(d(200)\) i približan \(2\theta\). Da li je taj simulirani pik dokaz da NaCl uzorak postoji u laboratoriji?

??? success "Odgovor"
    \(d(200)=a/2=2.8200\ \text{Å}\), a \(2\theta\approx31.7^\circ\). To je predikcija sintetičkog modela pod zadatim settings-ima, ne dokaz postojanja uzorka. Za bulk evidence potreban je nezavisno izmeren PXRD i definisan protokol poređenja.

## Kriterijum prolaza

Poglavlje si savladao kada možeš da uzmeš <code>cu_n14_a.cif</code>, napraviš tabelu svih navedenih quality polja, protumačiš ih bez univerzalnog praga, izvedeš \(hkl\rightarrow d\rightarrow2\theta\) za jednostavnu ćeliju i jasno odvojiš simulirani pattern od izmerenog PXRD bulk dokaza.

## Primarni i autoritativni izvori

- [IUCr Online Dictionary: Refinement](https://dictionary.iucr.org/Refinement)
- [IUCr Core CIF dictionaries](https://www.iucr.org/resources/cif/dictionaries)
- [IUCr checkCIF](https://checkcif.iucr.org/)
- [IUCr checkCIF FAQ](https://journals.iucr.org/services/cif/checking/checkfaq.html)
- [IUCr Statistical descriptors in crystallography](https://dictionary.iucr.org/Statistical_descriptors)
- [IUCr definition of CIF](https://dictionary.iucr.org/CIF)
- [IUCr Online Dictionary: Miller indices](https://dictionary.iucr.org/Miller_indices)
- [IUCr Online Dictionary: reciprocal lattice](https://dictionary.iucr.org/Reciprocal_lattice)
- [IUCr powder CIF dictionary](https://www.iucr.org/resources/cif/dictionaries/browse/cif_pd)
- [CCDC API: powder-pattern simulation settings](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/descriptors.html)
