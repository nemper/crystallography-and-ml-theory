# 17. Forenzika dostavljenog skupa

**Prioritet: MORAŠ.** Ova strana najpre izvodi prenosive pouke iz već zabeleženih nalaza, a zatim čuva referentni inventar lokalnog preseka. Preduslovi su formati, standardizacija, reprezentacije i CSD upiti iz poglavlja 12–16.

!!! info "Granica dokaza"
    Sve brojke označene kao lokalne potiču iz snapshot-a dostavljenog u folderu `2CDC`. Prvobitna beleška nosi datum 22. avgusta 2026; agregati formata i metadata ponovo su provereni 5. septembra 2026. pomoću Gemmi 0.7.5 i zasebnog čitanja MOL2/SDF/SMILES zapisa. One nisu statistika današnjeg punog CSD-a. Originalni CSD izvozi, `.cqs`, eksperimentalni CIF/MOL fajlovi i ugrađeni HKL podaci **nisu commit-ovani u ovaj dokumentacioni repo**; ovde su samo agregati, metod i minimalni didaktički primeri. Pre bilo kakvog javnog objavljivanja ili distribuiranja derivata potrebna je licencna provera.

## Kako čitati nalaz, posledicu i dokaz {#sinteza-nalaza}

Osnovni prolaz prati četiri pitanja iz postojeće analize. Reference u poslednjoj koloni vode na sačuvani trag; ova dorada ne predstavlja novu inspekciju izvornih fajlova.

| Pitanje i već zabeležen nalaz | Prenosiva posledica | Gde je trag dokaza |
|---|---|---|
| Šta gubi drugi zapis istog objekta? N14 izvozi ne nose jednaku semantiku veza. | izvor i namenski pogled se razlikuju; gubitak informacije nije nova hemijska struktura | slučaj N14, pa inventar formata |
| Šta upit zaista zahteva? `search2` je podskup `search1`, uz nepovezani metalni uslov. | članstvo ne dokazuje vezu metal–ciljni donor niti predstavlja nezavisnu labelu | odnos pretraga, zatim sačuvana semantika upita |
| Ko ulazi u uzorak? Motiv, stari release i dostupnost izvoza određuju presek. | dobijeni učinak ne prenosi se automatski na punu ciljnu populaciju | izbor uzorka, datumi i referentni missingness profil |
| Koliko imamo nezavisnih primera? Formati i srodna određivanja mogu deliti isti identitet/familiju. | grupisanje prethodi splitu i evaluaciji; broj redova nije broj nezavisnih objekata | slučaj duplikata i refcode porodica |

Prvo pročitaj sintezu i završene slučajeve do provere znanja. Duge inventare, brojnosti, raspodele, verzije i identifikatore u drugom delu otvaraj kada proveravaš određeni iskaz. Oni zadržavaju postojeće vrednosti i izvorna ograničenja.

## 17.1 Tri sloja: izvor, nalaz i interpretacija

Forenzički izveštaj mora da razlikuje:

| Sloj | Primer | Koliko je jak dokaz |
|---|---|---|
| direktno polje/bajt | CQS navodi ConQuest `2022.2.0`; CIF formula sadrži Zn | reproduktivno čitanje izvora |
| izvedena statistika | `search2` je podskup `search1`; median R je 0,051 | zavisi od parsera i jasno definisanog postupka |
| hemijska interpretacija | CAPHEK ima N3Cl2 Zn okolinu; APHZUC nije DAP–metal N3 kompleks | zahteva graf, mapping, geometriju i stručna pravila |

Naziv fajla nije poseban četvrti izvor istine. `2 - Kompleksi sa DAP SB.cqs` opisuje nameru autora, ali izvršiva semantika query-ja je slabija od tog naziva.

<span id="1715-sta-lokalna-forenzika-znaci-za-naucni-dizajn"></span>

## 17.14 Šta lokalna forenzika znači za naučni dizajn

### Ulaz i reprezentacije

Lokalni fajlovi pokazuju da ulaz može biti velik, multi-block, sadržati duga tekstualna polja, različite missing oznake, neizvesnosti i frakcione koordinate van osnovnog intervala. Entry, crystal, komponente i koordinacioni graf nisu isti objekat, a lossy reprezentacija ne može bez upozorenja zameniti bogatiji izvor. Poravnanje formata po refcode-u mora očuvati i vidljivost nedostajućih reprezentacija. Ovo su naučni zahtevi za značenje ingest-a, ne izbor parsera, storage slojeva ili izvršnog toka.

### Aplikacija 1: globalna pretraga

Lokalni izvozi nisu globalni CSD corpus i ne mogu dokazati performanse nad punom bazom. `search1/2` opisuju DAP-uslovljen slice, a 233 od 2.038 metal-containing zapisa nemaju SMILES. Zato 2D scaffold, prisustvo metala, potvrđena koordinacija i crystal similarity ostaju različite ose, dok rezultat mora biti tumačen uz release, mapping, score komponente, missingness, kvalitet i licencni scope. Poglavlje ne bira indeks, fallback ili način prikaza.

### Aplikacija 2: svi parovi

Za `n` ulaza postoji `n(n−1)/2` neuređenih parova, ali nijedan pair score nema smisla bez izabranog nivoa: ligand, coordination entity, conformer ili crystal packing. N14 pokazuje da različiti eksporti iste strukture mogu imati različite bond-order informacije. Packing claim nema dovoljan dokaz bez ćelije, simetrije i 3D podataka, dok atom mapping mora biti neosetljiv na fizički ekvivalentne promene zapisa. Tumačenje para zato zavisi od porekla reprezentacija, mapping-a, obima dokaza i razloga za neocenjen rezultat, bez propisivanja result schema-e.

### Ground truth

Stručna anotacija može razdvojiti valjanost motiva, scope prisustva metala, mapirane DAP donore i metal–donor veze, opaženi denticitet i geometriju, uloge komponenti, dovoljnost podataka, task-specific relevantnost i poreklo stručne odluke. To su dimenzije ground truth-a, ne fiksna lista polja.

Članstvo u query rezultatu može biti candidate label, nikada automatski similarity rank ili konačna koordinaciona istina.

## 17.8 N14: jedan identitet, tri vrlo nejednake reprezentacije

`cu_n14_a.cif` je jedan bogat eksperimentalni CIF, a ne CSD multi-entry eksport.

### Šta CIF direktno navodi

| Osobina | Vrednost |
|---|---|
| formula | `C25 H20 N3 O2 P` |
| formula mass | 425,41 |
| temperatura | 100 K |
| space group | `P 21/c`, broj 14 |
| ćelija | `a=12,7138`, `b=15,3951`, `c=10,6106 Å`; `α=90`, `β=93,235`, `γ=90°` |
| volumen / Z | 2.073,51 Å³ / 4 |
| calculated density | 1,363 g cm⁻³ |
| talasna dužina | 1,54178 Å, Cu Kα |
| refleksije | 87.254 measured; 4.237 unique; 3.891 `I>2σ(I)` |
| refinement | `R1(gt)=0,0322`; `R1(all)=0,0347`; `wR2(gt)=0,0820`; `wR2(ref)=0,0838`; GoF 1,095 |
| model | 284 parametra; 0 restraints; completeness 1,000 |
| residual density | +0,327 / −0,349 e Å⁻³ |

Nezavisna provera ćelije, Z i formula mass daje gustinu približno 1,36273 g cm⁻³, konzistentnu sa CIF vrednošću.

Fajl sadrži 51 atom site (`C25 H20 N3 O2 P`), 31 anisotropic records, 54 eksplicitne veze, 85 uglova i 59 torzija. Ugrađuje i oko 170 linija SHELX RES sadržaja i 89.111 HKL linija; zato ima oko 2,7 MB iako je molekul mali.

!!! example "Dve opasne pretpostavke iz imena"
    `cu_` u imenu nije dokaz prisustva bakra: formula nema Cu; ovde je konzistentno sa Cu Kα zračenjem. `N14` je sample/file label, ne dokaz izotopa azot-14. Hemiju čitaj iz sadržaja, a ime čuvaj samo kao provenance.

### Šta su MOL i MOL2 izgubili

| Osobina | `N14.mol` | `N14.mol2` | bogati CIF |
|---|---|---|---|
| atomi / veze | 51 / 54 | 51 / 54 | 51 site / 54 bond records |
| bond tipovi | svih 54 `single` | 34 `single` + 20 `un` | distance/geometrija i hemijski kontekst |
| charges | nema | svi 0 | širi eksperimentalni/strukturni kontekst |
| crystal data | nema | `CRYSIN` | puna ćelija, simetrija i refinement |
| RES/HKL | nema | nema | prisutni |

MOL zato ne prenosi očiglednu iminsku/aromatičnu/nitro bond-order hemiju. MOL2 otvoreno ostavlja 20 veza kao `un`. To je loss, ne kontradikcija da je realni molekul „samo single-bonded“.

Strukturne distance u CIF-u podržavaju razumnu hemiju: P–C 1,841–1,853 Å uz trigonalno-piramidalni P(III) centar; nitro N–O 1,2272/1,2274 Å; hydrazone-like C=N 1,2825 Å i N–N 1,3608 Å. Ove tvrdnje se ne bi smele rekonstruisati iz V2000 bond orders ovog konkretnog MOL fajla.

<div class="project-link" markdown="1">
**Pouka za parsiranje:** `cu_n14_a.cif` pokazuje da mali koordinatni model može biti upakovan sa višemegabajtnim semicolon-delimited HKL blokom. Resource-bounded čitanje i razlikovanje refleksionog teksta od hemijskih reprezentacija zato su bezbednosno i naučno važni; ova činjenica ne propisuje parser arhitekturu niti konkretan fixture.
</div>

## 17.3 Dokazani odnos `search1` i `search2`

Rezultati nisu dva nezavisna dataseta:

```text
search1: 2.110 DAP-motif entry-ja
└── search2: 2.038 istih entry-ja sa bar jednim 4M elementom

razlika: 72 entry-ja bez metala
```

- `search2` je **strogi podskup** `search1`;
- njegovi refcode-ovi se javljaju u potpuno istom redosledu kada se `search1` filtrira;
- tačno 72 refcode-a iz `search1` nedostaju u `search2`;
- svih 72 imaju SMILES i njihove formule su metal-free;
- svih 2.038 formula u `search2` sadrži najmanje jedan element iz ConQuest grupe `4M`;
- u nijednom kompletnom izvozu nema dupliranog punog refcode-a.

**CAPHAG** je prvi koristan član razlike: DAP-derived bis-iminski ligand formule `C25 H27 N3`, bez metala. **CAPHEK** je prvi `search2` primer: Zn koordinisan preko N3 liganda i dva Cl donora, uz odvojene molekule acetonitrila i vode.

Kontraprimeri **APHZUC**, **FOWLEJ**, **GEHCOM**, **MINQUV**, **SUZBAT** i **UJIXES** pokazuju zašto `search2` članstvo nije koordinaciona etiketa: metal može biti u odvojenom jonu/komponenti ili u okolini koja ne uključuje ciljne DAP azote.

## 17.11 Selection bias: šta ovaj skup sistematski favorizuje

Ovaj skup je **query-conditioned convenience snapshot**, ne slučajan uzorak CSD-a:

1. svaki entry mora imati usko 18-atomsko 2,6-diacetilpiridinsko query jezgro sa dve `C=N` veze;
2. `search2` dodatno bira metal presence, ne validiranu DAP koordinaciju;
3. svi standardni quality/disorder/polymer/ion/3D filteri bili su isključeni;
4. snapshot prestaje sa June 2022 update-om i ne predstavlja kasnije deponovane strukture;
5. metal distribution je snažno skewed ka određenim istraživačkim i sintetičkim serijama;
6. multi-component kristali dominiraju coordinate-bearing delu;
7. nema reprezentativnog skupa molekula van DAP motiva;
8. query membership ne sadrži similarity score, relevance order niti expert label.

Ne može se pošteno trenirati „univerzalna hemijska sličnost“ tako što se `search1=positive`, a ostatak sveta proglasi negativnim. Isto tako, `search2=complex` bi unelo label noise dokumentovan kontraprimerima.

## 17.13 Duplikati, refcode porodice i leakage

### Exact SMILES duplikati

U `search2` postoji 1.805 SMILES redova, ali samo 1.661 exact string vrednosti. Najveći exact cluster ima 36 entry-ja: `ORIFON`, `ORIGII` i `ORIGII01`–`ORIGII34`. `FAVKIA` porodica ima šest exact-identičnih SMILES zapisa.

Isti 2D molekul može zato predstavljati više kristalografskih određivanja, temperatura, polimorfa, solvata ili redeterminations. Za crystal/packing zadatak to mogu biti legitimno različiti target-i; za 2D ligand retrieval mogu biti gotovo duplikati.

### Refcode porodice

Minimalna CSD family heuristika koristi prvih šest slova refcode-a. Lokalno:

| Mera | `search1` | `search2` |
|---|---:|---:|
| base-refcode porodice | 1.960 | 1.899 |
| suffixed refcode-ovi | 170 | 159 |
| porodice sa više članova | 97 | 89 |

Samo split po punom refcode string-u dopušta da, na primer, `ORIGII01` završi u train-u, a `ORIGII22` u test-u. Model tada može memorisati ligand/seriju i dati lažno visok rezultat.

### Minimalna split politika

1. grupiši najmanje po base refcode-u;
2. dodatno grupiši exact canonical graph/SMILES identitete;
3. za ozbiljnu generalizaciju grupiši po scaffold/chemical family i, kada je cilj packing, jasno odluči da li polymorph/solvate parovi moraju ostati zajedno ili su namerni challenge parovi;
4. pravi temporalni split po **database release/deposition vremenu**, ne po datumu kada je stari snapshot pretražen;
5. deduplikuj pre podele i fituj sve learned preprocessing korake samo na train-u;
6. objavi koliko je porodica, ne samo koliko record-a, u svakom split-u.

!!! warning "Base refcode nije dovoljan"
    Exact-identičan SMILES cluster može da pređe granicu dve različite base-refcode porodice, kao `ORIFON` naspram `ORIGII...`. Zato je base refcode minimalna, ne konačna zaštita od leakage-a.

<span id="1717-mini-vezbe"></span>

## 17.16 Mini-vežbe

### 1. Dva datuma

CQS je sačuvan 2026, ali bira CSD bazu i update segmente samo do juna 2022. Koji datum određuje data coverage?

??? success "Odgovor"
    June 2022 release/update cutoff. Datum pretrage 2026 govori kada je stari snapshot upitan, ne da uključuje strukture deponovane do 2026.

### 2. Broj pogodaka

Zašto `search2` ima 2.038 record-a, ali samo 1.954 coordinate-bearing strukture?

??? success "Odgovor"
    Query nije zahtevao 3D. Osamdeset četiri entry-ja imaju record/metadata i matching/disorder status, ali nemaju upotrebljiv atomski koordinatni model u eksportu.

### 3. Razlika pretraga

Šta tačno predstavlja 72 člana `search1 \ search2`?

??? success "Odgovor"
    DAP-motif entry-je bez metala prema `4M` composition kriterijumu. To nisu svi „slobodni ligandi u hemijskom univerzumu“, već metal-free članovi ovog konkretnog query snapshot-a.

<span id="5-smiles-ciscenje"></span>

### 4. SMILES čišćenje

Data scientist odbacuje svih 233 `search2` entry-ja bez SMILES i kaže da je to nasumičnih 11,4%. Zašto je zaključak pogrešan?

??? success "Odgovor"
    Nedostajanje je isto u obe pretrage i koncentrisano u većim/složenijim metalnim zapisima, naročito Mn/Fe/Co/Ni. Complete-case skup menja ciljnu hemijsku distribuciju.

<span id="6-refcode-split"></span>

### 5. Refcode split

`ORIGII01` je u train-u, `ORIGII22` u test-u. Šta nije u redu?

??? success "Odgovor"
    Članovi iste refcode porodice i exact-SMILES klastera cure preko split-a. Grupisati najmanje po base refcode-u i hemijskom identitetu pre podele.

<span id="7-n14-ime"></span>

### 6. N14 ime

Da li `cu_n14_a.cif` dokazuje Cu kompleks sa izotopom 14N?

??? success "Odgovor"
    Ne. Formula nema Cu, `cu` je konzistentno sa Cu Kα zračenjem, a `N14` je label. Izotopski i elementarni identitet se ne izvode iz imena fajla.

<span id="8-jedna-formula-jedan-cn"></span>

### 7. Jedna formula, jedan CN?

CAPHEK formula ima Zn, četiri N i dva Cl. Zašto je koordinaciona signatura `N3Cl2`, a ne `N4Cl2`?

??? success "Odgovor"
    Formula obuhvata i odvojeni acetonitril i vodu. Samo tri ligandna N i dva Cl su neposredni susedi Zn; CN se određuje iz koordinacionog grafa/geometrije, ne iz ukupnog broja elemenata.

<span id="1718-kriterijum-prolaza"></span>

## 17.17 Kriterijum prolaza

Poglavlje si savladao kada možeš da reprodukuješ broj zapisa po formatu, nacrtaš stvarnu logiku oba query-ja, objasniš 2022/2026 provenance razliku, pokažeš najmanje tri izvora label leakage/bias-a i objasniš zašto nepoverljivi CQS i missingness zahtevaju različite bezbednosne i statističke provere.

## Referentni inventar i reproduktivnost {#referentni-inventar}

Sledeći blokovi čuvaju detalje konkretnog istorijskog preseka. Njihove brojke nisu statistika cele baze niti rezultat nove provere u ovoj doradi. Brojevi odeljaka ostaju oznake izvornih referenci kako bi postojeće veze i navodi ostali upotrebljivi; redosled čitanja određuje gornji osnovni tok.

## 17.2 Šta je dostavljeno

### Projektni zahtev

`dve funkcionalnosti.txt` definiše dva različita proizvoda:

1. **Globalna pretraga:** jedan uploadovani CIF se pretvara u hemijske/kristalografske reprezentacije, filtrira se i poredi sa velikom CSD kolekcijom; rezultat je rangirana lista sličnih struktura. Tekst predlaže slojeve za metadata, vektorsku i graf pretragu, ali ne definiše metriku relevantnosti ni ground truth.
2. **Poređenje svakog para:** za `n` uploadovanih CIF-ova obrađuje se `n(n−1)/2` parova uz detaljnije grafovsko, geometrijsko, packing i interaction poređenje. Veća tačnost je cilj iz zahteva; manji broj ulaza omogućava skuplje metode, ali sam po sebi ne dokazuje da će one biti tačnije.

To je product brief, ne hemijska specifikacija. Pojmovi „sličan“, „tip jedinjenja“, „osobina“ i „preciznije“ tek treba da se pretvore u merljive ugovore.

### Strukturni primer N14

| Fajl | Veličina | Forenzički tip |
|---|---:|---|
| `cu_n14_a.cif` | 2.700.216 B | jedan bogat eksperimentalni SHELX/coreCIF zapis sa koordinatama, refinement podacima i ugrađenim RES/HKL blokovima |
| `N14.mol` | 2.803 B | jedan MDL MOL V2000 zapis, uz završni `$$$$` delimiter |
| `N14.mol2` | 5.233 B | jedan Tripos MOL2 zapis sa Cartesian koordinatama i `CRYSIN` sekcijom |

### Dve CSD pretrage

| Artefakt | `search1` | `search2` | Uloga |
|---|---:|---:|---|
| `.cqs` | 548.864 B | 532.480 B | ConQuest query + sačuvano stanje/rezultati; binarno |
| `.cif` | 2.110 data blokova | 2.038 data blokova | entry metadata, ćelija/simetrija i, kada postoje, frakcione koordinate |
| `.mol2` | 2.110 record-a | 2.038 record-a | molekulski graf/koordinate; neki record-i nemaju atomsku strukturu |
| `.sd` | 2.110 record-a | 2.038 record-a | MDL V2000 record-i; neki su prazni zbog matching problema |
| `.smi` | 1.877 reda | 1.805 redova | `SMILES<TAB>refcode`; nepotpun podskup |

Refcode redosled u CIF/MOL2/SD izvozu je međusobno jednak unutar svake pretrage. SMILES zadržava isti relativni redosled, ali preskače zapise bez dostupnog izvoza.

## 17.4 Tačna rekonstrukcija oba query-ja

Oba `.cqs` sadrže isti povezani 2D connectivity motiv:

| Osobina | Vrednost iz query objekta |
|---|---|
| eksplicitni atomi | 18: 9 C, 3 N, 6 H |
| kostur | centralni pyridine-like prsten, supstituisan na 2,6 položajima |
| ruke | dve `ring-C–C(=N)–CH3` grupe |
| prstenaste veze | 6 veza sa kodom 5 |
| dvostruke `C=N` veze | 2, kod 2 |
| ostale veze | 10 `Any` veza, kod 99 |
| search flags | `exhaustive=1`, `symmchk=1` |

`search1` nema dodatni metalni criterion. To **ne znači** da zabranjuje metale; zato sadrži svih 2.038 metal-containing članova `search2` i još 72 metal-free zapisa.

`search2` dodaje nepovezan devetnaesti atom tipa `4M`. ConQuest vodič definiše `4M = 1M + 2M + TR + LN + AN`, odnosno svoju grupu metalnih elemenata. U nju preko `2M` ulaze i Ge i Sb; izrazi „metal-containing“ i „metal-free“ u ovoj forenzici prate tu softversku grupu. U query objektu ne postoji:

- bond-order veza od `AT19` do jednog od tri DAP N;
- contact/distance constraint;
- uslov da su metal i DAP motiv u istoj povezanoj komponenti;
- zahtev da isti metal vezuje sva tri mapirana N.

Zato je formalna semantika:

```text
EXISTS mapped 18-atom DAP-derived bis-C=N query core
AND EXISTS any metal atom in the same database entry
```

a ne:

```text
EXISTS metal coordinated to the mapped N_imine–N_pyridine–N_imine donors
```

Serializovani default filter flags `3dco`, `rfac`, `diso`, `erro`, `poly`, `ions`, `powd` i `orga` svi su isključeni. Pretraga zato nije zahtevala punu 3D strukturu, maksimalni R, odsustvo disorder-a/error-a, nepolimernost, određeni ionski/powder status ili organic/organometallic klasu.

!!! warning "Granica forenzičke rekonstrukcije"
    Ova rekonstrukcija je forenzičko čitanje sačuvanog objekta. Jača tvrdnja o originalnoj ljudskoj nameri zahtevala bi nezavisnu vizuelnu proveru u kompatibilnom, licenciranom ConQuest okruženju i stručnu potvrdu; ovaj dokument ne propisuje postupak te buduće provere.

## 17.5 CSD snapshot iz 2022. naspram datuma pretrage iz 2026.

`.cqs` navodi ConQuest verziju `2022.2.0` i tri izabrana CSD segmenta:

| Segment | Broj entry-ja kodiran u CQS-u |
|---|---:|
| osnovni CSD 5.43, novembar 2021. | 1.161.919 |
| mart 2022. update | 19.425 |
| jun 2022. update | 15.998 |
| **ukupno izabrano** | **1.197.342** |

Lokalne putanje/timestamp vrednosti u sačuvanom objektu nose trag pokretanja ili čuvanja pretraga 6. juna 2026. oko 18:49 i 18:53; vremenska zona i tačna semantika događaja nisu zabeležene. Otkrivena lokalna korisnička putanja namerno je redigovana u ovoj knjizi.

Ovo daje dve različite vremenske ose:

```text
data cutoff: najkasnije CSD June 2022 update
search/save event: tragovi iz June 2026
local audit: August 2026; ponovljena provera agregata September 2026
```

Pretraga pokrenuta 2026. nad instalacijom iz 2022. **nije CSD snapshot iz 2026.** Raspon publication year-a lokalnih rezultata 1967–2022 dodatno je konzistentan sa starim cutoff-om.

<div class="project-link" markdown="1">
**Pouka za provenance:** release baze, verzija query alata, vreme pokretanja pretrage, vreme eksporta i vreme kasnije analize predstavljaju različite događaje. Njihovo stapanje u jednu oznaku „datum skupa“ napravilo bi ozbiljnu provenance grešku i pokvarilo temporalnu evaluaciju. Ovo je semantički zahtev, ne predlog naziva polja.
</div>

## 17.6 Bezbednosni i provenance status `.cqs` artefakta

Lokalna inspekcija oba `.cqs` fajla pokazuje binarni Berkeley DB sadržaj sa Python pickle tokovima i lokalnim putanjama. Pickle deserializacija može izvršiti kod, pa poreklo fajla nije dokaz bezbednosti; CQS može sadržati i tragove o korisniku i lokalnom okruženju. Ovaj nalaz pripada provenance-u dostavljenih upita, ne hemijskoj semantici niti ulaznom formatu budućih aplikacija.

## 17.7 Šta svaki CSD izvozni format čuva i gubi

### CIF eksport

Lokalni multi-block CSD CIF ima 51 jedinstven tag. Dobar je za:

- refcode i entry metadata;
- formula, godina, CCDC deposition number kada postoji;
- ćeliju, crystal system i space group;
- frakcione koordinate kada postoji 3D model;
- pojedine quality/descriptive fields.

Ali ovaj **pojednostavljeni CSD CIF eksport** nema bond loop, occupancy niti ADP podatke. Atom-site petlja sadrži label, element i frakcione koordinate; CSD poluprečnici su u odvojenoj atom-type petlji (`_atom_type_symbol`, `_atom_type_radius_bond`). Zato ne treba iz njega očekivati isti nivo kao iz originalnog publication/deposition CIF-a niti samostalno smatrati graf eksplicitno zadatim.

| Pretraga | Svi CIF blokovi | Sa atom loop-om/koordinatama | Bez njih |
|---|---:|---:|---:|
| `search1` | 2.110 | 2.023 | 87 |
| `search2` | 2.038 | 1.954 | 84 |

### MOL2 eksport

Tripos MOL2 čuva Cartesian koordinate, atom types, bond records, substructures i često `CRYSIN`. Ipak:

- sam eksport upozorava da atom types treba proveriti;
- metal–ligand order i `un`/unknown tipovi su reprezentacione konvencije;
- charge model je `NO_CHARGES` za 1.232 i `USER_CHARGES` za 806 `search2` record-a;
- integer-like atom charges se javljaju od −2 do +3, a 192 coordinate-bearing record-a imaju nenulti zbir, ali to nisu automatski oksidaciona stanja;
- `Du` dummy atomi označavaju suppressed/disorder alternative i zahtevaju posebnu obradu.

| MOL2 mera | `search1` | `search2` |
|---|---:|---:|
| ukupno atoma, uključujući `Du` | 225.185 | 220.031 |
| `Du` atoma | 7.998 | 7.805 |
| atoma bez `Du` | 217.187 | 212.226 |
| bond records | 232.486 | 227.384 |

U `search2` se 7.805 `Du` atoma javlja u 627 record-a, uglavnom u `SUP*` substructure grupama. Oni nisu običan novi hemijski element.

### SDF/SD eksport

SDF koristi MDL V2000 fixed-width counts i bond records. Parser mora čitati kolone, ne samo `split()`:

```text
121150 ...
```

može značiti 121 atom i 150 veza, a ne jedan broj 121150. Formalni naboji mogu biti u `M  CHG` linijama.

U `search2` bond kodovi u strukturama su:

| Kod/tip | Broj |
|---|---:|
| single | 164.839 |
| aromatic | 47.822 |
| double | 11.187 |
| triple | 2.227 |
| any | 1.308 |

SDF sadrži 212.226 atoma — tačno MOL2 broj bez `Du` — i 227.383 veze. Jedna MOL2 veza dodiruje `Du`, pa je nema u SDF-u.

Svih 2.038 `search2` SD record-a ima status komentar:

- 1.778: `No disordered atoms`;
- 176: `Matching problem. No disordered atoms`;
- 84: `Matching problem. Disorder unknown`.

Poslednjih 84 odgovara record-ima bez upotrebljivog koordinatnog modela. Status nije dekoracija; ulazi u data quality i abstention logiku.

### SMILES eksport

`.smi` je po jedan red `SMILES<TAB>refcode`. Čuva 2D connectivity/stereo/charge onoliko koliko ih zapis kodira, ali ne čuva ćeliju, packing, eksperimentalni kvalitet ni 3D kristalne koordinate.

| Mera | `search1` | `search2` |
|---|---:|---:|
| svi entry-ji | 2.110 | 2.038 |
| SMILES dostupni | 1.877 | 1.805 |
| nedostaju | 233 | 233 |
| exact unique SMILES | 1.722 | 1.661 |
| redundantni redovi | 155 | 144 |

Istih 233 zajednička metal-containing entry-ja nedostaje u oba SMILES izvoza; svih 72 metal-free članova razlike imaju SMILES. Nedostajanje zato ima obrazac povezan sa sastavom i izvozom, pa se ne sme bez provere pretpostaviti da je potpuno slučajno. To samo po sebi ne određuje formalni MCAR/MAR/MNAR mehanizam. U `search2` ono pogađa oko 11,4% entry-ja, uz zastupljenost složenijih Mn/Fe/Co/Ni zapisa.

Od 1.805 dostupnih `search2` SMILES-a:

- 1.306 ima više komponenti razdvojenih tačkom, oko 72,4%;
- 769 sadrži eksplicitne znakove naboja;
- broj komponenti ide do 5;
- najduži SMILES string ima 1.114 karaktera; ceo red sa tabulatorom i refcode-om ima 1.121 karakter bez završetka reda.

SMILES-only model bi zato trenirao nad selektovanim podskupom i izgubio deo metalnih zapisa relevantnih za projekat. Da li su preostali primeri za određeni ML zadatak lakši mora se posebno ispitati; to ne sledi samo iz dostupnosti izvoza.

## 17.9 Profil `search2` metadata i kvaliteta

### Pokrivenost polja

| Polje | Dostupno / 2.038 |
|---|---:|
| formula, parametri ćelije, godina | 2.038 |
| H–M oznaka prostorne grupe | 2.035 |
| atom koordinate | 1.954 |
| R factor | 2.023 |
| CCDC deposition number | 1.838 |
| density | 1.927 |
| crystal colour | 1.796 |
| description | 1.618 |
| preparation text | 290 |
| common name | 50 |

`?`, `.`, odsutno polje i broj nula moraju ostati različita stanja. Tri zapisa nemaju poznatu H–M oznaku grupe, iako postoje parametri ćelije; potrebno je proveriti ostale simetrijske podatke pre periodičnog poređenja. Na primer, common name nedostaje za ogromnu većinu; to nije prazan string koji model sme da tumači kao hemijsku osobinu.

### R faktori

- medijana lokalnog R: 0,0512 (zaokruženo 0,051);
- maksimum: 0,1711;
- 71 zapisa ima `R > 0,10`;
- 15 nema R.

U svih 2.023 record-a u kojima postoje oba polja, `_refine_ls_wR_factor_gt` je tačno jednak `_refine_ls_R_factor_gt`. Izvoz uz ta polja izričito navodi da su obe vrednosti dobijene iz jednog CSD polja; taj komentar se javlja 2.023 puta. Ovo je dokaz dupliranog izvoznog mapiranja, pa ta polja nisu dva nezavisna pokazatelja kvaliteta. Stvarni ponderisani R ne može se rekonstruisati iz njihove jednakosti: zahteva izvorni eksperimentalni/refinement zapis ili drugi pouzdan podatak.

Godine publikovanja u lokalnom `search2` idu od 1967. do 2022, sa medijanom 2012. To je istorijska raspodela ovog query subset-a, a ne ravnomeran temporalni uzorak.

### Raw cell-setting etikete i space groups

| Raw `_symmetry_cell_setting` vrednost | Broj |
|---|---:|
| monoclinic | 1.232 |
| triclinic | 491 |
| orthorhombic | 264 |
| tetragonal | 26 |
| rhombohedral | 12 |
| hexagonal | 12 |
| cubic | 1 |

Ovo su doslovne etikete pojednostavljenog eksporta, a ne već završena standardizovana taksonomija. Vrednost `rhombohedral` treba pri normalizaciji mapirati u **trigonalni kristalni sistem**, uz čuvanje raw vrednosti i rhombohedral setting-a kao odvojenih provenance polja.

Najčešći space groups su `P-1` (480), `P21/c` (473), `P21/n` (368) i `C2/c` (228). Ovo opisuje DAP+metal query subset, ne baznu verovatnoću svih CSD struktura.

### Formule i elementi

Sve formule imaju C, H i N zbog query motiva. Najčešći dodatni elementi uključuju:

| Element | Entry-ja u čijoj se formuli javlja |
|---|---:|
| O | 1.404 |
| Cl | 930 |
| Fe | 511 |
| Co | 273 |
| Mn | 242 |
| Ni | 148 |
| Zn | 133 |
| Cu | 123 |
| Cr | 83 |
| Mo | 68 |
| Ru | 60 |
| Cd | 54 |
| Dy | 52 |
| Sn | 51 |
| U | 44 |

Brojevi se preklapaju: jedan entry može sadržati više elemenata, a 264 entry-ja imaju više od jednog različitog metalnog elementa. `metal=Fe` nije jednaka kategorija `only metal=Fe`.

Čak 250 `search2` formula ima fractional stoichiometry, na primer `O8.33` ili `Mn0.5`. Formula parser mora koristiti decimalne koeficijente; pretvaranje u `int` ili brojanje tekstualnih simbola daje pogrešan sastav.

## 17.10 Profil molekulskog/koordinacionog grafa

U 1.954 coordinate-bearing `search2` record-a:

- ima 4.070 eksplicitnih 4M centara nakon isključivanja `Du`; izbor elemenata prati ConQuest legacy grupu `4M`, uključujući Ge i Sb;
- median broja non-`Du` atoma po record-u je 92, prosek 108,61, maksimum 646;
- median broja povezanih komponenti je 2, prosek 2,93, maksimum 36;
- 1.425/1.954, odnosno 72,9%, ima više od jedne povezane komponente;
- 6 record-a nema nijednu metal–N ivicu;
- 35 nema metal sa najmanje tri N suseda;
- 1.919 ima neki metal sa najmanje tri N suseda, ali to još ne mapira te N na ciljni DAP podgraf.

Najčešće kompletne metal-neighbor signature uključuju `W–O6` (198 centara), `Fe–Cl2N3` (152), `Mn–N7` (89), `Co–Cl2N3` (89), `Ni–N6` (71), `Mn–N5O2` (68), `Co–N5O2` (58), `Zn–Cl2N3` (35) i `Cu–N4O1` (35).

Ove signature su korisne kao features, ali imaju tri caveat-a:

1. izvedene su iz eksportovanog grafa, ne nužno iz punog symmetry-expanded kristala;
2. ne govore koji N pripada DAP motivu bez atom mapping-a;
3. isti CN/signature može imati različitu 3D geometriju.

## 17.12 Dokazi ne podržavaju nekritičku MCAR pretpostavku

Nedostajuće reprezentacije pokazuju obrasce povezane sa procesom izvoza i složenošću strukture. Bez formalnog statističkog testa ne tvrdimo da je mehanizam missingness-a potpuno određen, ali sledeći dokazi ne podržavaju nekritičku pretpostavku *missing completely at random* (MCAR):

- 84 `search2` entry-ja nema koordinatni/atomski model u ovim izvozima;
- 233 nema SMILES, i to su isti metal-containing zapisi koji nedostaju i u `search1`;
- SMILES missing grupa je obogaćena većim i složenijim Mn/Fe/Co/Ni strukturama;
- deposition number nedostaje u 200, density u 111, description u 420, preparation tekst u 1.748;
- `Du`/suppressed disorder postoji u stotinama record-a;
- 176 SD record-a ima matching problem iako status kaže „No disordered atoms“, a 84 matching problem uz unknown disorder.

Za tumačenje missingness-a treba razlikovati poznatu vrednost, odsustvo podatka, nepoznato, neprimenljivo i neuspeh parsiranja, kao i poreklo, način izvođenja i kvalitet nalaza. To su različite semantičke kategorije, ne predlog konkretne data schema-e.

Model se evaluira po missingness slice-ovima. „Drop rows with missing SMILES“ nije neutralno čišćenje: menja hemijsku populaciju.

<span id="1716-pitanja-za-proveru-reproduktivnosti-zakljucka"></span>

## 17.15 Pitanja za proveru reproduktivnosti zaključka

- Da li broj potiče iz originalnog izvora ili je izveden pod poznatim pravilima?
- Da li su CSD release, datum query-ja i datum analize pravilno razdvojeni?
- Da li forenzičko čitanje query objekta potvrđuje samo mašinsku semantiku ili i ljudsku nameru?
- Da li je CQS analiziran bez izvršavanja nepoverljivog pickle sadržaja?
- Da li odnos `search2 ⊂ search1` i redosled refcode-ova važe za tačno navedeni snapshot?
- Da li nedostajanje CIF/MOL2/SDF/SMI reprezentacije ostaje vidljivo po entry-ju?
- Da li su `Du`, matching problem, fractional formula i multi-component status uključeni u tumačenje?
- Da li split sprečava curenje refcode/hemijskih familija i poštuje vremenski claim?
- Da li statistika navodi parser/verziju, populaciju i denominator?
- Da li interpretativni i licencni zaključci imaju odgovarajući stručni ili ugovorni dokaz?

## Primarni i autoritativni izvori

- [CCDC ConQuest User Guide and Tutorials — query atoms, element groups i search workflow](https://www.ccdc.cam.ac.uk/media/Documentation/2F0D7443-9739-46EB-BE9F-69E62E531FB7/2f0d7443973946ebbe9f69e62e531fb7.pdf)
- [CCDC Python API: substructure searching](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/substructure_searching.html)
- [CCDC Python API: reading/writing molecules, crystals i podržani formati](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/io.html)
- [CCDC Python API: entry, crystal i molecule kao različiti objekti](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/primer.html)
- [CCDC Python API: components, atoms i bonds](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/molecule.html)
- [CCDC Python API: disorder i entry metadata](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/entry.html)
- [IUCr: Crystallographic Information Framework](https://www.iucr.org/resources/cif)
- [IUCr: CIF dictionaries](https://www.iucr.org/resources/cif/dictionaries)
- [Python dokumentacija: pickle bezbednosno upozorenje](https://docs.python.org/3/library/pickle.html)
- [Oracle Berkeley DB Reference Guide](https://docs.oracle.com/cd/E17275_01/html/programmer_reference/index.html)
- [CCDC CSD Portfolio Conditions of Use](https://downloads.ccdc.cam.ac.uk/documentation/API/conditions_of_use.html)
