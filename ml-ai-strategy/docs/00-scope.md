# Scope i teorijska pravila poređenja

Ako su termini feature, target, embedding, recall, kalibracija ili train/test novi, počni od [ML/AI od nule](00a-osnove-ml.md). Taj modul objašnjava matematičke oznake i sadrži rešene primere; ova strana zatim određuje granice projekta.

## Dva problema, više algoritamskih porodica

### Aplikacija 1: globalna pretraga

Ulaz je jedan CIF. Teorijski problem obuhvata bezbedno tumačenje i standardizaciju dozvoljenog sadržaja, eligibility i filtriranje, pronalaženje i rangiranje kandidata nad velikim licenciranim korpusom i objašnjiv dokaz uz rezultat.

Primarni cilj nije klasifikacija nego **rangiranje uz visok recall, razuman računarski trošak i stručno proverljiv evidence**.

### Aplikacija 2: precizno poređenje skupa

Za \(n\) uploadovanih CIF-ova postoji \(n(n-1)/2\) neuređenih parova. Konceptualne ose poređenja obuhvataju sastav, molekulski graf, koordinaciono okruženje, mapiranu 3D geometriju, packing i interakcione mreže kada ulazi to dozvoljavaju.

Primarni cilj je **tačno i rastavljivo pairwise poređenje**, ne samo jedan neobjašnjen similarity score. Ovo je opis problema, ne zamrznuta arhitektura sistema.

## Šta ovde znači fer poređenje

Nijedna algoritamska porodica nije unapred „pobednik“ zato što je novija ili složenija. Smisleno poređenje zahteva isti target, ciljnu populaciju, split, budžet, coverage račun i kriterijume greške. Relevantne dimenzije su:

1. naučna validnost reprezentacije i target-a;
2. recall/ranking ili pairwise tačnost po važnim slice-ovima;
3. kalibracija, abstention i robusnost van domena;
4. latencija, memorija, trošak i skaliranje;
5. objašnjivost i mogućnost stručnog audita;
6. količina i kvalitet dostupnih labela;
7. privatnost, licenca i mogućnost lokalnog izvršavanja;
8. složenost i reproduktivnost.

Zato se porodice metoda opisuju kroz tri neutralne uloge:

- **referentna metoda**: transparentna kontrola koja pokazuje šta donosi dodatna složenost;
- **alternativna porodica**: metod sa drugačijim pretpostavkama, reprezentacijom ili kapacitetom;
- **uslov primenljivosti**: podatak i dokaz koji određuju kada je poređenje smisleno, a kada rezultat treba ograničiti ili izostaviti.

## Granica između strategije i implementacije

Ova dokumentacija objašnjava koje algoritamske funkcije postoje, zašto su naučno relevantne, pod kojim pretpostavkama važe i kako se porodice metoda mogu fer porediti. Ona nije specifikacija konkretnog proizvoda i ne određuje šta treba implementirati niti kojim redosledom.

Šeme podataka, fixture-i, endpoint-i, payload-i, storage topologija, deployment manifesti, backlog i rollout nisu normativni izlazi ove knjige. Ako se pojave u objašnjenju, služe samo kao nenormativni primer teorijskog principa i ne stvaraju implementacionu obavezu.

## Granice

- Nemamo pristup punom CSD-u, pa se globalni coverage i performanse ne mogu proglasiti potvrđenim.
- Lokalni `search1/search2` eksporti nisu unbiased trening skup niti ground truth univerzalne srodnosti.
- LLM nije CIF parser, geometrijski kalkulator, kristalografski validator ni izvor ground truth-a.
- Slanje CSD ili fakultetskih podataka eksternom API-ju nije dozvoljeno bez eksplicitne ugovorne odluke.
- Iz literature se ne može izvesti univerzalni pobednik. Fer poređenje nad odobrenim, reprezentativnim podacima može podržati kontekstualni zaključak, ali ga ova dokumentacija unapred ne donosi.
