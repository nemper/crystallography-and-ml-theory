# 2CDC ML/AI Strategy

Ova dokumentacija odgovara na teorijsko pitanje: **koje porodice algoritama mogu da opišu pojedine delove dva 2CDC problema, pod kojim pretpostavkama i uz kakva ograničenja dokaza?**

Ako počinješ bez ML/AI predznanja, prvo pročitaj [ML/AI od nule](00a-osnove-ml.md), sa osnovnim pojmovima, matematičkim oznakama i rešenim primerima. Zatim prati [plan učenja za početnika i ML inženjera](11-ml-ai-plan-ucenja.md). On povezuje redosled gradiva sa hemijskim preduslovima i proverama razumevanja, bez projektovanja ili implementiranja aplikacija tokom učenja.

Ne tražimo jedan univerzalni model. Globalni retrieval, precizno poređenje kristala, procena svojstava, objašnjenje rezultata i eventualni jezički interfejs imaju različite ciljeve, greške, podatke i kriterijume dokaza. Jezički model nije zahtev izvornog brief-a; posmatra se samo kao opcioni UX sloj nad determinističkim naučnim jezgrom.

Dokumentacija za svaku porodicu jasno razdvaja:

- algoritamsku funkciju u pipeline-u;
- ulaz, target i output;
- podršku iz primarnih radova ili zvanične dokumentacije;
- lokalno proverljivu hipotezu;
- referentnu metodu i uslove fer poređenja;
- failure modes, abstention i licencne granice.

Posle osnovnog računa koristi [scope](00-scope.md) i [pipeline mapu](01-pipeline-decision-map.md) samo za orijentaciju. Zatim prati [jedinstvenu putanju](11-ml-ai-plan-ucenja.md): deterministička osnova → osnovna evaluacija → klasični ML/boosting/kernel → učeno rangiranje i izabrane napredne grane. Neuralni deo nije preduslov evaluacije. Korake povezuje [nastavni primer Q–B–C–D](https://github.com/nemper/crystallography-and-ml-theory/blob/main/chemistry-foundations/docs/povezani-primer.md).

Modul [klasičnog ML-a](02-classical-ml.md) dolazi posle osnovne determinističke putanje i evaluacije: od linearnih baseline-a i Random Forest-a do boostinga, SVM-a, GPR-a, kalibracije i conformal abstention-a.

Modul [globalne pretrage](03-global-retrieval-ann-ranking.md) razdvaja hard filtere, hemijske reprezentacije, exact/ANN candidate generation, filter-aware indeksiranje i learning-to-rank.

Modul [preciznog pairwise poređenja](04-precise-pairwise.md) opisuje component assignment, VF2/MCS, Kabsch, koordinacionu geometriju, COMPACK/PAC, SOAP–REMatch, PXRD i interaction networks.

Modul [periodičnih crystal encodera](05-periodic-crystal-encoders.md) proverava CGCNN, SchNet, DimeNet, MEGNet, ALIGNN, Matformer i equivariant modele, sa eksplicitnim periodic-invariance i stereo gate-ovima.

Modul [metric learning-a i pair modela](06-metric-learning-and-evaluation.md) obrađuje loss-eve, positive/negative protokol, dual/cross-encoder uloge, splitove, kalibraciju i evaluaciju.

Modul [lokalnih SLM-ova i RAG-a](07-local-slm-rag.md) objašnjava kontrolisanu interpretaciju, granicu determinističkog naučnog jezgra, BM25/dense/RRF retrieval, LoRA/QLoRA i evaluaciju.

Modul [spoljnih LLM API-ja i bezbednosti](08-api-llm-security.md) razdvaja izvornu licencu, minimizaciju, processor/region/retention/cache kontrole, prompt-injection odbranu i vendor-neutral evaluaciju.

Centralni modul o [cross-format i lifecycle eligibility-ju](09-cross-format-eligibility.md) objašnjava kako CIF/MOL/MOL2/SDF/SMILES gubici, missingness, prava i lifecycle mogu promeniti fingerprint, graf, indeks, trening skup ili evaluation denominator.

[Uporedna mapa algoritamskih porodica i uslova primene](10-optimal-stack-roadmap.md) povezuje determinističke, retrieval/ANN, klasične, periodične/deep, jezičke, property, polymorph-risk i federativne metode bez propisivanja realizacionog redosleda.
