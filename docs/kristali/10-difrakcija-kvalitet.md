# 10. Difrakcija, refiniranje i kvalitet

## Šta treba da umeš posle ovog poglavlja

Posle ovog poglavlja treba da možeš da:

- objasniš kako od difrakcionih intenziteta nastaje atomski model;
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

## R faktor: koliko se amplitude ne slažu

Konvencionalni R faktor se najčešće piše:

\[
R =
\frac{\sum_{hkl}\left||F_o|-|F_c|\right|}
     {\sum_{hkl}|F_o|}
\]

Manje slaganje ostataka obično daje manji R. Ipak, R zavisi od kvaliteta i rezolucije podataka, hemijskog sastava, twinning-a, disorder-a, apsorpcije, skupa uključenih refleksija i samog modela.

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

Za least-squares refiniranje:

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

Tipičan tok je:

1. pokreni validaciju odgovarajućeg nivoa;
2. sačuvaj kompletan izveštaj i verziju alata;
3. za svaki alert utvrdi da li je greška, opravdani izuzetak ili nedostajući podatak;
4. zabeleži odluku i dokaz;
5. ne skrivaj alert samo da bi status postao zelen.

[IUCr FAQ](https://journals.iucr.org/services/cif/checking/checkfaq.html) naglašava da se anomalije rangiraju po ozbiljnosti i da opravdani izuzeci mogu dobiti Validation Response Form. Čak i objavljeni pragovi pojedinačnih testova služe kao screening pravila tog testa, ne kao univerzalni zakon za sve strukture.

!!! warning "Poverljivi fajlovi"
    Online checkCIF podrazumeva slanje fajla eksternom servisu. Za proprietary CIF prvo proveri licencu, ugovor i politiku poverljivosti. Ako slanje nije odobreno, koristi lokalno odobrenu validaciju ili testiraj samo javni/sintetički primer.

## Profil kvaliteta, ne jedna etiketa

Za ML i pretragu čuvaj vektor:

\[
q = [
R_{\text{all}}, R_{\text{gt}}, wR, S, R_{\text{int}},
\text{completeness}, d_{\min},
\rho_{\min}, \rho_{\max},
N_{\text{refl}}, N_{\text{param}},
\text{restraints}, \text{disorder}, \text{occupancy flags}
]
\]

Uz svaku komponentu čuvaj:

- izvorno CIF polje i originalni tekst;
- status nedostaje/neprimenljivo/izmereno/izvedeno;
- verziju parsera i checkCIF-a;
- temperaturu, talasnu dužinu i tip eksperimenta;
- upozorenja i ljudsko obrazloženje.

Jedinstven „quality score“ može postojati samo kao verzionisan, dokumentovan i kalibrisan pomoćni skor. Nikada ne sme zameniti sirove pokazatelje.

## Posledice za dve aplikacije

### Globalna pretraga

- Ingest mora prvo proveriti sintaksu, simetriju, hemijsku konzistentnost i quality profile.
- Teška greška ide u quarantine, ne u indeks.
- Strukture sa disorder-om ne treba automatski brisati; indeks mora znati koje reprezentacije su nepouzdane.
- Quality filter treba da bude korisnički i kontekstualan, a ne skriveni univerzalni prag.
- R i srodna polja mogu biti feature za re-ranking ili uncertainty, ne zamena za hemijsku sličnost.
- Nedostajuća vrednost mora ostati „nepoznato“, a ne nula.

### Poređenje svih parova

- Geometrijska razlika mora se posmatrati uz s.u. i način tretmana H atoma.
- Disorder alternative ne smeju se mapirati kao dva istovremeno prisutna atoma.
- Poređenje treba da vrati i kvalitet atomskog mapiranja i pokrivenost upoređenog dela.
- Nizak RMSD između dva slaba modela nije snažan dokaz.
- Izveštaj treba da razdvoji „strukturno različito“ od „nema dovoljno pouzdanih podataka“.

Za obe aplikacije test-skup treba da sadrži uredne, neuređene, nepotpune, redetermined i namerno oštećene CIF-ove. Inače će QA sloj biti testiran samo na idealnim primerima.

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

## Kriterijum prolaza

Poglavlje si savladao kada možeš da uzmeš <code>cu_n14_a.cif</code>, napraviš tabelu svih navedenih quality polja, protumačiš ih bez univerzalnog praga i objasniš kako bi svako polje uticalo na globalni dohvat i precizno poređenje parova.

## Primarni i autoritativni izvori

- [IUCr Online Dictionary: Refinement](https://dictionary.iucr.org/Refinement)
- [IUCr Core CIF dictionaries](https://www.iucr.org/resources/cif/dictionaries)
- [IUCr checkCIF](https://checkcif.iucr.org/)
- [IUCr checkCIF FAQ](https://journals.iucr.org/services/cif/checking/checkfaq.html)
- [IUCr Statistical descriptors in crystallography](https://dictionary.iucr.org/Statistical_descriptors)
- [IUCr definition of CIF](https://dictionary.iucr.org/CIF)
