# Izvori i metod validacije

**Datum poslednje provere linkova i navedenih verzija: 2026-08-22.**

!!! danger "Dinamičke i licencne tvrdnje moraju ponovo da se provere"
    CCDC licenca, Conditions of Use, portfolio/proizvodi, API ponašanje, dokumentacija i broj CSD zapisa mogu se promeniti. Proveri ih **pre svakog izdanja, deployment-a, novog načina obrade, deljenja ili objavljivanja**, a ne samo na datum ove stranice. Merodavan je ugovor konkretne institucije i pisano tumačenje vlasnika podataka; ova knjiga nije pravni savet.

Ova strana ima dve uloge:

1. propisuje kako jedna tvrdnja postaje dovoljno proverena za kurs, kod, proizvod ili disertaciju;
2. daje organizovan registar primarnih i autoritativnih izvora korišćenih kroz kurs.

## Hijerarhija nije „jedan sajt je uvek najbolji“

Autoritet zavisi od vrste tvrdnje. IUPAC je pravi izvor za hemijski termin, ali nije izvor za ponašanje CSD Python API-ja. CCDC dokumentacija je pravi izvor za sopstveni proizvod, ali vendor white paper nije dovoljan dokaz univerzalnog naučnog mehanizma.

| Vrsta tvrdnje | Prvi izbor | Drugi dokaz | Šta nije dovoljno |
|---|---|---|---|
| hemijska nomenklatura/definicija | važeća IUPAC preporuka ili Gold Book termin sa verzijom | stručni originalni/review rad za kontekst | blog, search snippet, LLM odgovor |
| kristalografska definicija/CIF polje | IUCr dictionary, International Tables ili CIF dictionary | originalni metodološki rad/IUCr vodič | softverski tooltip bez verzije |
| naučni metod ili empirijski rezultat | originalni peer-reviewed rad i njegov tačan scope | nezavisna replikacija/review; lokalni benchmark | vendor claim ili citiranje samo apstrakta |
| CCDC funkcija/proizvod | zvanična CCDC dokumentacija tačne release/API verzije | reprodukcioni test u licenciranom okruženju | pretpostavka na osnovu imena funkcije |
| licenca/dozvoljena upotreba | potpisani ugovor institucije + važeći zvanični CCDC uslovi | pisana odluka CCDC-a/data owner-a i interni pravni review | private repo, tehnička dostupnost ili citat |
| broj/obim CSD-a | datirani CCDC statistics snapshot | query manifest za stvarno korišćen release | hardkodovana brojka bez datuma |
| lokalni fajl/upit | netaknut fajl + hash + deterministička inspekcija | nezavisna alatka/render i stručni review | filename ili opis pošiljaoca |
| uvodna hemija | autoritativni udžbenik kao OpenStax | IUPAC/IUCr izvor kada termin ulazi u šemu | popularni sažetak kao jedini dokaz |
| FAIR/provenance | originalni FAIR rad + W3C PROV standard | implementacioni profil i audit test | slogan „open by default“ |

### Praktična hijerarhija dokaza

1. **Normativni izvor:** standard, rečnik ili važeći ugovor određuje značenje/pravilo.
2. **Primarni naučni izvor:** originalni rad određuje metod, dataset i empirijski rezultat u svom scope-u.
3. **Reprodukcioni dokaz:** kod/test nad tačno navedenim verzijama pokazuje šta naš sistem radi.
4. **Lokalni dokaz:** hashirani ulaz i audit trag potvrđuju šta postoji u konkretnom artefaktu.
5. **Sinteza:** review/udžbenik povezuje teme, ali se kritičan claim vraća na nivoe 1–4.
6. **Orijentir:** blog, prezentacija, search rezultat ili LLM mogu pomoći da se izvor pronađe; nisu kraj validacije.

!!! note "Dve vrste „primarnog izvora“"
    Za tvrdnju „šta piše u `cu_n14_a.cif`“ primaran je lokalni fajl. Za tvrdnju „šta je occupancy“ primaran je IUCr rečnik. Lokalni primer ne postaje univerzalna definicija, a rečnik ne potvrđuje da je konkretan fajl ispravno refiniran.

## Protokol validacije tvrdnje

### Korak 1 — napiši atomaran claim

Loše:

> CSD je kvalitetna baza i naš similarity radi dobro.

Dobro:

> U CCDC snapshot-u datiranom 1. januar 2026. prijavljeno je 1.431.347 CSD struktura; ta brojka opisuje taj snapshot, ne budući release.

Hipotetički primer dobre forme tvrdnje (broj nije rezultat ovog projekta):

> Kada bi validirani held-out compound-family test skupa `eval-v1` pokazao 97,2%, tvrdnja bi glasila: candidate generator vraća 97,2% ekspertski relevantnih DAP analoga u prvih 100 kandidata, uz fingerprint profil `ecfp-v3` i navedeni interval neizvesnosti.

Jedan ledger red treba da sadrži jednu proverljivu tvrdnju. Spoj „i zato“ često skriva nedokazanu inferenciju.

### Korak 2 — klasifikuj promenljivost i rizik

| Klasa | Primer | Tipični review trigger |
|---|---|---|
| `normative-stable` | definicija Braggovog zakona, CIF data name | nova verzija standarda/rečnika ili godišnji audit |
| `scientific-scoped` | rezultat konkretnog peer-reviewed rada | novi dokaz, replikacija, promenjen projektni scope |
| `local-forensic` | 2.038 lokalna metal-filterovana rezultata | promena bilo kog fajla/hash-a ili parsera |
| `empirical-system` | recall@100 modela v1 | novi model, dataset, split, feature ili threshold |
| `dynamic-statistic` | broj CSD struktura 1.1.2026. | svaki novi CSD snapshot/release |
| `product-behavior` | API metoda/field podržani u eksplicitno navedenom release-u | upgrade API-ja, licence ili platforme |
| `licence-legal` | redistribucija CSD-derived podataka | svaki release/deployment/partner/purpose/ugovor |
| `interpretive` | nevidljivi, tematski nepodudarni embedded PDF tekst; „zaostali sloj/šablon“ je samo mogući uzrok | novi PDF forensic dokaz; uzrok jasno označiti kao inference |

### Korak 3 — pronađi izvor odgovarajuće vrste

- za termin: idi na IUPAC/IUCr definiciju, ne na sekundarni članak;
- za metod: pronađi originalni rad, ne samo kasniju implementaciju;
- za alat: otvori zvaničnu dokumentaciju i zabeleži verziju;
- za licencu: pročitaj aktuelni tekst i konkretni institucijski ugovor;
- za lokalni artefakt: izračunaj hash i sačuvaj reproduktivnu komandu/test;
- za broj: zabeleži `as_of` datum, release i direktan snapshot.

### Korak 4 — proveri šta izvor zaista podržava

Zapiši:

- tačnu sekciju, tabelu, CIF data name, stranu ili DOI;
- populaciju, uslove, dataset i ograničenja;
- da li je tekst definicija, opažanje, preporuka ili vendor opis;
- da li naš zaključak stoji direktno u izvoru ili je **inferencija**;
- moguću kontradikciju ili noviji izvor.

Naslov i apstrakt nisu dovoljni za numerički ili metodološki claim. DOI potvrđuje identitet rada, ne da naš sistem reprodukuje rezultat.

### Korak 5 — reprodukuj lokalno, gde je primenljivo

Za CIF:

1. schema-aware parse;
2. nezavisna provera ključnih data names;
3. formula/site/<code>Z</code>/density cross-check;
4. symmetry/PBC i round-trip test;
5. checkCIF uz lokalnu politiku poverljivosti;
6. stručni pregled alerts/hemije.

Za PDF:

1. original + hash + broj strana;
2. embedded text po strani;
3. render relevantnih/svih strana;
4. OCR/visible-text poređenje kada treba;
5. conflict log i human QA odluka.

Za ML:

1. immutable dataset/split manifest;
2. transparentni baseline;
3. leakage/family audit;
4. held-out metrike i intervali;
5. slice, calibration, abstention i invariance testovi;
6. model/feature/environment verzije.

### Korak 6 — review i životni ciklus

- `draft`: claim postoji, dokaz nije kompletan;
- `verified`: izvor i lokalni test pokrivaju ceo navedeni scope;
- `qualified`: tačan samo uz eksplicitno ograničenje;
- `disputed`: izvori/stručnjaci se ne slažu;
- `superseded`: novija definicija/verzija ga je zamenila;
- `blocked`: nedostaje dozvola ili ključni dokaz; ne ide u proizvod/publikaciju.

Confidence (`high/medium/low`) nikad ne zamenjuje status ni dokaz.

## Claim ledger: potrebne kategorije dokaza

Format nije propisan, ali svaki proverljiv zapis treba da odgovori na sledeće:

| Kategorija | Značenje |
|---|---|
| `claim_id` | stabilan interni ID, npr. `CLM-CIF-0042` |
| `claim_text` | atomarna, proverljiva rečenica bez skrivene generalizacije |
| `claim_class` | jedna od klasa iznad |
| `scope` | objekat, populacija, uslovi, verzija i izuzeci |
| `source_id` | DOI/URL/ugovor/local SHA-256 manifest |
| `support_location` | strana, sekcija, tabela, data name ili test ID |
| `support_type` | `direct`, `derived`, `inference`, `expert-judgement` |
| `local_evidence` | test/report/artifact verzija koja reprodukuje claim |
| `counterevidence` | poznati konflikt ili `none-found-as-of-date` |
| `status` | draft/verified/qualified/disputed/superseded/blocked |
| `confidence` | high/medium/low sa razlogom |
| `verified_by` | osoba/uloga; za critical claim poželjna dva reviewera |
| `verified_on` | datum provere |
| `revalidate_on` | datum ili event trigger |
| `supersedes` | prethodni claim/version ID, ako postoji |

Ovo su evidencione kategorije, ne buduća YAML schema, baza ili review workflow. Ista informacija može živeti u tabeli, registru ili drugom odobrenom formatu.

## Primeri claim ledger-a za 2CDC

| ID | Sažeta tvrdnja | Dokaz i scope | Status/revalidacija |
|---|---|---|---|
| `CLM-LOCAL-CIF-001` | `cu_n14_a.cif` navodi `C25 H20 N3 O2 P`; Cu nije u formula/site elementima. | lokalni CIF, formula fields + atom-site loop; filename i `Cu Kα` nisu sastav | `verified`; ponovi ako se hash/parser promeni |
| `CLM-LOCAL-CIF-002` | isti CIF navodi R(all)=0,0347, wR(ref)=0,0838 i GoF=1,095. | direktna CIF polja; bez claim-a da jedan broj „dokazuje kvalitet“ | `verified/qualified`; ponovi na promeni fajla |
| `CLM-LOCAL-QUERY-003` | lokalni `search2` je podskup `search1` sa 2.038/2.110 refcodes; query `4M` nije povezan sa DAP motivom. | hashirani eksporti + set diff + `.cqs` constraints + ConQuest guide; važi samo za dostavljene fajlove | `verified/qualified`; novi query/export zahteva novi ledger red |
| `CLM-PDF-004` | embedded extraction sa strana 1–2 CCDC white paper-a vraća nevidljivi, tematski nepodudarni tekst o ultra-large GOLD docking-u koji render ne pokazuje. | originalni PDF, SHA-256 `3A4D2597158505C0B4956BB967B7DFA294FF7E8804AB29450444C9157D23C612`; page extraction + render svih 22 strana | `verified` kao lokalni konflikt; „zaostali sloj/šablon“ ostaje samo `inference` |
| `CLM-IUCR-005` | R i wR imaju različite definicije i ne smeju se tretirati kao ista skala. | IUCr CIF dictionary/statistical descriptors | `verified`; proveri dictionary verziju godišnje |
| `CLM-CSD-006` | CCDC snapshot 1.1.2026 navodi 1.431.347 struktura. | datirani official statistics PDF | `verified`; obavezno promeni/revalidiraj na sledećem release-u |
| `CLM-LIC-007` | javni Conditions of Use ograničava redistribuciju CSD komponenti i derived software/data bez odgovarajućeg odobrenja. | važeći CCDC Conditions of Use; konkretan institucijski ugovor ima prednost | `qualified`; legal review pre svakog načina deljenja/objave |
| `CLM-FAIR-008` | FAIR Accessible ne zahteva anoniman/open pristup; A1.2 dopušta authentication/authorization kada su potrebni. | originalni FAIR principi | `verified`; FAIR nije quality ili licence grant |
| `CLM-GSK-009` | u Kalash et al. analiziranom skupu GSK i CSD Drug Subset se podudaraju u nekim crystal descriptors, ali ne u diversity solid-form space. | originalni rad D1CE00665G; ne generalizovati na svaku proprietary bazu | `qualified`; novi dataset/studija zahteva nov claim |
| `CLM-ML-010` | federativno učenje ne daje samo po sebi punu privatnost. | FedAvg definiše decentralized update obrazac; secure aggregation i leakage radovi pokazuju dodatni threat model | `verified` kao bezbednosno ograničenje; revalidirati protokol/implementaciju |

## Pravila citiranja u kursu, kodu i disertaciji

- U tekstu navedi **tačan claim uz izvor**, ne listu URL-ova na kraju bez veze.
- Za definiciju navedi verziju rečnika kada je dostupna; IUPAC Gold Book se aktivno ažurira.
- Za DOI rad navedi autore, naslov, časopis/godinu i DOI u bibliografiji disertacije.
- Za software/API rezultat navedi CCDC release/API verziju, licence boundary i parametre.
- Za CSD statistiku uvek navedi `as of` datum.
- Za lokalni fajl navedi filename samo radi čitljivosti; identitet zasnivaj na hash-u i manifestu.
- Direktan citat koristi samo kada je formulacija normativno važna; inače sažmi svojim rečima i ne kopiraj duge odlomke.
- White paper je izvor ciljeva i primera; svaki naučni claim iz njega proveri u standardu ili originalnom radu koji citira.
- Claim u disertaciji koji zavisi od našeg modela mora imati zamrznut dataset/split/model/test manifest, ne samo Git commit.

## Autoritativni izvori: IUPAC

IUPAC izvori određuju hemijsku nomenklaturu i preporučene definicije. Online Gold Book termin navodi sopstveni DOI/status; verziju termina treba zabeležiti u ledger-u.

### Opšti jezik i koordinaciona hemija

| Izvor | Za šta se koristi u kursu |
|---|---|
| [IUPAC Gold Book — početna strana](https://goldbook.iupac.org/) | centralni indeks hemijske terminologije |
| [IUPAC Periodic Table](https://iupac.org/what-we-do/periodic-table-of-elements/) | važeći simboli, imena i standardni periodni sistem |
| [Ligands, L03518](https://goldbook.iupac.org/terms/view/L03518) | značenje liganda u koordinacionoj hemiji |
| [Coordination entity, C01330](https://goldbook.iupac.org/terms/view/C01330) | centralni atom + ligands kao jedinka |
| [Crystal field, CT06770](https://goldbook.iupac.org/terms/view/CT06770) | razdvajanje crystal-field i ligand-field pojma |
| [Ligand-field splitting, L03517](https://goldbook.iupac.org/terms/view/L03517) | termin za cepanje orbitalnih energetskih nivoa |
| [High-/low-spin, LT06788](https://doi.org/10.1351/goldbook.LT06788) | precizna razlika načina popunjavanja split \(d\)-orbitala |
| [Jahn–Teller effect, J03361](https://goldbook.iupac.org/terms/view/J03361) | veza elektronske degeneracije i strukturne distorzije |
| [Unit cell, U06562](https://goldbook.iupac.org/terms/view/U06562) | hemijsko-terminološka definicija ćelije; IUCr ostaje detaljniji kristalografski izvor |
| [Standard uncertainty, S05928](https://goldbook.iupac.org/terms/view/S05928) | s.u. kao jedna standardna devijacija |

### Interakcije i čvrste forme

| Izvor | Za šta se koristi |
|---|---|
| [IUPAC preporuka: definition of the hydrogen bond](https://publications.iupac.org/pac/83/8/1637/index.html) | kriterijumi i terminologija H-veze |
| [IUPAC preporuka: definition of the halogen bond](https://publications.iupac.org/pac/85/8/1711/index.html) | kriterijumi i terminologija halogene veze |
| [Polymorph, 15225](https://goldbook.iupac.org/terms/view/15225) | osnovna definicija polimorfa u pharmaceutics kontekstu |
| [Crystal polymorph, 14219](https://goldbook.iupac.org/terms/view/14219) | crystalline phase terminologija, naročito napomene za polimere |
| [Solvate, 15234](https://goldbook.iupac.org/terms/view/15234) | solvat |
| [Hydrate, 15195](https://goldbook.iupac.org/terms/view/15195) | hidrat |

## Autoritativni izvori: IUCr

### Rečnik kristalografije

| Izvor | Uloga |
|---|---|
| [IUCr Online Dictionary](https://dictionary.iucr.org/) | ulaz u standardizovane kristalografske pojmove |
| [Crystal structure](https://dictionary.iucr.org/Crystal_structure) | kristalna struktura naspram molekula/rešetke |
| [Unit cell](https://dictionary.iucr.org/Unit_cell) | ćelija i njena translaciona uloga |
| [Asymmetric unit](https://dictionary.iucr.org/Asymmetric_unit) | minimalni nezavisni deo space-group prostora |
| [Space group](https://dictionary.iucr.org/Space_group) | grupa operacija periodične simetrije |
| [Lattice system](https://dictionary.iucr.org/Lattice_system) | razlika lattice-system i crystal-system klasifikacije |
| [Miller indices](https://dictionary.iucr.org/Miller_indices) | značenje \((hkl)\) ravni/refleksije |
| [Reciprocal lattice](https://dictionary.iucr.org/Reciprocal_lattice) | operativni real-space/reciprocal-space most |
| [Bragg's law](https://dictionary.iucr.org/Bragg%27s_law) | `2d sin θ = nλ` i difrakcioni uslov |
| [Refinement](https://dictionary.iucr.org/Refinement) | razlika structure solution/refinement i cilj optimizacije |
| [Statistical descriptors](https://dictionary.iucr.org/Statistical_descriptors) | residuals, uncertainty i tumačenje statistike |
| [Co-crystal](https://dictionary.iucr.org/Co-crystal) | kristalografska definicija kokristala i terminološki opseg |
| [Crystallographic Information Framework](https://dictionary.iucr.org/Crystallographic_Information_Framework) | priroda CIF standarda |

### CIF, validacija i učenje simetrije

| Izvor | Uloga |
|---|---|
| [IUCr CIF dictionaries](https://www.iucr.org/resources/cif/dictionaries) | autoritativna semantika data names; zabeležiti dictionary verziju |
| [Core CIF dictionary browser](https://www.iucr.org/resources/cif/dictionaries/browse/cif_core) | direktna provera polja iz `cu_n14_a.cif` |
| [IUCr CIF guide](https://www.iucr.org/__data/assets/pdf_file/0019/22618/cifguide.pdf) | praktična sintaksa/data-block/loop osnova |
| [checkCIF](https://checkcif.iucr.org/) | strukturisana validacija CIF-a; za poverljive podatke prethodno proveriti policy slanja |
| [checkCIF FAQ](https://journals.iucr.org/services/cif/checking/checkfaq.html) | alerts i Validation Response tumačenje |
| [PLAT076 primer](https://journals.iucr.org/services/cif/checking/PLAT076.html) | occupancy/site multiplicity zamka |
| [Teaching pamphlet 2](https://www.iucr.org/education/pamphlets/2/full-text) | početnička mapa sistema i 14 Bravaisovih rešetki |
| [IUCr Bravais nomenklatura](https://www.iucr.org/resources/commissions/crystallographic-nomenclature/bravais) | standardne oznake `aP`–`cF` i trigonal/rhombohedral nijansa |
| [Teaching pamphlet 9](https://www.iucr.org/education/pamphlets/9) | matrice, translacije i transformacije |
| [Teaching pamphlet 10](https://www.iucr.org/education/pamphlets/10) | metric tensor i ćelijska geometrija |
| [Teaching pamphlet 21](https://www.iucr.org/education/pamphlets/21) | crystal packing |
| [Powder CIF dictionary](https://www.iucr.org/resources/cif/dictionaries/browse/cif_pd) | measured/calculated powder data, radiation, instrument i profile metadata |

## Autoritativni izvori: CCDC/CSD

Ovi linkovi su autoritativni za CCDC proizvode i njihove javne uslove, ali su **dinamički**. U produkcionom claim-u navedi datum pristupa, CSD Software/API release i stvarni ugovor.

### Baza, statistika, citiranje i licenca

| Izvor | Uloga i ograničenje |
|---|---|
| [CCDC Conditions of Use za CSD Portfolio/API](https://downloads.ccdc.cam.ac.uk/documentation/API/conditions_of_use.html) | javna licencna granica; konkretan ugovor/pisano odobrenje su merodavni |
| [CCDC Standard Licence Agreement stranica](https://www.ccdc.cam.ac.uk/licence-agreement/) | zvanični ulaz u standardni ugovor; proveriti trenutno izdanje i institucijski dodatak |
| [How does licensing work for the CSD Portfolio?](https://support.ccdc.cam.ac.uk/support/solutions/articles/103000306234-how-does-licensing-work-for-the-csd-portfolio-) | aktuelni produktni/licencni kontekst; nije zamena za ugovor |
| [CSD Entry Summary Statistics — 1 January 2026](https://www.ccdc.cam.ac.uk/media/CSD-Entries-Summary-Statistics-2026.pdf) | datirani broj 1.431.347 struktura i drugi snapshot pokazatelji; ne hardkodovati kao trajne |
| [How should I reference the CSD?](https://support.ccdc.cam.ac.uk/support/solutions/articles/103000306259-how-should-i-reference-the-csd-) | trenutno preporučena opšta CSD referenca; proveriti pre publikacije |
| [Groom et al. 2016: The Cambridge Structural Database](https://doi.org/10.1107/S2052520616003954) | peer-reviewed opis CSD-a i preporučena naučna referenca |
| [Taylor & Wood 2019: A Million Crystal Structures](https://doi.org/10.1021/acs.chemrev.9b00155) | pregled razvoja i naučne ponovne upotrebe CSD znanja |

### CSD Python API i ConQuest ponašanje

| Izvor | Uloga |
|---|---|
| [CSD Python API dokumentacija](https://downloads.ccdc.cam.ac.uk/documentation/API/) | release notes, podržane funkcije i verzije |
| [Reading/writing molecules and crystals](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/io.html) | razlika molekulskog i crystal I/O modela |
| [Search philosophy](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/search_philosophy.html) | vrste CSD pretrage |
| [Substructure searching](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/substructure_searching.html) | query graph i constraints |
| [Similarity searching](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/similarity_searching.html) | CCDC similarity behavior/parameters |
| [Reduced-cell searching](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/reduced_cell_searching.html) | lattice candidate search i tolerancije |
| [Molecular geometry analysis](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/molecular_geometry_analysis.html) | CSD-based bond/angle/torsion distribucije i standardizacija |
| [Crystal objects, packing i contacts](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/crystal.html) | symmetry expansion i crystal-level funkcije |
| [Packing similarity](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/packing_similarity.html) | CCDC implementation parameters/results; vezati na tačnu verziju |
| [Hydrogen-bond propensities](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/hbond_propensities.html) | fitting evidence, logistic model, propensities, uncertainty i grouping/coordination output |
| [Disorder](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/disorder.html) | CCDC representation/obrada disorder-a |
| [Descriptors](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/descriptors.html) | definicije dostupnih descriptor objekata |
| [ConQuest User Guide](https://www.ccdc.cam.ac.uk/media/Documentation/2F0D7443-9739-46EB-BE9F-69E62E531FB7/2f0d7443973946ebbe9f69e62e531fb7.pdf) | semantika `4M` i query UI; sačuvati verziju uz `.cqs` manifest |

!!! warning "Dokumentacija ne dokazuje lokalnu licencu"
    To što API stranica opisuje funkciju ne znači da je funkcija dostupna u vašem product tier-u, da imate CSD data access ili da rezultat smete eksportovati. Capability test i permission test su odvojeni.

## Originalni i peer-reviewed radovi korišćeni u kursu

### Kristalne interakcije i packing

| Rad | Zašto je ovde |
|---|---|
| [Etter, MacDonald & Bernstein 1990: Graph-set analysis of hydrogen-bond patterns in organic crystals](https://doi.org/10.1107/S0108768189012929) | originalna graph-set sistematika za H-bond motive |
| [Bernstein et al. 1995: Patterns in Hydrogen Bonding: Functionality and Graph Set Analysis in Crystals](https://doi.org/10.1002/anie.199515551) | proširenje/praktična primena graph-set jezika |
| [Galek et al. 2007: Knowledge-based model of hydrogen-bonding propensity](https://doi.org/10.1107/S0108768107030996) | primarni HBP metod; statistički output nije energetski ili polymorph oracle |
| [Chisholm & Motherwell 2005: COMPACK](https://doi.org/10.1107/S0021889804027074) | originalni pristup za prepoznavanje crystal-structure/packing sličnosti |

### Cheminformatika i reprezentacije

| Rad | Zašto je ovde |
|---|---|
| [Rogers & Hahn 2010: Extended-Connectivity Fingerprints](https://doi.org/10.1021/ci100050t) | primarni ECFP/circular fingerprint metod; implementation parametri i dalje moraju biti navedeni |
| [Groom et al. 2016: The Cambridge Structural Database](https://doi.org/10.1107/S2052520616003954) | sadržaj, kuracija i uloga CSD-a |
| [Taylor & Wood 2019: A Million Crystal Structures](https://doi.org/10.1021/acs.chemrev.9b00155) | širok pregled strukturnog znanja izvedenog iz CSD-a |

### Čvrste forme i relevantnost proprietary podataka

| Rad | Zašto je ovde i granica claim-a |
|---|---|
| [Aitipamula et al. 2012: Polymorphs, Salts, and Cocrystals — What's in a Name?](https://doi.org/10.1021/cg3002948) | stručna terminološka rasprava; regulatorna klasifikacija se dodatno proverava u aktuelnom FDA/EMA kontekstu |
| [Bryant et al. 2019: The CSD Drug Subset](https://doi.org/10.1016/j.xphs.2018.12.011) | scope approved-drug crystal subset-a i poređenje hemijskog prostora; broj zapisa je istorijski rezultat tog rada |
| [Xin et al. 2019: Solvate Prediction for Pharmaceutical Organic Molecules with Machine Learning](https://doi.org/10.1021/acs.cgd.8b01883) | primer CSD-derived supervised ML za solvate propensity; ne preneti objavljeni performance van njihovog skupa |
| [Kalash et al. 2021: First global analysis of the GSK database of small molecule crystal structures](https://doi.org/10.1039/D1CE00665G) | direktan dokaz da public/proprietary skupovi mogu pokriti različit solid-form prostor; zaključak je scoped na analizirane baze |
| [FDA Guidance: Regulatory Classification of Pharmaceutical Co-Crystals](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/regulatory-classification-pharmaceutical-co-crystals) | zvanični regulatorni kontekst; nije univerzalna hemijska definicija i mora se revalidirati |

### FAIR, provenance i federativna privatnost

| Izvor/rad | Zašto je ovde |
|---|---|
| [Wilkinson et al. 2016: FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18) | originalni FAIR principi; A1.2 pokazuje da Accessible može uključiti auth/authz |
| [W3C PROV-O Recommendation](https://www.w3.org/TR/prov-o/) | formalni model entity–activity–agent provenance relacija |
| [McMahan et al. 2017: Communication-Efficient Learning of Deep Networks from Decentralized Data](https://proceedings.mlr.press/v54/mcmahan17a.html) | primarni FedAvg/federated-learning obrazac |
| [Bonawitz et al. 2017: Practical Secure Aggregation for Privacy-Preserving Machine Learning](https://acmccs.github.io/papers/p1175-bonawitzA.pdf) | secure aggregation kao dodatna kontrola, pod navedenim threat model-om |
| [Zhu, Liu & Han 2019: Deep Leakage from Gradients](https://proceedings.neurips.cc/paper_files/paper/2019/file/60a6c4002cc7b29142def8871531281a-Paper.pdf) | konkretan dokaz da gradient/update razmena može otkriti input informacije |

## OpenStax: početnički most do standarda

[OpenStax Chemistry 2e](https://openstax.org/details/books/chemistry-2e) je autoritativan, otvoreno dostupan udžbenički uvod. Koristi se za intuiciju i osnovne primere; kada pojam ulazi u produkcionu šemu, definicija se proverava u IUPAC/IUCr izvoru.

| Tema kursa | Direktna OpenStax strana |
|---|---|
| atomska struktura, izotopi i simboli | [2.3 Atomic Structure and Symbolism](https://openstax.org/books/chemistry-2e/pages/2-3-atomic-structure-and-symbolism) |
| hemijske formule | [2.4 Chemical Formulas](https://openstax.org/books/chemistry-2e/pages/2-4-chemical-formulas) |
| jonska i molekulska jedinjenja | [2.6 Ionic and Molecular Compounds](https://openstax.org/books/chemistry-2e/pages/2-6-ionic-and-molecular-compounds) |
| Lewisovi simboli i veze | [7.3 Lewis Symbols and Structures](https://openstax.org/books/chemistry-2e/pages/7-3-lewis-symbols-and-structures) |
| formalni naboj i rezonanca | [7.4 Formal Charges and Resonance](https://openstax.org/books/chemistry-2e/pages/7-4-formal-charges-and-resonance) |
| VSEPR, 3D geometrija i polaritet | [7.6 Molecular Structure and Polarity](https://openstax.org/books/chemistry-2e/pages/7-6-molecular-structure-and-polarity) |
| intermolekulske sile | [10.1 Intermolecular Forces](https://openstax.org/books/chemistry-2e/pages/10-1-intermolecular-forces) |
| rešetke i kristalne čvrste supstance | [10.6 Lattice Structures in Crystalline Solids](https://openstax.org/books/chemistry-2e/pages/10-6-lattice-structures-in-crystalline-solids) |
| Brønsted–Lowry acid/base | [14.1 Brønsted–Lowry Acids and Bases](https://openstax.org/books/chemistry-2e/pages/14-1-bronsted-lowry-acids-and-bases) |
| Lewis acid/base i kompleksi | [15.2 Lewis Acids and Bases](https://openstax.org/books/chemistry-2e/pages/15-2-lewis-acids-and-bases) |
| Gibbsova slobodna energija | [16.4 Free Energy](https://openstax.org/books/chemistry-2e/pages/16-4-free-energy) |
| funkcionalne grupe | [OpenStax Organic Chemistry 3.1](https://openstax.org/books/organic-chemistry/pages/3-1-functional-groups) |

## Dodatni standardi i referentna dokumentacija

Ovi izvori su korisni za implementaciju, ali se njihova software/version semantika mora zamrznuti u manifestu:

- [Daylight SMILES theory](https://www.daylight.com/dayhtml/doc/theory/) — originalna teorija SMILES/SMARTS jezika;
- [RDKit Getting Started](https://www.rdkit.org/docs/GettingStartedInPython.html) — konkretna open-source implementacija fingerprints/descriptors; ne pretpostavljati kompatibilnost verzija;
- [Open Babel format overview](https://openbabel.org/docs/FileFormats/Overview.html) — format conversion mogućnosti; uspešna konverzija nije dokaz očuvanja značenja;
- [spglib symmetry dataset](https://spglib.readthedocs.io/en/stable/dataset.html) — standardization/symmetry output polja i verzije;
- [MIT OCW 3.091 Solid-State Chemistry](https://ocw.mit.edu/courses/3-091-introduction-to-solid-state-chemistry-fall-2018/) — dodatni edukativni most za rešetke i čvrsto stanje;
- [GO FAIR: difference between FAIR and Open](https://www.go-fair.org/resources/faq/ask-question-difference-fair-data-open-data/) — praktično objašnjenje; normativni claim vraćaj na originalni FAIR rad.

## Lokalni artefakti: šta mogu, a šta ne mogu da dokažu

| Artefakt | Validan lokalni dokaz | Nije validna generalizacija |
|---|---|---|
| `CCDC_white_paper_sharpen.pdf` | teme/problemi koje vendor white paper naglašava; 22 strane; konflikt nevidljivog, tematski nepodudarnog embedded teksta i rendera | univerzalna tačnost svakog marketinškog/naučnog claim-a; svaki cited rad se proverava zasebno |
| `dve funkcionalnosti.txt` | trenutni opis željena dva proizvoda | završni requirements, scientific definitions ili acceptance thresholds |
| `cu_n14_a.cif` | konkretna formula, ćelija, <code>P 2₁/c</code>, 100 K, refinement fields i ugrađeni blokovi | globalna distribucija CSD-a ili univerzalni quality prag |
| `N14.mol` / `N14.mol2` | kako dva izvoza kodiraju atoms/bonds/types/charges za ovaj primer | koji format je „uvek tačniji“ |
| `search1/search2` izvozi i `.cqs` | lokalni refcode skupovi, njihov set odnos i stvarni constraints | unbiased uzorak celog CSD-a ili dokaz DAP–metal koordinacije |

Svaki lokalni claim mora navesti hash konkretnog izvora. Ako fajl ne sme u repo, manifest može čuvati hash, originalno ime, owner/licence status, bez samog sadržaja.

## Šta ne prihvatamo kao finalni dokaz

- search-engine summary bez otvaranja izvora;
- Wikipedia ili blog kao jedini izvor kritične definicije;
- LLM odgovor, uključujući ovu knjigu, bez claim ledger dokaza;
- naslov rada bez čitanja metoda/scope-a;
- screenshot bez URL-a, datuma i verzije;
- vendor feature lista bez reprodukcionog testa;
- filename ili naziv ConQuest query-ja kao hemijska etiketa;
- korelacija kao uzročni claim;
- jedan globalni prosek bez relevantnih slices;
- `private`, `academic` ili `FAIR` kao zamena za licencu.

## Kada dokaz može da zastari

| Promena/događaj | Koji deo tvrdnje može izgubiti važenje |
|---|---|
| novi CSD/API release | statistike, product behavior, query rezultat i representation kontekst |
| novi partner, lokacija ili svrha | ugovor, dozvoljene operacije, primaoci, retention i derivati |
| nova publikacija/disertaciona tvrdnja | scope, DOI metadata, dataset/model snapshot, novija literatura i limitations |
| nova IUPAC/IUCr/regulatorna verzija | terminologija, standard i regulatorni kontekst |
| incident ili promenjen source hash | svi povezani downstream nalazi i zaključci |

Tačan raspored, odgovorne uloge i procedure održavanja nisu deo plana učenja.

## Završna kontrolna lista izvora

- [ ] Svaka kritična rečenica ima `claim_id`.
- [ ] Izvor je odgovarajućeg tipa za tvrdnju.
- [ ] Pročitana je podržavajuća sekcija, ne samo snippet/apstrakt.
- [ ] Direktan dokaz i naša inferencija su odvojeni.
- [ ] Scope, uslovi, dataset, verzije i izuzeci su zapisani.
- [ ] Lokalni artefakt ima hash i reprodukcioni test.
- [ ] Dinamična brojka ima `as_of` datum.
- [ ] Software ponašanje ima verziju i capability test.
- [ ] Licencni claim ima ugovor/review trigger i fail-closed status.
- [ ] Kontradiktoran ili noviji dokaz je zabeležen.
- [ ] Datum provere je `2026-08-22` ili noviji.
- [ ] U publikaciji nema tvrdnje šire od dokaza.

Kada sva polja postoje, „verovali smo izvoru“ postaje proverljiv lanac: **claim → autoritativni izvor → lokalni dokaz → review → verzija → revalidacija**.
