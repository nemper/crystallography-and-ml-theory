# 4. Organska hemija koja nam treba

**Prioritet: MORAŠ, selektivno.** Ne učimo katalog reakcija. Učimo da prepoznamo hemijsko okruženje koje određuje graf, koordinaciju, interakcije i standardizaciju.

## 4.1 Ugljenični skelet i funkcionalne grupe

**Funkcionalna grupa** je lokalni raspored atoma sa prepoznatljivim hemijskim ponašanjem. Za projekat su najvažnije:

| Grupa/motiv | Prepoznavanje | Zašto je važno |
|---|---|---|
| alkane/alkyl | pretežno C-C/C-H single veze | fleksibilnost, disperzija, rotatable bonds |
| alkene/alkyne | C=C / C≡C | rigidnost, geometrija, stereokemija |
| arene | aromatični karbociklus | planarnost, delokalizacija, π kontakti |
| heteroarene | aromatični prsten sa N/O/S | donor/acceptor svojstva; npr. pyridine N |
| alcohol/phenol | O-H | H-bond donor i često acceptor; acid-base kontekst |
| ether | C-O-C | acceptor, fleksibilnost |
| carbonyl | C=O | jak dipol; acceptor; osnova aldehida/ketona |
| carboxylic acid/carboxylate | COOH / COO⁻ | protonacija, soli, rezonanca, snažne mreže |
| ester/amide | C(=O)O / C(=O)N | rezonanca menja bazičnost i rotacionu rigidnost; neutralni amide N obično nije H-bond acceptor niti tipičan metalni donor, ali N-H može biti H-bond donor; carbonyl O je acceptor |
| amine | N sa single vezama/lone pair | baza i ligand, osim kada je lone pair delokalizovan/protonovan |
| imine | C=N | DAP Schiff-base motiv; geometrija i N donor |
| nitro | vezani \(\mathrm{NO_2}\) rezonantni sistem | formalni naboji, približno jednake N-O veze, jak polarni motiv |
| halogen | C-F/Cl/Br/I ili halidni jon | veličina, polarizabilnost, anion/ligand, halogen bonding |
| phosphine/phosphoryl motivi | P sa organskim/O susedima | promenljiva valenca, ligand/dipol; zahteva tačno tipovanje |

[OpenStax Organic Chemistry: functional groups](https://openstax.org/books/organic-chemistry/pages/3-1-functional-groups) je dobar vizuelni atlas. Za projekat je dovoljno da grupu prepoznaš i navedeš tip veze, tipičan naboj/protonaciju i moguću donor/acceptor ulogu.

## 4.2 DAP Schiff-base motiv

Iz prvog lokalnog CSD zapisa, `CAPHAG`, sistematsko ime opisuje pyridine-2,6-diyl jezgro sa dve imine grane. Dostavljeni ConQuest upit kodira 18-atomsku podstrukturu sa:

- centralnim šestočlanim pyridine prstenom;
- jednim prstenskim N donorom;
- dve bočne `C=N` jedinice;
- promenljivim terminalnim supstituentima.

Takav tridentatni N-donor raspored može koordinisati metal, ali prisustvo motiva samo po sebi ne dokazuje koordinaciju. Zato `search1` traži motiv, dok `search2` dodaje odvojeni `4M` atom-uslov za prisustvo člana ConQuest grupe „bilo koji metal“, čija taksonomija uključuje i Ge i Sb. Čak i tada treba proveriti da li je taj centar zaista povezan sa tri donor-atoma; "u istom kristalnom zapisu" nije isto što i "koordinisan ovim ligandom".

## 4.3 Kiselina i baza: dva modela koja nam trebaju

### Brønsted-Lowry

- kiselina donira proton \(\mathrm{H^+}\);
- baza prima proton.

### Lewis

- Lewisova baza donira elektronski par;
- Lewisova kiselina prima elektronski par.

Ligandni N sa lone pair može biti Lewisova baza prema metalnom centru. Ako je protonovan, lone pair može postati nedostupan za koordinaciju. Acid-base stanje zato menja graf, charge, donor/acceptor etikete, soli i kristalno pakovanje.

[OpenStax: Brønsted-Lowry](https://openstax.org/books/chemistry-2e/pages/14-1-bronsted-lowry-acids-and-bases) i [Lewis acids/bases i kompleksi](https://openstax.org/books/chemistry-2e/pages/15-2-lewis-acids-and-bases) su dovoljni izvori za ovaj nivo.

!!! warning "pH nije osobina izolovanog CIF-a"
    pH opisuje rastvor i zavisi od uslova. CIF solidne forme može pokazati protonovanu vrstu i counterion, ali iz samog 3D modela ne treba izmišljati pH kristalizacije.

## 4.4 Tautomeri, protonacija i soli

**Protonaciona stanja** se razlikuju položajem/brojem protona i neto nabojem.
**Tautomeri** su konstitucioni izomeri povezani formalnim premeštanjem protona
i \(\pi\)-veze, npr. keto/enol. Njihova interkonverzija nije univerzalno brza:
brzina i ravnoteža zavise od barijere, rastvarača, pH, katalizatora i
temperature. U čvrstom stanju kristalna rešetka može stabilizovati jedan
tautomer, ograničiti prenos protona ili zahtevati faznu transformaciju, pa se
ne sme automatski pretpostaviti brza tautomerna ravnoteža. U digitalnim bazama
dva validna zapisa mogu izgledati kao različiti grafovi iako ih hemičar za
određenu namenu grupiše.

Standardizacija mora odvojeno evidentirati:

1. originalnu eksperimentalnu formu;
2. fragmentisane komponente (glavna jedinka, counterion, solvent);
3. odabranu parent reprezentaciju za određenu pretragu;
4. tautomer/protomer policy;
5. sve transformacije i upozorenja.

Ne postoji univerzalno ispravno "neutralize everything" pravilo. Za pretragu ligandskog scaffold-a neutralni parent može pomoći; za solid-form i koordinacionu sličnost uklanjanje naboja/counteriona može uništiti suštinu.

## 4.5 Aromatičnost i heteroatomi

Pyridine N i pyrrole N su oba u aromatičnom prstenu, ali lone pair nema istu ulogu:

- pyridine-tip lone pair ne pripada aromatičnom \(\pi\) sekstetu i tipično može biti baza/metal donor;
- pyrrole-tip lone pair doprinosi aromatičnosti i mnogo je manje raspoloživ na isti način.

Zato atom-label "N.ar" sam bez hemijskog okruženja nije dovoljan za donor/acceptor klasifikaciju. SMARTS/feature definicije moraju biti verzionisane i testirane.

## 4.6 Konjugacija, planarnost i rotatable bonds

Naivno pravilo "svaka single veza je rotatable" nije tačno. Amide C-N ima parcijalni double-bond karakter zbog rezonance i obično je mnogo rigidniji. Ista delokalizacija čini neutralni amide N slabom Lewisovom bazom: on obično nije H-bond acceptor niti tipičan metalni donor, iako N-H može donirati H-vezu. Deprotonovani amid i posebna koordinaciona okruženja su izuzeci; carbonyl O ostaje uobičajeno acceptorsko/koordinaciono mesto. Veze u prstenu, terminalne veze i veze prema metalima zahtevaju posebne definicije.

Broj rotatable bonds iz white paper-a je koristan deskriptor fleksibilnosti, ali vrednost zavisi od implementacione definicije. U modelu čuvaj naziv alata, verziju i parametre.

## 4.7 Stereokemija kao podatak, ne ukras

Obavezno razlikuj:

- specifikovanu stereokemiju;
- nepoznatu/neodređenu stereokemiju;
- racemat;
- jednu izolovanu enantiomernu formu;
- stereoinformaciju izgubljenu konverzijom.

Canonical SMILES može grupisati samo ono što je zapisano njegovim stereooznakama i pravilima. U CSD familijama potrebni su struktura, stereokemija, solid-form kontekst i ekspertna kuracija; jedna string-kolona nije ground truth.

## 4.8 Posledice za aplikacije

<div class="project-link">
**Filteri:** elementi i formula se dopunjuju functional-group/substructure filterima. DAP motiv je eksplicitni podgraf; "metal complex" zahteva proveru metal-ligand povezanosti/okruženja, ne samo metal u formuli.

**Feature-i:** broj donora, acceptora, rotatable bonds, aromatic rings i formal charge su korisni samo uz dokumentovanu protonation/aromaticity policy.

**Objašnjenje rezultata:** prikaži koji se scaffold/funkcionalne grupe poklapaju, a ne samo fingerprint score.
</div>

## 4.9 Provera znanja

1. Zašto imine N može biti relevantan metalni donor?
2. Da li svaki N atom prihvata H-vezu i koordinira metal?
3. Zašto uklanjanje counterion-a može pomoći jednoj, a pokvariti drugu pretragu?
4. Da li su dva tautomera isti graf?
5. Zašto "broj rotatable bonds" mora imati verzionisanu definiciju?

??? success "Odgovori"
    1. Ima lone pair koji može donirati metalnom centru, u zavisnosti od protonacije i okruženja.  
    2. Ne. Dostupnost lone pair-a, naboj, rezonanca/aromatičnost i geometrija određuju ulogu.  
    3. Parent-scaffold pretraga želi ignorisati različite soli; solid-form pretraga mora sačuvati sastav i jonske interakcije.  
    4. Ne nužno: premeštanje H i double veze menja formalni graf, iako ih neka standardizacija grupiše.  
    5. Različiti alati drugačije tretiraju amide, ring bonds, terminalne i metalne veze.

**Kriterijum prolaza:** na lokalnom DAP pogotku označi pyridine, dve `C=N` jedinice, tri potencijalna N donor-atoma, terminalne supstituente, moguće protonacione tačke i veze čija rotacija menja konformaciju.
