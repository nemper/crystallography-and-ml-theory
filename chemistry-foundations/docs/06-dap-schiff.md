# 6. DAP Schiff-base motiv u ovom skupu

**Prioritet: MORAŠ.** Ovo poglavlje prevodi naziv koji su naučnici koristili — „DAP Schiff bases“ — u proverljiv hemijski graf. Cilj nije da zapamtiš katalog jedinjenja, nego da razumeš šta je motiv, kako nastaje, zašto može da koordinira metal i šta lokalni upit zaista dokazuje.

## 6.1 Šta „DAP“ znači ovde

Skraćenice u hemiji nisu globalno jedinstvene. U ovom projektu **DAP** treba čitati kao **2,6-diacetilpiridin** (*2,6-diacetylpyridine*), jer baš taj kostur rekonstruišemo iz dostavljenog ConQuest upita:

- centralni šestoročlani piridinski prsten sa jednim N;
- po jedna acetil-derived iminska ruka na položajima 2 i 6;
- dva `C=N` centra;
- po jedna metil-grupa uz svaki iminski C.

Najkraća tekstualna skica bis-iminskog proizvoda je:

```text
                    N_pyridine
                   /          \
        R–N=C(CH3)–              –C(CH3)=N–R′
                  \  pyridine  /

potencijalni donorski niz: N_imine – N_pyridine – N_imine
```

!!! warning "Inference, ne originalno ime u fajlu"
    Lokalni query graf eksplicitno kodira 18-atomsko 2,6-diacetilpiridinsko jezgro sa dve `C=N` veze. Sam query ne ograničava neposredni supstituent na svakom terminalnom N, pa klasifikacija pogotka kao bis-imina ili Schiffove baze zahteva proveru kompletne strukture. `.cqs` ne nosi autoritativnu hemijsku definiciju skraćenice; naučni tim treba pisano da potvrdi nameravani scope, uključujući dozvoljene supstitucije, protone/tautomere i parcijalno kondenzovane proizvode.

## 6.2 Od karbonila i amina do Schiffove baze

2,6-diacetilpiridin ima dve ketonske karbonilne grupe. Svaka može reagovati sa **primarnim aminom** `R–NH2` i dati iminsku vezu `C=N`. Idealizovana ukupna reakcija za simetrični bis-iminski proizvod je:

\[
\text{2,6-diacetilpiridin} + 2\,\mathrm{RNH_2}
\rightleftharpoons
\text{DAP bis(imine)} + 2\,\mathrm{H_2O}.
\]

### Rečnik pre mehanizma

**Pitanje:** šta znači da azot „napada“ ugljenik? Nukleofil (*nucleophile*) donosi elektronski par za novu vezu. Azot neutralnog primarnog amina koristi isti slobodni par koji smo upoznali kod [Lewisovog donorstva](04-organska.md#donorske-uloge). Elektrofil (*electrophile*) prima taj par; karbonilni C je elektronski osiromašen jer O privlači elektronsku gustinu veze C=O. „Nukleofilni napad“ ovde znači nastanak C–N veze uz pomeranje π-para C=O ka O, tako da C ne dobije pet veznih parova.

**Intermedijer** ili međuproizvod jeste vrsta koja nastaje u jednom koraku i troši se u sledećem. **Prenos protona** menja koji atom nosi H⁺, često uz pomoć rastvarača ili kiseline/baze; to nije prenos celog neutralnog H atoma. **Eliminacija** u ovom primeru uklanja malu molekulu vode iz međuproizvoda uz nastanak C=N veze.

### Jedna karbonilna grupa, od početka do imina

U sledećoj nastavnoj šemi R¹ i R² su grupe vezane za karbonilni C, a R³ je supstituent aminskog N. Svaka strelica može obuhvatiti više protonskih koraka:

```text
R¹–C(=O)–R² + H₂N:–R³
        ⇌ R¹–C(O⁻)(NH₂⁺–R³)–R²       nastaje C–N, π-par ide ka O
        ⇌ R¹–C(OH)(NH–R³)–R²         prenos protona: karbinolamin
        ⇌ [R¹–C(OH₂⁺)(NH–R³)–R²]    protonacija OH, priprema vode
        ⇌ [R¹–C(=NH⁺–R³)–R²] + H₂O  eliminacija: iminski N formira π-vezu
        ⇌ R¹–C(=N–R³)–R² + H⁺       deprotonovanje: imin
```

Treća strelica podrazumeva dodavanje H⁺ iz kiseline, a završna ga vraća; protonski donor i akceptor nisu posebno nacrtani. Šema ilustruje tok atoma i elektronskog para, a nije tvrdnja da svaka prikazana vrsta mora biti izdvojiva niti da su svi elementarni koraci isti u svakom rastvaraču. Karbinolaminski C je tetraedarski, za razliku od približno planarnog karbonilnog/iminskog C. Neto za jednu grupu ostaje `karbonil + primarni amin ⇌ imin + H₂O`, pa za dve grupe nastaju dve vode. [OpenStax mehanizam nastanka imina](https://openstax.org/books/organic-chemistry/pages/19-8-nucleophilic-addition-of-amines-imine-and-enamine-formation) razrađuje ulogu kiseline i povratne reakcije.

Reakcija je ravnotežna. Acid/base uslovi, voda, rastvarač, temperatura i stabilnost proizvoda mogu promeniti ishod. „Pomešali smo keton i amin“ nije dovoljan dokaz da je nastao čist bis-iminski ligand; identitet se potvrđuje analitikom i strukturom.

### Imine i Schiffove baze

IUPAC definiše **imine** kao jedinjenja sa motivom `RN=CR2`; aldehidni i ketonski analozi razlikuju se kao aldimini i ketimini ([imines](https://goldbook.iupac.org/terms/view/I02957)). **Schiffove baze** su imini kod kojih N nosi hidrokarbilnu grupu, `R2C=NR′`, uz `R′ ≠ H` ([Schiff bases](https://goldbook.iupac.org/terms/view/S05498)).

U našem DAP motivu svaki iminski C potiče od ketona i vezan je za `CH3` i piridinski kostur; zato su to ketiminske Schiff-base ruke kada iminski N nosi hidrokarbilni supstituent, kao arilnu grupu u CAPHAG-u. Samo prisustvo `C=N` i nekog organskog ostatka nije dovoljno za tu užu klasifikaciju: neposredno vezani N–N ili N–O supstituent traži razlikovanje hidrazonskog odnosno oksimskog tipa i pregled kompletne strukture.

## 6.3 CAPHAG kao konkretna reakcijska provera

Prvi `search1` pogodak, **CAPHAG**, ima formulu `C25 H27 N3` i SMILES:

```text
CCc1ccccc1N=C(C)c1cccc(n1)C(C)=Nc1ccccc1CC
```

On je konzistentan sa kondenzacijom 2,6-diacetilpiridina i dva ekvivalenta 2-etilanilina:

\[
\mathrm{C_9H_9NO_2} + 2\,\mathrm{C_8H_{11}N}
\rightarrow
\mathrm{C_{25}H_{27}N_3} + 2\,\mathrm{H_2O}.
\]

Provera atoma radi:

- C: `9 + 2×8 = 25`;
- N: `1 + 2×1 = 3`;
- O: dva karbonilna O odlaze u dve vode, pa ih nema u proizvodu;
- H: `9 + 2×11 − 2×2 = 27`.

Ovo je koristan sanity check, ali formula sama ne dokazuje povezivanje atoma. Graf/SMILES pokazuje dve `C=N` veze i centralni piridinski N; kristalna struktura ili drugi analitički dokaz potvrđuje konkretan identitet.

## 6.4 Zašto je N3 motiv dobar ligand

Tri azota imaju slobodne elektronske parove koji mogu biti donori:

| Donor | Gde se nalazi | Uloga u tipičnom N3 vezivanju |
|---|---|---|
| `N_imine,left` | leva `C=N–R` ruka | krajnji donor |
| `N_pyridine` | centralni heteroatom prstena | srednji donor |
| `N_imine,right` | desna `C=N–R′` ruka | krajnji donor |

Ako sva tri vežu isti metal, ligand je **tridentatno koordinisan**. Raspored 2,6-ruku preorganizuje donor-atome i obično omogućava dva helatna prstena. To često stabilizuje vezivanje, ali „potencijalno tridentatan“ i „u ovoj strukturi tridentatan“ nisu isti iskazi.

Donorska sposobnost može da se promeni kada:

- iminski ili piridinski N bude protonovan;
- dođe do tautomerije ili hemijske transformacije;
- konformacija okrene donor od metala;
- sterički glomazni `R` supstituenti zaklone džep;
- metal preferira drugi koordinacioni broj/geometriju;
- ligand koristi samo jedan ili dva N, premošćuje više metala ili ostane nekoordinisan;
- konkurentni anjoni/rastvarači zauzmu koordinaciona mesta.

<div class="project-link">
**Semantička posledica:** potencijalna tri donorska mesta liganda moraju se razlikovati od stvarno opažene dentatnosti i mapiranih M–N odnosa u konkretnom kompleksu. Jedna neobjašnjena etiketa „denticity = 3“ izgubila bi razliku između dizajna liganda i opažene strukture.
</div>

## 6.5 CAPHEK: kada se potencijalni džep zaista koristi

Prvi `search2` pogodak, **CAPHEK**, daje jasan pozitivan primer:

- formula celog entry-ja: `C27 H32 Cl2 N4 O Zn`;
- jedan DAP bis-iminski ligand koristi tri N donora;
- isti Zn vezuje i dva Cl donora;
- lokalni donor-sastav je `N3Cl2`, pa je `CN = 5`;
- Zn–N rastojanja su 2,081, 2,251 i 2,276 Å;
- Zn–Cl rastojanja su 2,241 i 2,254 Å;
- odvojeni acetonitril i voda objašnjavaju dodatni N i O u punoj formuli.

Zato formula ima četiri N, ali koordinacioni N3 džep čine tri N iz istog liganda. Četvrti N pripada acetonitrilu i nije automatski donor cinku. Ovo je praktičan dokaz zašto se koordinacioni broj ne izvodi iz elementarne formule.

Petokoordinisana geometrija CAPHEK-a nije idealna. Iz dva najveća ugla, 147,436° i 128,705°, dobija se `τ5 ≈ 0,312`: distordovana/intermedijarna okolina bliža kvadratno-piramidalnom kraju mere. Detaljno računanje je u [poglavlju 5](05-kompleksi.md#coordination-geometry).

## 6.6 Šta tačno kodira prvi ConQuest upit

Forenzičko čitanje fajla `1 - Sifove baze DAP.cqs` pokazuje jedan 2D connectivity query sa 18 eksplicitnih atoma:

| Deo query-ja | Broj / vrsta |
|---|---|
| elementi | 9 C, 3 N, 6 H |
| centralni prsten | 5 C + 1 N |
| prstenaste veze | 6 veza sa ConQuest kodom 5 |
| dvostruke `C=N` veze | 2, kod 2 |
| ostale query veze | 10 `Any`, kod 99 |
| režim | `exhaustive=1`, `symmchk=1` |

Dve ruke su na položajima 2 i 6 centralnog piridinskog prstena i svaka sadrži `ring-C–C(=N)–CH3` deo. Eksplicitnih šest H pripada dvema metil-grupama.

!!! note "Query graf nije hemijsko ime"
    Naziv fajla kaže „DAP Schiff bases“, ali izvršiva semantika je skup atomskih, veznih i opcionalnih constraints. Naučno tumačenje mora razlikovati ljudsku nameru od mašinskog query-ja. Kada se ne slažu, constraints opisuju šta je stvarno pretraženo, a nameru treba posebno potvrditi sa stručnim timom.

Prvi upit **ne zabranjuje metal**. On samo nema dodatni metalni uslov. Zato `search1` sadrži i metal-free ligande i entry-je sa metalima.

## 6.7 Drugi upit menja composition, ne koordinacionu vezu

Fajl `2 - Kompleksi sa DAP SB.cqs` sadrži isti 18-atomski povezani motiv i još jedan atom:

```text
AT19  4M
```

CCDC ConQuest vodič definiše `4M` kao zbir grupa `1M + 2M + TR + LN + AN`, pod nazivom „bilo koji metal“ ([ConQuest User Guide](https://www.ccdc.cam.ac.uk/media/Documentation/2F0D7443-9739-46EB-BE9F-69E62E531FB7/2f0d7443973946ebbe9f69e62e531fb7.pdf)). Ta legacy taksonomija preko `2M` uključuje i Ge i Sb; nije potpuno ista kao svaka školska podela na metale i metaloide. Atom 19 je u query objektu **nepovezan**: nema vezu, kontakt, distance constraint niti uslov da pripada istoj molekulskoj komponenti kao DAP motiv.

Tačna logika je:

\[
\text{search2} = \text{DAP motiv} \land \text{4M element negde u istom CSD entry-ju}.
\]

Netačna, jača interpretacija bila bi:

\[
\text{search2} = \text{DAP N3 ligand koordinisan metalu}.
\]

Lokalni izvozi to potvrđuju brojčano:

- `search1`: 2.110 rezultata;
- `search2`: 2.038 rezultata;
- `search2` je tačan podskup `search1` u istom redosledu nakon filtriranja;
- razlika od 72 entry-ja je deo `search1` bez `4M` elemenata, odnosno metal-free pod tom taksonomijom;
- svih 2.038 `search2` formula sadrži bar jedan `4M` element.

## 6.8 Kontraprimeri su važniji od lakih pozitivnih primera

Šest hemijski obrazloženih kontraprimera — APHZUC, FOWLEJ, GEHCOM, MINQUV, SUZBAT i UJIXES — dato je u [§5.8](05-kompleksi.md#58-kontraprimeri-metal-je-prisutan-ali-ciljna-koordinacija-nije-dokazana). Ovde je njihova posebna ML uloga da služe kao **hard negatives**: dele scaffold/composition signal sa pozitivima, ali padaju na presudnom M–N atom mapping-u.

!!! danger "SMILES tačka je signal, ne konačna presuda"
    Tačka u SMILES-u označava odvojene graf komponente u tom eksportu. Kod kristala ipak treba proveriti CIF koordinate, simetriju, periodične slike i provenance percepcije veza. Zaključak `not coordinated` treba da nosi dokaz i confidence, naročito kada je izvor lossy.

## 6.9 Evidence ladder za DAP i metal

Jedan boolean „jeste/nije kompleks“ skriva više različitih pitanja:

| Nivo dokaza | Pitanje |
|---|---|
| motiv | da li je mapirano 18-atomsko DAP query jezgro sa dve `C=N` veze prisutno? |
| sastav entry-ja | da li neki metal postoji bilo gde u entry-ju? |
| komponenta | da li metal i mapirani motiv pripadaju istoj hemijskoj komponenti? |
| lokalni kontakt | da li postoji hemijski/geometrijski podržan metal–N odnos? |
| donor mapping | da li isti metal vezuje baš mapirane DAP N atome i sa kojom dentatnošću? |
| okruženje | koji su CN, ostali donori, geometrija i neizvesnost? |
| dovoljnost prikaza | da li dostupni format i kvalitet uopšte dopuštaju odluku? |

Ovo je pojmovna lestvica dokaza, ne propisana label schema. Konačne positive/negative/ambiguous klase zahtevaju fakultetski odobrenu operativnu definiciju. APHZUC zato može biti kandidat na nivou scaffold-a, ali ne sme postati lažno pozitivan dokaz N3 koordinacije.

## 6.10 Varijacije koje model mora da očekuje

Jedan 2D scaffold može dati mnogo struktukturnih varijanti:

- `R = R′` ili nesimetrične ruke `R ≠ R′`;
- E/Z konfiguracije iminskih veza;
- različite konformacije i orijentacije aromatičnih supstituenata;
- neutralni ligand, protonovani oblik ili druga tautomerna/protonaciona stanja;
- jedan ili više metalnih centara;
- dodatni monodentatni ili polidentatni ligandi;
- koordinacioni polimeri, bridging i symmetry-generated veze;
- counterion-i, hidrati i solvatisane forme;
- disorder, parcijalna okupacija i zapisi bez punih koordinata.

To objašnjava zašto „isti DAP motiv“ nije isto što i „ista molekulska struktura“, „isti koordinacioni kompleks“ ili „ista kristalna forma“.

## 6.11 Moguće ose relevantne za dve aplikacije

### Aplikacija 1 — globalna pretraga

Potencijalne, međusobno različite search semantike uključuju:

- isti/sličan DAP scaffold;
- DAP scaffold + metal bilo gde u entry-ju;
- DAP ligand i metal u istoj komponenti;
- koordinacija preko najmanje jednog mapiranog N;
- N3 koordinacija istom metalu;
- slična koordinaciona geometrija i donor-okruženje.

One nisu unapred odobreni product modovi; njihov scope nije utvrđen dostupnim izvorima i mora ga potvrditi fakultet. Svaki stroži nivo može biti podskup prethodnog samo ako su podaci dovoljni. Zapis bez 3D ili pouzdane konektivnosti ostavlja nepoznat odgovor na odgovarajuću osu, umesto da postane lažno negativan.

### Aplikacija 2 — poređenje parova

Za dva ulazna CIF-a stručna analiza može da razdvoji:

- poklapanje 2D DAP podgrafa i njegov atom mapping;
- identitet/protonaciju/supstitucije liganda;
- koji mapirani N atomi koordiniraju koji metal;
- observed denticity i M–N distance;
- CN, ostale donore i geometriju metala;
- razliku kristalne forme, packing-a, solvata i disorder-a.

Visok ligand-similarity score uz različitu koordinaciju nije greška — to su dve različite ose sličnosti. Koje od njih treba uključiti ostaje nepotvrđena projektna odluka, ne zaključak ove lekcije.

## 6.12 Mini-vežbe

### 1. Reakcijska stehiometrija

Koliko molekula vode idealno nastaje kada 2,6-diacetilpiridin sa dve karbonilne grupe potpuno reaguje sa dva primarna amina do bis-imina?

??? success "Odgovor"
    Dva. Svaka karbonilna grupa daje jednu iminsku vezu i jednu molekulu vode u idealizovanoj kondenzaciji.

### 2. Potencijalno naspram opaženog

Ligand ima piridinski N i dva iminska N, ali u kristalu samo jedan iminski N vezuje metal. Koji je njegov potencijalni, a koji opaženi denticitet?

??? success "Odgovor"
    Potencijalno je tridentatan za taj N3 donorski set, ali je u konkretnoj strukturi monodentatno koordinisan. Potrebno je sačuvati oba podatka.

### 3. Query logika

Zašto 2.038 rezultata drugog upita nisu automatski 2.038 potvrđena DAP kompleksa?

??? success "Odgovor"
    Dodatni `4M` atom nema vezu ni geometrijski constraint prema DAP motivu. Upit traži motiv i metal u istom entry-ju, ne njihovu međusobnu koordinaciju.

### 4. CAPHAG i CAPHEK

Koji od ova dva lokalna primera je slobodni ligand, a koji potvrđen N3 kompleks?

??? success "Odgovor"
    CAPHAG je metal-free DAP bis-iminski ligand. CAPHEK sadrži Zn u N3Cl2 okolini; tri N iz DAP liganda vezuju isti Zn.

### 5. Hard negative

Zašto je SUZBAT bolji test modela od nasumičnog ugljovodonika bez N i metala?

??? success "Odgovor"
    SUZBAT prolazi široki DAP+metal query i zato deli relevantan scaffold/composition signal, ali Fe nije u ciljnom DAP–N3 okruženju. Model mora naučiti presudnu koordinacionu razliku, ne trivijalno odsustvo motiva.

### 6. Nedovoljni podaci

SMILES sadrži DAP motiv i metal u odvojenoj komponenti, a nemaš CIF koordinate. Koju etiketu daješ?

??? success "Odgovor"
    Možeš pouzdano označiti metal presence i odvojene komponente u toj reprezentaciji, ali ne treba izmišljati kristalografski contact zaključak. Za koordinaciju koristi `not shown in exported graph` ili `ambiguous/insufficient`, zavisno od ugovorenog annotation pravila.

## 6.13 Kriterijum prolaza

Poglavlje si savladao kada možeš da nacrtaš 2,6-diacetilpiridinski bis-iminski motiv, objasniš nastanak dve `C=N` veze, mapiraš N3 donorski set i napišeš test koji razlikuje:

```text
DAP motiv + metal presence
od
isti metal direktno koordinisan mapiranim DAP N atomima.
```

## Primarni i autoritativni izvori

- [IUPAC Gold Book: imines](https://goldbook.iupac.org/terms/view/I02957)
- [IUPAC Gold Book: Schiff bases](https://goldbook.iupac.org/terms/view/S05498)
- [IUPAC Gold Book: denticity](https://goldbook.iupac.org/terms/view/D01594)
- [IUPAC Gold Book: chelation](https://doi.org/10.1351/goldbook.C01012)
- [CCDC ConQuest User Guide and Tutorials](https://www.ccdc.cam.ac.uk/media/Documentation/2F0D7443-9739-46EB-BE9F-69E62E531FB7/2f0d7443973946ebbe9f69e62e531fb7.pdf)
- [CCDC Python API: substructure searching](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/substructure_searching.html)
- [OpenStax Organic Chemistry: imine formation from aldehydes and ketones](https://openstax.org/books/organic-chemistry/pages/19-8-nucleophilic-addition-of-amines-imine-and-enamine-formation)
