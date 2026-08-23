# Plan učenja ML/AI dela za 2CDC

Ovo je putanja kroz postojeći kurs hemije i ML/AI strategiju za inženjera koji već zna da trenira, validira i isporuči ML sistem, ali tek gradi domensko znanje iz hemije i kristalografije. Plan ne ponavlja teoriju iz postojećih poglavlja. On određuje **redosled, preduslove, projektantske vežbe i dokaze razumevanja**.

Osnovna putanja ima 16 nastavnih blokova i približno **178 fokusiranih sati**: oko 122 sata postojećeg kursa hemije i oko 56 sati projektno usmerene ML/AI nadogradnje. Ne uključuje implementiranje dve aplikacije, treniranje modela niti kompletno čitanje svake spoljne reference. Blokovi mogu stati u 16 intenzivnih nedelja samo uz približno 10–13 sati rada nedeljno; pri održivih osam sati računaj oko 22–23 nedelje. Kapije i redosled ostaju isti.

Ovaj plan dopunjuje [postojeći 15-nedeljni plan hemije](https://github.com/nemper/2cdc-chemistry-foundations/blob/main/docs/pocetak/plan-ucenja.md). Hemijski plan daje redosled domenskog gradiva; ova strana govori kada je to gradivo dovoljno savladano za određenu ML/AI odluku.

!!! info "Granica ovog plana"
    Tokom učenja pišeš kratke obrazložene skice, tabele odluka i očekivane ishode na ilustrativnim primerima. Konkretne šeme, fixture fajlovi, kod, benchmark run-ovi, treniranje, deployment i produkcioni artefakti ovde se samo navode kao buduće obaveze razvojne faze — ne izrađuju se u okviru plana učenja.

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

| ML/AI odluka | Hemija koju moraš završiti | Šta treba da razumeš pre kasnije realizacije |
|---|---|---|
| CIF ingest i izdvajanje polja | 1–2, 8–10, 12 i 12A | Razliku između ?, ., 0, standardne neizvesnosti, ASU, ćelije i simetrijskih operacija; filename nije hemijski sastav. |
| Molekulski graf, ECFP i Tanimoto | 1–6, 12–15 | Kako bond order, aromatičnost, naboj, tautomerija, stereohemija i politika komponenti menjaju fingerprint i rang. |
| Exact graph, subgraph, VF2 i MCS | 2, 4–6, 11–15 | Node/edge ograničenja, smer containment-a, coverage obe strane, timeout i ambiguity politiku. |
| Dodela komponenti | 4–6, 11–13 | Razliku između liganda, coordination entity-ja, counterion-a, solventa i coformer-a; pravilo „najveći fragment“ nije dovoljno. |
| Kabsch, mapirani 3D i stereo | 3–4, 8–9, 12–15 | Atom mapping prethodi RMSD-u, refleksija zavisi od stereo profila, a coverage mora stajati uz RMSD. |
| Koordinacioni deskriptori i graf | 5–10, 12–15 | Prisustvo metala nije isto što i direktno donor mapiranje; CN, donor set, geometrija/CSM i neodređenost su različiti izlazi. |
| Periodični graf i crystal encoder | 7–10, 12A–14 | Koje fizički ekvivalentne promene zapisa ne smeju promeniti rezultat i zašto se čuva provenance periodične slike. |
| Packing, polimorfi i interakcije | 7–11A, 13–15 | Isti molekulski graf nije nužno ista čvrsta forma; packing, PXRD, HBP i Mogul su odvojeni signali sa ograničenjima. |
| Retrieval, reranking i qrels | 5–6, 11–18, 20 | Razliku između hard filtera, candidate recall-a, semantic recall-a i finalnog ranga; postojeće search grupe nisu automatski gold. |
| Kalibracija, abstention i analiza grešaka | 10–15 i 20 | Raw score nije verovatnoća, kalibracija ne koristi finalni test, a risk–coverage opisuje cenu abstention-a. |
| Structure–property i polymorph-risk target | 10–11A, 20–22 | Target se vezuje za material/solid form, uslove, metod, vreme i neizvesnost; indikator nije oracle. |
| Federativno učenje | 21–22 | FL nije zamena za licencu niti automatska privatnost; bez opravdanog multi-site targeta odluka je **DEFER**. |

## Faze, vreme, roadmap i završni dokaz razumevanja

| Faza | Blokovi | Sati | Primarni roadmap domet | Dokaz razumevanja |
|---|---:|---:|---|---|
| F0 — scope, claims i prava | 1 | 8 | R0 | Kratka beleška o dva proizvoda, profilima poređenja/pretrage, pravima, nepoznanicama i stop-uslovima. |
| F1 — hemijski graf, stereo i koordinacija | 2–3 | 16 | R0 → R1 | Mapa pojmova i ručno obrazloženi pozitivni, negativni i neodređeni DAP/donor primeri. |
| F2 — 3D kristal i periodičnost | 4–6 | 27 | R1 | Checklist invarijansi i očekivanih ishoda fizički ekvivalentnih i stvarno različitih transformacija. |
| F3 — formati, reprezentacije i data contract | 7–8 | 21 | R1 | Checklist polja, matrica gubitaka među formatima i zamišljen denominator/eligibility primer. |
| F4 — determinističko poređenje parova | 9–10 | 24 | R2; osnova R4 App 2 | Predložak pair izveštaja i nekoliko ručno razrađenih slučajeva sa statusima i evidence-om. |
| F5 — retrieval, exact oracle i reranking | 11–12 | 24 | R2 App 1; osnova R4 i R6 | Beleška o dizajnu benchmarka, anotaciji i toku exact → candidate → rerank. |
| F6 — gold, split, klasični ML i kalibracija | 13 | 12 | R3 → R5 | Dizajn evaluacije, skica leakage-safe split-a i tumačenje hipotetičkih rezultata. |
| F7 — periodic deep i metric learning challenger | 14–15 | 26 | R7 | Uporedna projektantska tabela i obrazloženi budući **GO** ili **DEFER** kriterijumi. |
| F8 — governance, white paper i naredne faze | 16 | 20 | Odluke za R8–R10 | Završni memorandum o provenance-u, reproduktivnosti, SLM/API granici i FL odluci. |

Ukupno je oko **178 h**: približno 122 h postojećeg kursa hemije i 56 h ML/AI nadogradnje. Redovni blokovi sabiraju 168 h; poslednjih do 10 h služi za završnu sintezu i usmenu samoproveru. To je 16 intenzivnih nedelja pri 10–13 h rada, odnosno oko 22–23 nedelje pri tempu od 8 h.

## Nedelja po nedelja

### Nedelja 1 — problem pre algoritma (8 h)

**Čitaj:** početne strane oba dela dokumentacije, hemijsku mapu projekta i dijagnostiku; zatim ML/AI scope, pipeline mapu i izvršni deo roadmapa do R2.

**Fokus:** za oba proizvoda odredi objekat, korisničku odluku, target, cenu greške, evidence i ono što ostaje blokirano bez CSD prava ili gold podataka.

**Projektantska vežba:** frazu „sličan kristal“ razloži na najmanje pet različitih claim-ova. Uz svaki napiši dovoljan input i uslov za **UNKNOWN** ili **not_applicable**.

**Kapija:** umeš da objasniš zašto App 1 nije samo klasifikator, App 2 nije jedna univerzalna matrica score-a i LLM nije parser.

### Nedelja 2 — od atoma do stereo-svesnog grafa (8 h)

**Čitaj:** hemija 1–4.

**Fokus:** formula naspram grafa, formalni/parcijalni naboj i oksidaciono stanje, konfiguracija naspram konformacije, nepoznata stereo oznaka naspram ahiralnosti.

**Projektantska vežba:** na pet malih nacrtanih primera napravi node/edge tabelu i obrazloži očekivani uticaj promene aromatičnosti, tautomerije, protonacije i stereo politike na fingerprint.

**Kapija:** prolaziš hemijsku Kapiju A i ne pretvaraš nepoznato polje u podrazumevanu vrednost.

### Nedelja 3 — DAP, metali i koordinaciona semantika (8 h)

**Čitaj:** hemija 5–6.

**Fokus:** tri DAP N donora, potential naspram observed denticity, metal u entry-ju naspram metala u istoj komponenti i direktne N3 koordinacije.

**Projektantska vežba:** napiši kriterijume za pozitivan, težak negativan i reprezentaciono neodređen slučaj; posebno objasni tvrdnju „isti metal je direktno vezan za sva tri mapirana DAP N“.

**Kapija:** nijedan kriterijum se ne svodi samo na formulu, filename, SMILES tačku ili pripadnost staroj search grupi.

### Nedelja 4 — 3D, ćelija i periodični susedi (9 h)

**Čitaj:** hemija 7–8.

**Fokus:** frakcione i Cartesian koordinate, metric tensor, PBC i činjenica da fizički objekat ne prestaje na ivici nacrtane ćelije.

**Projektantska vežba:** ručno prođi kroz ilustrativan proračun iz L3/L4 i u tabeli zabeleži očekivano ponašanje kontakta pri wrap-u, translaciji, rotaciji i promeni redosleda atoma.

**Kapija:** umeš da obrazložiš koje udaljenosti moraju ostati iste i koji podaci o simetrijskoj operaciji i periodičnoj slici bi se kasnije čuvali.

### Nedelja 5 — simetrija, kvalitet i neizvesnost (9 h)

**Čitaj:** hemija 9–10.

**Fokus:** ASU, ćelija i supercell; setting/origin promena naspram fizičke razlike; measured naspram simulated PXRD; profil kvaliteta naspram jednog R praga.

**Projektantska vežba:** opiši jednu ekvivalentnu promenu zapisa i jednu stvarnu promenu strukture, pa za nekoliko problema kvaliteta odredi očekivani status.

**Kapija:** ekvivalentan zapis ne tretiraš kao novi kristal, a odsutan ili loš input ne pretvaraš u score 0.

### Nedelja 6 — polimorfi, packing i referentni signali (9 h)

**Čitaj:** hemija 11 i 11A.

**Fokus:** parent compound, solid form, polymorph, solvate/hydrate/co-crystal i redetermination; granice Mogul, HBP, packing i PXRD signala.

**Projektantska vežba:** obrazloži slučaj sa istim molekulskim grafom i različitim packing-om i navedi kakva bi nezavisna potvrda bila potrebna za jaču tvrdnju.

**Kapija:** prolaziš hemijsku Kapiju C i umeš da predvidiš očekivanja za origin, wrap, setting/basis, supercell, stereo i disorder slučajeve.

### Nedelja 7 — formati i loss-aware ingest (10 h)

**Čitaj:** hemija 12, 12A i 13; zatim prvi deo cross-format/lifecycle modula.

**Fokus:** šta CIF, MOL, MOL2, SDF i SMILES čuvaju, gube, dodeljuju ili ostavljaju nepoznatim; original i purpose-specific view nisu isto.

**Projektantska vežba:** napravi matricu gubitaka i checklist podataka koje bi budući sistem morao čuvati: izvor, hash, parser/verziju, field-level poreklo, konflikt, status i transformacioni lineage.

**Kapija:** lossy format ne prepisuje bogatiji izvor, uspešan parse nije isto što i validan crystal model i nijedan entry ne nestaje bez accounting-a.

### Nedelja 8 — eligibility, reprezentacije i lokalni bias (11 h)

**Čitaj:** hemija 14–17 i 21; dovrši cross-format/lifecycle ugovor.

**Fokus:** declared, curated i geometry-neighbor graf; granice 2D, isolated-3D i periodic reprezentacije; identity, family, lifecycle i rights pre splita.

**Projektantska vežba:** na malom zamišljenom primeru nacrtaj union inventar, channel coverage, međusobno isključiv exclusion waterfall i proveru očuvanja broja zapisa.

**Kapija:** isti entry u svim formatima/verzijama pripada istoj split grupi, a missing SMILES nije ni missing graph ni negativna labela.

### Nedelja 9 — deterministički App 2: mapping i 3D (12 h)

**Čitaj:** hemija 19 i pairwise modul 4.1–4.9.

**Fokus:** comparison profile, dodela komponenti sa unmatched opcijom, exact/subgraph/MCS semantika, automorfizmi, Kabsch posle mapping-a i koordinacioni evidence.

**Projektantska vežba:** za 4–6 ilustrativnih struktura ručno odredi broj parova i očekivano ponašanje grana pri timeout-u, unknown bond-u, missing cell-u i neodređenom donor assignment-u. Ne gradi engine.

**Kapija:** razumeš zašto svaki par i svaka grana moraju imati stanje i zašto smer A→B može menjati coverage, ali ne i simetrične veličine.

### Nedelja 10 — deterministički App 2: packing i evidence (12 h)

**Čitaj:** dovrši pairwise modul 4.10–4.21.

**Fokus:** uloge i granice COMPACK/PAC, CrystalCMP, SOAP–REMatch, PXRD i interaction networks; primenljivost i licencna dostupnost.

**Projektantska vežba:** skiciraj predložak evidence-rich izveštaja i ručno popuni nekoliko normalnih, failure i ambiguous slučajeva. Ako metoda nije dostupna ili validirana, predviđeni izlaz je precizan status, ne improvizovani rezultat.

**Kapija:** drugi inženjer iz tvoje skice može nedvosmisleno razumeti budući pair universe, mapping, parametre, statuse i evidence.

### Nedelja 11 — App 1: exact i višekanalni candidate retrieval (12 h)

**Čitaj:** hemija 18 i retrieval modul 3.1–3.12.

**Fokus:** eligibility/hard filter, 2D, coordination, shape i periodic kanal; exact ECFP/Tanimoto baseline, exact Flat oracle i ANN kao infrastrukturna optimizacija.

**Projektantska vežba:** na jednostavnim bit-vektorima ručno izračunaj Tanimoto za nekoliko kandidata i nacrtaj trag hard filter → kanali → unija kandidata. Zabeleži koje parametre i provenance bi budući sistem morao vezati za rang.

**Kapija:** umeš da objasniš set-equality zahtev za hard filter i zašto ANN evaluacija mora imati exact oracle iste reprezentacije i metrike.

### Nedelja 12 — reranking, qrels i retrieval evaluacija (12 h)

**Čitaj:** retrieval modul 3.13–3.22 i hemiju 20, sa fokusom na claim, gold, split i metrike.

**Fokus:** infrastructure Recall@N, expert candidate Recall@N i end-to-end nDCG/Recall; pool, unjudged primeri, hard negatives i granica candidate/reranker greške.

**Projektantska vežba:** na malom zamišljenom skupu napravi vodič za slepu graded-relevance anotaciju i ručno obrazloži jedan tok exact → candidate → rerank, uključujući izgubljen relevantan kandidat.

**Kapija:** candidate miss ne pripisuješ rerankeru, stare search grupe nisu gold i novi neocenjeni vrh rezultata zahteva dopunu pool-a.

### Nedelja 13 — split, baseline-i, kalibracija i analiza grešaka (12 h)

**Čitaj:** dovrši hemiju 20, zatim klasični ML i sekcije 6.8–6.12 metric-learning modula.

**Fokus:** estimand pre splita; query/family grouping, 1D warm/cold, 2D cold/cold i temporal holdout; nezavisne grupe naspram broja parova.

**Projektantska vežba:** nacrtaj leakage-safe train/validation/calibration/test podelu, tabelu budućih baseline-a i odluka, pa protumači zamišljene rezultate za intervale, worst slice, kalibraciju i risk–coverage. Ne treniraš modele.

**Kapija:** model, prag i calibrator se ne biraju na finalnom testu, raw score nije verovatnoća i **KEEP BASELINE** je ispravan ishod kada nema praktičnog dobitka.

### Nedelja 14 — periodični graf i encoder contract (13 h)

**Čitaj:** periodične crystal encodere.

**Fokus:** site features, edge vrste, image/lattice podaci, cell/global state, occupancy/disorder i invariance/equivariance ugovor; crystal encoder, pair model i property model nisu isto.

**Projektantska vežba:** uporedi input i invariance zahteve nekoliko opisanih encoder porodica i napiši očekivane metamorphic provere koje bi prethodile bilo kakvom treningu.

**Kapija:** znaš koje transformacije ne menjaju target semantiku, kako stereo profil utiče na refleksiju i zašto nevalidan periodic input nije zero-filled pseudo-kristal.

### Nedelja 15 — metric learning bez lažnih parova (13 h)

**Čitaj:** ceo metric learning i production-gate modul.

**Fokus:** equivalence, relation i query-conditioned relevantnost; granice contrastive/triplet/InfoNCE pristupa; dual encoder naspram exact evidence-a i cross-graph comparator-a.

**Projektantska vežba:** napravi uporednu tabelu descriptor+GBDT, CGCNN i izabranog Matformer/ALIGNN kandidata, kao i plan budućih kontrola: isti target/split/budžet, ablation, false-negative audit, više label-budget tačaka i seed-ova.

**Kapija:** umeš da definišeš unapred šta bi značili praktična pobeda, critical-slice non-inferiority, kalibracija, abstention, SLO, licence i reproduktivnost; inače je odluka **DEFER**.

### Nedelja 16 — governance, white paper i naredne faze (10 h + do 10 h sinteze)

**Čitaj:** hemija 22, ceo roadmap po drugi put i referentne audite; lokalni SLM/RAG samo na nivou odluke, a API modul samo ako se razmatra R9.

**Fokus:** white-paper pojmovi naspram state, property i evidence ugovora; polymorph-risk indikator naspram tvrdnje; poslovni i naučni uslovi za R8/R9/R10.

**Projektantska vežba:** usmeno odbrani jedan search query, pair rezultat, **UNKNOWN** slučaj, leakage incident i licence stop. Za FL prođi preduslove i nacrtaj threat model na konceptualnom nivou.

**Kapija:** FL je **DEFER** bez zakonitog, zajedničkog multi-site supervised targeta koji se ne može centralizovati; SLM/API su **DEFER** bez dokazane UX rupe.

## Kapije prelaza

| Kapija | Prelaziš kada razumeš i možeš da obrazložiš | Ne prolazi ako |
|---|---|---|
| G0 — claim i prava | objekat, target, scope, evidence, rights pitanja, abstention i stop-uslov za svaki output | nepoznata licenca se prećutno tretira kao dozvola |
| G1 — hemijski graf i koordinacija | DAP motif, stereo, charge, component i donor mapping na ilustrativnom primeru | formula, filename ili samo prisustvo metala glume povezanost |
| G2 — crystal i 3D | očekivano PBC/symmetry/setting/basis i stereo ponašanje | RMSD prethodi atom mapping-u ili cell/space group glume packing dokaz |
| G3 — data core | union inventar, lineage, purpose view, lifecycle i denominator accounting na malom primeru | silent overwrite, inner-join drop ili missing status postaje vrednost |
| G4 — deterministički App 2 | pair universe, branch state, evidence, simetriju i usmereni coverage | non-assessed grana nestaje, postaje nula ili dobija relation labelu |
| G5 — App 1 retrieval | exact filter/oracle, multichannel coverage i tri nivoa retrieval evaluacije | ANN brzina glumi hemijsku tačnost ili reranker skriva candidate miss |
| G6 — supervised evaluacija | leakage-safe gold/qrels, split, kalibraciju i error-analysis plan | stare grupe, duplikati ili finalni test utiču na trening i tuning |
| G7 — deep challenger | fer poređenje i budući GO/DEFER kriterijum za critical slice, invarijanse, SLO i licence | jedan random split, seed ili label budžet se smatra dovoljnim dokazom |
| G8 — sledeća faza | merljivu rupu, odobren budući data flow, baseline i stop-uslov za R8/R9/R10 | sama oznaka „AI“, „LLM“ ili „FL“ služi kao opravdanje |

## Minimalni paket beležaka svake faze

Za učenje je dovoljno da beleška sadrži:

- pitanje ili claim i populaciju na koju se odnosi;
- hemijski objekat, target i relevantnu reprezentaciju;
- relevantne izvore, status prava i ono što još nije poznato;
- ilustrativan primer i očekivani ishod;
- missing, ambiguous, not-applicable i failure slučajeve;
- buduće zahteve za validaciju, metrike i stop-uslov;
- poznate granice i odluku šta treba čitati ili proveravati sledeće;
- vezu sa rečnikom i čestim zabludama iz hemijskog dela.

Egzaktne šeme, manifesti, fixture fajlovi, kod, benchmark merenja, trenirani modeli, deployment i produkcioni izveštaji pripadaju kasnijoj razvojnoj fazi. Plan učenja treba samo da objasni **šta** će tada morati da postoji i **zašto**.

## Uslovni nastavak posle osnovnih blokova

Ovo nisu automatske obaveze osnovnog 2CDC scope-a.

### R8 — lokalni SLM i dokumentacioni RAG (oko 16 h teorijske nadogradnje)

Pročitaj lokalni SLM/RAG modul i uporedi uloge Tier 0 form/DSL/template pristupa, field-aware BM25, constrained NL→DSL, dense retrieval, RRF i malog reranker-a. Osmisli kako bi se kasnije proveravali intent/paraphrase grupe, multilingual i rare-token slučajevi, bez menjanja determinističkog naučnog rezultata.

**Ishod učenja:** plan buduće evaluacije lokalnog jezičkog sloja, sa fallback-om, bez implementiranja ili testiranja sistema.

### R9 — spoljni API (oko 8 h za odluku)

Pročitaj API/security modul. Odredi šta bi pre bilo kakvog poziva moralo biti formalno odobreno: klasa podataka, minimalni payload, broker, retention/region/processor uslovi, audit, circuit breaker i lokalni fallback. Projektni podaci se ne šalju radi probe.

**Ishod učenja:** obrazložen budući **GO/NO-GO** okvir; podrazumevani odgovor je **NO-GO** dok lokalni baseline nema dokazanu rupu i rights/security gate nije pozitivan.

### R10 — federativno učenje (oko 6 h za odluku)

Ponovo pročitaj FL delove hemijskog poglavlja 22 i roadmapa. Uporedi local-only, shared-public-pretraining i dozvoljeni centralni baseline, pa objasni kako threat model određuje secure aggregation, diferencijalnu privatnost i robust aggregation.

**Ishod učenja:** konceptualna **GO/DEFER** odluka. Bez stvarnog multi-site targeta koji se zakonito ne može centralizovati rezultat mora biti **DEFER**; implementacija nije deo plana.

## Završni kriterijum spremnosti

Spreman si za prelazak na zasebno planiranje realizacije kada možeš da odbraniš ceo lanac:

**odobren izvor → loss-aware purpose view → hemijski i periodični objekat → deterministički exact evidence → candidate retrieval i/ili pair comparison → leakage-safe gold/qrels i split → kalibrisan target-specific challenger sa abstention-om → reproduktivnost i licencna dozvoljenost → objašnjiv rezultat ili precizan UNKNOWN**

Ako bilo koja strelica nema jasno značenje, teorijsko opravdanje i plan buduće provere, složeniji model još nije sledeći korak.
