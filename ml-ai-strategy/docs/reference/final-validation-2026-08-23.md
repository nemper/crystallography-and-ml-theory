# Završni ML/AI validacioni audit — 23. avgust 2026.

Ova strana beleži završnu proveru ML/AI strategije za dve 2CDC aplikacije. Audit je namerno tražio samo objektivne greške i materijalne rupe; terminološke preference i proširenja koja ne menjaju projektantsku odluku nisu tretirana kao nalazi.

## Izvršni rezultat

- Auditovani sadržaj je zamrznut na commitu `4cbdd4a` u istom privatnom repozitorijumu `nemper/2cdc-chemistry-foundations`.
- Četiri nezavisna read-only audit toka pokrila su classical/retrieval, crystal/deep/data, SLM/RAG/API i potpunu pokrivenost lokalnih izvora.
- Prvi prolazi su našli pet P2 materijalnih rupa; svaka je ispravljena i poslata na novi nezavisni prolaz.
- Završni glas svakog domena je **PASS**, bez preostalog P1/P2 nalaza.
- Oba MkDocs projekta prolaze strict build. ML knjiga prolazi proveru internih targeta i fragmenata, parsiranje svih JSON/YAML primera i stvarni browser audit na desktop i mobilnoj širini.
- U Git-u nema dostavljenih fakultetskih/CSD raw fajlova. Jedini praćeni kontrolisani fajl je sintetički, CC0 nastavni `docs/assets/open/tutorial-minimal.cif`.
- Bez autorizovanog reprezentativnog CSD snapshot-a strategija ne tvrdi da je learned model već pobednik. Dokumentuje optimalni početni stack, challenger-e i testove koji odlučuju o promociji.

## Šta je tačno auditovano

| Sloj | Obuhvat |
|---|---|
| glavni hemijski kurs | svih 38 trenutnih Markdown modula; detaljan raniji audit je u `docs/referenca/validacioni-audit-2026-08-23.md` |
| ML/AI strategija | 13 sadržajnih modula na auditu + ova meta-audit strana |
| lokalni izvori | 15 artefakata: white paper, brief dve aplikacije, N14 CIF/MOL/MOL2, dva CQS-a i `search1/search2` eksporti |
| white paper | svih 22 fizičkih strana, tekstualno i vizuelno |
| algoritamski domeni | klasični ML; exact/ANN retrieval i ranking; pairwise scientific core; periodic/deep/metric learning; lokalni SLM/RAG; spoljni LLM API i security |
| ugovori | cross-format reconciliation, identity/split, rights/lifecycle, point-in-time leakage, denominatori, branch status/label, evidence i promotion gates |

Audit nije koristio pristup CSD bazi: taj pristup ne postoji u dostupnom okruženju. Lokalni brojevi proveravani su isključivo nad dostavljenim snapshot-om, a spoljna teorija prvenstveno standardima, zvaničnom dokumentacijom i originalnim radovima.

## Nezavisni glasovi posle korekcija

Auditori nisu uređivali fajlove. Svaki je vraćao samo `PASS` ili `NEEDS_FIX` uz P1/P2 dokaze; posle korekcije dobijao je trenutnu radnu verziju na ponovnu proveru.

| Auditor | Nezavisni scope | Prvi nalaz | Remediation | Završni glas |
|---|---|---|---|---|
| A | pipeline, classical ML, hard filter, retrieval/ANN/ranking, data i roadmap | P2: `precision = 1` ne otkriva false-negative/prazan hard-filter skup | nezavisni expected-ID set equality, FP=0/FN=0, positive/zero-hit/boundary/missing-status fixture-i, D28 pre ANN oracle-a | **PASS** |
| B | pairwise, periodic/deep, metric learning, data i roadmap | P2: branch status pomešan sa relation labelom; P2: lokalni `rhombohedral` nije imao izvršivu normalizaciju | `branch_status_v1` + nullable target label; packing `same/related/different`; D29 raw→trigonal/setting/axes ugovor | **PASS** |
| C | lokalni SLM/RAG, pair report schema, spoljni API/security | P2: stereo klase predstavljene kao status; P2: `assessed` naučni rezultat bez evidence ID-ja | odvojeni molecular/crystal stereo targeti; assessed/non-assessed maska; obavezni same-run evidence | **PASS** |
| D | brief, svih 15 lokalnih artefakata, 22 PDF strane, oba dokumentaciona stabla i navigacija | bez P1/P2 rupe | nije bila potrebna sadržajna izmena | **PASS** |

Pre ovih završnih prolaza centralni data contract i optimalni roadmap bili su zasebno provereni sa tri nezavisna `PASS` glasa nad identičnom verzijom. Kasnije korekcije nisu prećutno prihvaćene: ciljane oblasti su ponovo auditovane kako tabela iznad opisuje.

## Materijalne korekcije koje su preživele glasanje

### 1. Hard filter mora dokazati i recall membership-a

Prazan ili preuzak skup može imati precision 1. Zato je uveden odvojen evaluator:

- `actual_eligible_ids == independently_expected_eligible_ids`;
- FP = 0 i FN = 0;
- najmanje jedan non-vacuous positive;
- legitimni zero-hit slučaj;
- boundary i missing/unknown/invalid/failure fixture-i;
- tek zatim exact-after-filter ANN oracle.

Time se razdvajaju dve greške: „filter je izabrao pogrešan skup“ i „ANN je izgubio suseda unutar ispravnog skupa“.

### 2. Status izvršenja nije naučna klasa

Sve pair grane koriste isti `branch_status_v1`:

`assessed | ambiguous | not_applicable | missing_input | quality_blocked | timeout | failed`.

`relation_label` je zaseban nullable enum konkretnog target-a. Non-assessed slučaj nikada ne ulazi u relation loss kao dodatna klasa. `packing_relation_v1` koristi samo `same | related | different`; parcijalnost ostaje `evidence_coverage`, `matched_N`, coverage i RMSD.

### 3. Raw `rhombohedral` nije osmi crystal system

Lokalni `search2` ima tačno 12 raw `_symmetry_cell_setting = rhombohedral` zapisa. Ugovor sada čuva odvojeno:

- byte-veran `raw_export_label`;
- `normalized_crystal_system: trigonal`;
- `reported_lattice_setting: rhombohedral`;
- zaseban `coordinate_axes_setting`, koji ostaje `unknown` ako ga cell/space-group kontekst ne dokazuje;
- verziju normalizacionog pravila i D29 fixture.

Model feature/slice koristi normalizovani sistem; raw/setting/axes ostaju provenance i sensitivity polja.

### 4. Stereo profil, status i labela su tri različite stvari

Uvedeni su odvojeni `molecular_stereo_relation_v1` i `crystal_handedness_relation_v1` targeti. Kada dokaz postoji, rezultat je `branch_status: assessed` + `relation_label: same|mismatch`. Nedovoljan ili konfliktan dokaz daje `missing_input/ambiguous + null`; ahiralni slučaj ili stereo-agnostic profil daje `not_applicable + null`.

### 5. Assessed scientific output mora imati dokaz

Canonical pair primer i report gate sada zahtevaju da svaki assessed naučni score/label ima najmanje jedan autorizovan `evidence_id` iz istog run-a. SLM/API narativ može samo da renderuje taj dokaz; ne može da ga dopuni slobodnom tvrdnjom.

## Pokrivenost svega dostavljenog

| Dostavljeni materijal/tema | Šta je izvučeno | Gde je zatvoreno |
|---|---|---|
| `dve funkcionalnosti.txt` | App 1: jedan CIF prema bazi; App 2: svi neuređeni parovi `n(n-1)/2` | `00-scope.md`, `01-pipeline-decision-map.md`, `roadmap/10-optimal-stack-roadmap.md` |
| N14 CIF/MOL/MOL2 | isti entry, različiti loss/capability pogledi; bond-order konflikt; fractional/Cartesian razlika | glavni kurs 12/12A/17; `data/09-cross-format-eligibility.md` |
| `search1/search2` CIF/MOL2/SD/SMI | record/SMILES/coordinate coverage, `Du`, empty/matching, lineage i missingness | glavni kurs 17; data contract D01–D29 |
| dva CQS fajla | statički query graph i `4M` presence; runtime/UI semantika nije izmišljena | glavni kurs 16–17; query/DSL regressions u 07 |
| white paper 22/22 | lifecycle/curation, structure–property, manufacturability, polymorph-risk, Mogul/HBP/packing i FL | glavni kurs 22; roadmap R8–R10 i FL defer gate |
| CIF izgled | pun sintetički data block, tag/value, loop, ćelija, simetrija, atom sites, `?`, `.`, s.u. i text field | `docs/podaci/12a-anatomija-cif.md` + `tutorial-minimal.cif` |

Spot-check izvora ponovo je potvrdio 2.110 `search1` i 2.038 `search2` CIF/MOL2/SD zapisa, odnosno 1.877 i 1.805 SMILES redova. To su svojstva dostavljenog snapshot-a, ne globalne CSD statistike.

## Pokrivenost algoritamskih odluka

| Posao | Validirani default | Challenger samo kroz gate |
|---|---|---|
| parsing/standardizacija/rights/lifecycle | deterministički, verzionisan scientific/data core | ML samo kao review predlog, nikad source of truth |
| hard filter | exact SQL/bitmap/inverted/graph predicate + independent set-equality test | bez generativne zamene |
| App 1 candidate retrieval | exact ECFP/count i target-specific koordinacioni/shape kanali; Flat exact oracle | HNSW/IVF/MHFP/learned embedding tek uz tie-aware recall, coverage, latency i slice gate |
| App 1 reranking | rastavljivi exact features i rule score | logistic/RF/ExtraTrees/GBDT/LTR uz query-grouped gold i ablation |
| App 2 pair core | component assignment, exact graph/MCS, mapped 3D, coordination, packing/interaction evidence | SOAP/CrystalCMP/PXRD i learned comparator samo u dokazano primenljivom domenu |
| periodic/deep | nije MVP dependency | CGCNN baseline; Matformer/ALIGNN/equivariant/cross-graph challenger uz invariance i label-efficiency gate |
| property/review | dummy + linear/RF/boosting turnir, target-specific | GPR/SVR ili periodic GNN tek uz dovoljan validan skup i OOD/calibration dokaz |
| lokalni jezički sloj | Tier 0 forme, controlled vocabulary i templates | Qwen3.5-4B constrained NL→DSL; field-aware BM25 + opcioni dense/RRF RAG |
| spoljni LLM | isključen po default-u | C0 offline tournament, zatim C1 shadow/canary preko egress brokera; C2–C4/raw zabranjeni |
| federativno učenje | odloženo | tek uz stvarni multi-site target, threat model, legal/rights i held-out-site gate |

„Optimalno“ ovde znači najjednostavniji metod koji prolazi zamrznuti target, gold/qrels, leakage, coverage, failure, latency, memory, licence i security kriterijume — ne algoritam sa najvećim javnim benchmark brojem.

## Reproduktivne tehničke kontrole

| Kontrola | Rezultat |
|---|---|
| glavni `mkdocs build --strict` | PASS |
| ML `mkdocs build --strict` | PASS |
| izgrađene HTML strane | 15 ukupno, uključujući 404 |
| interni targeti | 1.251 provera, 0 grešaka |
| fragmenti/anchor-i | 972 provere, 0 grešaka |
| fenced JSON | 10/10 sintaksno validnih |
| fenced YAML | 25/25 sintaksno validnih |
| schema invariant | svi konkretni `branch_status` primeri pripadaju `branch_status_v1`; non-assessed + non-null label = 0; assessed labeled primer bez evidence-a = 0 |
| desktop browser | 14/14 ruta; 1 H1 po strani; 0 broken images; 0 horizontal overflow |
| mobilni browser 390×844 | 14/14 ruta; 0 broken images; 0 horizontal overflow |
| Mermaid | 7/7 kontejnera renderovano u SVG |
| MathJax | 238 renderovana math kontejnera |
| browser console | 0 warning/error zapisa |
| `git diff --check` | PASS |
| kontrolisane raw ekstenzije u Git tree-u | samo `docs/assets/open/tutorial-minimal.cif` |
| GitHub metadata | `nemper/2cdc-chemistry-foundations` je private; default branch `main` |

Jedini build ispis van regularnog loga je opšte upozorenje Material for MkDocs projekta o budućem MkDocs 2.0; trenutni strict build nije prijavio dokumentacionu grešku.

## Spoljni linkovi

Iz izgrađenog ML sajta izdvojena su 184 jedinstvena spoljna URL-a:

- 177 je prošlo direktnu automatizovanu proveru;
- 5 zvaničnih stranica blokira generički scripted HTTP sa 403, ali je ručno otvoreno u browseru: [OpenAI gpt-oss model card](https://openai.com/index/gpt-oss-model-card/), [IUCr Core dictionary](https://www.iucr.org/resources/cif/dictionaries/browse/cif_core), [IUCr Core 1 dictionary](https://www.iucr.org/resources/cif/dictionaries/browse/cif_core1), [IUCr pdCIF dictionary](https://www.iucr.org/resources/cif/dictionaries/cif_pd) i [IUCr CIF syntax](https://www.iucr.org/resources/cif/spec/version1.1/cifsyntax);
- 2 GitHub file linka vraćaju očekivani anonymous 404 jer je repo private; autentifikovana GitHub provera potvrdila je oba path-a i private status repoa.

HTTP 403/anonymous 404 zato nisu označeni kao netačan naučni link bez dodatne provere pristupa.

## Šta još nije i ne sme biti predstavljeno kao potvrđeno

1. **Globalni CSD kvalitet ili recall.** Nema pristupa autorizovanom reprezentativnom CSD snapshot-u, qrels-u ni entitlement matrici.
2. **Konačni learned pobednik.** RF, GBDT, Matformer, ALIGNN, Qwen ili bilo koji ANN engine ostaje kandidat dok ne pobedi zamrznuti baseline pod istim budžetom i splitom.
3. **Puna CQS runtime/UI semantika.** Statička forenzika nije zamena za kompatibilni ConQuest runtime.
4. **Fakultetska operational definition DAP scope-a.** Query fajl ne rešava sam šta tim želi da uključi među tautomerne, protonovane, supstituisane i koordinaciono granične slučajeve.
5. **Institucijska CCDC licenca i product capabilities.** Bulk eksport, API, Mogul/HBP/packing i redistribucija zahtevaju pisanu capability/permission matricu.
6. **Budući provider uslovi.** Model, retention, region, ZDR i ugovorni uslovi spoljnih API-ja moraju se ponovo proveriti neposredno pre procurement/deployment odluke.
7. **Naučna/disertaciona validnost produkcionog rezultata.** Ovaj audit je inženjerski i source-based; formalni claim i dalje zahteva domen eksperte, odobren protokol, podatke i statistički zaključan test.

## Konačna odluka

U dostupnom scope-u nema preostale poznate objektivno netačne informacije ili materijalne nastavne/projektantske rupe koje su auditori ocenili kao P1/P2. Vodič je spreman kao teorijska i projektantska osnova za sledeću fazu: razgovor sa fakultetom, data/rights contract, gold/qrels dizajn i determinističke MVP fixture-e.

To nije tvrdnja da je budući model unapred validiran. Najvažniji rezultat dokumentacije je upravo suprotan: svaka nepoznata stavka ima vidljiv status, vlasnika i eksperiment kojim se može zatvoriti.
