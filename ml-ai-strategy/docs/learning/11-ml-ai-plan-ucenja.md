# Plan učenja ML/AI dela za 2CDC

Ovo je operativna putanja kroz postojeći kurs hemije i ML/AI strategiju za inženjera koji već zna da trenira, validira i isporuči ML sistem, ali tek gradi domensko znanje iz hemije i kristalografije. Plan ne ponavlja teoriju iz postojećih poglavlja. On određuje **redosled, preduslove, vežbe, dokaze prolaza i projektne artefakte**.

Osnovna putanja traje približno **16 nedelja i 157 fokusiranih sati**. Vreme uključuje navedeno čitanje, beleške i praktične zadatke, ali ne i kompletno čitanje svake spoljne reference. Ako radiš najviše osam sati nedeljno, istu putanju rastegni na oko 20 nedelja; kapije i redosled ostaju isti.

Ovaj plan dopunjuje [postojeći 15-nedeljni plan hemije](https://nemper.github.io/2cdc-chemistry-foundations/pocetak/plan-ucenja/). Hemijski plan daje redosled domenskog gradiva; ova strana govori kada je to gradivo dovoljno savladano za određenu ML/AI odluku.

## Pravila rada

1. **Napredovanje je zasnovano na dokazu, ne na datumu.** Ako kapija ne prolazi, ponovi ciljanu vežbu; nemoj samo nastaviti čitanje.
2. **Svaki score prvo dobija semantiku.** Pre implementacije napiši objekat poređenja, target, primenljivost, reprezentaciju, metricu i failure ponašanje.
3. **Determinističko jezgro prethodi ML-u.** Parser, standardizacija, hard filteri, atom/component mapping i periodična geometrija nisu poslovi za generativni model.
4. **`UNKNOWN` nije nula.** U korisničkom prikazu može postojati zajednička oznaka `UNKNOWN`, ali se u podacima izvodi iz preciznog statusa `ambiguous`, `missing_input`, `quality_blocked`, `timeout` ili `failed`, uz `relation_label: null`. `not_applicable` ostaje zasebno. Nijedan od tih statusa ne postaje negativna labela ili similarity `0`.
5. **Restricted podaci ostaju u odobrenom data-plane-u.** U Git ulaze samo šeme, manifesti, agregati čije je objavljivanje odobreno i sintetički/otvoreni fixture-i. Raw CSD/fakultetski CIF, MOL, MOL2, SDF, SMI, CQS i PDF ne ulaze u repo.
6. **Ne uči opšti ML ponovo.** Linearni modeli, tree ensemble-i, GNN, metric learning i kalibracija obrađuju se samo kroz 2CDC targete, splitove, failure slice-ove i production gate-ove.

## Prioriteti i tačan redosled čitanja

Oznake u tabeli znače:

- **O — obavezno:** potrebno za sledeću kapiju;
- **P — preporučeno:** potrebno pre odgovarajuće implementacione faze, ali ne blokira raniji prototip;
- **R — referenca:** otvara se tokom dizajna, error analysis-a ili audita; ne čita se linearno unapred.

Roadmap se čita dva puta: prvi put samo radi orijentacije, a drugi put u celosti u 16. nedelji, kada već možeš da osporiš ili odbraniš svaku odluku.

| Red | Dokumentacija | Prioritet | Kada i zašto |
|---:|---|---|---|
| 1 | Hemija: naslovna, „Šta projekat zapravo traži“, plan i dijagnostika | O | Pre svega: razdvoji sastav, graf, konformer, kristal i eksperimentalni model. |
| 2 | ML/AI: [početna](../index.md), [scope](../00-scope.md) i [mapa pipeline-a](../01-pipeline-decision-map.md) | O | Definiši dva proizvoda, poslove 0–7 i uloge baseline/candidate/challenger. |
| 3 | [Optimalni stack i roadmap](../roadmap/10-optimal-stack-roadmap.md): izvršna odluka, globalni gate-ovi i R0–R2 | O | Prvi, orijentacioni prolaz; bez proučavanja model shortlist-a. |
| 4 | Hemija 1–6: atomi/formule, veze, 3D/stereo, organski minimum, koordinaciona hemija i DAP/Schiff-base | O | Preduslov za svaki 2D graf, fingerprint, motif, metal/donor i stereo target. |
| 5 | Hemija 7–11A: interakcije, ćelija, simetrija, kvalitet, čvrste forme, referentne raspodele/HBP | O | Preduslov za periodične grafove, packing, polimorfe, PXRD, uncertainty i crystal modele. |
| 6 | Hemija 12–17: formati, pun CIF, standardizacija, reprezentacije, sličnost, CSD/ConQuest i lokalni skup | O | Pre bilo kog dataseta, feature-a ili modela; ovde se vidi stvarni cross-format gubitak i selection bias. |
| 7 | [Cross-format i lifecycle eligibility](../data/09-cross-format-eligibility.md) | O | Prvi kompletan ML/AI modul posle hemijskih preduslova; postaje ugovor za sve naredne faze. |
| 8 | Hemija 19 + [precizno pairwise poređenje](../pairs/04-precise-pairwise.md) | O | App 2 se uči prva jer se najveći deo može validirati bez pune CSD baze i bez ML-a. |
| 9 | Hemija 18 i 20 + [globalni retrieval, ANN i ranking](../retrieval/03-global-retrieval-ann-ranking.md) | O | Razdvoji exact filter, candidate recall, semantic recall, qrels i finalni ranking. |
| 10 | [Klasični ML](../classical/02-classical-ml.md) | O za R5 | Čitaj tek kada postoje target, group/time split i zamrznuti deterministički baseline-i. |
| 11 | [Periodični crystal encoderi](../deep/05-periodic-crystal-encoders.md), pa [metric learning i evaluacija](../deep/06-metric-learning-and-evaluation.md) | P pre R7; O za R7 | Ne počinji dok periodične/stereo invarijanse, exact Flat oracle i gold/split protokol nisu izvršivi. |
| 12 | Hemija 21–22 + ceo [optimalni roadmap](../roadmap/10-optimal-stack-roadmap.md) | O | Licence, FAIR, provenance, lifecycle, white-paper granice, property targeti i FL odluka. |
| 13 | [Lokalni SLM i RAG](../language/07-local-slm-rag.md) | P; O samo za R8 | Jezički adapter i dokumentacioni retrieval; nije crystal representation niti naučni autoritet. |
| 14 | [Spoljni LLM API i bezbednost](../language/08-api-llm-security.md) | R; O samo za R9 | Čita se tek kada je dokazana rupa koju Tier 0/lokalni sloj ne rešava i postoji dozvoljen `C0/C1` tok. |
| 15 | [Metod dokaza](../reference/evidence-method.md), [završni ML/AI audit](../reference/final-validation-2026-08-23.md), hemijski rečnik/zablude/izvori/audit | R | Koristi pri pisanju claim-a, proveri terminologije i završnom auditu; rešenja praktikuma tek posle sopstvenog pokušaja. |

Za osnovnu putanju su obavezna sva glavna hemijska poglavlja 1–22, ali ne i svaka bibliografska stavka na njihovom kraju. Spoljne radove čitaj u celosti samo kada implementiraš ili validiraš metod koji taj rad definiše, na primer ECFP, VF2, Kabsch, COMPACK/PAC, HNSW ili konkretan periodic encoder.

## Hemijski preduslovi po ML/AI temi

| ML/AI odluka | Hemija koju moraš završiti | Dokaz da je preduslov stvarno savladan |
|---|---|---|
| CIF ingest i field extraction | 1–2, 8–10, 12 i 12A | Parser razlikuje `?`, `.`, `0`, s.u., ASU, ćeliju i symmetry; filename ne postaje sastav. |
| Molekulski graf, ECFP i Tanimoto | 1–6, 12–15 | Možeš navesti uticaj bond order-a, aromatičnosti, naboja, tautomera, stereo i component politike na fingerprint i rang. |
| Exact graph, subgraph, VF2/MCS | 2, 4–6, 11–15 | Napišeš node/edge constraint-e, smer containment-a, coverage obe strane, timeout i ambiguity politiku. |
| Component assignment | 4–6, 11–13 | Ne biraš „najveći fragment“; razlikuješ ligand, coordination entity, counterion, solvent, coformer i multiplicity. |
| Kabsch, mapped 3D i stereo | 3–4, 8–9, 12–15 | Atom mapping prethodi RMSD-u; refleksija je zabranjena u stereo-sensitive profilu; coverage stoji uz RMSD. |
| Koordinacioni deskriptori/graf | 5–10, 12–15 | Razlikuješ metal presence od direktnog donor mapping-a; vraćaš CN, donor set, geometry/CSM i ambiguity. |
| Periodični graf i crystal encoder | 7–10, 12A–14 | Isti rezultat dobijaš posle wrap-a, origin/setting/basis promene i dozvoljenog supercell zapisa; image provenance nije izgubljen. |
| Packing, polymorph i interaction modeli | 7–11A, 13–15 | Isti molecular graph ne proglašavaš istom formom; packing, PXRD, HBP i Mogul ostaju odvojeni signali sa granicama. |
| Retrieval, reranking i qrels | 5–6, 11–18, 20 | Razlikuješ exact-neighbor ANN recall, expert candidate recall i end-to-end ranking; `search2` nije positive gold. |
| Kalibracija, abstention i error analysis | 10–15 i 20 | Raw cosine/Tanimoto/LambdaMART score ne zoveš verovatnoćom; kalibraciju fituješ van finalnog testa i prikazuješ risk–coverage. |
| Structure–property ili polymorph-risk target | 10–11A, 20–22 | Target vezuješ za material/solid form, uslove, metod, vreme i uncertainty; indikator ne postaje oracle. |
| Federativno učenje | 21–22 | Možeš nacrtati threat model i dokazati zašto FL nije ni licenca ni automatska privatnost; bez multi-site targeta odluka je `DEFER`. |

## Faze, vreme, roadmap i završni artefakt

| Faza | Nedelje | Sati | Primarni roadmap domet | Projektni artefakt na izlazu |
|---|---:|---:|---|---|
| F0 — scope, claims i prava | 1 | 6 | R0 | `claims-rights-brief-v1.md`: dva product claim-a, comparison/search profili, permission pitanja i stop uslovi. |
| F1 — hemijski graf, stereo i koordinacija | 2–3 | 16 | R0 → R1 | `chemical-object-contract-v1.md` + hash-ovan DAP motif/donor manifest i pozitivni/negativni/ambiguous primeri. |
| F2 — 3D kristal i periodičnost | 4–6 | 27 | R1 | `periodic-invariance-contract-v1.md` + sintetički metamorphic fixture manifest sa očekivanim ishodima. |
| F3 — formati, reprezentacije i data contract | 7–8 | 18 | R1 | `entry-inventory-schema-v1.yaml`, cross-format loss matrix i denominator/eligibility report. |
| F4 — determinističko poređenje parova | 9–10 | 20 | R2; osnova R4 App 2 | `pair-evidence-schema-v1.json`, full all-pairs mini-run i branch-status/error report. |
| F5 — retrieval, exact oracle i reranking | 11–12 | 20 | R2 App 1; osnova R4 i R6 | `retrieval-benchmark-v1.md`, qrels protocol, exact→candidate→rerank trace i recall/latency/memory tabela. |
| F6 — gold, split, klasični ML i kalibracija | 13 | 10 | R3 → R5 | `evaluation-protocol-v1.md`, split manifest, baseline tournament card, calibration i error-analysis izveštaj. |
| F7 — periodic deep i metric learning challenger | 14–15 | 22 | R7 | `periodic-challenger-report-v1.md` ili obrazložen `DEFER` ADR, sa ablation-ima i production gate odlukom. |
| F8 — governance, white paper i naredne faze | 16 | 18 | R8–R10 odluka, ne automatska implementacija | `governance-and-next-stages-v1.md`: provenance/repro checklist, SLM/API granica i FL go/defer odluka. |

Ukupno je oko **157 h**. F8 uključuje osam sati osnovne nedelje i do deset sati ciljane završne sinteze/odbrane; ta sinteza se može prebaciti u 17. nedelju ako radiš održivim tempom.

## Nedelja po nedelja

### Nedelja 1 — problem pre algoritma (6 h)

**Čitaj:** početne strane oba sajta, hemijsku mapu projekta i dijagnostiku; zatim ML/AI scope, pipeline mapu i samo izvršni deo roadmapa do R2.

**Moraš postići:** za oba proizvoda napiši objekat, korisničku odluku, target, failure cenu, evidence i šta je trenutno blokirano bez CSD prava/gold-a.

**Vežba:** uzmi frazu „sličan kristal“ i razloži je na najmanje pet odvojenih claim-ova. Za svaki napiši koji input je dovoljan i kada rezultat mora biti `UNKNOWN`/`not_applicable`.

**Provera:** bez dokumentacije objasni zašto App 1 nije klasifikator, zašto App 2 nije jedna matrica univerzalnog score-a i zašto LLM nije parser. Predaj F0 artefakt.

### Nedelja 2 — od atoma do stereo-svesnog grafa (8 h)

**Čitaj:** hemija 1–4.

**Moraš postići:** razlikuj formulu od grafa, formalni naboj od parcijalnog naboja/oxidation state-a, konfiguraciju od konformacije i nepoznatu stereo oznaku od ahiralnog slučaja.

**Vežba:** za pet malih primera ručno napravi node/edge tabelu, zatim variraj aromaticity, tautomer, protonation i stereo politiku. Zapiši koje ECFP bitove/rang očekuješ da se promene, bez potrebe da unapred znaš konkretne hash vrednosti.

**Provera:** hemijska Kapija A iz kursa i kratka specifikacija `graph-policy-v1`; nijedno polje `unknown` ne sme biti prepisano podrazumevanom vrednošću.

### Nedelja 3 — DAP, metali i koordinaciona semantika (8 h)

**Čitaj:** hemija 5–6.

**Moraš postići:** mapiraj tri DAP N donora, odvoji potential od observed denticity, metal u entry-ju od metala u istoj komponenti i direktne N3 koordinacije.

**Vežba:** reprodukuj logiku laboratorije L6 kao mašinski query manifest. Dodaj najmanje po jedan positive, hard negative i `AMBIGUOUS_REPRESENTATION` slučaj. Ne koristi `search1/search2` članstvo kao labelu.

**Provera:** napiši exact predicate „isti metal direktno koordinira sva tri mapirana DAP N“. Ako se predicate svodi na formulu, filename ili SMILES tačku, kapija nije prošla. Predaj F1 artefakt.

### Nedelja 4 — 3D, ćelija i periodični susedi (9 h)

**Čitaj:** hemija 7–8.

**Moraš postići:** pređi iz frakcionih u Cartesian koordinate, koristi metric tensor/PBC i objasni zašto atom/molekul ne završava na ivici nacrtane ćelije.

**Vežba:** uradi L3 i početak L4 na sintetičkom ili eksplicitno dozvoljenom fixture-u. Sačuvaj symmetry operation i lattice image uz svaki periodični kontakt.

**Provera:** distance moraju ostati iste posle wrap-a, rigidne rotacije/translacije i promene redosleda atoma.

### Nedelja 5 — simetrija, kvalitet i neizvesnost (9 h)

**Čitaj:** hemija 9–10.

**Moraš postići:** razlikuj ASU, ćeliju i supercell; setting/origin promenu od fizičke razlike; measured od simulated PXRD-a; profil kvaliteta od jednog R praga.

**Vežba:** završi L4 i napravi dve vrste fixture-a: invarijantnu promenu zapisa i stvarnu promenu strukture. Za bar jedan quality problem odredi `missing_input` naspram `quality_blocked`.

**Provera:** isti kristal u ekvivalentnom setting-u prolazi, mirror/stereo ponašanje prati profil, a loš/odsutan input ne daje score 0.

### Nedelja 6 — polimorfi, packing i referentni signali (9 h)

**Čitaj:** hemija 11 i 11A.

**Moraš postići:** razlikuj parent compound, solid form, polymorph, solvate/hydrate/co-crystal i redetermination. Mogul outlier, HBP, packing score i simulated PXRD ne smeju postati termodinamički oracle.

**Vežba:** uradi L5 i L11; zatim napravi par sa istim molecular graph-om i različitim packing očekivanjem. Napiši koju nezavisnu eksperimentalnu potvrdu bi zahtevao jači claim.

**Provera:** prolaz kroz hemijsku Kapiju C i predat F2 artefakt sa origin/wrap/setting/basis/supercell, stereo i disorder očekivanjima.

### Nedelja 7 — formati i loss-aware ingest (9 h)

**Čitaj:** hemija 12, 12A i 13; zatim prvu polovinu cross-format/lifecycle modula do purpose-specific canonical view-a.

**Moraš postići:** za CIF/MOL/MOL2/SDF/SMILES navedi očuvano, izgubljeno, dodeljeno i nepoznato; original i purpose-specific view ostaju odvojeni.

**Vežba:** uradi L0A i L2. Implementacioni nacrt mora čuvati byte hash, parser/verziju, field-level source binding, conflict/loss/status i transformacioni lineage.

**Provera:** lossy format ne prepisuje bogatiji source, uspešan parse nije automatski validan crystal model, a `inner join` ne briše entry bez accounting-a.

### Nedelja 8 — eligibility, reprezentacije i lokalni bias (9 h)

**Čitaj:** hemija 14–17 i 21; dovrši [cross-format/lifecycle ugovor](../data/09-cross-format-eligibility.md).

**Moraš postići:** odvoji declared, curated i geometry-neighbor graf; objasni granice 2D, isolated-3D i periodic reprezentacije; definiši identity/family/lifecycle/rights pre splita.

**Vežba:** uradi L7 nad dozvoljenim lokalnim data-plane-om ili napravi sintetički ekvivalent sa istim vrstama missingness-a. Proizvedi union inventar, channel coverage, međusobno isključiv exclusion waterfall i conservation assert.

**Provera:** isti entry u svim formatima/verzijama ide u istu split grupu; missing SMILES ne znači missing graph ni negative label; predaj F3 artefakt. Ovo je R1 learning gate.

### Nedelja 9 — deterministički App 2: mapping i 3D (10 h)

**Čitaj:** hemija 19 i pairwise modul 4.1–4.9.

**Moraš postići:** definiši comparison profile, component assignment sa unmatched opcijom, exact/subgraph/MCS semantiku, automorphism politiku, Kabsch posle mapping-a i coordination evidence.

**Vežba:** na 6–10 sintetičkih/otvorenih struktura izračunaj full `n(n-1)/2` universe. Ubrizgaj timeout, unknown bond, missing cell i ambiguous donor assignment. Proveri A↔B symmetry i directional coverage.

**Provera:** svaki pair i svaka grana postoje u long-form rezultatu; timeout/failure se ne gube i ne pretvaraju u score.

### Nedelja 10 — deterministički App 2: packing i evidence (10 h)

**Čitaj:** dovrši pairwise modul 4.10–4.21.

**Moraš postići:** razumeš uloge i granice COMPACK/PAC, CrystalCMP, SOAP–REMatch, PXRD i interaction networks; znaš kada metoda nije primenljiva ili licencno dostupna.

**Vežba:** uradi L9 i L10. Napravi evidence-rich report bez obaveznog overall score-a i najmanje pet failure/ambiguous slučajeva. Ako nema validirane packing implementacije, vrati tačan status i dokumentuj gap; ne improvizuj referencu.

**Provera:** drugi inženjer iz manifesta može reprodukovati pair universe, mapping, parametre, statuse i evidence. Predaj F4 artefakt. Ovo dokazuje R2 App 2 spremnost i priprema R4.

### Nedelja 11 — App 1: exact i višekanalni candidate retrieval (10 h)

**Čitaj:** hemija 18 i retrieval modul 3.1–3.12.

**Moraš postići:** odvoji eligibility/hard filter, 2D/coordination/shape/periodic kanal, exact ECFP/Tanimoto baseline, exact Flat oracle i ANN kao infrastrukturnu optimizaciju.

**Vežba:** uradi L8. Napravi exact binary i count fingerprint rangiranje sa pinovanim standardization/stereo parametrima. Dodaj exact DAP predicate i kanal provenance. Izmeri promenu ranga posle jedne dozvoljene promene reprezentacije.

**Provera:** hard filter daje set equality prema nezavisnom expected-ID fixture-u, FP=0 i FN=0; nijedan ANN test ne počinje pre exact oracle-a iste reprezentacije/metrike.

### Nedelja 12 — reranking, qrels i retrieval evaluacija (10 h)

**Čitaj:** retrieval modul 3.13–3.22 i hemiju 20 sa fokusom na claim, gold, split i metrike.

**Moraš postići:** razlikuj infrastructure Recall@N, expert candidate Recall@N i end-to-end nDCG/Recall; razumeš pool, `unjudged`, hard negative i candidate/reranker error boundary.

**Vežba:** napravi mali qrels protokol: duboka unija različitih baseline-a, slepa randomizovana anotacija, graded relevance, `unjudged`, confidence i version. Uporedi transparentno pravilo sa jednim pointwise baseline-om na istom candidate set-u. Napravi exact→candidate→rerank trace za svaki poznati positive.

**Provera:** relevantan kandidat izgubljen u candidate fazi ne pripisuje se rerankeru; `search2` i stari ranking nisu gold; novi retriever sa mnogo novih unjudged top rezultata pokreće dopunu pool-a. Predaj F5 artefakt.

### Nedelja 13 — split, baseline turnir, kalibracija i error analysis (10 h)

**Čitaj:** dovrši hemiju 20, zatim [klasični ML](../classical/02-classical-ml.md) i sekcije 6.8–6.12 metric-learning modula.

**Moraš postići:** definiši estimand pre splita; razlikuj query/family grouping, 1D warm/cold, 2D cold/cold i temporal holdout; broj nezavisnih grupa ne zamenjuj brojem parova.

**Vežba:** zamrzni train/validation/calibration/test manifest. Pokreni samo relevantan turnir: dummy/rule → logistic/ordinal → RF → ExtraTrees → GBDT. Prijavi paired interval, worst-slice, Brier/NLL/reliability i risk–coverage. Uradi error analysis po najmanje: parser/representation, candidate miss, rerank, stereo, polymorph/packing, metal/coordination, missing/quality, source/time i OOD.

**Provera:** prag, model i calibrator nisu birani na finalnom testu; raw similarity/ranking score nije probability; abstention smanjuje risk na unapred dogovorenoj coverage tački. Predaj F6 artefakt. Ako model nema praktičan dobitak, ispravan izlaz je da R4 ostane optimum.

### Nedelja 14 — periodični graf i encoder contract (11 h)

**Čitaj:** [periodični crystal encoderi](../deep/05-periodic-crystal-encoders.md).

**Moraš postići:** definiši site features, edge vrste, image/lattice podatke, cell/global state, occupancy/disorder i invariance/equivariance ugovor. Razlikuj crystal encoder, pair model i property model.

**Vežba:** napravi jedan `crystal_view` i metamorphic suite pre treninga. Na istim fixtures proveri CGCNN kontrolni baseline i najmanje jedan periodic challenger samo ako input contract prolazi. Beleži representation coverage, embedding collapse/hubness i sve non-assessed slučajeve.

**Provera:** atom order, wrap, origin, setting/basis i dozvoljeni supercell zapis ne menjaju target-semantiku; chirality/reflection ponašanje prati profil; nevalidan periodic input nije zero-filled pseudo-kristal.

### Nedelja 15 — metric learning bez lažnih parova (11 h)

**Čitaj:** ceo [metric learning i production gate](../deep/06-metric-learning-and-evaluation.md).

**Moraš postići:** razlikuj equivalence, relation i query-conditioned relevantnost; znaš kada contrastive/triplet/InfoNCE nisu usklađeni sa targetom; dual encoder ne zamenjuje exact evidence niti cross-graph comparator.

**Vežba:** zamrzni positive/negative/augmentation/mining ugovor. Poredi descriptor+GBDT, CGCNN i odabrani Matformer/ALIGNN kandidat na istom targetu, splitu i budžetu. Exact Flat je oracle za isti embedding; ANN dolazi samo zbog SLO-a. Uradi minus-one ablation, false-negative audit, najmanje pet label-budget tačaka i više seed-ova ako podaci to omogućavaju.

**Provera:** challenger prolazi invariance, semantic recall/pair metric, critical-slice non-inferiority, kalibraciju, abstention, SLO, licence i reproducibility gate. U suprotnom predaj obrazložen `DEFER`. To je validan F7 artefakt, ne neuspeh.

### Nedelja 16 — governance, white paper i odluka o narednim fazama (8 h + do 10 h odbrane)

**Čitaj:** hemija 22, ceo optimalni roadmap po drugi put, reference/audite; lokalni SLM/RAG samo na nivou odluke. API modul ostaje referenca osim ako je R9 stvarno aktiviran.

**Moraš postići:** mapiraj white-paper pojmove na state, property i evidence ugovore; odvoji polymorph-risk indikator od tvrdnje; objasni kada R8/R9/R10 imaju poslovni i naučni razlog.

**Vežba:** uradi završnu odbranu jednog search query-ja, jednog pair rezultata, jednog `UNKNOWN` slučaja, jednog leakage incidenta i jednog licence stop-a. Za FL popuni osam preduslova iz roadmapa i nacrtaj threat model: client, coordinator, update, endpoint i final-model leakage.

**Provera:** predaj F8 artefakt. FL je `DEFER` ako ne postoji zajednički multi-site supervised target koji se zakonito ne može centralizovati. SLM/API su `DEFER` ako Tier 0 nema dokazanu UX rupu.

## Kapije prelaza

| Kapija | Prelaziš kada možeš da dokažeš | Ne prolazi ako |
|---|---|---|
| G0 — claim i prava | svaki output ima objekat, target, scope, evidence, rights i abstention pravilo | ključna operacija ili licenca je `unknown`, a plan ipak pretpostavlja produkciju |
| G1 — hemijski graf/koordinacija | DAP motif, stereo, charge, component i donor mapping su izvršivi i verzionisani | formula/filename/metal presence glume povezanost ili koordinaciju |
| G2 — crystal/3D | PBC/symmetry/setting/basis i stereo metamorphic testovi prolaze | RMSD prethodi atom mapping-u ili cell/space group glume packing dokaz |
| G3 — data core | union inventar, lineage, purpose view, lifecycle i denominator accounting se reprodukuju | silent overwrite, `inner join` drop ili missing status postaje vrednost |
| G4 — deterministic App 2 | full pair universe, branch state machine, evidence i swap/directionality testovi prolaze | non-assessed grana nestane, postane nula ili dobije relation labelu |
| G5 — App 1 retrieval | exact filter/oracle, multichannel coverage i tri nivoa retrieval evaluacije su odvojeni | ANN brzina glumi hemijsku tačnost ili reranker skriva candidate miss |
| G6 — supervised evaluation | gold/qrels, split, calibration i error analysis su zamrznuti i leakage-safe | `search1/search2`, duplicates ili test-set odluke procure u trening/tuning |
| G7 — deep challenger | pobeda je praktična, intervalno podržana i prolazi critical slice/invariance/SLO/licence | rezultat je bolji samo na random split-u, jednom seed-u ili najvećem label budžetu |
| G8 — sledeća faza | R8/R9/R10 ima merljivu rupu, odobren data flow, baseline i stop uslov | „AI/FL/LLM“ je razlog sam po sebi |

## Minimalni dokazni paket svake faze

Svaki predati artefakt treba da sadrži:

- claim/target i populaciju na koju se odnosi;
- source, rights, lifecycle i purpose odluku;
- verzije reprezentacije, parsera, pravila, koda i podataka;
- input/output schema-u i značenje svakog missing/non-assessed statusa;
- fixture-e i očekivane rezultate pre pokretanja;
- split/qrels/gold verziju kada postoji evaluacija;
- baseline, challenger, tuning budžet i stop uslov;
- overall i worst-slice rezultate sa odgovarajućim intervalima;
- failure accounting, error taxonomy, calibration/coverage–risk kada postoji probability output;
- latenciju, memoriju, build/rebuild trošak i checksum izvršenog artefakta;
- poznate granice, rollback/invalidation pravilo i sledeću odluku `PROMOTE`, `KEEP BASELINE` ili `DEFER`.

## Uslovni nastavak posle osnovnih 16 nedelja

Ovo nisu automatske obaveze osnovnog 2CDC scope-a.

### R8 — lokalni SLM i dokumentacioni RAG (još 2 nedelje, oko 16 h)

Pročitaj u celosti [lokalni SLM/RAG modul](../language/07-local-slm-rag.md). Prvo napravi Tier 0 form/DSL/template baseline i field-aware BM25. Tek zatim testiraj constrained NL→DSL, dense retrieval, RRF i mali reranker. Gold grupiši po intent/paraphrase i source/topic familiji. Gate je bolji task completion/UX uz nula promene deterministic scientific rezultata i nula policy bypass-a.

**Artefakt:** `local-language-layer-evaluation-v1.md` sa NL→DSL gold-om, RAG qrels-om, multilingual/rare-token/security slice-ovima, latency/RAM i tested Tier 0 fallback-om.

### R9 — spoljni API (još 1 nedelja za odluku, oko 8 h)

Pročitaj [API/security modul](../language/08-api-llm-security.md). Ne šalji projektne podatke radi „probnog poziva“. Najpre zamrzni `C0` offline tournament, minimalni payload, centralni broker, retention/region/processor odluke, content-free audit, circuit breaker i local fallback. Bez pisanog `C1` odobrenja nema shadow/canary faze.

**Artefakt:** `external-api-go-no-go-v1.md`; podrazumevani rezultat je `NO-GO` dok lokalni Pareto baseline nema dokazanu rupu i rights/security gate nije pozitivan.

### R10 — federativno učenje (oko 6 h za odluku; implementacija nije planirana)

Ponovo pročitaj samo FL delove hemijskog poglavlja 22 i roadmapa. Uporedi local-only, shared-public-pretraining i dozvoljeni centralni baseline. Secure aggregation, DP i robust aggregation biraju se prema konkretnom threat model-u, ne kao checklist dekoracija.

**Artefakt:** `federated-learning-decision-v1.md` sa target/schema/split ugovorom, pravima za update i finalni model, per-site/worst-site evaluacijom i jasnim `GO` ili `DEFER`. Bez stvarnog multi-site, non-centralizable targeta rezultat mora biti `DEFER`.

## Završni kriterijum spremnosti

Spreman si da vodiš ML/AI deo 2CDC-a kada možeš da odbraniš ceo lanac:

```text
odobren source
→ loss-aware purpose view
→ hemijski i periodični objekat
→ deterministički exact evidence
→ candidate retrieval i/ili pair comparison
→ leakage-safe gold/qrels i split
→ kalibrisan target-specific challenger sa abstention-om
→ reproduktivan, licencno dozvoljen artefakt
→ objašnjiv rezultat ili precizan UNKNOWN
```

Ako bilo koja strelica nema izvršiv ugovor i dokaz, sledeći složeniji model još nije sledeća faza učenja ni implementacije.
