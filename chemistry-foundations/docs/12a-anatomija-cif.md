# 12A. Anatomija jednog CIF fajla

**Prioritet: MORAŠ.** CIF nije binarni „crtež kristala“, već strukturisan tekst. Možeš ga otvoriti u običnom editoru, ali njegovo hemijsko i kristalografsko značenje tumačiš pomoću CIF rečnika i odgovarajućeg parsera.

Ova lekcija koristi [ceo sintetički CIF za preuzimanje](tutorial-minimal.cif). Fajl je ručno napisan za kurs, ne predstavlja eksperiment i ne sadrži CSD, fakultetske ni korisničke podatke. Zato jedini `.cif` koji se nalazi u repozitorijumu može bezbedno da se deli.

## 12A.1 Ovako CIF zaista izgleda

```cif
# SYNTHETIC TEACHING FIXTURE -- NOT AN EXPERIMENTAL OR CSD RECORD
# Hand-written for this course. CC0-1.0. CIF 1.1-compatible ASCII text.

data_synthetic_nacl_tutorial
_audit_creation_method            'Hand-written teaching fixture; no experiment'
_chemical_name_common             'Synthetic sodium chloride tutorial'
_chemical_name_systematic         ?
_chemical_formula_sum             'Cl Na'
_chemical_formula_weight          58.44

_cell_length_a                    5.6400(10)
_cell_length_b                    5.6400(10)
_cell_length_c                    5.6400(10)
_cell_angle_alpha                 90
_cell_angle_beta                  90
_cell_angle_gamma                 90
_cell_volume                      179.41(10)
_cell_formula_units_Z             4

_symmetry_space_group_name_H-M    'F m -3 m'
_symmetry_Int_Tables_number       225
_diffrn_ambient_temperature       .
_exptl_crystal_density_diffrn     2.164

# These values deliberately demonstrate CIF missing-value tokens.
_refine_ls_R_factor_gt            .
_refine_ls_wR_factor_ref          .

_publ_section_comment
;
This is a synthetic syntax example, not a measured crystal structure.
Its deliberately small data block is meant for parser and reading exercises.
;

loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_occupancy
Na1  Na  0.00000  0.00000  0.00000  1.0
Cl1  Cl  0.50000  0.50000  0.50000  1.0
```

Ovo je mali, sintaksno validan **CIF 1.1 data block**, ali nije publication-ready crystallographic information file. Nema merene refleksije, refinement model, displacement parametre, detalje instrumenta ni bibliografiju. „Parser ga čita“ i „dokazuje eksperiment“ potpuno su različite tvrdnje.

## 12A.2 Čitanje red po red

| Deo | Primer | Šta znači |
|---|---|---|
| komentar | `# SYNTHETIC ...` | `#` započinje komentar do kraja reda; parser ga ne tumači kao data item |
| data block | `data_synthetic_nacl_tutorial` | otvara imenovani blok; jedan fajl može imati više `data_` blokova |
| scalar item | `_chemical_formula_weight 58.44` | data name i jedna vrednost |
| quoted value | `'F m -3 m'` | razmaci pripadaju jednoj tekstualnoj vrednosti, pa su potrebni navodnici |
| broj sa s.u. | `5.6400(10)` | procena 5,6400 uz standardnu nesigurnost 0,0010 u istim jedinicama |
| nepoznato | `?` | vrednost nije poznata |
| neprimenljivo/namerno bez vrednosti | `.` | nema vrednosti za taj item u ovom kontekstu; nije broj nula |
| višeredni tekst | redovi između samostalnih `;` u prvoj koloni | jedna tekstualna vrednost može zauzimati više redova |
| tabela | `loop_` + imena kolona + vrednosti | vrednosti se dele u redove prema broju navedenih kolona |

Autoritativna pravila za tokene, quoting, komentare, `loop_`, `?`, `.`, višeredni tekst i brojeve sa nesigurnošću daje [IUCr CIF 1.1 sintaksa](https://www.iucr.org/resources/cif/spec/version1.1/cifsyntax). Značenje pojedinačnih data names ne određuje izgled imena, već [IUCr core CIF dictionary](https://www.iucr.org/resources/cif/dictionaries/browse/cif_core1).

Missing-value značenje imaju samostalni **nenavodnički** tokeni `?` i `.`. Znak `'?'` u navodnicima ili `?` unutar semicolon-delimited tekstualnog polja sintaksno je tekst, čak i kada ga je autor upotrebio kao placeholder. Upravo tako je zapisano systematic-name polje lokalnog N14 CIF-a. Parser treba da očuva tu razliku; kasnija kuracija može prepoznati placeholder uz trag izmene.

!!! warning "Zagrada nije interval ni množenje"
    U `5.6400(10)` cifre u zagradi odnose se na poslednje cifre vrednosti. Dakle, s.u. je 0,0010. To samo po sebi ne znači da je „prava vrednost sigurno između 5,6390 i 5,6410“; standardna nesigurnost nije tvrda granica.

## 12A.3 Kako se čita `loop_`

Posle `loop_` dolazi šest data names, pa parser očekuje vrednosti u grupama od šest:

```text
label  element  fract_x  fract_y  fract_z  occupancy
Na1    Na       0.00000  0.00000  0.00000  1.0
Cl1    Cl       0.50000  0.50000  0.50000  1.0
```

Prelomi reda služe čitaocu, ali CIF petlju suštinski čini ravan niz tokena. Broj vrednosti zato mora biti celobrojni umnožak broja kolona. Ako jedna ćelija nedostaje, mora stajati odgovarajući `?` ili `.`, inače se sve sledeće vrednosti mogu pomeriti u pogrešne kolone ili će parser odbiti petlju.

Ovde su `fract_x`, `fract_y` i `fract_z` **frakcione koordinate** u bazisu jedinične ćelije. Tačka `(0.5, 0.5, 0.5)` nije automatski `(0.5 Å, 0.5 Å, 0.5 Å)`. Kartezijanska pozicija dobija se množenjem frakcionog vektora matricom ćelije, kao u [poglavlju 8](08-celija.md).

`occupancy = 1.0` znači da model tom atomskom mestu dodeljuje punu zauzetost. Ne znači „jedan atom u celom kristalu“: space-group operacije i translaciona periodičnost generišu ekvivalentna mesta.

## 12A.4 Od kojih slojeva se realan CIF često sastoji

Redosled nije obavezan, a mnoga polja mogu nedostajati. Tipičan small-molecule CIF može sadržati:

1. identitet bloka, audit istoriju, autora i bibliografiju;
2. formulu, relativnu formulsku masu i opis uzorka;
3. parametre ćelije, prostornu grupu, (Z), temperaturu i gustinu;
4. instrument, talasnu dužinu, strategiju prikupljanja i obradu refleksija;
5. detalje rešavanja i refiniranja, R faktore, restraints i upozorenja;
6. atom-site petlju sa frakcionim koordinatama, occupancy i displacement parametrima;
7. opciono anisotropne parametre, geometrijske tabele i H-bond/contact liste;
8. opciono višeredne ugrađene refinement ili reflection blokove.

Veze nisu obavezno primarni sadržaj CIF-a. Program ih može preuzeti iz eksplicitne geometrijske tabele ili ih **percipirati** iz elemenata, udaljenosti, simetrije i hemijskih pravila. Zato dva alata iz istih koordinata mogu izvesti različite molecular graphs, naročito kod metala, disorder-a ili neobičnih bond orders.

## 12A.5 Gde se nalazi „ceo kristal“

Atom-site petlja obično opisuje **asimetričnu jedinicu**, ne listu svakog atoma u jediničnoj ćeliji, a još manje beskonačni kristal. Za periodični model potrebni su zajedno:

```text
ćelija + prostorna grupa/simetrija + atom sites + occupancy/disorder
```

U sintetičkom NaCl primeru nema eksplicitne petlje simetrijskih operacija: kristalografski alat ih mora dobiti iz pouzdane tabele za zadatu grupu `F m -3 m`. Čisto tekstualni CIF parser to ne mora da ume. U ovom konkretnom slučaju ekvivalentne pozicije daju četiri Na i četiri Cl u konvencionalnoj ćeliji, u skladu sa `Z=4`; specijalne pozicije se ne broje više puta. Kod realnih grupa treba proveriti i setting i izbor koordinatnog početka, jer sam broj grupe ne određuje uvek ceo koordinatni prikaz.

Parser zatim primenjuje simetrijske operacije i celobrojne translacije. Ako izvučeš samo atom-site redove i protumačiš ih kao izolovan molekul, možeš izgubiti simetrijskog suseda, preseći molekul preko granice ćelije ili pogrešno zaključiti da kontakt ne postoji.

## 12A.6 Kako izgleda dostavljeni `cu_n14_a.cif`, bez objavljivanja fajla

Dostavljeni fajl koristi istu gramatiku, ali je mnogo veći: oko 2,7 MB. U njemu se mogu prepoznati sledeći slojevi:

| Šta tražiš | Tipičan prefiks/tag | Šta dobijaš |
|---|---|---|
| data block | `data_` | granica zapisa |
| formula | `_chemical_formula_...` | deklarisani sastav |
| ćelija | `_cell_length_...`, `_cell_angle_...` | metrički okvir periodičnog modela |
| simetrija | `_symmetry_...` / `_space_group_...` | prostorna grupa i operacije |
| atom sites | `loop_` + `_atom_site_...` | oznake, elementi, koordinate, occupancy i displacement model |
| geometrija | `_geom_bond_...`, `_geom_angle_...` | izvedene ili prijavljene geometrijske relacije |
| kvalitet/refinement | `_refine_...`, `_reflns_...` | pokazatelji modela i podataka |
| ugrađeni sadržaj | višeredno polje između `;` | razlog zbog kojeg fajl može biti neobično velik |

Iz imena `cu_n14_a.cif` ne zaključuj da struktura sadrži bakar. U tom lokalnom primeru sastav i atom-site lista nemaju Cu; oznaka Cu Kα opisuje rendgensko zračenje. Uvek proveri data items, ne filename.

Za formalnu i kristalografsku proveru koristi CIF-aware validator, na primer IUCr-ov [checkCIF](https://checkcif.iucr.org/).

!!! danger "Ne šalji poverljiv CIF na javni servis"
    Pre slanja proveri pravo i poverljivost. Sintaksna, kristalografska i hemijska validacija nisu ista provera; nijedan alat ih sam ne garantuje.

## 12A.7 Minimalna provera pre tumačenja

Pre zaključivanja utvrdi CIF dijalekt i rečnik, izabrani data block i parser warnings; zajedno proveri ćeliju, simetriju, atom sites, occupancy/disorder i sastav; `?` i `.` sačuvaj kao različita značenja nedostajanja; vizuelno uporedi asimetričnu jedinicu, proširenu ćeliju i periodične kontakte. Uvek razlikuj originalne, parsirane i izvedene podatke.

## 12A.8 Provera znanja

1. Zašto `loop_` nije isto što i proizvoljna tabela u CSV-u?
2. Kolika je s.u. u `5.6400(10)`?
3. Šta je razlika između `?`, `.` i `0`?
4. Da li dva atom-site reda u primeru znače da cela ćelija ima samo dva atoma?
5. Zašto sintaksno validan CIF nije automatski naučno validna struktura?
6. Koji sadržaj gubiš ako iz CIF-a uzmeš samo molekulski graf?

??? success "Odgovori"
    1. Kolone definišu data names iz dictionary sistema, a vrednosti su token stream čiji broj mora odgovarati broju kolona.
    2. `0.0010` u istoj jedinici kao vrednost.
    3. `?` je nepoznato, `.` nema primenljivu/dodeljenu vrednost u tom kontekstu, a `0` je poznata numerička nula.
    4. Ne; to su jedinstvena mesta, dok simetrija i translacije grade ćeliju i kristal.
    5. Sintaksa proverava da je zapis čitljiv; ne potvrđuje poreklo, eksperiment, hemiju, model ni kvalitet.
    6. Ćeliju, simetriju, periodično pakovanje, većinu eksperimentalnih metapodataka i moguće occupancy/disorder značenje.

**Kriterijum prolaza:** bez pomoći možeš da otvoriš nepoznat CIF, označiš data block, scalar items, jednu petlju, missing-value tokene, cell/symmetry i atom-site polja, a zatim jasno kažeš šta još nije dokazano.
