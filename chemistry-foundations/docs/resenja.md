# Rešenja i rubrike

Ne čitaj ovo pre prvog pokušaja. Rešenja daju kontrolne vrednosti za opcione nastavne vežbe, ali ne zamenjuju sopstveni provenance i objašnjenje. Ona nisu acceptance testovi, fixture specifikacija ili implementacioni zahtevi budućeg projekta.

## L0 — očekivani inventar

U dostavljenom korenu postoji 15 izvornih fajlova:

- white paper PDF;
- opis dve funkcionalnosti TXT;
- jedan CIF, jedan MOL i jedan MOL2 za N14;
- dva `.cqs` upita;
- po četiri export formata za `search1` i `search2`: CIF, MOL2, SD i SMI.

Za multi-record eksport očekuj:

| Skup | CIF | MOL2 | SD | SMI lines |
|---|---:|---:|---:|---:|
| search1 | 2.110 | 2.110 | 2.110 | 1.877 |
| search2 | 2.038 | 2.038 | 2.038 | 1.805 |

SMI nije potpuna record lista. Razlika 233 u oba skupa je signal konverzije/representability, ne dozvola da se rows izbrišu.

## L0A — ceo sintetički CIF

- uz repozitorijumski propisane LF završetke redova, SHA-256 je `E6740DCB099445C3D4C30B94213CBCE915A844E81AFF39306F6FAFBB5BC9B6DE`;
- očekuje se jedan data block, 26 data items i atom-site loop sa šest kolona i dva reda, `Na1`/`Cl1`;
- `5.6400(10)` znači \(5.6400\pm0.0010\ \text{Å}\) na nivou standardne neizvesnosti zapisa;
- `?` znači unknown, a `.` not applicable/inapplicable u datom kontekstu;
- \(V=a^3=179.406144\ \text{Å}^3\), što se slaže sa zaokruženih 179,41 Å³;
- NaCl, \(Z=4\), formula mass 58,44 i ta zapremina daju približno \(2.164\ \text{g cm}^{-3}\).

Parser koji prihvati nepotpun loop red bez jasnog warning-a nije dovoljan za produkcioni ingest test.

## L1 — gustina i Cu zamka

Iz CIF-a:

- formula \(\mathrm{C_{25}H_{20}N_3O_2P}\);
- formula mass \(M=425.41\ \mathrm{g\,mol^{-1}}\);
- \(Z=4\);
- \(V=2073.51\ \text{Å}^3\);
- ista zapremina je \(2.07351\times10^{-21}\ \text{cm}^3\).

Najpre masa jedne jedinične ćelije:

\[
m_{\mathrm{cell}}=
\frac{4(425.41)}{6.02214076\times10^{23}}
=2.82564\times10^{-21}\ \mathrm{g}.
\]

\[
\rho=
\frac{2.82564\times10^{-21}}{2.07351\times10^{-21}}
\approx1.363\ \mathrm{g\ cm^{-3}}.
\]

Formula i atom sites nemaju Cu. Raw CIF vrednost `CuK\a` označava Cu Kα zračenje; talasna dužina je približno 1,54178 Å.

## L2 — N14 formati

- sva tri molekulska prikaza imaju 51 atom;
- MOL i MOL2 imaju 54 bond records;
- MOL je vrlo siromašan bond-order izvoz;
- MOL2 sadrži mnogo `un` bond types i `NO_CHARGES`;
- CIF čuva cell, symmetry, experiment/refinement i uncertainties koje molekulski formati ne čuvaju;
- dve N–O distance su obe približno 1.2273 Å, što je kompatibilno sa delokalizovanim nitro-like motivom i upozorava protiv doslovnog single/double čitanja eksportovanih veza.

## L3 — coordinate kontrola

Ćelija:

```text
a = 12.7138 Å
b = 15.3951 Å
c = 10.6106 Å
beta = 93.235 degrees
```

Za C1, korišćenjem odgovarajuće fractional-to-Cartesian matrice, očekuj približno:

```text
(6.9635, 8.3141, 1.6738) Å
```

Mala odstupanja poslednjih cifara dolaze od zaokruživanja i konvencije ispisa. Veliko odstupanje obično znači pogrešnu matricu, stepene/radijane ili atom mapping.

## L4 — symmetry kontrola

Lokalni CIF je monoklinski, \(P\,2_1/c\), International Tables broj 14, sa \(Z=4\). Za atom na opštoj poziciji očekuju se četiri symmetry-equivalent položaja u conventional cell-u. Precizne operacije čitaj iz CIF/dictionary-aware biblioteke i čuvaj zajedno sa translation image-om; nemoj ih pamtiti kao neprovereni string.

## L6 — query semantika

- oba query-ja dele isto povezano 18-atomsko DAP query jezgro sa dve `C=N` veze;
- drugi dodaje atom 19 tipa `4M`;
- `4M` znači svi metali;
- atom 19 je nepovezana query component;
- minimalni zaključak: isti CSD entry sadrži motiv i metal;
- metal–DAP koordinacija zahteva zasebnu proveru connectivity/geometrije i component membership-a.

## L7 — ključne forenzičke vrednosti

- `search2` je ordered i set subset `search1`;
- uklonjeno je tačno 72 records;
- svi 72 imaju SMI i ne zadovoljavaju `4M` uslov u query semantici;
- 3D/strukturna reprezentacija nije potpuna za sve records jer query nije zahtevao 3D;
- 87 `search1` i 84 `search2` zapisa imaju praznu/neupotrebljivu strukturnu reprezentaciju u relevantnom export pogledu;
- MOL2 audit nalazi `Du` atoms, `un` bonds, records bez `CRYSIN` i mnogo multi-component entries;
- `search2` ima 2.038 records, ali 1.899 base-refcode families; suffix/revision leakage je realan;
- 1.805 SMI redova daju manje unique exact strings, pa exact SMILES duplicate nije nužno nezavisna hemijska struktura.

Tačne counts po svakoj error kategoriji zavise od precizne parser definicije. U izveštaju uvek navedi definiciju, npr. šta znači „empty molecule“ i da li `Du` brojiš po atomu ili record-u.

## Ocena evidence-rich para

| Stavka | 0 | 1 | 2 |
|---|---|---|---|
| component relation | izostavljena | zaključak bez mapping-a | mapping + unmatched + role evidence |
| graph | score samo | policy ili coverage | mapping + policy + coverage + differences |
| coordination | metal present | distance-only | donor membership + CN/geometry + uncertainty |
| 3D | raw RMSD | RMSD + N | mapping/alignment/coverage/symmetry provenance |
| packing | space group only | cell comparison | periodic packing method + parameters + evidence |
| interactions | short contacts | typed contacts | geometry + periodic image + H/disorder confidence |
| quality | ignorisana | jedan R value | multi-field compatibility + missing/error status |
| conclusion | universal scalar | component scores | task claim + confidence + abstention where needed |

Maksimum je 16. Za prolaz treba najmanje 13 i nijedna nula u component, coordination, packing ili quality redu kada su ti nivoi deo claim-a.

## L11 — referenca i PXRD kontrola

- empirical percentile je \(100(247/250)=98.8\);
- robustni imenilac je \(1.4826\cdot0.012=0.0177912\), pa je
  \(z_\mathrm{robust}=(1.390-1.340)/0.0177912\approx2.81\);
- kružna udaljenost između \(-179^\circ\) i \(+179^\circ\) je \(2^\circ\);
- \(d(200)=5.6400/2=2.8200\ \text{Å}\);
- za \(\lambda=1.5406\ \text{Å}\), \(2\theta\approx31.7^\circ\);
- dozvoljen claim: „model predviđa pik oko 31,7° pod navedenim simulation settings-ima“;
- claim „bulk uzorak je ova faza“ zahteva nezavisno izmeren PXRD, metadata/protokol i kontekst mešavine/texture/background-a;
- individual HBP propensity, observed status, grouping i coordination score moraju ostati odvojeni, uz fitting counts i applicability.

## Najvažniji kriterijum

Tačan broj bez značenja nije dovoljno rešenje. Za svaku vrednost odgovori:

1. iz kog polja/atoma je došla;
2. kojim pravilom je izvedena;
3. koja je jedinica i uncertainty;
4. koja verzija alata/profile-a;
5. koji slučaj bi je učinio neupotrebljivom.
