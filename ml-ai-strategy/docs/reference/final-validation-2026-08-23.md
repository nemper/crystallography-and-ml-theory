# Istorijski ML/AI QA snapshot — 23. avgust 2026.

Ova strana je datirani zapis provere tadašnje verzije ML/AI dokumentacije. Čuva proverljive QA rezultate, naučne korekcije i pokrivenost izvora; nije aktuelna specifikacija sistema, izbor realizacione arhitekture niti plan rada.

## Izvršni rezultat

- Auditovani sadržaj bio je zamrznut na commitu `4cbdd4a` u privatnom repozitorijumu `nemper/2cdc-chemistry-foundations`.
- Četiri nezavisna read-only toka pokrila su classical/retrieval, crystal/deep/data, SLM/RAG/API i lokalne izvore.
- U prvim prolazima pronađeno je pet materijalnih P2 rupa. Posle korekcija svaki ciljani domen dobio je završni **PASS**, bez preostalog P1/P2 nalaza u tom snapshot-u.
- Oba tadašnja MkDocs projekta prošla su strict build; ML sajt je prošao i provere internih targeta, fragmenata, strukturisanih primera i browser prikaza.
- U Git tree-u nije bilo dostavljenih fakultetskih/CSD raw fajlova; jedini kontrolisani primer bio je sintetički CC0 `chemistry-foundations/docs/assets/open/tutorial-minimal.cif`.
- Pošto nije postojao autorizovan reprezentativni CSD snapshot, audit nije mogao da potvrdi globalni kvalitet retrieval-a niti pobednika među naučenim modelima.

## Obuhvat istorijskog snapshot-a

| Sloj | Obuhvat |
|---|---|
| glavni hemijski kurs | svih 38 tadašnjih Markdown modula; detaljan raniji audit je u `chemistry-foundations/docs/referenca/validacioni-audit-2026-08-23.md` |
| ML/AI strategija | 13 sadržajnih modula na auditu + ova meta-audit strana |
| lokalni izvori | 15 artefakata: white paper, brief dve aplikacije, N14 CIF/MOL/MOL2, dva CQS-a i `search1/search2` eksporti |
| white paper | svih 22 fizičkih strana, tekstualno i vizuelno |
| algoritamski domeni | klasični ML; exact/ANN retrieval i ranking; pairwise naučne ose; periodic/deep/metric learning; lokalni SLM/RAG; spoljni LLM API i bezbednost |
| poprečne teme | cross-format reconciliation, identity i split, prava i lifecycle, vremensko curenje, denominatori, odvajanje statusa od naučne labele i evidence |

Audit nije koristio pristup CSD bazi. Lokalni brojevi proveravani su isključivo nad dostavljenim snapshot-om, a spoljna teorija prvenstveno prema standardima, zvaničnoj dokumentaciji i originalnim radovima.

## Nezavisni glasovi posle korekcija

Auditori nisu uređivali fajlove. Svaki je vraćao `PASS` ili `NEEDS_FIX` uz P1/P2 obrazloženje, a ciljana oblast je posle korekcije ponovo proverena.

| Auditor | Nezavisni obuhvat | Materijalni nalaz u prvom prolazu | Završni glas |
|---|---|---|---|
| A | pipeline, klasični ML, filteri, retrieval/ANN/ranking i podaci | precision sam ne otkriva false-negative niti prazan eligibility skup | **PASS** |
| B | pairwise, periodic/deep, metric learning i podaci | status izvršenja bio je pomešan sa naučnom labelom; `rhombohedral` nije bio pravilno razdvojen od crystal-system pojma | **PASS** |
| C | lokalni SLM/RAG, izveštavanje i spoljni API/security | stereo klase bile su pomešane sa statusom; naučno ocenjen rezultat nije uvek zahtevao dokaz | **PASS** |
| D | brief, svih 15 lokalnih artefakata, 22 PDF strane, oba dokumentaciona stabla i navigacija | bez P1/P2 rupe | **PASS** |

Ovi glasovi potvrđuju konzistentnost datirane dokumentacije posle navedenih korekcija. Ne predstavljaju validaciju realizovanog sistema ili naučnog rezultata.

## Materijalne korekcije koje su preživele glasanje

### 1. Precision filtera nije dokaz potpunosti

Prazan ili preuzak eligibility skup može imati precision 1. Ispravnost filtera zato zahteva nezavisan očekivani skup i proveru i false-positive i false-negative slučajeva, uključujući legitimni zero-hit, granice i missing/unknown stanja. Tek odvojeno od toga može se meriti gubitak približne pretrage unutar pravilno definisanog skupa.

### 2. Status izvršenja nije naučna klasa

Uspešno ocenjeno, dvosmisleno, neprimenljivo, nedostajući ulaz, blokada kvaliteta, timeout i tehnički neuspeh opisuju mogućnost procene. Naučna relation labela pripada odvojenom target-u. Neocenjen slučaj ne sme postati dodatna hemijska klasa niti lažna nulta sličnost.

### 3. Raw `rhombohedral` nije osmi crystal system

Lokalni `search2` ima tačno 12 raw `_symmetry_cell_setting = rhombohedral` zapisa. Raw izvozna oznaka, normalizovani trigonalni crystal system, prijavljeni rhombohedral lattice setting i izbor koordinatnih osa nisu ista činjenica. Poslednje ostaje nepoznato kada ga ćelija i space-group kontekst ne dokazuju.

### 4. Stereo profil, status i labela su tri različite stvari

Molekulska stereo relacija i kristalografska handedness relacija nisu isti target. Kada dokaz nedostaje ili je konfliktan, ishod je neocenjen ili dvosmislen, ne „mismatch“. Ahiralni slučaj i poređenje koje namerno zanemaruje stereo takođe se ne smeju pretvoriti u negativnu naučnu labelu.

### 5. Assessed scientific output mora imati dokaz

Svaki naučno ocenjen score ili labela mora biti vezan za proverljiv dokaz iz iste procene. Jezički sloj može da objasni postojeći dokaz, ali ne sme da dopuni rezultat slobodnom hemijskom tvrdnjom.

## Pokrivenost svega dostavljenog

| Dostavljeni materijal/tema | Šta je provereno | Dokumentaciona pokrivenost |
|---|---|---|
| `dve funkcionalnosti.txt` | App 1: jedan CIF prema bazi; App 2: svi neuređeni parovi `n(n-1)/2` | scope, pipeline mapa i uporedna mapa porodica |
| N14 CIF/MOL/MOL2 | isti lokalni primer kroz reprezentacije različite informacione potpunosti; bond-order konflikt; fractional/Cartesian razlika | glavni kurs 12/12A/17 i cross-format modul |
| `search1/search2` CIF/MOL2/SD/SMI | record/SMILES/coordinate coverage, `Du`, empty/matching, lineage i missingness | glavni kurs 17 i cross-format/eligibility teorija |
| dva CQS fajla | statički query graph i `4M` presence; runtime/UI semantika nije izmišljena | glavni kurs 16–17 i kontrolisana interpretacija query-ja |
| white paper 22/22 | lifecycle/curation, structure–property, manufacturability, polymorph-risk, Mogul/HBP/packing i FL | glavni kurs 22 i teorijska mapa relevantnih porodica |
| CIF izgled | pun sintetički data block, tag/value, loop, ćelija, simetrija, atom sites, `?`, `.`, s.u. i text field | `chemistry-foundations/docs/podaci/12a-anatomija-cif.md` i `tutorial-minimal.cif` |

Spot-check izvora ponovo je potvrdio 2.110 `search1` i 2.038 `search2` CIF/MOL2/SD zapisa, odnosno 1.877 i 1.805 SMILES redova. To su svojstva dostavljenog snapshot-a, ne globalne CSD statistike.

## Pokrivenost algoritamskih porodica

Audit je proverio da dokumentacija razlikuje sledeće porodice bez proglašavanja jedne od njih za realizacioni izbor:

- determinističko parsiranje, standardizaciju, eligibility i proverljive filtere;
- exact i približni retrieval, hemijske reprezentacije i rangiranje;
- grafovsko, geometrijsko, koordinaciono, packing, PXRD i interaction poređenje parova;
- klasične statističke/ML metode, periodične crystal encodere, metric learning i kalibraciju;
- kontrolisanu interpretaciju, sparse/dense retrieval i generativne jezičke metode kao odvojen UX/objašnjavački sloj;
- target-specifične property modele, polymorph-risk indikatore i federativno učenje kao uslovne istraživačke teme.

Fer poređenje ovih porodica zahteva isti target, populaciju, split, budžet, coverage i tretman failure/abstention slučajeva. Javni benchmark ili složenost modela sami po sebi nisu dokaz primenljivosti na 2CDC podatke.

## Reproduktivne tehničke kontrole

| Kontrola | Rezultat |
|---|---|
| `mkdocs build --strict -f chemistry-foundations/mkdocs.yml` iz korena repoa | PASS |
| `mkdocs build --strict -f ml-ai-strategy/mkdocs.yml` iz korena repoa | PASS |
| izgrađene HTML strane | 15 ukupno, uključujući 404 |
| interni targeti | 1.251 provera, 0 grešaka |
| fragmenti/anchor-i | 972 provere, 0 grešaka |
| fenced JSON | 10/10 sintaksno validnih |
| fenced YAML | 25/25 sintaksno validnih |
| status/label/evidence invarianti | 0 pronađenih nedozvoljenih kombinacija u tadašnjim primerima |
| desktop browser | 14/14 ruta; 1 H1 po strani; 0 broken images; 0 horizontal overflow |
| mobilni browser 390×844 | 14/14 ruta; 0 broken images; 0 horizontal overflow |
| Mermaid | 7/7 kontejnera renderovano u SVG |
| MathJax | 238 renderovana math kontejnera |
| browser console | 0 warning/error zapisa |
| `git diff --check` | PASS |
| kontrolisane raw ekstenzije u Git tree-u | samo `chemistry-foundations/docs/assets/open/tutorial-minimal.cif` |
| GitHub metadata | `nemper/2cdc-chemistry-foundations` je private; default branch `main` |

Jedini build ispis van regularnog loga bio je opšte upozorenje Material for MkDocs projekta o budućem MkDocs 2.0; tadašnji strict build nije prijavio dokumentacionu grešku.

!!! note "Naknadna urednička provera"
    Raniji konkretni primeri potom su sažeti na teorijske zahteve visokog nivoa, a Mermaid 11.17.0 i MathJax 3.2.2 smešteni su lokalno u repo. Ponovljeni strict build oba sajta, provera lokalnih linkova/fragmenata i lokalno HTTP učitavanje obe biblioteke i MathJax fontova prošli su bez greške. Brojčani redovi u tabeli iznad ostaju zapis prvobitnog audit snapshot-a, pre ovog uredničkog skraćivanja.

## Spoljni linkovi u istorijskoj proveri

Od 184 jedinstvena spoljna URL-a, 177 je prošlo direktnu automatizovanu proveru. Pet zvaničnih stranica ručno je potvrđeno u browseru jer su generičkom HTTP klijentu vraćale 403, a dva linka u privatnom repozitorijumu potvrđena su autentifikovanim pristupom. Ograničenje pristupa zato nije automatski tretirano kao netačan naučni link.

## Šta još nije i ne sme biti predstavljeno kao potvrđeno

1. **Globalni CSD kvalitet ili recall.** Nema pristupa autorizovanom reprezentativnom CSD snapshot-u, qrels-u ni entitlement matrici.
2. **Nadmoć jedne naučene porodice.** Bez autorizovanih reprezentativnih podataka nije pokazano da jedna ML/deep/ANN porodica nadmašuje druge pod istim uslovima poređenja.
3. **Puna CQS runtime/UI semantika.** Statička forenzika nije zamena za kompatibilni ConQuest runtime.
4. **Fakultetska operational definition DAP scope-a.** Query fajl ne rešava sam šta tim želi da uključi među tautomerne, protonovane, supstituisane i koordinaciono granične slučajeve.
5. **Institucijska CCDC licenca i product capabilities.** Dokazi nisu utvrdili lokalna prava ili dostupnost bulk eksporta, API-ja, Mogul/HBP/packing funkcija i redistribucije.
6. **Trajnost provider uslova.** Datirani model, retention, region, ZDR i ugovorni podaci nisu tretirani kao nepromenljive činjenice.
7. **Naučna/disertaciona validnost rezultata.** Source-based dokumentacioni audit nije zamena za domen eksperte, odobren protokol, odgovarajuće podatke i statistički zaključan test.

## Granica istorijskog zaključka

U tada dostupnom scope-u, posle pet korekcija, auditori nisu našli preostalu poznatu objektivnu P1/P2 grešku u pregledanoj dokumentaciji. Taj zaključak važi za datirani QA snapshot: ne potvrđuje realizovan sistem, ne validira budući model i ne uspostavlja obavezu ili redosled daljeg razvoja.
