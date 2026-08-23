# 2CDC ML/AI Strategy

Ova dokumentacija odgovara na praktično pitanje: **koji algoritam ili kombinacija algoritama je najbolji za svaku fazu dve 2CDC aplikacije, pod kojim uslovima i na osnovu kog dokaza?**

Ne tražimo jedan univerzalni model. Globalni retrieval, precizno poređenje kristala, procena svojstava, objašnjenje rezultata i eventualni jezički interfejs imaju različite ciljeve, greške, podatke i acceptance kriterijume. Jezički model nije zahtev izvornog brief-a; ispituje se kao opcioni UX sloj nad potpunim determinističkim Tier 0 sistemom.

Dokumentacija će za svaki kandidat jasno razdvojiti:

- algoritamsku funkciju u pipeline-u;
- ulaz, target i output;
- podršku iz primarnih radova ili zvanične dokumentacije;
- lokalno proverljivu inženjersku hipotezu;
- baseline, challenger i uslov pod kojim se bira pobednik;
- failure modes, abstention i licencne granice.

Počni od [scope-a i pravila odlučivanja](00-scope.md), a zatim koristi [mapu pipeline-a](01-pipeline-decision-map.md) da vidiš gde pripada svaka porodica algoritama.

Prvi detaljni modul obrađuje [klasični ML](classical/02-classical-ml.md): od linearnih baseline-a i Random Forest-a do boosting-a, SVM-a, GPR-a, kalibracije i conformal abstention-a.

Modul [globalne pretrage](retrieval/03-global-retrieval-ann-ranking.md) razdvaja hard filtere, hemijske reprezentacije, exact/ANN candidate generation, filter-aware indeksiranje i learning-to-rank.

Modul [preciznog pairwise poređenja](pairs/04-precise-pairwise.md) opisuje component assignment, VF2/MCS, Kabsch, koordinacionu geometriju, COMPACK/PAC, SOAP–REMatch, PXRD i interaction networks.

Modul [periodičnih crystal encodera](deep/05-periodic-crystal-encoders.md) proverava CGCNN, SchNet, DimeNet, MEGNet, ALIGNN, Matformer i equivariant modele, sa eksplicitnim periodic-invariance i stereo gate-ovima.

Modul [metric learning-a i pair modela](deep/06-metric-learning-and-evaluation.md) određuje loss-eve, positive/negative protokol, dual/cross-encoder uloge, splitove, kalibraciju i production gate.

Modul [lokalnih SLM-ova i RAG-a](language/07-local-slm-rag.md) definiše bezbedan NL→DSL tok, granicu determinističkog naučnog jezgra, aktuelni model shortlist, hibridni retrieval, fine-tuning lestvicu i production evaluaciju.
