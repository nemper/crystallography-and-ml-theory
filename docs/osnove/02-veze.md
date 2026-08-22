# 2. Elektroni i hemijske veze

**Prioritet: MORAŠ.** Softver ne vidi "hemiju" direktno. On vidi elemente, koordinate i dodeljene veze; kvalitet tih dodela određuje graf, podstrukturnu pretragu i fingerprint.

## 2.1 Minimalni model elektrona

Za ovaj projekat dovoljno je sledeće:

- elektroni zauzimaju kvantna stanja/orbitale, ne kružne putanje kao planete;
- spoljašnji, valentni elektroni dominantno određuju uobičajene veze;
- atomi dele ili formalno prenose elektrone da bi formirali stabilnije celine;
- elektronska gustina je kontinuirana, dok su red veze i formalni naboj diskretni modeli.

**Elektronegativnost** opisuje sklonost vezanog atoma da privlači elektronsku gustinu. Razlika može dati nepolarnu/polarnu kovalentnu ili pretežno jonsku vezu, ali granice nisu oštre. U kristalima i koordinacionim kompleksima "jonsko naspram kovalentno" često je spektar, ne binarna etiketa.

## 2.2 Lewisova struktura

Lewisov crtež prati valentne elektrone kao:

- crte između atoma - deljeni elektronski parovi;
- tačke na atomu - nevezani parovi (lone pairs);
- zagrade i superskript - neto naboj jedinke.

Za elemente druge periode C, N, O i F korisno je pravilo okteta, ali ono ima izuzetke. Metali, elektron-deficitarne i hipervalentne vrste ne treba siliti u jednostavan organski obrazac.

[OpenStax Lewisov uvod](https://openstax.org/books/chemistry-2e/pages/7-3-lewis-symbols-and-structures) daje postupak za jednostavne vrste.

## 2.3 Formalni naboj

Za atom u jednoj Lewisovoj formi:

\[
q_\mathrm{formal}=V-N-\frac{B}{2},
\]

gde je \(V\) broj valentnih elektrona slobodnog atoma, \(N\) broj nevezanih elektrona, a \(B\) broj elektrona u vezama.

Formalni naboj je konzistentno knjigovodstvo, ne direktno izmerena lokalna količina. Zbir formalnih naboja mora dati neto naboj jedinke. Ovo je važno kod protonacije, soli, nitro-grupa i metalnih kompleksa.

## 2.4 Red veze i rezonanca

U osnovnom modelu:

- single bond deli jedan elektronski par;
- double dva;
- triple tri.

Višestruka veza je obično kraća i jača od odgovarajuće jednostruke, ali "obično" zavisi od istih elemenata i sličnog okruženja.

Neke vrste ne može verno opisati jedna Lewisova forma. Kod **rezonance** više crteža ima isti raspored jezgara, a različitu formalnu raspodelu elektrona. Prava vrsta ne skače između crteža; elektronska struktura je rezonantni hibrid. [OpenStax objašnjenje rezonance](https://openstax.org/books/chemistry-2e/pages/7-4-formal-charges-and-resonance) pokazuje zašto jednake N-O dužine u nitritu ne odgovaraju jednoj fiksnoj single i jednoj double vezi.

### Lokalni dokaz

U `N14.mol2` rastojanja od N1 do O1 i O2 su praktično jednaka:

| Par | Rastojanje iz koordinata |
|---|---:|
| N1-O1 | 1,22731 Å |
| N1-O2 | 1,22732 Å |

Ipak, oba MOL2 bond zapisa imaju tip `1`, dok je N atom tipovan kao `N.3`, a O kao `O.2`. To je formalna digitalna reprezentacija, ne potpuna teorija nitro elektronske strukture. Geometrija i bond typing ovde se ne smeju slepo izjednačiti.

## 2.5 Aromatičnost

Aromatični sistemi imaju cikličnu delokalizaciju elektrona i karakterističnu geometriju/stabilnost. U klasičnim organskim primerima koristi se Hückelovo \(4n+2\) pravilo za planarni konjugovani ciklus. Za cheminformatiku je još važnije:

> aromatičnost u fajlu je rezultat određenog modela i algoritma percepcije.

Isti benzenski prsten može biti zapisan kao tri naizmenične single/double veze (Kekulé forma) ili aromatične veze. [Daylight Theory Manual](https://www.daylight.com/dayhtml/doc/theory/theory.mol.html) izričito razlikuje hemijski pojam od pravila aromatičnosti namenjenog digitalnom jeziku.

Posledica: fingerprint ili substructure query može da se promeni samo zato što dva parsera koriste druga pravila aromatičnosti.

## 2.6 Kovalentna, jonska i koordinaciona veza

- **Kovalentna veza:** atomi dele elektronsku gustinu.
- **Jonska interakcija:** privlačenje suprotnih neto naboja; u kristalu je mreža, ne izolovana crta.
- **Koordinaciona (dativna) veza:** u Lewisovom formalizmu oba elektrona deljenog para potiču od donora/liganda. Kada se formira, nije zasebna fizička "vrsta crte" koju svaki format jednoznačno čuva.

Metal-ligand i metal-metal veze su naročito problematične za jednostavan integer bond order. CCDC dokumentacija preporučuje standardizaciju atom- i bond-tipova pre geometrijske analize; [CSD Python API primer](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/molecular_geometry_analysis.html) eksplicitno poziva dodelu unknown bond tipova i standardizaciju aromatičnih/delokalizovanih veza.

## 2.7 Eksplicitni i implicitni vodonici

Vodoničnik može biti:

- poseban atomski čvor sa koordinatama;
- implicitni broj vezan za heavy atom;
- nedostajući atom koji parser pokuša da doda prema valenci;
- eksperimentalno rafiniran, geometrijski postavljen ili delimično određen.

To menja molekulsku formulu, donor/acceptor svojstva, formalni naboj, stereokemiju i mrežu H-veza. "Remove hydrogens" nije bezazlena kozmetička transformacija.

## 2.8 Veza u fajlu nije nužno posmatrana veličina

Kod rendgenske kristalografije direktno se meri difrakcija, iz nje se modeluje elektronska gustina i položaji atoma, a hemijska povezanost/redovi veza se zatim dodeljuju uz hemijsko znanje. CIF može imati geometrijske bond liste, ali kristalografski minimum nisu nužno eksplicitni integer bond orders. CCDC zato navodi da su MOL2/SDF prikladniji kada je cilj molekulska informacija, dok CIF čuva kristalni kontekst: [Reading and writing molecules and crystals](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/io.html).

## 2.9 Posledice za aplikacije

<div class="project-link">
**Pre bilo kog fingerprinta:** definiši politiku za formalne naboje, protonaciju, implicitne H, aromatičnost, delokalizovane i metal-ligand veze. Čuvaj i original i standardizovanu reprezentaciju, uz verziju softvera i upozorenja.

**Za poređenje:** odvoji "ista povezanost pod našom normalizacijom" od "isti zapis bond tipova". Neslaganje parsera mora biti dijagnostika, ne automatski hemijska razlika.
</div>

## 2.10 Provera znanja

1. Izračunaj formalni naboj O sa tri lone pairs i jednom single vezom.
2. Da li dve rezonantne forme predstavljaju dva konformera?
3. Zašto tri alternating single/double veze i šest aromatic bonds mogu opisivati isti prsten?
4. Šta može poći pogrešno ako automatski dodaš H pre određivanja neto naboja?
5. Da li nulta MOL2 parcijalna charge kolona dokazuje da je veza nepolarna?

??? success "Odgovori"
    1. Za O je \(V=6\), \(N=6\), \(B=2\), pa \(q=6-6-1=-1\).  
    2. Ne. Raspored jezgara je isti; razlikuje se formalni elektronski crtež. Konformeri imaju različit 3D raspored usled rotacija/oblikovanja.  
    3. Prvi je Kekulé reprezentacija, drugi aromatična percepcija iste delokalizovane mreže.  
    4. Možeš dobiti pogrešnu protonaciju, valencu, formulu, donor/acceptor etikete i graf.  
    5. Ne; može samo značiti da charges nisu izračunate ili zapisane.

**Kriterijum prolaza:** uz jedan lokalni zapis jasno označi šta je element, koordinata, dodeljeni atom-tip, dodeljeni bond tip, formalni naboj i parcijalni naboj.

