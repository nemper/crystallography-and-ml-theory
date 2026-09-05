# 2. Elektroni i hemijske veze

**Prioritet: MORAŠ.** Softver ne vidi "hemiju" direktno. On vidi elemente, koordinate i dodeljene veze; kvalitet tih dodela određuje graf, podstrukturnu pretragu i fingerprint.

**Preduslov:** iz [poglavlja 1](01-atomi-joni-formule.md) razlikuješ element, atom, jon, formulu i neto naboj; Lewisova struktura se ovde gradi od početka.

## 2.1 Minimalni model elektrona

Za ovaj projekat dovoljno je sledeće:

- elektroni zauzimaju kvantna stanja/orbitale, ne kružne putanje kao planete;
- spoljašnji, valentni elektroni dominantno određuju uobičajene veze;
- atomi dele ili formalno prenose elektrone da bi formirali stabilnije celine;
- elektronska gustina je kontinuirana, dok su red veze i formalni naboj diskretni modeli.

**Elektronegativnost** opisuje sklonost vezanog atoma da privlači elektronsku gustinu. Razlika može dati nepolarnu/polarnu kovalentnu ili pretežno jonsku vezu, ali granice nisu oštre. U kristalima i koordinacionim kompleksima "jonsko naspram kovalentno" često je spektar, ne binarna etiketa.

## 2.2 Lewisova struktura

**Pitanje:** kako iz formule saznati koliko veza i slobodnih parova treba nacrtati? Počni od raspoloživih valentnih elektrona, pa proveri njihov utrošak. Za neutralne atome koji nam prvi trebaju:

| Atom | Valentni elektroni | Početni cilj u jednostavnoj Lewisovoj strukturi |
|---|---:|---|
| H | 1 | duet: 2 elektrona oko H |
| C | 4 | oktet: 8 elektrona oko C |
| N | 5 | oktet: 8 elektrona oko N |
| O | 6 | oktet: 8 elektrona oko O |

Lewisov crtež prati te elektrone kao:

- crte između atoma - deljeni elektronski parovi;
- tačke na atomu - nevezani parovi (lone pairs);
- zagrade i superskript - neto naboj jedinke.

**Elektronski par** sadrži dva elektrona. Jednostruka veza deli jedan par, a slobodni par ostaje nevezan. **Broj susednih atoma**, **zbir redova veza** (vezivna valenca u ovom jednostavnom modelu) i **naboj** nisu ista veličina: karbonilni C može imati tri suseda i zbir redova veza četiri; N u NH₃ ima tri jednostruke veze i naboj nula. Naboj se proverava raspodelom elektrona, a ne brojem nacrtanih crta.

### Postupak od formule do crteža

1. Saberi valentne elektrone svih atoma; za svaki pozitivan jedinični naboj oduzmi jedan elektron, a za negativan dodaj jedan.
2. Izaberi hemijski smislen skelet i poveži susede jednostrukim vezama. H je terminalan. Formula sama ne bira između svih mogućih izomera.
3. Za svaku vezu potroši dva elektrona. H tada ima duet; preostalim elektronima popuni oktete terminalnih atoma, pa centralnog atoma.
4. Ako centralnom atomu nedostaje oktet, proveri da li slobodni par suseda može dati dodatni vezni par, odnosno višestruku vezu.
5. Prebroj sve elektrone ponovo, a zatim formalne naboje i njihov zbir.

### Potpun primer: NH₃ i NH₄⁺

Za **NH₃** raspolažemo sa \(5+3\times1=8\) elektrona. Tri N–H veze troše šest, pa preostala dva čine jedan slobodni par na N:

```text
       :
   H – N – H       NH₃: 3 vezna para + 1 slobodni par
       |
       H
```

Svaki H okružuju dva elektrona njegove veze. N okružuje \(6+2=8\) elektrona, ali se pri sabiranju ukupnih elektrona svaki deljeni par računa samo jednom.

Za **NH₄⁺** imamo \(5+4\times1-1=8\) elektrona. Četiri N–H veze troše svih osam; na N ne ostaje slobodni par:

```text
  [    H    ]⁺
  [    |    ]
  [ H– N –H ]      NH₄⁺: 4 vezna para, bez slobodnog para
  [    |    ]
  [    H    ]
```

N ponovo ima oktet, a svaki H duet. Crtež prikazuje povezanost; prostorni oblik sledi u [poglavlju 3](03-geometrija.md#31-od-lewisovog-crteza-do-3d).

!!! note "Granice osnovnog modela"
    Pravilo okteta je koristan početni postupak za C, N, O i F, ali ima izuzetke. Metali, elektron-deficitarne i hipervalentne vrste ne treba da se silom uklapaju u jednostavan organski obrazac.

[OpenStax Lewisov uvod](https://openstax.org/books/chemistry-2e/pages/7-3-lewis-symbols-and-structures) daje dodatne vežbe; gornji postupak je samostalan obavezni uvod.

## 2.3 Formalni naboj

Za atom u jednoj Lewisovoj formi:

\[
q_\mathrm{formal}=V-N-\frac{B}{2},
\]

gde je \(V\) broj valentnih elektrona slobodnog atoma, \(N\) broj nevezanih elektrona, a \(B\) broj elektrona u vezama.

Formalni naboj je konzistentno knjigovodstvo, ne direktno izmerena lokalna količina. Zbir formalnih naboja mora dati neto naboj jedinke. Ovo je važno kod protonacije, soli, nitro-grupa i metalnih kompleksa.

Sada su ulazi u formulu poznati iz sopstvenog crteža (oznaka \(N\) u formuli znači broj nevezanih elektrona, ne simbol elementa azota):

| Jedinka i atom | \(V\) | \(N\) | \(B\) | \(q_\mathrm{formal}\) |
|---|---:|---:|---:|---|
| N u NH₃ | 5 | 2 | 6 | \(5-2-6/2=0\) |
| svaki H u NH₃ | 1 | 0 | 2 | \(1-0-2/2=0\) |
| N u NH₄⁺ | 5 | 0 | 8 | \(5-0-8/2=+1\) |
| svaki H u NH₄⁺ | 1 | 0 | 2 | \(1-0-2/2=0\) |

Ukupno: NH₃ ima \(0+3\times0=0\), a NH₄⁺ ima \(+1+4\times0=+1\). **Protonacija** \(\mathrm{NH_3+H^+\rightarrow NH_4^+}\) koristi slobodni par N za novu N–H vezu; proton ne donosi elektron. NH₃ ima tri vezna domena i jedan slobodni par, pa je trigonalno-piramidalan; NH₄⁺ ima četiri vezna domena, pa je tetraedarski. Slobodni par NH₃ može se donirati metalu ili prihvatiti vodoničnu vezu; NH₄⁺ nema taj raspoloživi par, ali njegove N–H grupe mogu biti donori vodonične veze. [Različita značenja donorstva](04-organska.md#donorske-uloge) razdvojena su pre funkcionalnih grupa. Nitro-grupa u sledećem odeljku je složeniji nastavak ovog istog knjigovodstva.

## 2.4 Red veze i rezonanca

U osnovnom modelu:

- single bond deli jedan elektronski par;
- double dva;
- triple tri.

Višestruka veza je obično kraća i jača od odgovarajuće jednostruke, ali "obično" zavisi od istih elemenata i sličnog okruženja.

### Zašto se kasnije pojavljuju σ, π i konjugacija

U osnovnom orbitalnom modelu **σ-veza** nastaje preklapanjem orbitala duž ose između jezgara, dok **π-veza** uključuje bočno preklapanje, sa elektronskom gustinom sa obe strane te ose. Obična jednostruka veza ima jedan σ doprinos, dvostruka jedan σ i jedan π, a trostruka jedan σ i dva π doprinosa. To objašnjava zašto je rotacija oko izolovane dvostruke veze ograničena: menja se preklapanje π-orbitala.

**Konjugacija** znači da susedne odgovarajuće orbitale mogu povezano da se preklapaju preko više atoma, kao u nizu `C=C–C=C`. Elektroni tada nisu opisani samo jednim izolovanim parom atoma. To je most ka rezonanci, aromatičnosti i rigidnosti amida, a ne dodatna vrsta bond koda u fajlu. [OpenStax: višestruke veze](https://openstax.org/books/chemistry-2e/pages/8-3-multiple-bonds) ilustruje σ/π preklapanje.

Neke vrste ne može verno opisati jedna Lewisova forma. Kod **rezonance** više crteža ima isti raspored jezgara, a različitu formalnu raspodelu elektrona. Prava vrsta ne skače između crteža; elektronska struktura je rezonantni hibrid. [OpenStax objašnjenje rezonance](https://openstax.org/books/chemistry-2e/pages/7-4-formal-charges-and-resonance) pokazuje zašto jednake N-O dužine u nitritu ne odgovaraju jednoj fiksnoj single i jednoj double vezi.

### Lokalni dokaz

U `N14.mol2` rastojanja od N1 do O1 i O2 su praktično jednaka:

| Par | Rastojanje iz koordinata |
|---|---:|
| N1-O1 | 1,22731 Å |
| N1-O2 | 1,22732 Å |

Ipak, oba MOL2 bond zapisa imaju tip `1`, dok je N atom tipovan kao `N.3`, a O kao `O.2`. Ti tipovi zajedno nisu valenciono dosledan Lewisov prikaz neutralne nitro-grupe. To je problem eksportovanog atom/bond typing-a koji treba proveriti, a ne alternativna, jednako valjana Lewisova forma.

Za nitro-grupu vezanu za organski ostatak R dve uobičajene rezonantne forme su \(\mathrm{R-N^{+}(=O)-O^{-}}\), uz zamenu uloga dva O atoma u drugoj formi. N ima četiri vezna para i formalni naboj +1, jednostruko vezani O ima −1, a dvostruko vezani O nulu; grupa je ukupno neutralna. Rezonanca objašnjava delokalizaciju i slične N–O dužine, ali sama dužina ne određuje jedinstvenu digitalnu dodelu veza i naboja. Standardizacija treba da sačuva original, proveri ceo motiv i zabeleži korekciju pre računanja fingerprinta ili donor/acceptor etiketa.

## 2.5 Aromatičnost

Aromatični sistemi imaju cikličnu delokalizaciju elektrona i karakterističnu geometriju/stabilnost. **Pitanje:** koji elektroni se broje u Hückelovom pravilu? Broje se elektroni u neprekinutom prstenu preklopljenih \(p\)-orbitala, odnosno u cikličnom \(\pi\)-sistemu; ne svi valentni elektroni niti elektroni \(\sigma\)-veza.

U benzenu svaki od šest C daje po jedan takav elektron: \(6\times1=6\). Isti broj dobija se brojanjem tri \(\pi\)-para u Kekulé crtežu: \(3\times2=6\). To su dva načina brojanja istih elektrona.

Za jednostavan planarni potpuno konjugovani ciklus Hückelov uslov glasi:

\[
N_\pi=4n+2,\qquad n=0,1,2,\ldots
\]

\(n\) je nenegativan ceo broj koji proverava dopušteni broj elektrona; nije broj prstenova niti broj dvostrukih veza. Za šest elektrona, \(n=(6-2)/4=1\).

| Prsten | Doprinos atoma \(\pi\)-sistemu | Gde je slobodni par N? | Posledica za neutralni N |
|---|---|---|---|
| benzen | šest C × 1 = 6 elektrona | nema N | tri delokalizovana \(\pi\)-para |
| piridin | pet C × 1 + N × 1 = 6 | u orbitali približno u ravni prstena, izvan \(\pi\)-sistema | par je tipično dostupan za vezivanje metala ili prihvatanje H-veze; N nema vezani H |
| pirol | četiri C × 1 + N par × 2 = 6 | u \(p\)-orbitali normalnoj na ravan prstena, deo \(\pi\)-sistema | par nije uobičajeno raspoloživ kao kod piridina; neutralni N–H je H-donor, N obično nije H-akceptor |

```text
piridin: N p-elektron (1) → π prsten; slobodni par (2) ostaje izvan njega
pirol:   N slobodni par (2) → π prsten; nema dodatnog nezavisnog N para
```

Ovde je pirol neutralni N–H oblik. Deprotonacija ili druga promena hemijskog stanja zahteva novu analizu. [OpenStax poređenje piridina i pirola](https://openstax.org/books/organic-chemistry/pages/15-5-aromatic-heterocycles-pyridine-and-pyrrole) prikazuje orbitalni položaj parova. Same vrednosti \(4n+2\) nisu dovoljne bez cikličnosti, planarnosti i konjugacije. Za cheminformatiku je dodatno važno:

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

<div class="project-link" markdown="1">
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
