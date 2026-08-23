# 2CDC ML/AI Strategy

Ova dokumentacija odgovara na praktično pitanje: **koji algoritam ili kombinacija algoritama je najbolji za svaku fazu dve 2CDC aplikacije, pod kojim uslovima i na osnovu kog dokaza?**

Ne tražimo jedan univerzalni model. Globalni retrieval, precizno poređenje kristala, procena svojstava, objašnjenje rezultata i razgovorni interfejs imaju različite ciljeve, greške, podatke i acceptance kriterijume.

Dokumentacija će za svaki kandidat jasno razdvojiti:

- algoritamsku funkciju u pipeline-u;
- ulaz, target i output;
- podršku iz primarnih radova ili zvanične dokumentacije;
- lokalno proverljivu inženjersku hipotezu;
- baseline, challenger i uslov pod kojim se bira pobednik;
- failure modes, abstention i licencne granice.

Počni od [scope-a i pravila odlučivanja](00-scope.md), a zatim koristi [mapu pipeline-a](01-pipeline-decision-map.md) da vidiš gde pripada svaka porodica algoritama.

Prvi detaljni modul obrađuje [klasični ML](classical/02-classical-ml.md): od linearnih baseline-a i Random Forest-a do boosting-a, SVM-a, GPR-a, kalibracije i conformal abstention-a.
