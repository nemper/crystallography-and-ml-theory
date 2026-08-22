# 15. Sličnost nije jedna veličina

**Prioritet: MORAŠ.** „Nađi slične strukture“ je nepotpun zahtev. Pre implementacije se mora reći: slične po čemu, za koju odluku, pod kojom standardizacijom i sa kakvim dokazom?

## 15.1 Pet odvojenih pitanja

| Nivo | Pitanje | Primer metode |
|---|---|---|
| sastav | da li sadrže iste elemente/formulu? | set/count distance, filter |
| 2D hemijski graf | da li dele scaffold/substructures? | fingerprint, subgraph, MCS |
| konformacija/geometrija | da li isti mapirani atomi imaju sličan 3D raspored? | aligned RMSD, torsion comparison |
| kristalno pakovanje | da li se molekuli periodično slažu slično? | packing overlay/COMPACK-like search |
| interakcije | da li grade slične H-bond/coordination/contact mreže? | interaction fingerprints/graph comparison |

Dve strukture mogu biti identične na prvom i drugom nivou, a različite polymorphs na četvrtom. Mogu imati različite supstituente, ali isti coordination motif. Jedan scalar ne može bez gubitka objasniti sve.

## 15.2 Exact, substructure i similarity nisu isto

- **exact graph match** traži isti definisani graf, uz policy za stereo/charge/isotopes;
- **substructure search** pita da li target sadrži query podgraf — odnos je asimetričan;
- **similarity search** rangira po numeričkoj meri — prag je projektna odluka;
- **MCS** traži najveću zajedničku podstrukturu pod zadatim pravilima i može biti skup/višeznačan.

CCDC dokumentacija razdvaja [search pristupe](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/search_philosophy.html), [substructure searching](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/substructure_searching.html) i [similarity searching](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/similarity_searching.html).

## 15.3 Tanimoto nad binarnim fingerprintima

Ako su \(A\) i \(B\) skupovi uključenih bitova:

\[
T(A,B)=\frac{|A\cap B|}{|A|+|B|-|A\cap B|}.
\]

Primer: A ima 10 bitova, B 8, a dele 6:

\[
T=\frac{6}{10+8-6}=0.50.
\]

Vrednost zavisi od fingerprinta, radius-a, bit length-a, stereochemistry i standardizacije. „Tanimoto 0.8“ bez tih podataka nije reproducibilna činjenica. Isti prag nema isto značenje za male i velike molekule, različite hemijske domene ili različite ciljeve.

## 15.4 RMSD i geometrijska sličnost

Za mapiranih \(N\) parova atoma, posle optimalnog poravnanja:

\[
\mathrm{RMSD}=\sqrt{\frac{1}{N}\sum_{i=1}^{N}\|\mathbf{x}_i-\mathbf{y}_i\|^2}.
\]

Ali rezultat zavisi od:

- atom mapping-a i izabranog common core-a;
- heavy atoms vs all atoms;
- symmetry-equivalent atoma;
- rigidnog ili fleksibilnog alignment-a;
- crystal coordinates vs generated conformer-a;
- disorder/occupancy izbora.

Zato izveštaj prikazuje i \(N\), mapping coverage, RMSD, maksimum odstupanja i policy, ne samo jednu decimalu.

## 15.5 Packing similarity

Packing comparison traži lokalni periodični klaster molekula oko referentnog molekula i pokušava da nađe dovoljno velik skup koji se geometrijski poklapa. CCDC-ov [Packing Similarity API](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/packing_similarity.html) vraća broj matched molecules i RMSD; zasnovan je na COMPACK pristupu opisanom u [Chisholm i Motherwell, 2005](https://onlinelibrary.wiley.com/doi/abs/10.1107/S0021889804027074).

Neophodni parametri uključuju veličinu shell-a/klastera, tolerancije, molecular matching i izbor komponente. Slična ćelija sama po sebi ne dokazuje isti packing; ista space group takođe ne dokazuje isti polymorph.

## 15.6 Interaction similarity

Za H-bond ili coordination mreže mogu se porediti:

- tipovi čvorova i ivica;
- donor/acceptor/metal identities;
- distance i angle distributions;
- periodic topology i dimensionality;
- motivi/rings/chains;
- pokrivenost i pouzdanost detekcije.

Kontakt koji ispunjava cutoff je kandidat, ne automatski „jaka veza“. Hydrogen positions, protonation, disorder i temperatura utiču na sigurnost.

## 15.7 Hibridni rezultat treba da ostane rastavljiv

Ako je poslovno potreban combined score, prvo prikaži komponente:

```text
2D graph            0.84
mapped 3D core      0.71  (28/34 heavy atoms; RMSD 0.62 Å)
coordination env.   exact donor set; geometry mismatch
packing             9/15 molecules; RMSD 0.91 Å
interaction network 0.58
quality compatibility medium
```

Tek zatim može postojati verzionisana formula, kalibrisana prema konkretnom zadatku. Težine ne treba birati „po osećaju“ niti trenirati bez jasno označenih ekspertskih parova.

## 15.8 Skaliranje za dostavljeni skup

Potpuno poređenje \(n\) struktura zahteva:

\[
\binom{n}{2}=\frac{n(n-1)}{2}
\]

parova. Za 2.110 zapisa to je **2.224.995** parova; za 2.038 metal-filterovanih zapisa **2.075.703**. Ako jedna duboka analiza traje samo 0,5 s, prvi posao bi serijski trajao skoro 13 dana.

Praktična arhitektura:

1. jeftini validacioni i metadata filteri;
2. approximate-nearest-neighbor retrieval nad verzionisanim embedding/fingerprint indeksom;
3. exact 2D reranking top-\(k\);
4. skupa 3D/packing/interaction analiza samo kandidata;
5. simetričan cache za par `(min_id, max_id, metric_version)`.

Za stvarno traženje svih parova iznad praga potrebna je empirijska provera recall-a prefiltera; top-\(k\) sam može propustiti relevantan par.

## 15.9 Kako se prag validira

Ne postoji univerzalni „slično“. Napravi ekspertno označen evaluation set sa:

- jasnim use case-om i nivoom sličnosti;
- pozitivnim, lakim negativnim i teškim negativnim parovima;
- grupisanjem da bliske family kopije ne procure u test;
- više nezavisnih eksperata i pravilom za neslaganje;
- confidence/ambiguous oznakama;
- metrikama retrieval-a: recall@k, precision@k, MAP/nDCG i latency;
- kalibracijom i error slicing-om po metalima, solvatima, disorder-u, veličini i kvalitetu.

## 15.10 Provera znanja

1. Da li Tanimoto 0.8 ima smisla bez fingerprint definicije?
2. Zašto substructure relation nije simetrična?
3. Da li ista space group znači isti packing?
4. Koje informacije moraju pratiti RMSD?
5. Koliko parova ima 100 struktura?

??? success "Odgovori"
    1. Ne; rezultat zavisi od reprezentacije, parametara i standardizacije.  
    2. Mali query može biti sadržan u velikom target-u, dok obrnuto ne važi.  
    3. Ne; mnogo različitih pakovanja deli istu space group.  
    4. Mapping/common core, broj/pokrivenost atoma, alignment, atom/H/stereo/symmetry policy i poreklo koordinata.  
    5. \(100\times99/2=4.950\).

**Kriterijum prolaza:** možeš da napišeš similarity specification koja navodi objekat, reprezentaciju, metriku, parametre, threshold/calibration, evidence i failure modes.
