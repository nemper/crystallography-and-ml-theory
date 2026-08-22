# Završni mini-projekat

## Zadatak

Bez treniranja „velikog modela“, projektuj i demonstriraj hemijski validan vertikalni presek obe 2CDC aplikacije na malom, lokalno dozvoljenom skupu.

Poenta nije broj feature-a. Poenta je da svaki ulaz, score, izuzetak i claim imaju precizno značenje i dokaz.

## Deo A — Global-search prototip

Za jedan query CIF demonstriraj:

1. immutable ingest, hash i provenance;
2. CIF parse/QC report;
3. component i crystal prikaze;
4. najmanje dva odvojena search moda;
5. formula/element/component/quality filtere sa eksplicitnim scope-om;
6. transparentni 2D baseline;
7. exact ili high-cost rerank malog candidate set-a;
8. karticu rezultata sa matched evidence i warnings;
9. abstention za nepodržan packing/coordination claim;
10. licence-aware export odluku.

## Deo B — Pair-comparator prototip

Za 10–20 pažljivo izabranih CIF-ova:

1. izračunaj svih (n(n-1)/2) parova;
2. odvoji composition, graph, coordination, conformation, cell, packing i interaction rezultate;
3. sačuvaj atom/component mapping i parameters;
4. `not assessed` drži odvojeno od score 0;
5. generiši jednu metric-specific matricu i drill-down report;
6. demonstriraj symmetric cache i resumable job;
7. pokreni invariance/metamorphic suite;
8. prikaži najmanje pet failure/ambiguous slučajeva.

## Deo C — Naučna evaluacija

Napravi mini gold-set od najmanje 30 parova:

- 5 self/equivalent encoding;
- 5 easy negatives;
- 10 hard negatives;
- 5 near positives;
- 5 edge/ambiguous cases.

Dva pregledača, gde je moguće, nezavisno popunjavaju višekomponentnu rubricu. Prijavi agreement, adjudication i confidence; nijedan score threshold se ne bira na final testu.

## Obavezni artefakti

```text
design/
  claims.md
  data-contract.md
  representation-profiles.md
  similarity-specifications.md
  licence-boundary.md
evaluation/
  gold-schema.md
  split-manifest.md
  metrics.md
  error-analysis.md
tests/
  invariance-cases.md
  regression-cases.md
reports/
  ingest-example.html
  search-example.html
  pair-example.html
```

Licencirani raw podaci, CSD exports, reconstructive feature dumps i tajni credentials ne ulaze u repo.

## Claim template

```text
Naziv:
Korisnička odluka:
Populacija / scope:
Input requirements:
Relevantnost / label:
Reprezentacija:
Algoritam i verzija:
Metric i acceptance prag:
Split i leakage kontrola:
Known failure modes:
Abstention pravilo:
Evidence prikazan korisniku:
Licence/provenance boundary:
```

## Similarity specification template

| Polje | Popuniti |
|---|---|
| objekat A/B | ligand, entity, form, determination… |
| component policy | kako se mapiraju/čuvaju solventi i counterions |
| graph policy | charge, H, stereo, tautomer, aromaticity, metal bonds |
| geometry policy | mapping, alignment, H, symmetry, coordinate origin |
| periodic policy | cell setting, ASU, neighbors, shell/tolerance |
| metric | formula i parametri |
| output | score + coverage + status + evidence |
| version | immutable profile ID |

## Demo scenariji

Demo mora obuhvatiti:

1. `cu_n14_a.cif` — filename `cu` ne postaje Cu filter;
2. MOL/MOL2 bond typing neslaganje;
3. DAP motif bez metala;
4. DAP motif + metal u entry-ju, ali bez dokazane koordinacije;
5. validiran metal–DAP coordination candidate;
6. record bez 3D;
7. multi-component solvate/salt;
8. `Du` ili `un`/failed molecular graph;
9. equivalent cell/atom ordering;
10. isti molecule graph sa različitim packing-om, ako je dozvoljen primer dostupan.

## Rubrika (100 poena)

| Oblast | Poeni | Kritični zahtev |
|---|---:|---|
| hemijska semantika i component model | 18 | nema tihog brisanja charge/metal/solvent značenja |
| kristalografija i periodičnost | 15 | symmetry/cell/packing nisu svedeni na molecule coordinates |
| loss-aware ingest i provenance | 15 | original + versioned transformations + warnings |
| similarity dizajn i objašnjenje | 15 | odvojeni nivoi, coverage i evidence |
| evaluacija i leakage kontrola | 15 | expert rubric, hard negatives, group split |
| failure handling i abstention | 8 | missing/ambiguous nije score 0 |
| licence i bezbednost | 7 | raw CSD ostaje u odobrenom data plane-u |
| reproducibilnost/testovi | 7 | invariance + regression + pinned profiles |

## Automatski pad bez obzira na zbir

- tvrditi da CIF filename određuje sastav;
- proglasiti svaki `4M` result koordinisanim DAP kompleksom;
- mešati SMILES/molekulski graf sa crystal packing-om;
- ukloniti problematične zapise bez prijave coverage-a;
- koristiti nasumični split uz očigledne family duplicates;
- commit-ovati licencirane raw CSD izvoze;
- prikazati predicted/assigned vrednost kao eksperimentalno izmerenu;
- izbaciti overall score kada ključni sloj nije validno procenjen.

## Odbrana

Za 30 minuta treba da:

1. objasniš pet nivoa strukture bez slajdova;
2. prođeš jedan ingest i pokažeš provenance;
3. odbraniš jedan dobar i jedan varljiv search hit;
4. rastaviš jedan pair result do atoma i symmetry image-a;
5. pokažeš jedan failed/abstained slučaj;
6. objasniš split, metric i najveću preostalu neizvesnost;
7. navedeš šta se menja kada dobijemo pun licencirani CSD pristup.

**Prolaz:** najmanje 80/100, nijedan automatski-pad uslov i uspešna usmena odbrana svih ključnih pretpostavki.
