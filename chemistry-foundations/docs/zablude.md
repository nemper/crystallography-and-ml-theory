# Opasne zablude

Ovo nije lista trivijalnih grešaka. Svaka zabluda ispod može napraviti naučno pogrešan label, nevalidan similarity score, curenje licence ili sistem koji deluje ubedljivo baš kada nema dokaz.

Čitaj poslednju kolonu kao **konceptualnu posledicu i ilustrativan način opovrgavanja zablude**. Ona ne propisuje buduća polja, fixture-e, UI ponašanje, gate-ove ili review proceduru; konkretan oblik eventualne realizacije određuje se kasnije.

Broj u prvoj koloni je identifikator zablude, ne redosled čitanja; redovi su grupisani po temi.

## 1. Identitet, sastav i hemijske veze

| # | Zabluda | Šta je tačno | Konceptualna posledica / primer provere |
|---:|---|---|---|
| 1 | „Ista molekulska formula znači isti molekul.“ | Formula daje broj elemenata, ne povezanost. Etanol i dimetil-etar dele \(\mathrm{C_2H_6O}\), a različiti su konstitucioni izomeri. | Formula je jeftin filter, nikad exact graph label. Test: isti sastav/drugi graf mora biti hard negative. |
| 2 | „Isti molekul znači isti CSD entry.“ | Entry predstavlja konkretno određivanje kristala; isti compound može imati više temperatura, redeterminations, polimorfa i solvata. | Deduplikacija mora imati odvojene `entry`, `chemical entity`, `solid form` i `determination` identitete. |
| 3 | „Isti SMILES znači isti kristal.“ | Standardni SMILES opisuje molekulski graf, ne ćeliju, simetriju, packing, occupancy ili eksperiment. | SMILES exact-match ne sme biti packing/polymorph ground truth. Test: isti SMILES, dva dokazano različita packing-a. |
| 4 | „Različiti SMILES stringovi znače različite molekule.“ | Isti graf ima mnogo validnih traversal zapisa; canonical SMILES zavisi od implementacije/verzije. | Pre string poređenja uradi parser + graph identity pod eksplicitnim charge/stereo/isotope policy-jem. |
| 5 | „Ime fajla je hemijski metadata.“ | Filename je ljudska oznaka. `cu_n14_a.cif` nema Cu u formuli/atom sites; `Cu Kα` je izvor rendgenskog zračenja. | Element filter koristi strukturisana polja i cross-check, nikad substring imena. `cu` u imenu, bez Cu u formuli ili atomskim mestima, direktan je kontraprimer. |
| 6 | „Formula u CIF-u je nepogrešiva.“ | Formula je prijavljena/izvedena stavka i može biti nesaglasna sa atom sites, occupancy, symmetry multiplicity ili \(Z\). | Neslaganje formula sum/moiety, site composition, charge i density računa pokazuje internu nekonzistentnost; samo po sebi ne utvrđuje da je greška u sastavu. |
| 7 | „Formalni, oksidacioni i parcijalni naboj su isti broj.“ | Formal charge je Lewis knjigovodstvo; oxidation state jonska formalizacija; partial charge zavisi od modela i obično nije ceo broj. | Formalni, oksidacioni i parcijalni naboj nisu zamenljive veličine; vrednost jedne ne određuje druge. |
| 8 | „Nula u MOL2 charge koloni dokazuje nepolarnost.“ | `NO_CHARGES`/nule mogu značiti da parcijalni charge model nije dodeljen. Polarne veze i dipol i dalje mogu postojati. | `charge_model=none` je missing model, ne fizička nula. Ne koristiti kao feature bez provenance-a. |
| 9 | „Bond order u fajlu je direktno eksperimentalno meren.“ | Difrakcija meri intenzitete; položaji/gustina se modeluju, a bond types se hemijski dodeljuju. Aromatic/unknown/metal bonds zavise od softvera. | Čuvaj originalni tip, perception alat/verziju i confidence. Testiraj razliku CIF/MOL/MOL2 prikaza istog uzorka. |
| 10 | „Uspešan valence check dokazuje tačnu hemiju.“ | Više pogrešnih grafova može zadovoljiti lokalna pravila valence; metali, disorder i delokalizacija dodatno komplikuju model. | Valence je jedan signal. Potrebni su formula, geometrija, charge, component i stručni cross-check. |
| 11 | „Svaki N ili O je donor/prihvatilac.“ | Protonacija, formalni naboj, rezonanca, amide-like delokalizacija i koordinacija menjaju raspoloživ lone pair. | Donor/acceptor etiketa je kontekstualna i verzionisana. DAP donor mapping proverava konkretne N atome. |
| 12 | „Nedostajući H nije važan za similarity.“ | H položaj određuje protonaciju, salt/cocrystal granicu, stereo, H-bond donor/acceptor uloge i interaction network. Rendgenski H često je modelovan. | Missing H daje uncertainty/ambiguous status; ne dodeljuj exact form identity bez dokaza. |
| 13 | „Neutralizacija, odvajanje soli i izbor tautomera su bezazlena normalizacija.“ | Te transformacije mogu promeniti stvarni objekat, charge, donor set, komponentu i query odgovor. | Čuvaj raw/full crystal i task-specific parent prikaze paralelno; transformation log mora navesti pravilo. |
| 14 | „Najveći fragment je uvek aktivni ligand/parent.“ | Counterion ili metalna mreža može biti veća; koordinacioni polimer nema jednostavan konačni „najveći molekul“. | Component role classification koristi hemiju i korisnički cilj. Uklanjanje ostalih komponenti menja identitet punog kristalnog sastava. |

## 2. Metali i koordinaciona hemija

| # | Zabluda | Šta je tačno | Konceptualna posledica / primer provere |
|---:|---|---|---|
| 15 | „Ako entry sadrži metal i DAP motiv, DAP koordinira metal.“ | Lokalni ConQuest `4M` atom je nepovezan sa 18-atomski DAP query motivom; dokazano je samo da se metal nalazi negde u istom entry-ju. | Candidate label nije coordination ground truth. Potrebni su component assignment, metal-neighbor perception i donor mapping. |
| 16 | „Metal–ligand veza postoji ako je rastojanje ispod jednog globalnog cutoff-a.“ | Tipične distance zavise od elemenata, oxidation/spin stanja, CN, geometrije, disorder-a i modela. | Neighbor model mora biti element/context-aware i verzionisan; blizina može vratiti `ambiguous`. |
| 17 | „Ako CIF/MOL nema nacrtanu metalnu vezu, koordinacije nema.“ | Neki formati/izvoznici metal connectivity ostavljaju unknown ili je izvode iz geometrije. Odsustvo ivice može biti odsustvo anotacije. | Razdvoji `explicit bond`, `inferred neighbor` i `expert-confirmed coordination`; ne pretvaraj missing u false. |
| 18 | „Koordinacioni broj je broj liganada.“ | CN broji direktne donor-atome; jedan tridentatni ligand doprinosi tri, a bridging ligand može vezati više centara. | CN, broj liganada, denticity i bridging su različiti deskriptori; isti CN može nastati iz različite raspodele donor-atoma po ligandima. |
| 19 | „Isti metal i isti CN znače istu geometriju.“ | CN=4 može biti tetraedarski, kvadratno-planaran ili između; distortion nosi bitnu informaciju. | Poredi angles/shape measures uz metal/donor mapping. Hard negative: isti M/CN, druga geometrija. |
| 20 | „Oksidaciono stanje se čita iz elementa ili formalnog broja veza.“ | Isti metal ima više oxidation states; covalency, charge i ligandi zahtevaju balans i stručni dokaz. | Ako evidence nije dovoljan, koristi `unknown/ambiguous`; ne imputiraj tipičnu vrednost kao činjenicu. |
| 104 | „Izduženi pseudo-octahedral Cu(II) automatski dokazuje Jahn–Teller efekat.“ | Obrazac je kompatibilan sa \(d^9\) efektom, ali ligandna nejednakost, strain, packing, disorder i model mogu dati sličnu geometriju. | Prijavi hipotezu uz oxidation state/\(d^n\), donor mapping, s.u., quality i alternativne uzroke. |
| 21 | „Coordination entity je isto što i ceo kristalni sastav.“ | Counterions, solventi i coformers mogu biti van koordinacione jedinke, a ipak su deo crystal form-a. | Zaključak zavisi od toga da li se poredi koordinaciona jedinka ili ceo kristalni sastav; ta dva scope-a nisu ekvivalentna. |
| 22 | „Metalni kompleksi se mogu standardizovati istim organskim sanitization pravilima.“ | Organska valenca/aromatičnost pravila mogu pogrešno cepati koordinacione veze ili menjati charges. | Neuspešna organska sanitizacija može značiti neadekvatan model, ne nevalidnu hemiju; ista pravila mogu izbrisati koordinaciju ili promeniti naboje. |

## 3. Kristal, simetrija i periodičnost

| # | Zabluda | Šta je tačno | Konceptualna posledica / primer provere |
|---:|---|---|---|
| 23 | „CIF je samo još jedan molekulski format.“ | CIF može opisati ćeliju, space group, ASU, occupancy, eksperiment, refleksije i refinement. CIF→SMILES je bogata-to-siromašna projekcija. | Molekulska projekcija gubi informacije i ne može podupreti tvrdnje o ćeliji, simetriji, occupancy-ju ili packing-u. |
| 24 | „Jedan CIF sadrži tačno jedan molekul.“ | Može imati više data block-ova, components, nezavisnih molekula, disorder alternatives, solvent i periodičnu mrežu. | Identitet i poređenje zavise od izabranog data block-a i objekta; prvi molekul nema poseban naučni status. |
| 25 | „ASU je isto što i jedna ćelija ili jedan molekul.“ | ASU je najmanji nezavisni deo iz kog simetrija generiše strukturu; može biti deo molekula ili više formula units. | Symmetry expansion mora prethoditi punom packing/contact računu. Čuvaj \(Z'\) uz ograničenja definicije. |
| 26 | „Svaki atom-site red je jedan pun atom u ćeliji.“ | Site se širi kroz symmetry multiplicity i ponderiše occupancy; special positions menjaju broj kopija. | Sastav računaj iz elementa × multiplicity × occupancy, ne brojem redova. |
| 27 | „Occupancy i multiplicity su isto.“ | Occupancy je populacija mesta; multiplicity broj symmetry-equivalent mesta. | Occupancy i multiplicity nezavisno ulaze u račun sastava i nisu zamenljivi. |
| 28 | „Frakcione koordinate su ångströmi.“ | Frakcione koordinate su koeficijenti cell vectors; u neortogonalnoj ćeliji kartezijanska konverzija koristi punu matricu. | Distance račun koristi cell matrix + PBC. Testiraj monoklinični `cu_n14_a.cif`. |
| 29 | „Atomi na 0,99 i 0,01 su daleko.“ | Periodični wrap može ih učiniti susedima preko granice ćelije. | Minimum-image/symmetry contact search; metamorphic test translacije za ceo lattice vector. |
| 30 | „Dve ćelije sa različitim parametrima moraju biti različiti kristali.“ | Ista rešetka/struktura može biti zapisana drugom bazom, setting-om, origin-om, konvencionalnom ćelijom ili supercell-om. | Standardizuj/redukuj pre candidate poređenja i proveri invertibilnu transformaciju. |
| 31 | „Slična reduced cell dokazuje isto pakovanje.“ | Metrika rešetke je samo candidate signal; sadržaj i orijentacije mogu biti drugačiji. | Packing proof zahteva mapirane periodične klastere, broj matched molecules, RMSD i parametre. |
| 32 | „Ista space group znači isti polimorf.“ | Hiljade različitih struktura mogu deliti \(P\,2_1/c\); space group je simetrijska kategorija. | Ne koristi space-group equality kao identity label; uključi composition, graph i packing. |
| 33 | „Različita space group automatski znači različit materijal.“ | Ekvivalentni settings mogu imati različite simbole; phase transition, pseudosymmetry ili različit izbor mogu zahtevati ekspertizu. | Kanonizuj space-group type/setting, zadrži original i transformation evidence. |
| 34 | „\(Z=Z'\).“ | \(Z\) broji formula units u ćeliji; \(Z'\) nezavisni ASU sadržaj u jednostavnom slučaju. Odnos uključuje multiplicity i može biti složen. | \(Z\) i \(Z'\) nisu zamenljive veličine; njihova jednakost važi samo u ograničenim slučajevima. |
| 35 | „Crystal packing je samo nearest-neighbor distance.“ | Packing uključuje periodični 3D raspored, orijentacije, više shells i component roles. | Izveštaj navodi shell/cluster, mapping, tolerancije i coverage; jedan kontakt nije packing score. |
| 36 | „Spoljašnji oblik kristala identifikuje unutrašnju strukturu.“ | Habit zavisi od relativnog rasta lica i uslova; ista struktura može imati različit habit, a sličan habit različite strukture. | Ne koristiti fotografiju/shape label kao polymorph ground truth bez difrakcionog dokaza. |

## 4. Difrakcija i quality — nema magičnog semafora

| # | Zabluda | Šta je tačno | Konceptualna posledica / primer provere |
|---:|---|---|---|
| 37 | „R < 0,05 znači dobar CIF; iznad toga odbaci.“ | R zavisi od sastava, disorder/twinning-a, rezolucije, apsorpcije, skupa refleksija i modela. Nizak R može pratiti pogrešan/prefleksibilan model. | Quality je vektor dokaza; prag, ako postoji za claim, validira se po domenu i ostaje objašnjiv. |
| 38 | „R(all), R(gt) i wR mogu direktno da se porede.“ | Koriste različite skupove/formule/težine; wR je često na \(F^2\), R na amplitudama. | Svaka vrednost nosi CIF field i semantics; ne rangiraj modele mešanim kolonama. |
| 39 | „GoF=1 dokazuje tačnu strukturu.“ | GoF blizu 1 govori da su weighted residuals saglasni sa pretpostavljenim uncertainties/weights; ne potvrđuje identitet, space group ili propušten solvent. | Pregledaj weights, residual density, geometriju, model i alerts. `cu_n14_a.cif` S=1,095 je dokaz samo u tom ograničenom smislu. |
| 40 | „checkCIF alert znači da je struktura nevalidna.“ | Alert označava anomaliju za pregled; opravdani izuzeci postoje i zahtevaju objašnjenje. | Čuvaj alert code/severity/response i review; ne briši zapis samo zbog boje. |
| 41 | „Bez checkCIF alert-a struktura je sigurno tačna.“ | Automatizovani testovi ne znaju punu hemijsku nameru, uzorak, sintezu ili svaki model defect. | Automatska validacija + hemijski/kristalografski pregled + scope-specific acceptance. |
| 42 | „Disorder znači loši podaci koje treba odbaciti.“ | Disorder može biti realna osobina ili najbolji prosečni model. Ignorisanje alternative menja sastav i kontakte. | Čuvaj alternatives/occupancy i quality confidence; samo claim koji zahteva jednoznačnu geometriju može abstain. |
| 43 | „Dve pozicije occupancy 0,5 su dva cela atoma.“ | Često su alternativni položaji iste populacije. Pretvaranje u dva puna atoma duplira masu i stvara lažne kontakte. | Disorder-group-aware expansion i formula round-trip test. |
| 44 | „Occupancy 1 dokazuje odsustvo disorder-a.“ | Samo pokazuje da u datom modelu mesto ima punu navedenu occupancy; ne isključuje nemodelovan nered ili druge sistematske probleme. | Formulacija izlaza mora biti „nema eksplicitno modelovanog disorder-a“, ne univerzalna negacija. |
| 45 | „H atomi su opaženi jednako pouzdano kao teži atomi.“ | X-ray rasipanje prati elektrone; H je slab i često idealizovan/refiniran uz constraints. | H-bond/protonation claim nosi H provenance i uncertainty; neutron/X-ray i refinement model nisu isti dokaz. |
| 46 | „Broj u zagradi je tolerancija ili interval.“ | `12.7138(3)` u CIF konvenciji znači s.u. 0,0003 poslednjih cifara, ne ±3 ili tri merenja. | Vrednost i s.u. čine povezanu mernu informaciju; razdvajanje menja značenje neizvesnosti. |
| 47 | „100 K kristalna geometrija je ista na sobnoj temperaturi.“ | Ćelija, ADP, konformacija, faza i disorder mogu zavisiti od temperature. | Temperature je deo identity/evidence i pair quality compatibility; ne spajaj uslove bez oznake. |
| 48 | „Jedan kvalitet score može bezbedno zameniti sva polja.“ | R, resolution, completeness, s.u., residuals, restraints, disorder, twinning i temperatura odgovaraju na različita pitanja. | Čuvaj quality vector; learned score mora ostati rastavljiv, kalibrisan i bez rigidnog univerzalnog cutoff-a. |
| 107 | „Simulirani PXRD iz CIF-a potvrđuje taj CIF i bulk uzorak.“ | Simulacija je derivat istog modela i zato kružni dokaz; nema informacije iz realnog bulk merenja. | Za fazni evidence koristi measured PXRD sa radiation/instrument/sample metadata i unapred definisanim poređenjem. |

## 5. Čvrste forme, stabilnost i svojstva

| # | Zabluda | Šta je tačno | Konceptualna posledica / primer provere |
|---:|---|---|---|
| 49 | „Svaka različita čvrsta forma je polimorf.“ | Salt, hydrate, drugi solvate i cocrystal menjaju component/charge/composition klasifikaciju; amorfno nije kristalni polymorph. | Solid-form relation je višekomponentna etiketa, ne jedno `polymorph=true`. |
| 50 | „Hidrat/solvat je nečist polimorf.“ | Molekuli vode/rastvarača mogu biti stehiometrijski, strukturno ključni deo jednofaznog kristala. | Komponentu ne briši kao noise; parent i full-form poređenje prikazuj odvojeno. |
| 51 | „So i kokristal se uvek razlikuju samo formulom.“ | Granica često zavisi od proton transfer-a i lokacije H; ista komponentna formula može biti ambiguous u slabom X-ray modelu. | Čuvaj protonation evidence, charge i terminološku verziju; dozvoli `salt–cocrystal ambiguous`. |
| 52 | „Najstabilnija forma prva kristališe.“ | Nukleacija i rast su kinetički; metastabilna forma može nastati prva i opstati zbog barijere. | Model property/form selection mora uključiti uslove, proces i vreme, ne samo energy rank. |
| 53 | „Metastabilno znači pogrešno ili neupotrebljivo.“ | Metastabilna faza je realan lokalni minimum i može imati korisna svojstva i dug vek. | Ne filtrirati label; zabeležiti uslove transformacije i storage rizik. |
| 54 | „Više talište uvek znači stabilniji polimorf.“ | Stabilnost određuje Gibbsova energija i može se menjati temperaturom; melting/enthalpy odnosi zahtevaju punu termalnu analizu. | Ne praviti universal rank iz jednog melting point-a. Potrebni DSC/solubility/transition podaci i context. |
| 55 | „Najniža energija izolovanog konformera daje najstabilniji kristal.“ | Kristalna stabilnost uključuje intermolekulske interakcije, packing, entropy i uslove; molekul može platiti conformational strain radi boljeg packing-a. | Gas-phase/conformer feature je samo jedan signal; ne label za polymorph stability. |
| 56 | „Jedan uspešan screen dokazuje da druge forme ne postoje.“ | Polymorph landscape zavisi od rastvarača, temperature, vlage, seeding-a, vremena i tehnike. Odsustvo dokaza nije dokaz odsustva. | Coverage protokola i negative claim scope moraju biti zapisani; sistem ne kaže „nema drugih formi“ bez granica. |
| 105 | „Mogul outlier ili 99. percentil znači visoku energiju/nestabilnost.“ | To je neuobičajenost u konkretnoj query/filter/release populaciji, ne energetski račun. | Čuvaj referentni manifest/support/applicability; energiju i fazu testiraj odvojenim modelom/eksperimentom. |
| 106 | „HBP propensity 0,8 znači da je H-veza opažena ili da polimorf postoji.“ | Propensity je output fitting/logistic modela za kandidatni par; observed status, grouping, coordination i realna faza su druga pitanja. | Prikaži output-e odvojeno sa evidence counts, uncertainty i applicability. |
| 57 | „Jedan difraktovani kristal predstavlja ceo bulk uzorak.“ | Izabrani single crystal može biti manjinska faza; bulk phase purity zahteva odgovarajuće tehnike (npr. powder diffraction/thermal analysis). | Ne prenosi single-crystal identity automatski na batch property label. |
| 58 | „Rastvorljivost i brzina rastvaranja su isto.“ | Prvo je ravnoteža, drugo kinetika zavisna od površine/habit-a/čestica i uslova. | Rastvorljivost i brzina rastvaranja su različita svojstva, a obe vrednosti zavise od jedinica i uslova merenja. |
| 59 | „Različit habit znači drugi polimorf.“ | Habit je spoljašnja morfologija; isti polymorph može rasti kao igla ili ploča. | Vizuelna klasifikacija nije crystal-form label bez strukturne potvrde. |
| 60 | „Crystal structure sama deterministički određuje property.“ | Property zavisi i od defekata, veličine čestica, kompozicije, temperature, procesa i mernog protokola. | Structure–property ML label nosi conditions/provenance i uncertainty; razdvojiti causal claim od korelacije. |

## 6. Formati, ingest i provenance

| # | Zabluda | Šta je tačno | Konceptualna posledica / primer provere |
|---:|---|---|---|
| 61 | „Konverzija CIF→SDF/SMILES samo menja ekstenziju.“ | Odbacuju se cell, symmetry, packing, occupancy i quality, a components/bonds se biraju ili inferiraju. | Svaka konverzija ima loss matrix, source link i task scope; original se čuva. |
| 62 | „Ako parser nije prijavio grešku, zapis je validan.“ | Sintaktički validan fajl može imati pogrešnu formulu, nesmislen graf, pogrešne units ili ozbiljne alerts. | Sintaktička ispravnost ne implicira hemijsku ili kristalografsku validnost, kvalitet dokaza ni dozvolu upotrebe. |
| 108 | „`parser_ok` znači `Curated`.“ | Sintaksno parsiranje i verzionisana automatska validacija nisu isto što i završena stručna/policy kuracija. | Parsiranje, automatska validacija, stručna kuracija i odobrenje za objavu jesu različiti nivoi potvrde; nijedan ne implicira sledeći. |
| 63 | „Canonical record je nova istina pa raw može da se obriše.“ | Canonical je rezultat verzionisanih odluka i može se promeniti. Bez raw dokaza nema audit-a niti ponovnog parsiranja. | Immutable original + hash, raw parsed, canonical i derived slojevi ostaju povezani. |
| 64 | „Canonical SMILES je globalni persistent identifier.“ | Canonicalization zavisi od toolkit-a, verzije, aromaticity, salt/tautomer/stereo policy-ja. | Za interni ID koristi stable source/version ID; SMILES čuvaj uz generator profil. |
| 65 | „Missing vrednost je isto što i nula.“ | `?`, `.`, blank, parse failure, not measured i not applicable nose različita značenja. | Različiti razlozi odsustva podatka imaju različito značenje; nijedan nije fizička nula, a njihovo mešanje može pristrasiti model. |
| 66 | „Nepoznato znači negativno.“ | Nema veze, nema H ili nema metal annotation može biti missing evidence, ne dokaz odsustva. | Ternary/multi-state labels: true/false/unknown/ambiguous/not-applicable. |
| 67 | „Hash potvrđuje da je sadržaj tačan.“ | Hash potvrđuje identitet bajtova. Isti pogrešan ili licencno nedozvoljen fajl ima savršeno stabilan hash. | Hash kombinuј sa validation, source, licence i review statusom. |
| 68 | „Ekstrahovan PDF tekst je ono što korisnik vidi.“ | Embedded text layer može sadržati skriveni/stari sadržaj. U CCDC white paper-u strane 1–2 izvlače nevidljiv tekst o ultra-large GOLD docking-u. | Neslaganje text layer-a i rendera čini ekstrahovani sadržaj nepotvrđenim dokazom za naučne tvrdnje. |
| 69 | „Nevidljiv/stari PDF tekst treba obrisati bez traga.“ | To bi uništilo dokaz incidenta i otežalo reprodukciju. | Raw evidence ostaje; canonical approved text ga isključuje uz datiranu odluku i parser/render verzije. |
| 70 | „Skriveni PDF tekst je samo dokumentni problem, nema veze sa hemijom.“ | Pogrešan tekst može kontaminirati RAG, klasifikaciju teme, labels, deduplikaciju i provenance. | Hemijske tvrdnje izvedene iz dokumenta nasleđuju neizvesnost ekstrakcije; nevidljiv tekst nije isto što i opažen sadržaj. |

## 7. Sličnost i ML evaluacija

| # | Zabluda | Šta je tačno | Konceptualna posledica / primer provere |
|---:|---|---|---|
| 71 | „Hemijska sličnost je objektivno jedan broj.“ | Composition, graph, coordination, conformation, packing, interactions i property relevance su različiti claim-i. | Prikazuj component scores/evidence; combined score samo verzionisan i task-kalibrisan. |
| 72 | „Tanimoto 0,8 univerzalno znači veoma slično.“ | Značenje zavisi od fingerprinta, radius-a, bit length-a, standardizacije, veličine i domena. | Score mora nositi representation profile; threshold se bira na validation set-u za konkretan task. |
| 73 | „2D fingerprint meri crystal packing.“ | Fingerprint lokalnog grafa ne kodira cell/symmetry/periodično okruženje. | Koristi ga za candidate generation, zatim posebno packing poređenje. Hard test: isti graf/drugi polymorph. |
| 74 | „Nizak RMSD dokazuje slične strukture.“ | RMSD može biti nizak na tri odabrana atoma, pogrešnom mapping-u ili mirror-u; zavisi od alignment policy-ja. | Navedi mapping, \(N\), coverage, max deviation, symmetry/H/stereo i coordinate provenance. |
| 75 | „RMSD se može računati pre component/atom mapping-a.“ | Bez uparivanja ne znaš koji atomi/komponente odgovaraju; ekvivalentni atomi daju više mapiranja. | Component mapping → atom mapping → alignment → RMSD, sa tie-breaker-om. |
| 76 | „`not comparable` je score 0.“ | Nula tvrdi validno izmerenu odsutnost sličnosti; `not comparable` znači da merenje nije moguće/primenljivo. | `Not comparable` je nedefinisano merenje, ne maksimalna udaljenost; tretiranje kao nule pristrasuje rangiranje i agregate. |
| 77 | „Embedding udaljenost je hemijska istina.“ | Embedding optimizuje cilj i bias trening podataka; može ignorisati metal, stereo ili packing. | Probe, hard-negative, out-of-domain i explanation testovi; transparentni baseline-i ostaju obavezni. |
| 78 | „Vector database je source of truth.“ | Indeks je lossy/verzionisani derived cache i može biti zastareo. | Original/provenance žive drugde; svaki vektor ima source/version ID i može se reindeksirati. |
| 79 | „Brz ANN je dobar retrieval sistem.“ | ANN može tiho propustiti relevantne kandidate. Latency bez recall-a nije validacija. | Merenje candidate recall-a prema exact/high-cost referenci ukupno i po slice-ovima. |
| 80 | „Top-k susedi sadrže sve parove iznad praga.“ | Asimetričan/pruned top-k može izostaviti relevantan par, naročito u gustom delu prostora. | Ako se tvrde svi parovi, empirijski dokaži recall prefiltera ili radi exact/all-pairs za dozvoljeni obim. |
| 81 | „Više podataka automatski daje bolji model.“ | Duplikati, pogrešne etikete, bias, missingness i licencne granice mogu pogoršati generalizaciju. | Data audit, family dedup, slice balans, label provenance i learning curves. |
| 82 | „Lokalni ConQuest rezultati reprezentuju ceo CSD.“ | To je query-conditioned DAP subset bez uključenih standardnih quality/3D filtera; pun CSD nije dostupan. | Ne generalizuj globalne distribucije. Evaluation population i query snapshot moraju biti eksplicitni. |
| 83 | „Random record split je dovoljno pošten.“ | Bliski refcodes, redeterminations, ista compound family ili publikacija mogu završiti na obe strane. | Group/scaffold/solid-form/time split prema claim-u, pre tuninga. |
| 84 | „Accuracy je dovoljna metrika.“ | Kod retkih pozitivnih parova model `sve negativno` može imati visoku accuracy; retrieval zahteva ranking metrike. | Precision/recall/PR-AUC, recall@k/nDCG, calibration, coverage i slice analiza. |
| 85 | „Lepa heatmap ili klaster dokazuje naučnu validnost.“ | Vizuelni obrazac može biti artefakt distance, linkage, scaling-a ili dataset bias-a. | Ground truth/rubrika, stability test, baseline i ekspertna analiza grupa pre claim-a. |
| 86 | „Ground truth je naziv query-ja ili database field.“ | Naziv izražava nameru; query constraints mogu biti slabiji. Kurirana polja mogu imati scope i missingness. | Naziv upita ili polja nije ground truth; validna etiketa zahteva unapred definisan kriterijum vezan za dokaze. |
| 87 | „Ako dva eksperta ne slažu, većina daje objektivnu istinu.“ | Neslaganje otkriva ambiguous definiciju ili nedovoljan dokaz. | Čuvaj individual labels/confidence/reason; adjudication i verzionisana rubrika. |
| 88 | „Score 0,9 znači 90% verovatnoću relevantnosti.“ | Sirov similarity/logit nije kalibrisana probability. | Validation calibration, reliability analiza i jasno različita polja `similarity`, `probability`, `evidence_confidence`. |
| 89 | „Visok model confidence poništava loš input.“ | Model može biti samouveren nad pogrešno percipiranim grafom ili out-of-domain metalom. | Input quality i model uncertainty su odvojeni; claim može abstain uprkos visokom score-u. |
| 90 | „Jedna ukupna metrika znači da sistem radi svuda.“ | Prosek može sakriti neuspeh za metale, solvates, disorder, velike/fleksibilne molekule ili missing 3D. | Ukupan prosek ne implicira pouzdanost po podgrupama; neuspeh u relevantnom slice-u ograničava opšti claim. |
| 91 | „LLM može sam potvrditi hemijsku istinu iz teksta/CIF-a.“ | LLM može korisno objašnjavati, ali može halucinirati, pogrešno parsirati i nema eksperimentalni oracle. | LLM izlaz nije nezavisan dokaz hemijske istine; zaključak ostaje ograničen primarnim podacima i proverljivim metodama. |

## 8. Federativno učenje, privatnost i licence

| # | Zabluda | Šta je tačno | Konceptualna posledica / primer provere |
|---:|---|---|---|
| 92 | „Federativno učenje garantuje privatnost jer raw fajlovi ne napuštaju instituciju.“ | Gradients/update-i i konačni model mogu odavati informacije; lokalni logovi i coordinator su deo threat model-a. | Secure aggregation/DP gde odgovara, leakage testovi, minimalni outputs i pravno odobren protokol. |
| 93 | „Secure aggregation rešava svaku privatnost.“ | Skriva pojedinačne update-e od servera pod pretpostavkama, ali ne rešava malicious clients, final-model inference, endpoint security ili licencu. | Threat model po akteru i artefaktu; kombinuj kontrole, ne naziv tehnologije. |
| 94 | „Differential privacy je besplatna i automatska.“ | Potrebni su clipping, noise, \(\varepsilon,\delta\), composition accounting i utility trade-off; pogrešna implementacija nema garanciju. | Privatnost budget i scientific utility se prijavljuju zajedno. |
| 95 | „Embedding/model nije raw CIF, pa se slobodno objavljuje.“ | Može biti licencno izvedeni materijal, memorisati detalje ili omogućiti rekonstrukciju/inference. | Ugovorna analiza, derivative registry, leakage/reconstruction test i pisano odobrenje kada je potrebno. |
| 96 | „CSD je akademska baza pa su raw podaci open.“ | CSD Portfolio i njegovi data files/subsets su licencirani proprietary sadržaj po javnim CCDC uslovima. | Akademska dostupnost ne daje pravo na redistribuciju; dozvoljeni obim upotrebe određuje konkretna licenca. |
| 97 | „Private GitHub repo rešava CSD licencu.“ | Private kontroliše vidljivost, ali i dalje kopira podatke trećem hostu, backup-ima, nalozima i lokacijama. | Proveri dozvoljenu lokaciju/korisnike; bez odobrenja licensed data-plane ostaje odvojen. |
| 98 | „Ako nešto mogu preuzeti preko API-ja, smem da ga keširam i delim.“ | Tehnički access, processing, retention, redistribution i publication su odvojena prava. | Dozvola za pristup ne implicira dozvolu za obradu, čuvanje, izvedene artefakte ili redistribuciju; svako pravo je zasebno. |
| 99 | „Citiranje zamenjuje dozvolu.“ | Citiranje priznaje izvor; ne daje pravo kopiranja/redistribucije ili treninga. | I citation i licence compliance su potrebni; proveri obavezni CCDC citation tekst. |
| 100 | „FAIR znači open, besplatno i bez logina.“ | FAIR Accessible može koristiti authentication/authorization; cilj je pronalaženje, standardan pristup, interoperabilnost i ponovna upotreba pod uslovima. | Kontrolisan ili ograničen pristup nije suprotan FAIR principu. |
| 101 | „Open fajl je automatski FAIR.“ | Bez stabilnog ID-a, metadata, semantike, provenance-a i licence javni dump može biti slabo reusable. | Otvorenost nije ni nužan ni dovoljan uslov za FAIR; ponovna upotrebljivost zavisi i od stabilnog ID-a, metapodataka, semantike, provenance-a i licence. |
| 102 | „FAIR je potvrda naučnog kvaliteta.“ | FAIR opisuje upravljanje/pristup/semantiku; ne garantuje tačan crystal model, property ili unbiased labels. | FAIR status sam po sebi ne potvrđuje naučnu validnost, bezbednost ni licencnu usklađenost; svaka od tih tvrdnji zahteva odgovarajući dokaz. |
| 103 | „Brisanje raw fajla briše njegov uticaj.“ | Cache, fingerprints, embeddings, modeli, pair reports i backup-i mogu ostati derivative. | Brisanje izvora ne uklanja informaciju već kodiranu u izvedenim artefaktima; njihov preostali uticaj mora se proceniti zasebno. |

## Brzi test za novu tvrdnju

Ako rečenica sadrži **„uvek“**, **„nikad“**, **„isti“**, **„tačan“**, **„stabilan“**, **„privatan“** ili **„sličan“**, postavi šest pitanja:

1. Koji tačno objekat i scope?
2. Pod kojim hemijskim, temperaturnim i eksperimentalnim uslovima?
3. Da li je informacija izmerena, prijavljena, izvedena ili modelovana?
4. Koja definicija, algoritam, verzija i prag?
5. Koja neizvesnost, missingness i domen važenja?
6. Koja dozvola važi za ulaz i svaki derivative?

Ako odgovor nedostaje, ublaži claim ili vrati `unknown/ambiguous/not assessed`.

## Mini-vežbe sa odgovorima

### 1. Visok 2D score, bez ćelije

Query i pogodak imaju Tanimoto 0,91, ali target nema cell/symmetry. Da li sistem sme da napiše „isti packing“?

??? success "Odgovor"
    Ne. Može prijaviti 2D similarity uz pun fingerprint profil. Packing grana vraća `missing-input`; 2D graf ne meri periodični raspored.

### 2. Metal u rezultatu

ConQuest query nalazi DAP motiv i nepovezan `4M`. Da li je label `DAP_tridentate_complex=true`?

??? success "Odgovor"
    Ne. To je kandidat koji sadrži motiv i neki metal. Potrebni su component assignment, tri konkretna donor N mapping-a, metal-neighbor/geometry dokaz i pravilo za ambiguous slučajeve.

### 3. Dobar R i ozbiljan alert

CIF ima nizak R, ali checkCIF upozorava na moguću propuštenu simetriju. Koji signal pobeđuje?

??? success "Odgovor"
    Nijedan sam. Pregledaj alert, alternative space-group model, residuals, refinement i hemijsku razumnost. Quality je skup dokaza; nizak R ne poništava strukturnu hipotezu koju alert dovodi u pitanje.

### 4. Skrivene dve rečenice u PDF-u

Embedded extractor nalazi temu koju render ne prikazuje. Da li je brisanje tih rečenica dovoljno?

??? success "Odgovor"
    Ne. Sačuvaj raw tekst kao provenance evidence, označi stranice i konflikt, potvrdi render/OCR, isključi ga iz approved indeksa i zapiši alat/verziju/QA odluku.

### 5. Model iz CSD-derived podataka

Weights ne sadrže lako čitljiv CIF. Da li mogu u javni repo?

??? success "Odgovor"
    To se ne može zaključiti iz formata weights-a. Proveri konkretni ugovor i CCDC uslove za derived artifacts, svrhu/distribuciju, mogućnost memorisanja ili rekonstrukcije i potrebno pisano odobrenje.

## Gde proveriti detalje

- hemijski identitet i veze: [poglavlja 1–4](01-atomi-joni-formule.md);
- koordinaciona hemija: [poglavlje 5](05-kompleksi.md);
- interakcije, ćelija i kvalitet: [interakcije](07-interakcije.md), [ćelija](08-celija.md), [difrakcija](10-difrakcija-kvalitet.md);
- forme, referentne raspodele i stabilnost: [čvrste forme](11-cvrste-forme.md), [Mogul/HBP](11a-referentne-raspodele-hbp.md);
- konverzija, standardizacija i lifecycle: [formati](12-formati.md), [standardizacija](13-standardizacija.md), [lifecycle stanja](22-whitepaper-tokovi-fl.md#lifecycle-stanja);
- reprezentacije i score: [reprezentacije](14-reprezentacije.md), [sličnost](15-slicnost.md);
- evaluacija, licence i FAIR: [evaluacija](20-evaluacija.md), [licence i provenance](21-licence-fair.md).
