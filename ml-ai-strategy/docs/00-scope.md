# Scope i pravila odlučivanja

## Dva proizvoda, više algoritamskih poslova

### Aplikacija 1: globalna pretraga

Ulaz je jedan CIF. Sistem bezbedno parsira i standardizuje dozvoljeni sadržaj, primenjuje hard filtere, generiše visok-recall kandidate nad velikim licenciranim korpusom, preciznije ih rerangira i vraća objašnjene rezultate.

Primarni cilj nije klasifikacija nego **rangiranje uz visok recall, kontrolisanu latenciju i stručno proverljiv evidence**.

### Aplikacija 2: precizno poređenje skupa

Za (n) uploadovanih CIF-ova postoji (n(n-1)/2) neuređenih parova. Za svaki par sistem odvojeno poredi sastav, molekulski graf, koordinaciono okruženje, mapiranu 3D geometriju, packing i interakcione mreže kada ulazi to dozvoljavaju.

Primarni cilj je **tačno i rastavljivo pairwise poređenje**, ne samo jedan neobjašnjen similarity score.

## Šta ovde znači „optimalan“

Algoritam nije optimalan zato što je noviji ili složeniji. Optimalan je kandidat koji na unapred zamrznutom protokolu najbolje zadovoljava relevantnu kombinaciju:

1. naučna validnost reprezentacije i target-a;
2. recall/ranking ili pairwise tačnost po važnim slice-ovima;
3. kalibracija, abstention i robusnost van domena;
4. latencija, memorija, trošak i skaliranje;
5. objašnjivost i mogućnost stručnog audita;
6. količina i kvalitet dostupnih labela;
7. privatnost, licenca i mogućnost lokalnog izvršavanja;
8. složenost održavanja i reproduktivnost.

Zato će svaka preporuka imati najmanje tri uloge:

- **baseline**: jednostavan metod koji kompleksniji kandidat mora pošteno da pobedi;
- **production candidate**: trenutno najbolji odnos kvaliteta, troška i rizika;
- **challenger**: složeniji metod koji ulazi tek ako unapred definisan eksperiment pokaže materijalnu korist.

## Granice

- Nemamo pristup punom CSD-u, pa se globalni coverage i performanse ne mogu proglasiti potvrđenim.
- Lokalni `search1/search2` eksporti nisu unbiased trening skup niti ground truth univerzalne srodnosti.
- LLM nije CIF parser, geometrijski kalkulator, kristalografski validator ni izvor ground truth-a.
- Slanje CSD ili fakultetskih podataka eksternom API-ju nije dozvoljeno bez eksplicitne ugovorne odluke.
- Konačni izbor algoritma je eksperimentalna odluka nad odobrenim podacima; literatura sužava prostor kandidata, ali ne zamenjuje lokalni benchmark.
