# Opcione nastavne laboratorijske vežbe

Ove male, ograničene vežbe služe isključivo da teoriju pretvore u intuiciju. **Nisu faze, prototipi, backlog niti redosled realizacije budućeg 2CDC projekta.** Mogu se prolaziti konceptualno, ručnim računom ili nad sintetičkim primerom; programsko izvođenje nije uslov za završetak plana učenja.

Ako se koriste originalni lokalni fajlovi, rad je **read-only**: ne menjaj ih, ne šalji ih javnim servisima i ne commit-uj ih u ovaj repo.

## Pre početka

Napravi za svaki rezultat malu evidenciju:

```text
vežba / datum
source file + SHA-256
alat + verzija + parametri
šta je direktno pročitano
šta je izračunato
šta je hemijski dodeljeno/pretpostavljeno
warnings i nerešena pitanja
```

Za opcioni programski rad korisni su [Gemmi](https://gemmi.readthedocs.io/en/stable/) za CIF/crystallography i [RDKit](https://www.rdkit.org/docs/) za molekulske grafove. Oni su pomoćna sredstva, ne propisani projektni stack i ne autoritet nad značenjem. Svaki rezultat proveri na malom ručno razumljivom primeru.

## L0 — Inventar i dokazni lanac

**Cilj:** naučiti da dataset počinje poreklom, ne DataFrame-om.

1. Rekurzivno popiši lokalne fajlove.
2. Zabeleži relativni path, bytes, extension, SHA-256 i vreme izmene.
3. Format detektuj i po sadržaju; ekstenzija je samo signal.
4. Za multi-record formate izbroj records nezavisno na dva načina gde je moguće.
5. Označi fajlove koje licenca/provenance ne dozvoljava da napuste lokalni data plane.

**Kontrola:** dobijaš isti hash pri ponovnom čitanju; nijedan original nije promenio vreme/hash.

**Isporuka:** `source-manifest.local.csv`, van Git repoa.

## L0A — Anatomija celog bezbednog CIF-a

**Ulaz:** repo fixture [`tutorial-minimal.cif`](tutorial-minimal.cif). Ovo je jedini CIF u praktikumu koji sme da se deli javno: ručno je napravljen i sintetički.

1. Otvori fajl kao običan tekst i označi komentar, `data_` blok, scalar data items, quoted value, semicolon text field i `loop_`.
2. Za svaki atom-site red poveži šest vrednosti sa šest loop kolona.
3. Pronađi standard uncertainty zapis, nepoznatu vrednost `?` i neprimenljivu vrednost `.`.
4. Parserom pročitaj broj blokova/items/atom rows; uporedi sa ručnim brojanjem.
5. Iz \(a=b=c=5.6400\ \text{Å}\) reprodukuj zapreminu.
6. Iz formule NaCl, \(Z=4\), formule mase i zapremine proveri gustinu.
7. U privatnoj privremenoj kopiji ukloni jednu vrednost iz atom loop reda i zabeleži kako parser prijavljuje cardinality grešku; original ne menjaj.

**Kontrola:** parser i ručno čitanje moraju dati isti atom-column mapping. `?` i `.` ostaju različiti tokeni, a sintetički model se ne opisuje kao eksperimentalni dokaz.

## L1 — Formula, molarna masa i kristalna gustina

**Ulaz:** `cu_n14_a.cif`.

1. Pronađi moiety i sum formula, \(Z\), cell volume i reported density.
2. Izračunaj molarnu masu iz standardnih atomskih masa ili proveri reported formula weight.
3. Pretvori Å³ u cm³ i izračunaj:

\[
\rho=\frac{Z M}{N_A V}.
\]

4. Objasni svaki faktor i jedinicu.
5. Dokaži iz formule i atom-site petlje da fajl nema Cu atom.
6. Pronađi gde se `Cu` zaista pojavljuje i objasni njegovo značenje.

**Kontrola:** dimenziona analiza mora završiti sa g cm⁻³.

## L2 — Veza kao model: N14 cross-format audit

**Ulazi:** `cu_n14_a.cif`, `N14.mol`, `N14.mol2`.

Napravi tabelu:

| Svojstvo | CIF | MOL | MOL2 | observed / derived / assigned |
|---|---|---|---|---|
| atoms | | | | |
| bonds | | | | |
| bond types | | | | |
| formal/partial charge | | | | |
| coordinates | | | | |
| cell/symmetry | | | | |
| uncertainty/quality | | | | |

Zatim:

1. uporedi dve N–O distance oko nitro-like N/O motiva;
2. uporedi te distance sa single/double/unknown oznakama u MOL/MOL2;
3. objasni resonance i zašto geometrija ne potvrđuje naivni integer bond assignment;
4. napiši loss matrix za CIF → MOL → MOL2.

**Kontrola:** `NO_CHARGES` ne sme postati tvrdnja „svi naboji fizički nula“.

## L3 — Frakcione i kartezijanske koordinate

**Ulazi:** isti N14 fajlovi.

Za monoklinsku ćeliju sa jedinstvenom b osom, \(\alpha=\gamma=90^\circ\), jedan čest izbor matrice je:

\[
\begin{aligned}
x_c &= ax_f+c\cos\beta\,z_f\\
y_c &= by_f\\
z_c &= c\sin\beta\,z_f.
\end{aligned}
\]

1. Iz CIF-a pročitaj \(a,b,c,\beta\) i frakcione koordinate C1.
2. Ručno i programski izračunaj Cartesian koordinatu.
3. Uporedi je sa C1 u MOL2 uz toleranciju na zaokruživanje.
4. Transformiši još pet atoma.
5. Primeni proizvoljnu rigidnu translaciju/rotaciju i pokaži da distance ostaju iste.

**Kontrola:** ne pretpostavljaj orthogonal ćeliju samo zato što tri parametra nose oznake a,b,c.

## L4 — Simetrija i periodični susedi

**Ulaz:** `cu_n14_a.cif`.

1. Pročitaj space-group symbol i IT number.
2. Izlistaj symmetry operations.
3. Od jednog atoma generiši general-position ekvivalente i wrap-uj fractional coordinates u ([0,1)).
4. Za ovaj N14 fixture i zadati kontaktni cutoff, nakon provere dometa, generiši candidates preko \(3\times3\times3\) translations oko referentnog molekula.
5. Ukloni duplikate koristeći symmetry/site identitet, ne samo zaokružen Cartesian string.
6. Pronađi najbliže međumolekulske O/N kontakte.
7. Za svaki zapiši symmetry operation i translation image.

**Kontrola:** kontakt preko granice ćelije mora ostati isti nakon wrap-a referentnog molekula.

\(3\times3\times3\) nije univerzalno pravilo. U opštem algoritmu potreban broj translacionih slika izvodi se iz cutoff-a i geometrije ćelije, a zatim se testira na vrlo kratkim i kosim ćelijama.

## L5 — Od kratkog kontakta do interakcione hipoteze

Koristi kandidate iz L4.

1. Za svaki kontakt navedi elemente, distance, potencijalne donor/acceptor uloge i dostupni angle.
2. Proveri protonation i H position confidence.
3. Obeleži `geometric candidate`, `chemically plausible`, `ambiguous` ili `rejected`.
4. Napiši jednu rečenicu dokaza i jednu moguću alternativu.
5. Uporedi pravila sa [IUPAC H-bond preporukom](https://publications.iupac.org/pac/83/8/1637/index.html).

**Kontrola:** nijedan kontakt nije automatski „jak“ samo zato što je kratak.

## L6 — ConQuest query anatomija

**Ulazi:** dva `.cqs` fajla i [ConQuest vodič](https://www.ccdc.cam.ac.uk/media/Documentation/2F0D7443-9739-46EB-BE9F-69E62E531FB7/2f0d7443973946ebbe9f69e62e531fb7.pdf).

1. Napravi atom/bond tabelu za 18-atomski zajednički query motif.
2. Označi centralni pyridine N i dva imine N.
3. U drugom query-ju pronađi atom 19 i njegov tip `4M`.
4. Nacrtaj connected components oba query-ja.
5. Napiši minimalnu tvrdnju koju drugi query dokazuje.
6. Predloži post-validation algoritam za tvrdnju „DAP koordinira metal“.
7. Sastavi šest pitanja za autora upita.

**Kontrola:** drugi query ima dve disconnected components; ne izmišljaj metal–N edge.

## L7 — Multi-format audit CSD izvoza

**Ulazi:** `search1.*` i `search2.*`.

Za svaki format izmeri:

- record count i identifier coverage;
- prazan/failed record count;
- 2D/3D availability;
- component count;
- unknown/dummy atom i bond type;
- cell/`CRYSIN` availability;
- SMILES coverage i duplicates;
- refcode family/revision groups.

Zatim:

1. proveri da je `search2` set i ordered subset `search1`;
2. izračunaj 72 uklonjena entry-ja;
3. proveri da li isti IDs nedostaju iz svih formata;
4. napravi contingency tabelu missing SMILES vs `un` bonds/`Du` atoms/empty structure;
5. objasni zašto opaženi dokazi ne podržavaju nekritičku MCAR pretpostavku i koje bi dodatne testove zahtevala jača tvrdnja;
6. napravi quality/error taxonomy umesto da obrišeš problematične rows.

**Kontrola:** broj SMI linija nije broj CIF entries i ne sme postati denominator bez oznake.

## L8 — Prvi similarity baseline

Radi samo na zapisima sa dovoljno pouzdanim molekulskim grafom.

1. Verzoniši standardization profile.
2. Izračunaj Morgan/circular fingerprints sa dokumentovanim radius/bit/stereo parametrima.
3. Izaberi jedan query i rangiraj Tanimoto candidates.
4. Za top 10 vizuelno/strukturno obeleži matched i unmatched motif.
5. Promeni radius ili tautomer/aromaticity policy i izmeri promenu ranga.
6. Dodaj exact DAP substructure filter.
7. Napiši tri hard negative primera.

**Kontrola:** fingerprint radi na grafu koji je parser dodelio; excluded/problematic records moraju biti prijavljeni, ne nevidljivi.

## L9 — Jedan evidence-rich par

Izaberi metal-free DAP ligand i jedan kandidat sa metalom, zatim dva koordinaciona kandidata.

Za svaki par popuni:

- composition/component relation;
- graph mapping i coverage;
- tri DAP donor atoma;
- metal membership i metal–donor edges;
- coordination number/geometry i uncertainty;
- conformational RMSD/torsions;
- cell/packing comparability;
- H-bond/contact evidence;
- data-quality compatibility;
- odluku po nivou, confidence i reviewer note.

**Kontrola:** dozvoljeno je ostaviti ukupni score `null` ako ključna semantika nije potvrđena.

## L10 — Invariance i adversarial suite

Napravi kontrolisane varijante jednog fixture-a:

1. promenjen atom order;
2. promenjen component order;
3. rigid rotation/translation;
4. periodic wrap;
5. symmetry-equivalent ASU;
6. ekvivalentan cell setting;
7. drugi validni SMILES traversal;
8. uklonjena stereo oznaka;
9. metal premešten u odvojenu komponentu;
10. dodata solvent voda.

Za svaku unapred napiši koje score komponente moraju ostati iste, koje se smeju promeniti i gde sistem mora da upozori.

**Kontrola:** očekivanja se pišu pre gledanja izlaza algoritma.

## L11 — Referentni signal i diffraction evidence

**Ulazi:** sintetički brojevi iz [lekcije 11A](11a-referentne-raspodele-hbp.md) i `tutorial-minimal.cif`.

1. Reprodukuj empirical percentile \(247/250\) i robustni \(z\) za 1,390 Å, medijanu 1,340 Å i MAD 0,012 Å.
2. Napiši četiri alternativna objašnjenja outlier-a koja ne tvrde energiju.
3. Izračunaj kružnu udaljenost između \(-179^\circ\) i \(+179^\circ\).
4. Za sintetički HBP primer napravi odvojena polja za individual propensity, uncertainty, observed status, grouping score, coordination score i fitting support.
5. Za cubic ćeliju \(a=5.6400\ \text{Å}\) izračunaj \(d(200)\) i \(2\theta\) za \(\lambda=1.5406\ \text{Å}\).
6. Napiši dva različita claim-a: jedan koji podržava simulated pattern i jedan koji bi zahtevao measured PXRD.

**Kontrola:** nijedan output ne sme da kaže „outlier = nestabilan“, „propensity = opažena veza“ ili „simulacija = potvrđen bulk uzorak“.

## Završna evidencija

Vežba je završena tek kada možeš odgovoriti:

- Šta je bio source of truth?
- Koje transformacije su bile lossy?
- Koju hemijsku tvrdnju rezultat podržava?
- Koju ne podržava?
- Koji edge case bi oborio zaključak?
- Može li drugi inženjer ponoviti rezultat iz manifesta?
