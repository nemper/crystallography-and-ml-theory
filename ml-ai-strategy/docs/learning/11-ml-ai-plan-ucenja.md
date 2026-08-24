# Plan učenja ML/AI dela za 2CDC

Ovo je putanja kroz postojeći kurs hemije i ML/AI strategiju za inženjera koji već zna da trenira, validira i isporuči ML sistem, ali tek gradi domensko znanje iz hemije i kristalografije. Plan ne ponavlja teoriju iz postojećih poglavlja. On određuje **redosled, preduslove, projektantske vežbe i dokaze razumevanja**.

Osnovna putanja organizovana je kao niz tematskih celina povezanih preduslovima i kapijama razumevanja. Nema kalendarski raspored niti procenu trajanja: napredovanje zavisi isključivo od savladanih preduslova i prolaska odgovarajućih kapija. Putanja ne uključuje implementiranje dve aplikacije, treniranje modela niti kompletno čitanje svake spoljne reference.

Ovaj plan dopunjuje [postojeći plan učenja hemije](https://github.com/nemper/crystallography-and-ml-theory/blob/main/chemistry-foundations/docs/pocetak/plan-ucenja.md). Hemijski plan daje redosled domenskog gradiva; ova strana govori kada je to gradivo dovoljno savladano za određenu ML/AI odluku.

!!! info "Granica ovog plana"
    Tokom učenja pišeš kratke obrazložene skice, uporedne tabele i očekivane ishode na ilustrativnim primerima. Plan ostaje na pojmovima, pretpostavkama i dokazima; ne projektuje konkretan sistem niti izvodi praktične sistemske probe.

## Pravila rada

1. **Napredovanje je zasnovano na dokazu, ne na datumu.** Ako kapija ne prolazi, ponovi ciljanu vežbu; nemoj samo nastaviti čitanje.
2. **Svaki score prvo dobija semantiku.** Pre poređenja metoda napiši objekat, target, primenljivost, reprezentaciju, metriku i značenje neuspeha.
3. **Determinističko jezgro prethodi ML-u.** Parser, standardizacija, hard filteri, atom/component mapping i periodična geometrija nisu poslovi za generativni model.
4. **`UNKNOWN` nije nula.** Dvosmisleno, odsutno, neprimenljivo, blokirano kvalitetom, isteklo i neuspešno nisu ista stanja i nijedno automatski ne postaje negativna labela ili similarity `0`.
5. **Restricted podaci ostaju u odobrenom data-plane-u.** Raw CSD i fakultetski sadržaj ne kopira se radi vežbe; primer mora biti otvoren, sintetički ili eksplicitno dozvoljen za tu svrhu.
6. **Ne uči opšti ML ponovo.** Linearni modeli, tree ensemble-i, GNN, metric learning i kalibracija obrađuju se kroz 2CDC targete, splitove, failure slice-ove i uslove fer evaluacije.

## Prioriteti i tačan redosled čitanja

Oznake u tabeli znače:

- **O — obavezno:** potrebno za sledeću kapiju;
- **P — preporučeno:** potrebno pre odgovarajuće napredne teme, ali ne blokira ranije gradivo;
- **R — referenca:** otvara se tokom dizajna, error analysis-a ili audita; ne čita se linearno unapred.

Uporedna mapa algoritamskih porodica čita se dva puta: prvi put radi orijentacije, a drugi put u celosti nakon osnovnih hemijskih i ML/AI preduslova, kada već možeš da osporiš primenljivost svake porodice.

| Red | Dokumentacija | Prioritet | Kada i zašto |
|---:|---|---|---|
| 1 | Hemija: naslovna, „Šta projekat zapravo traži“, plan i dijagnostika | O | Pre svega: razdvoji sastav, graf, konformer, kristal i eksperimentalni model. |
| 2 | ML/AI: [početna](../index.md), [scope](../00-scope.md) i [mapa pipeline-a](../01-pipeline-decision-map.md) | O | Definiši dva problema, funkcije pipeline-a i razliku između referentnih i learned metoda. |
| 3 | [Uporedna mapa algoritamskih porodica](../roadmap/10-optimal-stack-roadmap.md) | O | Prvi, orijentacioni prolaz kroz objekte, targete i uslove primene; nije realizacioni plan. |
| 4 | Hemija 1–6: atomi/formule, veze, 3D/stereo, organski minimum, koordinaciona hemija i DAP/Schiff-base | O | Preduslov za svaki 2D graf, fingerprint, motif, metal/donor i stereo target. |
| 5 | Hemija 7–11A: interakcije, ćelija, simetrija, kvalitet, čvrste forme, referentne raspodele/HBP | O | Preduslov za periodične grafove, packing, polimorfe, PXRD, uncertainty i crystal modele. |
| 6 | Hemija 12–17: formati, pun CIF, standardizacija, reprezentacije, sličnost, CSD/ConQuest i lokalni skup | O | Pre bilo kog dataseta, feature-a ili modela; ovde se vidi stvarni cross-format gubitak i selection bias. |
| 7 | Hemija 21 + [cross-format i lifecycle eligibility](../data/09-cross-format-eligibility.md) | O | FAIR, prava, provenance i lifecycle dopunjuju pojmovnu osnovu za sve naredne ML/AI teme. |
| 8 | Hemija 19 + [precizno pairwise poređenje](../pairs/04-precise-pairwise.md) | O | App 2 se uči prva jer se najveći deo može validirati bez pune CSD baze i bez ML-a. |
| 9 | Hemija 18 i 20 + [globalni retrieval, ANN i ranking](../retrieval/03-global-retrieval-ann-ranking.md) | O | Razdvoji exact filter, candidate recall, semantic recall, qrels i finalni ranking. |
| 10 | [Klasični ML](../classical/02-classical-ml.md) | O | Čitaj kada razumeš target, group/time split i determinističke reference. |
| 11 | [Periodični crystal encoderi](../deep/05-periodic-crystal-encoders.md), pa [metric learning i evaluacija](../deep/06-metric-learning-and-evaluation.md) | P | Ne počinji dok ne razumeš periodične/stereo invarijanse, exact oracle i gold/split protokol. |
| 12 | Hemija 22 + cela [uporedna mapa](../roadmap/10-optimal-stack-roadmap.md) | O | White-paper granice, structure–property i polymorph-risk targeti, uslovi za FL i završno poređenje algoritamskih porodica. |
| 13 | [Lokalni SLM i RAG](../language/07-local-slm-rag.md) | P | Jezička interpretacija i dokumentacioni retrieval; nije crystal representation niti naučni autoritet. |
| 14 | [Spoljni LLM API i bezbednost](../language/08-api-llm-security.md) | R | Čita se radi razumevanja minimizacije, processor/retention razlika, prompt injection-a i granica prava. |
| 15 | [Metod dokaza](../reference/evidence-method.md), [završni ML/AI audit](../reference/final-validation-2026-08-23.md), hemijski rečnik/zablude/izvori/audit | R | Koristi pri pisanju claim-a, proveri terminologije i završnom auditu; rešenja praktikuma tek posle sopstvenog pokušaja. |

Za osnovnu putanju su obavezna sva glavna hemijska poglavlja 1–22, ali ne i svaka bibliografska stavka na njihovom kraju. Spoljne radove čitaj u celosti kada dublje proučavaš metod koji taj rad definiše, na primer ECFP, VF2, Kabsch, COMPACK/PAC, HNSW ili konkretan periodic encoder.

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

## Nastavne celine i dokaz razumevanja

| Celina | Dokaz razumevanja |
|---|---|
| F0 — scope, claims i prava | Kratka beleška o dva problema, profilima poređenja/pretrage, pravima, nepoznanicama i granicama tvrdnje. |
| F1 — hemijski graf, stereo i koordinacija | Mapa pojmova i ručno obrazloženi pozitivni, negativni i neodređeni DAP/donor primeri. |
| F2 — 3D kristal i periodičnost | Checklist invarijansi i očekivanih ishoda fizički ekvivalentnih i stvarno različitih transformacija. |
| F3 — formati, reprezentacije i eligibility | Matrica gubitaka među formatima i zamišljen denominator/eligibility primer. |
| F4 — determinističko poređenje parova | Konceptualni pair izveštaj i nekoliko ručno razrađenih slučajeva sa stanjima i evidence-om. |
| F5 — retrieval, exact oracle i reranking | Beleška o anotaciji i razlikama između exact, candidate i finalnog ranga. |
| F6 — gold, split, klasični ML i kalibracija | Skica leakage-safe evaluacije i tumačenje hipotetičkih rezultata. |
| F7 — periodični deep i metric learning | Uporedna tabela modelskih porodica, njihovih pretpostavki i failure režima. |
| F8 — governance, white paper i uslovne teme | Završni memorandum o provenance-u, reproduktivnosti, SLM/API granici, polymorph-risk-u i FL uslovima. |

## Tematske celine po redosledu preduslova

### Problem pre algoritma

**Čitaj:** početne strane oba dela dokumentacije, hemijsku mapu projekta i dijagnostiku; zatim ML/AI scope, pipeline mapu i uvodne delove uporedne algoritamske mape.

**Fokus:** za oba proizvoda odredi objekat, korisničku odluku, target, cenu greške, evidence i ono što ostaje blokirano bez CSD prava ili gold podataka.

**Projektantska vežba:** frazu „sličan kristal“ razloži na najmanje pet različitih claim-ova. Uz svaki napiši dovoljan input i uslov za **UNKNOWN** ili **not_applicable**.

**Kapija:** umeš da objasniš zašto App 1 nije samo klasifikator, App 2 nije jedna univerzalna matrica score-a i LLM nije parser.

### Od atoma do stereo-svesnog grafa

**Čitaj:** hemija 1–4.

**Fokus:** formula naspram grafa, formalni/parcijalni naboj i oksidaciono stanje, konfiguracija naspram konformacije, nepoznata stereo oznaka naspram ahiralnosti.

**Projektantska vežba:** na pet malih nacrtanih primera napravi node/edge tabelu i obrazloži očekivani uticaj promene aromatičnosti, tautomerije, protonacije i stereo politike na fingerprint.

**Kapija:** prolaziš hemijsku Kapiju A i ne pretvaraš nepoznato polje u podrazumevanu vrednost.

### DAP, metali i koordinaciona semantika

**Čitaj:** hemija 5–6.

**Fokus:** tri DAP N donora, potential naspram observed denticity, metal u entry-ju naspram metala u istoj komponenti i direktne N3 koordinacije.

**Projektantska vežba:** napiši kriterijume za pozitivan, težak negativan i reprezentaciono neodređen slučaj; posebno objasni tvrdnju „isti metal je direktno vezan za sva tri mapirana DAP N“.

**Kapija:** nijedan kriterijum se ne svodi samo na formulu, filename, SMILES tačku ili pripadnost staroj search grupi.

### 3D, ćelija i periodični susedi

**Čitaj:** hemija 7–8.

**Fokus:** frakcione i Cartesian koordinate, metric tensor, PBC i činjenica da fizički objekat ne prestaje na ivici nacrtane ćelije.

**Projektantska vežba:** ručno prođi kroz ilustrativan proračun iz L3/L4 i u tabeli zabeleži očekivano ponašanje kontakta pri wrap-u, translaciji, rotaciji i promeni redosleda atoma.

**Kapija:** umeš da obrazložiš koje udaljenosti moraju ostati iste i koji podaci o simetrijskoj operaciji i periodičnoj slici bi se kasnije čuvali.

### Simetrija, kvalitet i neizvesnost

**Čitaj:** hemija 9–10.

**Fokus:** ASU, ćelija i supercell; setting/origin promena naspram fizičke razlike; measured naspram simulated PXRD; profil kvaliteta naspram jednog R praga.

**Projektantska vežba:** opiši jednu ekvivalentnu promenu zapisa i jednu stvarnu promenu strukture, pa za nekoliko problema kvaliteta odredi očekivani status.

**Kapija:** ekvivalentan zapis ne tretiraš kao novi kristal, a odsutan ili loš input ne pretvaraš u score 0.

### Polimorfi, packing i referentni signali

**Čitaj:** hemija 11 i 11A.

**Fokus:** parent compound, solid form, polymorph, solvate/hydrate/co-crystal i redetermination; granice Mogul, HBP, packing i PXRD signala.

**Projektantska vežba:** obrazloži slučaj sa istim molekulskim grafom i različitim packing-om i navedi kakva bi nezavisna potvrda bila potrebna za jaču tvrdnju.

**Kapija:** prolaziš hemijsku Kapiju C i umeš da predvidiš očekivanja za origin, wrap, setting/basis, supercell, stereo i disorder slučajeve.

### Formati i loss-aware ingest

**Čitaj:** hemija 12, 12A i 13; zatim prvi deo cross-format/lifecycle modula.

**Fokus:** šta CIF, MOL, MOL2, SDF i SMILES čuvaju, gube, dodeljuju ili ostavljaju nepoznatim; original i purpose-specific view nisu isto.

**Projektantska vežba:** napravi matricu gubitaka i obrazloži koje vrste provenance-a su potrebne da bi se razlikovali izvor, verzija, konflikt, raspoloživost i transformacija.

**Kapija:** lossy format ne prepisuje bogatiji izvor, uspešan parse nije isto što i validan crystal model i nijedan entry ne nestaje bez accounting-a.

### Eligibility, reprezentacije i lokalni bias

**Čitaj:** hemija 14–17 i 21; dovrši cross-format/lifecycle ugovor.

**Fokus:** declared, curated i geometry-neighbor graf; granice 2D, isolated-3D i periodic reprezentacije; identity, family, lifecycle i rights pre splita.

**Projektantska vežba:** na malom zamišljenom primeru nacrtaj union inventar, channel coverage, međusobno isključiv exclusion waterfall i proveru očuvanja broja zapisa.

**Kapija:** isti entry u svim formatima/verzijama pripada istoj split grupi, a missing SMILES nije ni missing graph ni negativna labela.

### Deterministički App 2: mapping i 3D

**Čitaj:** hemija 19 i pairwise modul 4.1–4.8.

**Fokus:** comparison profile, dodela komponenti sa unmatched opcijom, exact/subgraph/MCS semantika, automorfizmi, Kabsch posle mapping-a i koordinacioni evidence.

**Projektantska vežba:** za 4–6 ilustrativnih struktura ručno odredi broj parova i očekivano ponašanje grana pri timeout-u, unknown bond-u, missing cell-u i neodređenom donor assignment-u. Ne gradi engine.

**Kapija:** razumeš zašto svaki par i svaka grana moraju imati stanje i zašto smer A→B može menjati coverage, ali ne i simetrične veličine.

### Deterministički App 2: packing i evidence

**Čitaj:** dovrši pairwise modul 4.9–4.21.

**Fokus:** uloge i granice COMPACK/PAC, CrystalCMP, SOAP–REMatch, PXRD i interaction networks; primenljivost i licencna dostupnost.

**Projektantska vežba:** skiciraj predložak evidence-rich izveštaja i ručno popuni nekoliko normalnih, failure i ambiguous slučajeva. Ako metoda nije dostupna ili validirana, predviđeni izlaz je precizan status, ne improvizovani rezultat.

**Kapija:** drugi inženjer iz tvoje skice može nedvosmisleno razumeti budući pair universe, mapping, parametre, statuse i evidence.

### App 1: exact i višekanalni candidate retrieval

**Čitaj:** hemija 18 i retrieval modul 3.1–3.12.

**Fokus:** eligibility/hard filter, 2D, coordination, shape i periodic kanal; exact ECFP/Tanimoto baseline, exact Flat oracle i ANN kao infrastrukturna optimizacija.

**Projektantska vežba:** na jednostavnim bit-vektorima ručno izračunaj Tanimoto za nekoliko kandidata i nacrtaj trag hard filter → kanali → unija kandidata. Zabeleži koje parametre i provenance bi budući sistem morao vezati za rang.

**Kapija:** umeš da objasniš set-equality zahtev za hard filter i zašto ANN evaluacija mora imati exact oracle iste reprezentacije i metrike.

### Reranking, qrels i retrieval evaluacija

**Čitaj:** retrieval modul 3.13–3.22 i hemiju 20, sa fokusom na claim, gold, split i metrike.

**Fokus:** infrastructure Recall@N, expert candidate Recall@N i end-to-end nDCG/Recall; pool, unjudged primeri, hard negatives i granica candidate/reranker greške.

**Projektantska vežba:** na malom zamišljenom skupu napravi vodič za slepu graded-relevance anotaciju i ručno obrazloži jedan tok exact → candidate → rerank, uključujući izgubljen relevantan kandidat.

**Kapija:** candidate miss ne pripisuješ rerankeru, stare search grupe nisu gold i novi neocenjeni vrh rezultata zahteva dopunu pool-a.

### Split, baseline-i, kalibracija i analiza grešaka

**Čitaj:** dovrši hemiju 20, zatim klasični ML i sekcije 6.8–6.12 metric-learning modula.

**Fokus:** estimand pre splita; query/family grouping, 1D warm/cold, 2D cold/cold i temporal holdout; nezavisne grupe naspram broja parova.

**Projektantska vežba:** nacrtaj leakage-safe train/validation/calibration/test podelu, tabelu budućih baseline-a i odluka, pa protumači zamišljene rezultate za intervale, worst slice, kalibraciju i risk–coverage. Ne treniraš modele.

**Kapija:** model, prag i calibrator se ne biraju na finalnom testu, raw score nije verovatnoća i **KEEP BASELINE** je ispravan ishod kada nema praktičnog dobitka.

### Periodični graf i encoder contract

**Čitaj:** periodične crystal encodere.

**Fokus:** site features, edge vrste, image/lattice podaci, cell/global state, occupancy/disorder i invariance/equivariance ugovor; crystal encoder, pair model i property model nisu isto.

**Projektantska vežba:** uporedi input i invariance zahteve nekoliko opisanih encoder porodica i napiši očekivane metamorphic provere koje bi prethodile bilo kakvom treningu.

**Kapija:** znaš koje transformacije ne menjaju target semantiku, kako stereo profil utiče na refleksiju i zašto nevalidan periodic input nije zero-filled pseudo-kristal.

### Metric learning bez lažnih parova

**Čitaj:** ceo metric learning i evaluacioni modul.

**Fokus:** equivalence, relation i query-conditioned relevantnost; granice contrastive/triplet/InfoNCE pristupa; dual encoder naspram exact evidence-a i cross-graph comparator-a.

**Projektantska vežba:** napravi uporednu tabelu descriptor+GBDT, CGCNN i Matformer/ALIGNN porodica, sa istim targetom i splitom, potrebnim ablation-om, false-negative pitanjima i uticajem label budžeta.

**Kapija:** umeš da objasniš praktičnu korist, critical-slice non-inferiority, kalibraciju, abstention, resurse, licence i reproduktivnost bez pretpostavke da deep model mora pobediti.

### Governance, white paper i uslovne teme

**Čitaj:** hemija 22, celu uporednu mapu po drugi put i referentne audite; zatim teorijske granice lokalnog SLM/RAG-a i spoljnog API-ja.

**Fokus:** white-paper pojmovi naspram state, property i evidence semantike; polymorph-risk indikator naspram tvrdnje; naučni, pravni i bezbednosni uslovi za SLM, API i FL.

**Projektantska vežba:** usmeno odbrani jedan search query, pair rezultat, **UNKNOWN** slučaj, leakage incident i licence stop. Za FL prođi preduslove i nacrtaj threat model na konceptualnom nivou.

**Kapija:** umeš da objasniš zašto FL zahteva zakonit zajednički multi-site supervised target, a SLM/API ne postaju naučni autoritet time što su jezički sposobni.

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
| G7 — deep modeli | fer poređenje za critical slice, invarijanse, resurse i licence | jedan random split, seed ili label budžet se smatra dovoljnim dokazom |
| G8 — uslovne teme | koje dodatno pitanje rešavaju SLM, API, polymorph-risk ili FL i koje pretpostavke zahtevaju | sama oznaka „AI“, „LLM“ ili „FL“ služi kao opravdanje |

## Minimalni paket beležaka svake nastavne celine

Za učenje je dovoljno da beleška sadrži:

- pitanje ili claim i populaciju na koju se odnosi;
- hemijski objekat, target i relevantnu reprezentaciju;
- relevantne izvore, status prava i ono što još nije poznato;
- ilustrativan primer i očekivani ishod;
- missing, ambiguous, not-applicable i failure slučajeve;
- buduće zahteve za validaciju, metrike i stop-uslov;
- poznate granice i odluku šta treba čitati ili proveravati sledeće;
- vezu sa rečnikom i čestim zabludama iz hemijskog dela.

Plan učenja beleži pojmove, pretpostavke i načine dokazivanja. Ne definiše tehničke artefakte, konkretne modele, servise ili operativne izveštaje.

## Uslovni nastavak posle osnovnih blokova

Ovo nisu automatske obaveze osnovnog 2CDC scope-a.

### Lokalni SLM i dokumentacioni RAG

Pročitaj lokalni SLM/RAG modul i uporedi formulare/rečnike, kontrolisanu međureprezentaciju, BM25, constrained decoding, dense retrieval, RRF i reranking. Objasni kako intent/paraphrase grupe, višejezični i rare-token slučajevi utiču na evaluaciju, bez menjanja determinističkog naučnog rezultata.

**Ishod učenja:** uporedna beleška o ulozi, ograničenjima i evaluaciji lokalnog jezičkog sloja.

### Spoljni API

Pročitaj API/security modul. Objasni razliku između izvorne licence, minimizacije, processor/region uslova, retention-a, cache/state-a, audit-a i prompt-injection odbrane. Projektni podaci se ne šalju radi vežbe.

**Ishod učenja:** obrazložena procena koje činjenice bi morale biti poznate pre razmatranja spoljne obrade, bez izbora providera ili modela.

### Federativno učenje

Ponovo pročitaj FL delove hemijskog poglavlja 22 i uporedne mape. Uporedi centralizovano, local-only, shared-public-pretraining i federativno učenje, pa objasni kako threat model određuje secure aggregation, diferencijalnu privatnost i robust aggregation.

**Ishod učenja:** konceptualno objašnjenje uslova pod kojima FL ima smisla. Bez stvarnog multi-site targeta koji se zakonito ne može centralizovati, FL ostaje samo teorijska porodica.

## Završni kriterijum spremnosti

Integrisano razumevanje imaš kada možeš da odbraniš ceo lanac:

**odobren izvor → loss-aware purpose view → hemijski i periodični objekat → deterministički exact evidence → candidate retrieval i/ili pair comparison → leakage-safe gold/qrels i split → kalibrisana target-specific learned metoda sa abstention-om → reproduktivnost i licencna dozvoljenost → objašnjiv rezultat ili precizan UNKNOWN**

Ako bilo koja strelica nema jasno značenje, teorijsko opravdanje i plan buduće provere, složeniji model još nije sledeći korak.
