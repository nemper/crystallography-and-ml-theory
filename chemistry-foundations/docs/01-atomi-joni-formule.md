# 1. Atomi, elementi, joni i formule

**Prioritet: MORAŠ.** Ovo poglavlje postavlja rečnik bez kog se CIF polja, atom-tipovi i filteri lako pogrešno tumače.

## 1.1 Šta je šta

**Element** je vrsta atoma određena brojem protona u jezgru, odnosno atomskim brojem \(Z\). Svaki atom sa 6 protona je ugljenik (C); sa 7 je azot (N); sa 8 kiseonik (O). Broj neutrona može da se razlikuje - to su izotopi istog elementa.

**Atom** je pojedinačna elektroneutralna jedinka kada ima isti broj protona i elektrona. Ako izgubi ili primi elektrone postaje **jon**:

- kation ima pozitivan neto naboj, npr. \(\mathrm{Na^+}\);
- anion ima negativan neto naboj, npr. \(\mathrm{Cl^-}\).

**Molekul** je elektroneutralna, diskretna jedinka od najmanje dva atoma povezana hemijskim vezama. Analogna diskretna jedinka sa neto nabojem je **molekulski (poliatomski) jon**. **Jedinjenje** je supstanca sastavljena od najmanje dva elementa. Nisu sva jedinjenja diskretni molekuli: za beskonačnu jonsku rešetku NaCl korisnije je govoriti o **formula unit**, najjednostavnijem stehiometrijskom odnosu Na:Cl = 1:1.

!!! example "Formula nije graf"
    Formula \(\mathrm{C_2H_6O}\) govori da jedinka sadrži dva C, šest H i jedan O. Ne govori da li je povezanost etanol \(\mathrm{CH_3CH_2OH}\) ili dimetil-etar \(\mathrm{CH_3OCH_3}\). To su konstitucioni izomeri. Filter po formuli zato nije zamena za podstrukturnu ili graf-sličnost.

Za vizuelan uvod pogledaj [OpenStax: atomska struktura i simboli](https://openstax.org/books/chemistry-2e/pages/2-3-atomic-structure-and-symbolism) i [hemijske formule](https://openstax.org/books/chemistry-2e/pages/2-4-chemical-formulas).

## 1.2 Periodni sistem kao mapa ponašanja

Ne treba da pamtiš ceo periodni sistem. Za ovaj projekat prvo prepoznaj:

| Grupa | Projektno značenje |
|---|---|
| H | često implicitno izostavljen; određuje protonaciju, H-veze i stereokemiju |
| C | osnovni skelet organskih liganada |
| N, O, S, P | česti heteroatomi; lone pairs, donor/acceptor uloge, promenljive valence i naboji |
| F, Cl, Br, I | halogeni; supstituenti, anioni, ligandi i potencijalne halogene interakcije |
| alkalni/zemnoalkalni metali | jonske soli i koordinacija, često visoki koordinacioni brojevi |
| prelazni metali | više oksidacionih stanja i koordinacionih geometrija; centralni za `search2` |
| lantanoidi/aktinoidi | visoki i promenljivi koordinacioni brojevi; ređi, ali `4M` ih ne isključuje |

Pozicija u tabeli pomaže da proceniš broj valentnih elektrona i tipične naboje, ali kod prelaznih metala to nije pouzdana funkcija same grupe. [OpenStax pregled jonskih i molekulskih jedinjenja](https://openstax.org/books/chemistry-2e/pages/2-6-ionic-and-molecular-compounds) eksplicitno pokazuje zašto Cu može imati, na primer, +1 ili +2.

## 1.3 Tri vrste "naboja" koje ne treba mešati

1. **Neto naboj jedinke** - zbir svih naboja; npr. kompleks može biti \(2+\).
2. **Formalni naboj atoma** - knjigovodstvena dodela elektrona u Lewisovom modelu.
3. **Parcijalni naboj** - model kontinuirane, nejednake raspodele elektronske gustine; zavisi od metode dodele.

MOL2 kolona `charge` obično sadrži parcijalni naboj samo ako je neka charge metoda zaista primenjena. U lokalnom `N14.mol2` zaglavlje kaže `NO_CHARGES`, a kolona sadrži nule. To ne znači da su svi atomi fizički nepolarni; znači da parcijalni naboji nisu dodeljeni.

## 1.4 Količina supstance, masa i skale

Jedan mol sadrži Avogadrov broj jedinki:

\[
N_A = 6.02214076\times10^{23}\ \mathrm{mol^{-1}}.
\]

Molarna masa izražava se u \(\mathrm{g\ mol^{-1}}\). Lokalni CIF navodi:

```text
_chemical_formula_sum     'C25 H20 N3 O2 P'
_chemical_formula_weight  425.41
```

Vrednost 425,41 g/mol je zbir prosečnih atomskih masa u formuli. Kristalografska gustina povezuje molarnu masu \(M\), broj formulskih jedinki \(Z\) i zapreminu ćelije \(V\); kompletan N14 račun, konverzija Å³→cm³ i granice ove provere dati su u [Gustina kao provera konzistentnosti](08-celija.md#gustina-kao-provera-konzistentnosti).

### Jedinice koje moraš trenutno prepoznati

| Veličina | Uobičajena jedinica | Napomena |
|---|---|---|
| atomsko rastojanje | Å (angstrom) | \(1\ \mathrm{\mathring{A}}=10^{-10}\ \mathrm{m}=0.1\ \mathrm{nm}\) |
| ugao | stepen | ćelijski i molekulski uglovi |
| temperatura | K | \(T[\mathrm{K}]=t[\,^{\circ}\mathrm{C}]+273.15\) |
| molarna masa | g/mol | nije masa jednog molekula |
| gustina | g/cm³ | CIF može navesti izmerenu i izračunatu |
| energija | kJ/mol | poređenje energija po molu |

## 1.5 Primer koji razbija pretpostavku iz naziva fajla

Fajl se zove `cu_n14_a.cif`, ali sumarna formula nema Cu atom. `Cu` se pojavljuje u:

```text
_diffrn_radiation_type        CuK\a
_diffrn_radiation_wavelength  1.54178
```

To označava karakteristično **Cu Kα rendgensko zračenje** korišćeno u merenju, ne bakar u uzorku. Ime fajla i slobodan tekst nikada ne smeju imati veći autoritet od semantičkih polja i atomskih zapisa.

## 1.6 Posledice za aplikacije

<div class="project-link">
**Globalna pretraga:** element-set, formula, prisustvo metala i neto naboj su jeftini filteri, ali nisu dovoljan dokaz hemijskog identiteta. `4M` u ConQuest-u znači bilo koji metalni element, ne samo prelazni metal.

**Poređenje parova:** sastav treba prikazati kao odvojenu komponentu sličnosti. Razlika u H broju može biti eksplicitnost formata, protonacija, disorder ili prava hemijska razlika; ne kažnjava se automatski bez standardizacije.
</div>

## 1.7 Provera znanja

1. Da li su \(\mathrm{Fe^{2+}}\) i \(\mathrm{Fe^{3+}}\) isti element? Da li su ista hemijska vrsta?
2. Koliko ukupno atoma navodi formula \(\mathrm{C_{25}H_{20}N_3O_2P}\)? Koliko je heavy atoms?
3. Čelija sadrži \(Z=4\), a formula ima tri N. Koliko N atoma odgovara punoj idealnoj ćeliji?
4. Zašto filter "sadrži Cu" ne sme pretraživati ceo tekst CIF-a?
5. Šta `NO_CHARGES` u MOL2 znači, a šta ne znači?

??? success "Odgovori"
    1. Da: oba imaju 26 protona, pa su Fe. Ne: razlikuju se brojem elektrona i nabojem, pa nisu ista hemijska vrsta.  
    2. Ukupno 51; heavy atoms su svi osim H, dakle 31.  
    3. \(4\times3=12\).  
    4. Jer se `Cu` može odnositi na izvor zračenja, autora, softver ili komentar. Elementi se izvode iz hemijskih/atomskih polja.  
    5. Parcijalni naboji nisu dodeljeni/zapisani; ne tvrdi da nema formalnih naboja, polarnih veza ili nejednake elektronske gustine.

**Kriterijum prolaza:** bez gledanja objasni razliku element - atom - jon - molekul - formula unit - kristal i proveri gustinu lokalnog CIF-a sa ispravnim jedinicama.
