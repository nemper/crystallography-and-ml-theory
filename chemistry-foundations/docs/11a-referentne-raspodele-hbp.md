# 11A. Referentne raspodele, Mogul i hydrogen-bond propensity

Ova lekcija objašnjava kako se CSD koristi kao **empirijska referenca**, a ne kao oracle. White paper na stranama 17–18 pominje Mogul, packing comparison i hydrogen-bond propensity (HBP) u proceni polymorph risk-a. Da bi taj tok imao značenje, moraš umeti da razdvojiš tri pitanja:

1. da li je jedna geometrijska vrednost tipična među hemijski uporedivim fragmentima;
2. koliko je statistički model dobro podržan relevantnim fitting podacima;
3. šta iz rezultata **ne** sledi o energiji, stabilnosti ili postojanju polimorfa.

Svi brojevi u worked primerima na ovoj strani su **ručno napravljeni sintetički podaci za račun**. Nisu CSD statistika, Mogul output ni rezultat dostavljenih fajlova.

## Šta treba da umeš posle ovog poglavlja

Treba da možeš da:

- definišeš tačno koju dužinu, ugao ili torziju porediš i kako je mapiran fragment;
- dokumentuješ query, filtere, bazu/release, broj pogodaka i domain coverage;
- izračunaš jednostavan percentile ili robustan outlier signal bez proglašavanja energije;
- pravilno tretiraš kružne torzione uglove i multimodalne raspodele;
- objasniš kako HBP fitting skup, positive/negative ishodi i logistička regresija daju propensity;
- razlikuješ individual propensity, observed H-bond, grouping i coordination score;
- uvedeš abstention kada nema dovoljno relevantnog dokaza.

## Referentna raspodela nije „svi brojevi iz baze“

Ako kandidat ima C–N dužinu 1,390 Å, besmisleno je porediti je sa svim C–N vezama bez konteksta. Referentna populacija mora da odgovara pitanju. Reproduktivno tumačenje zahteva sledeće kategorije:

| Sloj | Primer pitanja koje mora biti zamrznuto |
|---|---|
| merena veličina | koji atom mapping i koja bond/angle/torsion definicija? |
| hemijsko okruženje | element, bond typing/aromaticity, formalni naboj, susedne grupe, ring status |
| koordinacioni kontekst | slobodan donor ili vezan za metal; koji metal/oxidation state/CN? |
| kristalografski filter | 3D coordinates, disorder, errors, polymeric status, R/temperature pravilo |
| baza | CSD release i skup dozvoljenih privatnih/javnih baza |
| deduplikacija | po entry-ju, fragmentu, compound/form familiji ili drugoj jedinici? |
| podrška | broj exact/generalized pogodaka, missingness i razlog proširenja query-ja |
| računarski kontekst | alat/verzija, parametri, transformacije i random seed ako postoji |

Bez ovoga „98. percentil“ nije reproduktivna tvrdnja. Promena protonacije, bond type-a ili filtera može promeniti populaciju više nego sama razlika koju meriš.

~~~mermaid
flowchart LR
    M["Mapiraj ciljnu geometriju"]
    Q["Definiši hemijski query<br/>i quality filtere"]
    R["Zamrzni bazu/release<br/>i deduplikaciju"]
    D["Izgradi raspodelu<br/>+ support/coverage"]
    S["Izračunaj signal<br/>percentile/local density"]
    I["Protumači uz strukturu,<br/>s.u. i applicability"]
    M --> Q --> R --> D --> S --> I
~~~

## Worked primer: neobična dužina kao signal

Pretpostavi da je hemijski uparen, sintetički referentni skup dao:

| Veličina | Vrednost |
|---|---:|
| broj pogodaka \(n\) | 250 |
| medijana | 1,340 Å |
| MAD, medijana apsolutnih odstupanja | 0,012 Å |
| kandidat | 1,390 Å |
| broj referentnih vrednosti \(\le\) kandidatu | 247 |

Jednostavan empirical percentile po ovde eksplicitno izabranoj konvenciji je:

\[
P_\mathrm{emp}=100\frac{\#\{x_i\le x\}}{n}
=100\frac{247}{250}=98.8.
\]

Robustni standardizovani signal može se napisati:

\[
z_\mathrm{robust}
=\frac{x-\mathrm{median}}{1.4826\,\mathrm{MAD}}
=\frac{1.390-1.340}{1.4826(0.012)}
\approx2.81.
\]

Faktor 1,4826 daje MAD-u skalu standardne devijacije za normalnu raspodelu; ne dokazuje da je konkretna hemijska raspodela normalna i ne pretvara ovaj signal automatski u p-vrednost. Račun zahteva \(\mathrm{MAD}>0\). Kada je MAD nula, na primer zbog jednakih ili jako zaokruženih vrednosti, ovaj skor nije definisan: treba prijaviti ograničenje i pregledati raspodelu ili koristiti drugi opravdan opis rasipanja. [Zvanična R dokumentacija za MAD](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/mad.html) objašnjava faktor skaliranja; neki alati vraćaju već skalirani MAD, pa ga ne treba pomnožiti dva puta.

Oba broja kažu: kandidat je na dugom repu **ove konkretne** raspodele. Ne kažu zašto. Najmanje četiri hipoteze ostaju otvorene:

1. atom/bond mapping, protonacija ili disorder model je pogrešan;
2. geometrija je stvarna i hemijski retka, na primer zbog koordinacije ili strain-a;
3. referentni query je preuzak, pristrasan ili iz drugog domena;
4. kandidat je slab eksperimentalni model i s.u./quality profil ne podržavaju oštar zaključak.

!!! danger "Outlier nije energija"
    Percentile, \(z\)-signal ili mala lokalna gustina nisu lattice energy, conformer energy ni verovatnoća polimorfa. Za energetsku tvrdnju potreban je posebno validiran energetski model; za faznu tvrdnju eksperimentalni i termodinamički evidence.

### Šta kada je podrška mala

Ne postoji univerzalan broj pogodaka koji svaku raspodelu čini „dobrom“. Potrebna podrška zavisi od heterogenosti i cilja. Sistem ipak mora razlikovati:

| Situacija | Pošten output |
|---|---|
| dovoljno hemijski bliskih pogodaka i stabilna raspodela | prijavi signal, support, filtere i uncertainty |
| nekoliko exact pogodaka, mnogo generalized pogodaka | prikaži oba nivoa odvojeno i sensitivity na generalizaciju |
| multimodalna raspodela | prijavi modove/local density; jedna sredina može biti besmislena |
| nula ili premalo relevantnih pogodaka | `insufficient_reference_support`, ne „ekstremni outlier“ |
| kandidat van domena query/model-a | abstention + razlog i predlog stručnog pregleda |

Generalizovanje query-ja sme da povećava coverage samo ako se istovremeno beleži šta je hemijski relaksirano. U suprotnom broj \(n\) raste, a relevantnost pada nevidljivo.

## Torzije su kružne, ne obične linearne promenljive

Uglovi \(-179^\circ\) i \(+179^\circ\) udaljeni su \(2^\circ\), ne \(358^\circ\). Minimalna kružna razlika je:

\[
d_\mathrm{circ}(\alpha,\beta)
=\min\left(|\alpha-\beta|,\ 360^\circ-|\alpha-\beta|\right).
\]

Za torzione raspodele zato ne koristi slepo linearnu sredinu i standardnu devijaciju preko granice \(-180/180^\circ\). Koristi circular statistics, periodičnu kernel density ili eksplicitne modove. Ako su konformacije grupisane oko \(60^\circ\) i \(180^\circ\), globalna sredina može pasti u oblast gde nema nijednog realnog konformera.

Gornji izraz pretpostavlja da su oba ugla već svedena na isti osnovni interval dužine 360°. Za proizvoljan broj punih obrtaja najpre izračunaj \(\delta=\operatorname{wrap}_{[-180,180)}(\alpha-\beta)\), pa koristi \(|\delta|\); inače zapis 540° može proizvesti pogrešan rezultat u naivnoj formuli.

## Kako hydrogen-bond propensity metod radi

CCDC implementacija je parametrizovana i version-dependent, ali metodski tok može da se nauči bez pristupa licenci:

1. **Identifikuj funkcionalne grupe.** Za ciljnu strukturu određuju se donorni i akceptorski atomi, uključujući intra- i intermolekulske mogućnosti.
2. **Napravi fitting skup.** Iz izabranih baza uzimaju se kandidatne strukture koje mogu da odgovaraju funkcionalnim grupama cilja. Matching i filteri određuju applicability domain.
3. **Anotiraj evidence.** Za svaki relevantan donor/acceptor tip broje se positive i negative ishodi u fitting strukturama. „Negative“ ovde znači da je prilika pod definisanim pravilom postojala, ali ishod nije opažen; to nije dokaz fizičke zabrane.
4. **Fituj logistički model.** Explanatory features mogu obuhvatiti identitet donor/acceptor grupe, competition, steric density i aromaticity. Model vraća verovatnoću tipa:

\[
\operatorname{logit}(p)
=\log\frac{p}{1-p}
=\beta_0+\sum_j\beta_jx_j,
\qquad
p=\frac{1}{1+e^{-\left(\beta_0+\sum_j\beta_jx_j\right)}}.
\]

5. **Proveri model i coverage.** Čuvaju se fitting counts, excluded grupe, regresiona jednačina/feature-i, AUC ili drugi dijagnostički output, uncertainty i savet alata. Dobar AUC ne popravlja target van domena.
6. **Izračunaj individualne propensity vrednosti.** Svaki potencijalni donor–acceptor par dobija model output, bounds/uncertainty i vezu sa dokazima. Posebno se beleži da li je veza stvarno opažena u target kristalu.
7. **Generiši groupings.** Kompatibilni skupovi mogućih H-veza predstavljaju putative network-e. Group H-bond score sažima propensity uključenih veza, dok coordination score sažima koliko su donorni/akceptorski coordination outcomes saglasni sa modelom. Ovde „coordination“ znači koliko H-veza donor donira ili akceptor prihvata u predloženoj mreži, na primer „donira jednom“. To nije koordinacioni broj metala iz poglavlja 5.

Zvanična [CCDC HBP dokumentacija](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/hbond_propensities.html) eksplicitno prikazuje fitting counts, positive/negative evidence, logistic regression, AUC, propensity uncertainty i group/coordination scores. Originalni metod je opisan u [Galek et al., Acta Cryst. B 2007](https://doi.org/10.1107/S0108768107030996).

## Worked HBP primer: četiri output-a, četiri značenja

Pretpostavi sintetički cilj sa jednim donorom `D1` i dva akceptora `A1`, `A2`. Posle dokumentovanog fitting-a alat daje:

| Kandidat | Propensity | 90% model interval | Opažen u target kristalu? |
|---|---:|---:|---|
| D1···A1 | 0,72 | 0,61–0,81 | da |
| D1···A2 | 0,61 | 0,46–0,74 | ne |

Ovo se ne čita kao „A1 veza postoji sa 72% fizičke sigurnosti“. Preciznije:

- `0,72` je output konkretnog modela za definisani par i fitting domen;
- `observed = da` je zasebna geometrijsko-kristalografska činjenica pod korišćenim H-bond kriterijumom;
- alternativni grouping sa D1···A2 može imati drugačiji H-bond i coordination score;
- neopaženi, ali visoko rangirani par je **hipoteza za pregled**, ne dokaz druge ostvarive packing strukture;
- razlika 0,72 naspram 0,61 možda nije odlučiva ako su intervali široki ili je fitting support slab.

| Izlaz | Odgovara na pitanje | Ne odgovara automatski |
|---|---|---|
| individual propensity | šta model očekuje za jedan mogući donor–acceptor par? | da li je veza opažena u target strukturi |
| observed H-bond | da li target geometrija zadovoljava definisani kriterijum? | da li je to energetski najpovoljnija interakcija |
| grouping/H-bond score | kakav je skup međusobno kompatibilnih putative veza? | da li taj network gradi realan kristal |
| coordination score | koliko su donor/acceptor coordination outcomes tipični po modelu? | ukupnu stabilnost, lattice energy ili polymorph probability |

## Moguće primene u dve aplikacije

### Globalna pretraga

- Referentni signal može imati smisla kao filter/rerank feature samo uz query, release, support i applicability.
- Retka geometrija ne sme biti automatski odbačena; može biti upravo naučno zanimljiv kandidat.
- Promena CSD snapshot-a, standardizacije ili filtera menja referentnu raspodelu i prekida direktnu uporedivost rezultata.
- Proprietary i public fitting slojevi moraju ostati odvojeni ako licenca ili provenance to zahtevaju.

### Poređenje svih parova

- Poređenje geometrije ima smisla uz raw vrednosti, s.u., atom mapping i položaj u istoj referentnoj raspodeli.
- Poredi support i applicability, ne samo dva percentile-a.
- Za torzije koristi circular distance/modove.
- HBP poređenje razdvaja potential pairs, observed network, grouping i coordination rezultate; jedna zbirna ocena ne sme sakriti različit uzrok.

Ovo su mogući načini upotrebe, ne unapred odobren feature set. Dostupni izvori ne potvrđuju da li je referentni signal deo targeta; za to je potreban zaseban fakultetski odgovor. Bez obzira na format budućeg evidence-a, moraju ostati vidljivi merena veličina, referentni query/release i podrška, outlier signal, applicability i zabranjena inferencija „nije energija niti polymorph probability“.

## Tipične zamke

1. Uključiti isti compound/redetermination mnogo puta i tretirati redove kao nezavisne uzorke.
2. Pomešati exact i generalized query hits bez oznake.
3. Koristiti globalni \(z\)-score za multimodalnu ili kružnu raspodelu.
4. Zanemariti s.u., disorder i pogrešan atom/bond typing kandidata.
5. Proglasiti „nema pogodaka“ za ekstremni outlier umesto za nedostatak reference.
6. Tumačiti propensity kao opaženu H-vezu ili verovatnoću postojanja polimorfa.
7. Uporediti output-e iz različitih CSD release-a/settings-a kao da su ista skala.
8. Objaviti fitting-derived artefakt bez licence i provenance pregleda.

## Provera znanja

1. Kandidat je na 99. percentilu referentne dužine. Navedi tri moguća objašnjenja koja nisu „visoka energija“.
2. Zašto su \(-179^\circ\) i \(+179^\circ\) bliski?
3. Da li HBP propensity 0,8 znači da je veza opažena?
4. Šta radiš kada target funkcionalna grupa ima premalo fitting evidence-a?
5. Zašto simulated „alternativni grouping“ nije predviđen polimorf?

??? success "Odgovori"
    1. Greška/mapiranje ili disorder; stvarna retka koordinacija/strain; pogrešan ili pristrasan referentni domen; može i slab eksperimentalni model.
    2. Ugao je kružna veličina: minimalna razlika preko granice je \(2^\circ\).
    3. Ne. To je output modela za kandidatni par; observed status se određuje zasebno.
    4. Prijavi insufficient support/abstention, ne forsiraj broj; po potrebi transparentno generalizuj query i uradi sensitivity proveru.
    5. Grouping je kombinatorna/statistička hipoteza o H-bond network-u. Ne dokazuje geometrijsku ostvarivost, povoljnu energiju, nukleaciju ni eksperimentalnu fazu.

**Kriterijum prolaza:** dobiješ jednu neobičnu dužinu ili HBP chart i možeš da rekonstruišeš population/fitting evidence, izračunaš ili proveriš signal, razlikuješ sva četiri HBP output-a i napišeš zaključak koji ne prelazi granicu dokaza.

## Primarni i autoritativni izvori

- [CCDC API: molecular geometry/Mogul analiza](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/molecular_geometry_analysis.html)
- [CCDC API: hydrogen-bond propensities](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/hbond_propensities.html)
- [Galek et al. 2007: Knowledge-based model of hydrogen-bonding propensity](https://doi.org/10.1107/S0108768107030996)
- [Taylor & Wood 2019: A Million Crystal Structures](https://doi.org/10.1021/acs.chemrev.9b00155)
- [CCDC API: packing similarity](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/packing_similarity.html)
