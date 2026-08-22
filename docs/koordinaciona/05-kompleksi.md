# 5. Metali, ligandi i kompleksi

**Prioritet: MORAŠ.** Ako ovo poglavlje savladaš, moći ćeš da razlikuješ zapis koji samo sadrži metal od stvarnog koordinacionog kompleksa i da pravilno čitaš lokalno okruženje metala. To je osnovna hemijska kontrola za obe 2CDC aplikacije.

## 5.1 Četiri ideje koje ne smeju da se pomešaju

Koordinaciona hemija proučava **centralni atom ili jon**, najčešće metal, i atome ili grupe koji su za njega neposredno vezani. Ti partneri su **ligandi**, a atom liganda koji se neposredno vezuje za metal je **donor-atom**.

Na početnom nivou koristan je Lewisov model:

```text
ligand sa slobodnim elektronskim parom  +  metalni centar sa dostupnom orbitalom
                  Lewisova baza         +            Lewisova kiselina
                                      ↓
                              koordinaciona veza
```

Na primer, azot može da donira slobodni elektronski par cinku. Strelica `N → Zn` opisuje poreklo elektronskog para pri nastanku veze. Kada je veza nastala, ona nije neka posebna „slabija vrsta crte“: njena priroda može imati jonski i kovalentni doprinos, a način crtanja je model i konvencija. IUPAC zato naglašava da poreklo elektrona samo po sebi ne određuje karakter konačne veze ([coordination](https://goldbook.iupac.org/terms/view/C01329)).

Četiri nivoa dokaza su različita:

| Tvrdnja | Šta je potrebno da bi bila opravdana |
|---|---|
| „U entry-ju postoji metal“ | metal se javlja u formuli ili među atomima |
| „Metal ima susede“ | postoji eksplicitna ili pouzdano izvedena koordinaciona okolina |
| „Metal je vezan za neki azot“ | konkretna M–N veza ili geometrijski potvrđen kontakt |
| „DAP Schiff-base ligand koordinira metal preko N3 džepa“ | mapirana su baš tri ciljna DAP azota i potvrđena njihova veza sa istim metalom |

<div class="project-link">
**Projektna posledica:** filter „metal prisutan“ ne sme u korisničkom interfejsu da bude nazvan „metal koordinisan ligandu“. To su različite operacije nad različitim slojevima podataka.
</div>

## 5.2 Koordinaciona jedinka nije isto što i ceo kristalni zapis

Kristalni zapis može da sadrži više od jedne hemijske komponente:

- koordinacionu jedinku, na primer neutralni kompleks ili kompleksni jon;
- protivjone potrebne za ravnotežu naelektrisanja;
- molekule rastvarača ili vode;
- koformere i više nezavisnih molekula;
- delove polimernog lanca ili disorder alternative.

Zato su sledeći prikazi povezani, ali nisu sinonimi:

```text
CSD entry
├── puna formula i kristalno pakovanje
├── koordinaciona jedinka: metal + neposredno vezani ligandi
├── odvojeni protivjoni
└── solvatisani molekuli / druge komponente
```

Ako formula sadrži Fe, ne sledi da je Fe vezan za ciljnu organsku komponentu. Ako graf ima dve odvojene komponente, metal može biti u drugoj komponenti. Čak i kada su svi atomi nacrtani u jednom CIF bloku, component assignment i koordinacione veze mogu ostati neizvesni.

## 5.3 Lokalni dokaz: CAPHAG i CAPHEK

Dva prva zapisa iz dostavljenih pretraga daju dobar par za učenje.

### CAPHAG — slobodni organski ligand

Lokalni eksport za **CAPHAG** daje formulu `C25 H27 N3`, 55 atoma i 57 veza kada se računaju eksplicitni vodonici u eksportovanom molekulskom zapisu. Njegov SMILES je:

```text
CCc1ccccc1N=C(C)c1cccc(n1)C(C)=Nc1ccccc1CC
```

U strukturi postoje tri relevantna azota: jedan piridinski i dva iminska. Oni grade **potencijalni N3 donorski džep**, ali nema metalnog atoma. Zbog toga CAPHAG jeste DAP-derived bis(imine) ligand, ali nije metalni kompleks.

### CAPHEK — N3Cl2 okruženje cinka

Za **CAPHEK** lokalni CIF navodi formulu `C27 H32 Cl2 N4 O Zn`. U koordinacionoj jedinki jedan Zn ima pet neposrednih suseda:

| Veza | Lokalno rastojanje / Å |
|---|---:|
| Zn–N | 2,081 |
| Zn–N | 2,251 |
| Zn–N | 2,276 |
| Zn–Cl | 2,241 |
| Zn–Cl | 2,254 |

Donor-sastav je zato `N3Cl2`, a koordinacioni broj cinka je 5. Eksport takođe sadrži odvojene molekule acetonitrila i vode. Njihovo prisustvo u istoj kristalnoj formuli ne znači automatski da su koordinisani cinku.

!!! example "Jedna rečenica, tri nivoa"
    „CAPHEK sadrži Zn“ je composition tvrdnja. „Zn ima N3Cl2 okolinu“ je coordination tvrdnja. „Sva tri N pripadaju istom DAP bis-iminskom ligandu“ zahteva atom mapping ciljnih N atoma. Lokalni zapis podržava sva tri nivoa za CAPHEK, ali sistem mora da ih proverava zasebnim testovima.

## 5.4 Koordinacioni broj: broje se donor-atomi, ne molekuli

**Koordinacioni broj (CN)** centralnog atoma u koordinacionoj jedinki jeste broj njegovih direktno vezanih donor-atoma; IUPAC-ova precizna definicija govori o broju ligand–centralni atom σ-veza ([coordination number](https://goldbook.iupac.org/terms/view/C01331)).

Primeri:

- četiri monodentatna liganda, svaki preko jednog atoma, mogu dati `CN = 4`;
- dva bidentatna liganda mogu takođe dati `CN = 4`;
- jedan tridentatni DAP ligand i dva monodentatna hlorido liganda daju `CN = 3 + 1 + 1 = 5`, kao u CAPHEK;
- broj liganada i koordinacioni broj zato nisu ista veličina.

### Šta lokalni eksport pokazuje

U `search2` ima 2.038 entry-ja, ali samo 1.954 imaju eksportovane atomske koordinate/graf dovoljan za ovu lokalnu analizu. U njima je nađeno 4.070 centara čiji elementi pripadaju ConQuest grupi `4M`. CCDC-ova legacy taksonomija u `4M` uključuje i Ge i Sb preko grupe `2M`, pa ovu operativnu selekciju ne treba neopaženo zameniti školskom podelom na „metale“ i „metaloide“ ([ConQuest User Guide](https://www.ccdc.cam.ac.uk/media/Documentation/2F0D7443-9739-46EB-BE9F-69E62E531FB7/2f0d7443973946ebbe9f69e62e531fb7.pdf)). Za svaki takav centar CN ispod je samo broj incidentnih bond records u eksportovanom MOL2 grafu:

| MOL2 graph degree („CN“) | Broj 4M centara | Udeo |
|---:|---:|---:|
| 0 | 8 | 0,2% |
| 1 | 221 | 5,4% |
| 2 | 32 | 0,8% |
| 3 | 9 | 0,2% |
| 4 | 390 | 9,6% |
| 5 | 831 | 20,4% |
| 6 | 1.187 | 29,2% |
| 7 | 975 | 24,0% |
| 8 | 158 | 3,9% |
| 9 | 136 | 3,3% |
| 10 | 100 | 2,5% |
| 11–15 | 23 | 0,6% |

!!! warning "Ovo nisu apsolutne hemijske istine"
    Tabela je forenzika jednog eksportovanog grafa, ne referentna raspodela CSD-a. MOL2 može propustiti symmetry-generated veze, pojednostaviti metal–ligand vezivanje ili nezgodno predstaviti hapticitet, disorder i polimere. `CN = 0` u eksportu znači „nema suseda u ovom grafu“, ne „dokazano izolovan goli metalni jon“.

Najčešći neposredni tipovi suseda u istom grafu bili su N (12.041 metal–N ivica), O (6.307), C (2.647), Cl (1.635), S (461), Br (162), F (122), P (117) i I (58). Jedan metal može doprineti više ivica i više tipova, pa ovo nisu brojevi entry-ja.

## 5.5 Koordinacioni broj ne određuje sam geometriju {#coordination-geometry}

**Koordinaciona geometrija** opisuje prostorni raspored donor-atoma oko centra. Isti CN može imati različite geometrije:

| CN | Česti idealizovani modeli | Šta moraš proveriti |
|---:|---|---|
| 2 | linearna, savijena | ugao D–M–D |
| 3 | trigonalno-planarna, trigonalno-piramidalna | planarnost i uglovi |
| 4 | tetraedarska, kvadratno-planarna | uglovi, dijagonale i elektronska konfiguracija |
| 5 | kvadratno-piramidalna, trigonalno-bipiramidalna | dva najveća ugla i continuous-shape mera |
| 6 | oktaedarska, trigonalno-prizmatična, distorzije | trans/cis uglovi i raspored lica |
| 7+ | više mogućih poliedara | puna 3D analiza; naziv iz CN nije dovoljan |

Realni kompleksi su skoro uvek distordovani: veze nisu identične, helatni prstenovi ograničavaju uglove, a packing i dodatni ligandi pomeraju idealne pozicije.

### CAPHEK i mera τ₅

Za petokoordinisani centar korisna je Addisonova mera:

\[
\tau_5 = \frac{\beta-\alpha}{60^\circ},
\]

gde su \(\beta\) i \(\alpha\) dva najveća ugla oko metala. Idealna kvadratna piramida ima \(\tau_5=0\), a idealna trigonalna bipiramida \(\tau_5=1\).

Za lokalni CAPHEK dva najveća ugla su 147,436° i 128,705°:

\[
\tau_5 = \frac{147{,}436-128{,}705}{60} \approx 0{,}312.
\]

To je distordovana/intermedijarna petokoordinaciona geometrija, bliža kvadratno-piramidalnom kraju mere nego trigonalno-bipiramidalnom. Ne treba je proglasiti idealnom geometrijom samo na osnovu `CN = 5`.

<div class="project-link">
**Za model:** čuvaj sirove M–D distance i D–M–D uglove, mapping atoma, CN i verzionisanu geometrijsku meru. Tekstualna etiketa „square pyramidal“ je izvedena i može biti neizvesna.
</div>

## 5.6 Denticitet i helatacija

**Denticitet** je broj donor-grupa jednog liganda koje su vezane za isti centralni atom ([IUPAC](https://goldbook.iupac.org/terms/view/D01594)).

| Denticitet | Naziv | Minimalni primer |
|---:|---|---|
| 1 | monodentatan | jedan `Cl⁻` preko jednog Cl atoma |
| 2 | bidentatan | ligand sa dva N koja se oba vezuju za isti metal |
| 3 | tridentatan | DAP bis-imine preko `N_imine–N_pyridine–N_imine` |
| 4+ | tetra-/polidentatan | četiri ili više donor-mesta istog liganda |

Kada najmanje dva odvojena donor-mesta **istog** liganda vežu isti centralni atom, nastaje **helat**; proces ili prisustvo takvog vezivanja zove se **helatacija** ([IUPAC](https://doi.org/10.1351/goldbook.C01012)). DAP-derived N3 vezivanje obično zatvara dva helatna prstena oko istog metala.

Važne nijanse:

- `potencijalno tridentatan` opisuje raspoloživa donor-mesta u ligandu;
- `tridentatno koordinisan` opisuje ono što se stvarno vidi u konkretnom kompleksu;
- isti ligand u drugom kristalu može biti mono-, bi-, tridentatan, protonovan, premošćujući ili potpuno nekoordinisan;
- helatni efekat je termodinamička tendencija, ne pravilo da svaki polidentatni ligand u svakoj situaciji mora koristiti sva mesta.

## 5.7 Formalno naelektrisanje, ukupni naboj i oksidaciono stanje

Ova tri pojma rešavaju različite računovodstvene probleme.

### Formalno naelektrisanje atoma

Formalno naelektrisanje pripada atomu u izabranoj Lewisovoj strukturi. Pretpostavlja ravnopravno deljenje veznih elektrona bez obzira na elektronegativnost ([IUPAC formal charge](https://goldbook.iupac.org/terms/view/08169)):

\[
q_\mathrm{formal}=N_\mathrm{valentnih}-N_\mathrm{neveznih}-\frac{1}{2}N_\mathrm{veznih\ elektrona}.
\]

To nije izmereno parcijalno naelektrisanje i može zavisiti od rezonantnog zapisa.

### Ukupni naboj komponente ili koordinacione jedinke

Ukupni naboj je zbir formalnih naboja u toj jedinici. Ceo kristal mora zadovoljiti ravnotežu naboja, ali pojedina komponenta može biti jon. Protivjon može biti odvojen tačkom u SMILES-u ili zasebnim fragmentom u grafu.

### Oksidaciono stanje

Oksidaciono stanje je formalni model raspodele elektrona posle jonske aproksimacije heteronuklearnih veza, a ne eksperimentalno parcijalno naelektrisanje metala ([IUPAC oxidation state](https://goldbook.iupac.org/terms/view/O04365)). Na početnom nivou često se određuje iz bilansa:

\[
\mathrm{OS(M)} + \sum q_\mathrm{liganada} = q_\mathrm{koordinacione\ jedinke}.
\]

Za neutralnu koordinacionu jedinku CAPHEK-a, ako je DAP Schiff-base ligand neutralan, a dva hlorido liganda su svaki `−1`, bilans daje:

\[
x + 0 + 2(-1)=0 \Rightarrow x=+2,
\]

pa se cink opisuje kao Zn(II). Acetonitril i voda u odvojenim komponentama su neutralni i ne menjaju taj bilans.

!!! danger "Ne čitaj oksidaciono stanje iz MOL2 charge kolone"
    `USER_CHARGES`, `NO_CHARGES`, `M  CHG` ili formalni naboj u eksportovanom SMILES-u opisuju konkretnu reprezentacionu šemu. Oni nisu automatski oksidaciona stanja. U lokalnom APHZUC SMILES-u uranijumski fragment čak nosi reprezentacioni zapis koji se ne sme doslovno prevesti u oksidaciono stanje bez hemijskog bilansa i provere strukture.

## 5.8 Kontraprimeri: metal je prisutan, ali ciljna koordinacija nije dokazana

Drugi lokalni ConQuest upit zahteva DAP motiv i nepovezan atom grupe `4M` — bilo koji metal. Zato prolaze i entry-ji u kojima je metal u odvojenoj komponenti.

| Refcode | Šta lokalni eksport pokazuje | Zašto nije dovoljan pozitivan N3 primer |
|---|---|---|
| APHZUC | protonovani organski ligand, odvojen U/O/Cl fragment i acetonitril | nema metal–N ivice do ciljnog liganda |
| FOWLEJ | DAP motiv i zaseban Cd/Cl metalatni fragment | metal presence, ne DAP coordination |
| GEHCOM | organska komponenta i zaseban Sn/Cl fragment | isto |
| MINQUV | ligand i odvojena Cu/Cl komponenta | Cu u entry-ju nije isto što i Cu–DAP veza |
| SUZBAT | Fe je u organometalnom C okruženju | metal je vezan, ali ne za ciljna DAP N mesta |
| UJIXES | ligand i zaseban `[Mn+2]` fragment | nepovezan Mn nije koordinisan DAP ligandu |

Među 1.954 `search2` zapisa sa koordinatama/grafom:

- 6 nema nijednu metal–N ivicu u eksportovanom grafu;
- 35 nema nijedan metal sa najmanje tri N suseda;
- 1.919 ima bar jedan metal sa najmanje tri N suseda, ali ni to samo po sebi ne dokazuje da su baš ta tri N mapirana na ciljni DAP motiv.

Pravi pozitivni kriterijum zato izgleda ovako:

```text
nađi DAP podgraf i njegovo mapiranje atoma
→ identifikuj tri ciljna N donor-atoma
→ nađi metal u istoj relevantnoj komponenti
→ potvrdi M–N veze ili validirane distance uz PBC/simetriju
→ proveri da sva tri N vezuju isti metal
→ prijavi denticitet, CN, druge donore i confidence
```

## 5.9 Kako reprezentacija može da promeni odgovor

U organskim molekulima bond order je često dovoljno stabilan za graf. Kod kompleksa postoje dodatne zamke:

- CIF može imati koordinate, ali ne eksplicitne hemijske veze;
- MOL2/SDF eksport može dodeliti veze po pravilima konkretnog alata;
- metal–ligand bond order često nije običan celobrojni fizički red veze;
- veze kroz granicu ćelije zahtevaju symmetry i periodične slike;
- hapticity, na primer vezivanje metala za više atoma π-sistema, ne staje uredno u jednostavno „broj crta“ pravilo;
- disorder i parcijalna okupacija mogu dati alternativne lokalne okoline.

Zato svaki izvedeni koordinacioni graf treba da nosi:

1. izvor veze: eksplicitna, CSD-kurirana, symmetry-generated ili distance-inferred;
2. pravilo, verziju i pragove;
3. confidence i upozorenja;
4. originalne koordinate i mapiranje atoma;
5. mogućnost `unknown/ambiguous`, a ne prinudnu etiketu.

## 5.10 Mini-vežbe

### 1. Brojanje

Kompleks ima jedan tridentatni N3 ligand, jedan bidentatni O2 ligand i jedan monodentatni Cl ligand. Koliko liganada i koliki CN ima metal?

??? success "Odgovor"
    Tri liganda, ali `CN = 3 + 2 + 1 = 6`. Broj molekula/grupa oko metala nije isto što i broj donor-atoma.

### 2. CAPHEK

Zašto iz formule `C27 H32 Cl2 N4 O Zn` ne možeš samo brojanjem elemenata dobiti `CN = 5`?

??? success "Odgovor"
    Formula ne kodira koje su veze prisutne ni koje komponente su odvojene. CN=5 dolazi iz lokalne okoline Zn: tri neposredno vezana N i dva Cl. Jedan dodatni N pripada odvojenom acetonitrilu, a O vodi; oni nisu automatski koordinisani.

### 3. Dve petokoordinisane strukture

Dva kompleksa imaju `CN = 5`. Da li imaju istu geometriju?

??? success "Odgovor"
    Ne nužno. Jedan može biti bliži kvadratnoj piramidi, drugi trigonalnoj bipiramidi, a oba mogu biti snažno distordovana. Potrebni su 3D uglovi/distance i odgovarajuća mera, ne samo CN.

### 4. Presence naspram coordination

Upit traži ciljni organski podgraf i nepovezan metalni atom. Da li su svi pogoci koordinacioni kompleksi tog liganda?

??? success "Odgovor"
    Ne. Dokazano je samo supostojanje motiva i metala u istom entry-ju. APHZUC, FOWLEJ, GEHCOM, MINQUV, SUZBAT i UJIXES pokazuju različite načine na koje ta pretpostavka može da padne.

### 5. Naboj

MOL2 kolona za metal ima vrednost `+2.0`. Da li je to dovoljan dokaz da je oksidaciono stanje M(II)?

??? success "Odgovor"
    Ne. To može biti formalni ili modelom dodeljen atom charge. Oksidaciono stanje se određuje hemijskim electron-counting pravilima i bilansom celog koordinacionog entiteta, uz proveru identiteta liganada i njihovih naboja.

## 5.11 Kriterijum prolaza

Poglavlje si savladao kada za proizvoljan zapis možeš da:

- odvojiš ceo entry, koordinacionu jedinku, protivjone i solvatisane komponente;
- navedeš metal, neposredne donore, CN, denticitet i moguću geometriju;
- pokažeš dokaz za svaku M–donor vezu i prijaviš neizvesnost;
- odvojeno izračunaš formalne naboje, ukupni naboj i oksidaciono stanje;
- objasniš zašto metal presence nije DAP coordination ground truth.

## Primarni i autoritativni izvori

- [IUPAC Gold Book: coordination](https://goldbook.iupac.org/terms/view/C01329)
- [IUPAC Gold Book: ligand](https://goldbook.iupac.org/terms/view/L03518)
- [IUPAC Gold Book: coordination number](https://goldbook.iupac.org/terms/view/C01331)
- [IUPAC Gold Book: denticity](https://goldbook.iupac.org/terms/view/D01594)
- [IUPAC Gold Book: chelation](https://doi.org/10.1351/goldbook.C01012)
- [IUPAC Gold Book: formal charge](https://goldbook.iupac.org/terms/view/08169)
- [IUPAC Gold Book: oxidation state](https://goldbook.iupac.org/terms/view/O04365)
- [OpenStax Chemistry 2e: Coordination Chemistry of Transition Metals](https://openstax.org/books/chemistry-2e/pages/19-2-coordination-chemistry-of-transition-metals)
