# 19. Precizno poređenje parova

**Cilj druge aplikacije:** za učitani skup CIF-ova izračunati svako potrebno poređenje i vratiti rastavljiv, stručno proverljiv izveštaj — ne samo matricu neobjašnjenih brojeva.

## 19.1 Prvo definiši jedinicu poređenja

Jedan upload može sadržati:

- jedan hemijski molekul;
- coordination entity i counterions;
- solvate/hydrate/co-crystal;
- više independent molecules u asymmetric unit;
- disorder alternatives;
- polymeric coordination network.

Pre pair scoring-a, aplikacija pravi **comparison plan**: koje komponente se mapiraju, da li je objekat ligand, ceo entity ili crystal, i koji nivoi su validni za oba zapisa.

## 19.2 Kvadratna složenost

Za \(n\) različitih struktura broj neuređenih parova je:

\[
N_{pairs}=\frac{n(n-1)}{2}.
\]

| \(n\) | parova |
|---:|---:|
| 10 | 45 |
| 100 | 4.950 |
| 1.000 | 499.500 |
| 2.110 | 2.224.995 |

Zato je obavezno:

- precompute per-structure features samo jednom;
- kanonski pair key `(min(structure_version_id), max(...), metric_version)`;
- symmetric cache;
- task queue sa retry/idempotency;
- chunked output i progres po nivou;
- odvojiti „svi parovi exact“ od „candidate-pruned“ moda u UI-ju i izveštaju.

## 19.3 Pair pipeline

```mermaid
flowchart TD
    A[CIF A] --> QA[QC + representations A]
    B[CIF B] --> QB[QC + representations B]
    QA --> CP[Comparison plan]
    QB --> CP
    CP --> CM[Component mapping]
    CM --> G[2D graph mapping]
    G --> M[Metal environment]
    G --> D[3D conformation]
    CP --> C[Cell/packing]
    CP --> I[Interactions]
    M --> R[Evidence-rich pair report]
    D --> R
    C --> R
    I --> R
```

Svaka grana može dati `valid`, `ambiguous`, `not-applicable`, `missing-input` ili `failed`, uz razlog.

## 19.4 Component mapping

Pre atom mapping-a rešava se problem komponenti:

1. classify components bez brisanja originala;
2. generiši candidate pairings po sastavu/grafu/ulozi;
3. pronađi globalno konzistentno uparivanje komponenti;
4. prijavi unmatched solvente, counterions i coformers;
5. odvojeno izračunaj parent i full-composition poređenje.

„Uporedi samo najveći fragment“ je neprihvatljiv default za metalne komplekse i solid forms.

## 19.5 Molekulski graf i atom mapping

Izveštaj sadrži:

- exact/substructure/MCS status;
- broj i procenat mapiranih heavy atoms;
- mapirane atom pairs;
- unmatched atoms/bonds i funkcionalne grupe;
- charge, stereo i tautomer policy;
- multiple equivalent mappings i chosen-tie-breaker;
- confidence ako bond typing nije pouzdan.

Za DAP use case posebno se mapiraju centralni pyridine N, dva imine N i scaffold atoms, pa tek zatim terminalni supstituenti.

## 19.6 Koordinaciono okruženje

Za svaki relevantni metal:

- element i formal/oxidation-state evidence;
- koordinacioni broj pod eksplicitnim neighbor modelom;
- donor atom elements/types i ligand membership;
- denticity/bridging/hapticity flags;
- ideal geometry candidates i distortion measure;
- M–donor distances i ključni angles;
- da li mapirani DAP donors stvarno koordiniraju isti metal.

Ne koristi jedan globalni distance cutoff za sve elemente i oxidation states. Nejasan connectivity rezultat ostaje `ambiguous` i ide na human review.

## 19.7 Konformaciono/3D poređenje

Za svaki validni common core navesti:

- alignment policy;
- RMSD i maksimalno odstupanje;
- coverage \(N_{\mathrm{mapped}}/N_{\mathrm{eligible}}\);
- ključne torsion razlike;
- symmetry-equivalent atom handling;
- mirror/stereo status;
- experimental vs generated coordinate provenance.

Visok coverage sa umerenim RMSD često je informativniji od veoma niskog RMSD nad tri atoma.

## 19.8 Cell i packing nisu isto

Cell grana može porediti:

- crystal system/space-group type;
- standardized/reduced lattice parameters;
- volume per formula unit;
- density i temperature.

Packing grana mora nezavisno porediti periodični raspored mapiranih molekula/komponenti, uz shell size, tolerancije, matched molecules i RMSD. Slična reduced cell je candidate signal, ne packing proof.

## 19.9 Interakcije

Izgradi periodične contact networks, pa poredi:

- H-bond donor/acceptor pairs i geometriju;
- halogen/π i druge definisane kontakte;
- coordination links;
- chain/ring/network motifs;
- solvent-mediated veze;
- coverage i uncertainty zbog H/disorder-a.

Interakcioni rezultat uvek navodi definiciju i cutoff/angle parametre.

## 19.10 Predložena schema rezultata

```yaml
pair:
  a: structure-version-A
  b: structure-version-B
  comparison_profile: dap-crystal-v1
quality_compatibility:
  status: medium
  reasons: ["B has unresolved disorder"]
composition:
  exact: false
  unmatched_components: ["water in B"]
graph:
  status: valid
  similarity: 0.84
  mapped_heavy_atoms: 28
  coverage: 0.82
coordination:
  status: ambiguous
  reason: "two plausible metal-neighbor assignments in B"
geometry:
  rmsd_angstrom: 0.62
  policy: heavy-atom-rigid-v2
packing:
  status: missing-input
  reason: "A has no valid unit cell"
overall:
  score: null
  decision: human-review
```

`null` je tačniji od izmišljenog overall score-a kada ključna grana nije pouzdana.

## 19.11 Matrice i klasteri

UI može ponuditi:

- heatmap za pojedinačnu metric component;
- sort/filter po confidence-u i data-quality statusu;
- drill-down na evidence za jednu ćeliju;
- hierarchical clustering uz jasno navedenu distance/linkage definiciju;
- mrežu samo iznad validiranog threshold-a;
- eksport long-form tabele, ne samo screenshot matrice.

Ne mešati `not comparable` sa score 0: prvo znači da odgovor nije poznat/primenljiv, drugo da je validno poređenje pokazalo odsustvo sličnosti.

## 19.12 Metamorphic i adversarial testovi

Ista struktura treba da ostane ista nakon:

- permutacije redosleda atoma/komponenti;
- rigidne rotacije/translacije;
- wrap-a preko cell boundary-ja;
- symmetry-equivalent ASU/origin izbora;
- ekvivalentnog \(P\,2_1/c\leftrightarrow P\,2_1/n\) setting-a;
- invertibilne basis/conventional-cell promene;
- validnog različitog SMILES atom ordering-a.

Namerno različiti testovi:

- isti ligand, drugi metal;
- isti metal/donor set, druga geometry;
- isti molekul, drugi polymorph;
- ista formula, drugi constitutional isomer;
- metal samo u counterion-u;
- solvent-mediated vs direct H-bond;
- disorder alternative i missing H.

## 19.13 Provera znanja

1. Zašto `not comparable` nije score 0?
2. Šta mora prethoditi RMSD-u?
3. Zašto se component mapping radi pre atom mapping-a?
4. Da li reduced-cell hit dokazuje isti packing?
5. Koja promena CIF encoding-a ne sme promeniti rezultat?

??? success "Odgovori"
    1. Nema validnog merenja, dok 0 tvrdi validno izmerenu nepodudarnost.  
    2. Definisan common core/atom mapping, alignment i symmetry/H/stereo policy.  
    3. Inače se mogu mapirati solvent/counterion/nezavisni molekuli na pogrešne uloge.  
    4. Ne, samo generiše kandidata na lattice nivou.  
    5. Atom ordering, rigid transform, periodic wrap i ekvivalentni setting/origin/basis, u granicama definisanog zadatka.

**Kriterijum prolaza:** možeš za jedan par napraviti report u kome je svaka tvrdnja vezana za atomski/periodični evidence, algoritam, parametre i confidence.
