# Validacioni audit — 23. avgust 2026.

Ova strana beleži šta je provereno, kako su neslaganja razrešena i šta još **nije moguće potvrditi**. Cilj nije da se kurs proglasi nepogrešivim, već da svaka važna tvrdnja ima jasan dokaz, scope i put ponovne provere.

!!! note "Istorijski audit, ne plan realizacije"
    Ovo je zapis stanja i dokumentacionog QA postupka od 23. avgusta 2026. Komande, tadašnji remediation koraci i opis potrebnog dokaza nisu backlog niti redosled implementacije 2CDC aplikacija. Aktuelna pitanja za fakultet nalaze se u [jedinstvenom registru pitanja](pitanja-za-fakultet.md).

## Izvršni rezultat

- Zamrznut je baseline commit `08dad2bacae5064a0d5fc1da5a23ac859c811dd5`.
- Tri auditora su nezavisno pregledala svih **34 baseline Markdown strana**, svih **15 lokalnih izvornih artefakata** i svih **22 fizičkih strana white paper PDF-a**.
- Pronađena je jedna lokalizovana objektivna greška: statistike molekulskih grafova bile su izračunate preko 2.038 record-a, ali predstavljene kao statistike 1.954 neprazna record-a. Sada je ispravljeno.
- Nije pronađena druga objektivno netačna hemijska, kristalografska ili ML tvrdnja u pregledanom scope-u.
- Šest nastavnih rupa dobilo je najmanje 2/3 glasova i zatvoreno je: ligandno polje/spin/Jahn–Teller, HBP metod, worked referentna raspodela, 7 sistema/14 Bravaisovih tipova, reciprocal/PXRD most i precizan `Curated` state contract.
- Pun bezbedan CIF i koherentna mapa svih 22 white-paper strana dobili su 3/3 glasa da su remediation-om rešeni.
- Puna CQS runtime/UI semantika i nameravana fakultetska definicija DAP scope-a ostaju 3/3 `UNCERTAIN`. Kurs ih ne predstavlja kao potvrđene činjenice.

## Metod bez međusobnog usaglašavanja

Prvi krug je radio ovako:

1. Svaki auditor je dobio isti baseline, svih 15 izvora i iste oznake `VALID`, `FALSE`, `MATERIAL_GAP` i `UNCERTAIN`.
2. Svaki je morao da evidentira svih 34 strana, 15 artefakata i 22 PDF strane, ne samo da prijavi izdvojene primedbe.
3. Auditori nisu čitali izveštaje drugih auditora i nisu menjali repo.
4. Lokalni brojevi su proveravani parserom/računom; spoljne tvrdnje prvenstveno IUCr, IUPAC, CCDC dokumentacijom, standardima i originalnim radovima.
5. Neizvesnost bez pristupa nije pretvarana u grešku niti u potvrdu.

U drugom krugu svi nalazi su pretvoreni u istih 15 anonimizovanih kandidatura. Svaki auditor je glasao bez uvida u tuđe glasove:

- `FALSE` — trenutna tvrdnja je objektivno netačna;
- `MATERIAL_GAP` — nedostatak menja razumevanje izvora ili projektovanje aplikacija;
- `NOT_MATERIAL` — korisno proširenje, ali ne neophodna rupa u sadašnjem scope-u;
- `RESOLVED` — ranija rupa je već zatvorena trenutnom izmenom;
- `UNCERTAIN` — dostupni dokazi nisu dovoljni za poštenu odluku.

Prag za proširenje bio je najmanje 2/3 glasa `MATERIAL_GAP`. Deterministički opovrgnuta brojčana tvrdnja ispravlja se nezavisno od terminologije glasa. Kandidatura sa samo 1/3 glasa nije dodavana osim ako postoji zaseban autoritativni ili reproduktivan dokaz da je neophodna.

## Anonimizovani glasovi i odluke

| ID | Normalizovana kandidatura | A | B | C | Konačna odluka |
|---|---|---|---|---|---|
| C01 | denominator `search2` statistike | `NOT_MATERIAL` | `RESOLVED` | `RESOLVED` | **ispravljeno i reprodukovano** |
| C02 | ligandno polje, spin i Jahn–Teller | `MATERIAL_GAP` | `MATERIAL_GAP` | `MATERIAL_GAP` | **dodato** |
| C03 | HBP fitting/logistic/propensity/grouping minimum | `MATERIAL_GAP` | `MATERIAL_GAP` | `MATERIAL_GAP` | **dodato** |
| C04 | worked Mogul-style referentna raspodela | `NOT_MATERIAL` | `MATERIAL_GAP` | `MATERIAL_GAP` | **dodato** |
| C05 | 7 kristalnih sistema i 14 Bravaisovih tipova | `NOT_MATERIAL` | `MATERIAL_GAP` | `MATERIAL_GAP` | **dodato kao referentna mapa, ne bubanje** |
| C06 | reciprocal space/Miller/\(d\)/odsustva/simulated-vs-measured PXRD | `MATERIAL_GAP` | `MATERIAL_GAP` | `NOT_MATERIAL` | **dodato** |
| C07 | cross-silo naspram cross-device FL | `NOT_MATERIAL` | `NOT_MATERIAL` | `MATERIAL_GAP` | **nije obavezno sada; aktivira se uz FL cilj** |
| C08 | formalni DP manifest | `NOT_MATERIAL` | `NOT_MATERIAL` | `NOT_MATERIAL` | **implementation gate tek uz DP claim** |
| C09 | held-out-site/LOSO i site-macro/sample-micro | `NOT_MATERIAL` | `NOT_MATERIAL` | `NOT_MATERIAL` | **uslovno uz unseen-site claim** |
| C10 | sintetički FL praktikum | `NOT_MATERIAL` | `NOT_MATERIAL` | `NOT_MATERIAL` | **odložen dok FL nije zahtev** |
| C11 | ceo bezbedan CIF primer | `RESOLVED` | `RESOLVED` | `RESOLVED` | **rešeno 12A + fixture-om** |
| C12 | svih 22 PDF strana, lifecycle i FedAvg | `RESOLVED` | `RESOLVED` | `RESOLVED` | **rešeno stranom 22** |
| C13 | puna CQS runtime/UI semantika bez ConQuest-a | `UNCERTAIN` | `UNCERTAIN` | `UNCERTAIN` | **ostaje otvoreno** |
| C14 | precizan nameravani DAP scope bez fakulteta | `UNCERTAIN` | `UNCERTAIN` | `UNCERTAIN` | **ostaje otvoreno** |
| C15 | `Curated` značenje i automatski gate | `MATERIAL_GAP` | `MATERIAL_GAP` | `MATERIAL_GAP` | **state contract dodat** |

Napomena za C01: auditor A je glasao prema već ispravljenom trenutnom tekstu i zato ga nije smatrao postojećom rupom. Sva tri su prihvatila isti denominator i brojčani rezultat; B i C su ga eksplicitno označili `RESOLVED`.

## Jedina objektivna korekcija

Tekst je rekao „u 1.954 coordinate-bearing record-a“, ali je za atome i connected components koristio statistiku svih 2.038 SDF record-a, uključujući 84 prazna:

| Scope | N | Atomi: medijana / prosek / max | Komponente: medijana / prosek / max |
|---|---:|---:|---:|
| svi record-i, uključujući 84 prazna | 2.038 | 89 / 104,13 / 646 | 2 / 2,81 / 36 |
| samo neprazni/coordinate-bearing | 1.954 | **92 / 108,61 / 646** | **2 / 2,93 / 36** |

Pošto je pasus namerno opisivao drugi scope, [strana 17](../projekat/17-lokalni-skup.md) sada koristi drugi red. Vrednost 1.425/1.954 = 72,9% multikomponentnih nepraznih zapisa bila je i ostala tačna. Proračun je nezavisno ponovljen nad `search2.sd` connectivity tabelama.

## Gde su rupe zatvorene

| Tema | Remediation |
|---|---|
| C02 ligandno polje/spin/Jahn–Teller | [5. Metali, ligandi i kompleksi](../koordinaciona/05-kompleksi.md#minimalni-ligand-field-most-zasto-elektroni-uticu-na-geometriju) |
| C03–C04 HBP i referentni outlier | [11A. Referentne raspodele, Mogul i HBP](../kristali/11a-referentne-raspodele-hbp.md) |
| C05 sistemi/Bravais | [8. Ćelija](../kristali/08-celija.md#sedam-sistema-i-14-bravaisovih-tipova-bez-taksonomske-zamke) |
| C06 reciprocal/PXRD | [10. Difrakcija i kvalitet](../kristali/10-difrakcija-kvalitet.md#reciprocal-space-operativni-most-hklrightarrow-drightarrow2theta) |
| C11 pun CIF | [12A. Anatomija CIF-a](../podaci/12a-anatomija-cif.md) + [sintetički fixture](../assets/open/tutorial-minimal.cif) |
| C12 svih 22 PDF strana | [22. White paper tokovi i FL](../projekat/22-whitepaper-tokovi-fl.md) |
| C15 lifecycle gate | [konceptualne razlike lifecycle stanja](../projekat/22-whitepaper-tokovi-fl.md#lifecycle-stanja) |
| redosled gradiva | [plan učenja zasnovan na ishodima](../pocetak/plan-ucenja.md) |
| praktična provera | [L0A i L11](../praktikum/laboratorije.md) + [kontrolna rešenja](../praktikum/resenja.md) |

## Checklist svih 34 baseline strana

`VALID` ovde znači da nije pronađena objektivna greška u scope-u strane. `VALID + REMEDIATED` znači da je postojeći sadržaj bio tačan, ali je konsenzus zahtevao dodatni nastavni most.

| # | Baseline strana | Audit odluka posle remediation-a |
|---:|---|---|
| 1 | `chemistry-foundations/docs/index.md` | `VALID`; ulaz u nove obavezne strane dodat |
| 2 | `koordinaciona/05-kompleksi.md` | `VALID + REMEDIATED` — ligand-field minimum |
| 3 | `koordinaciona/06-dap-schiff.md` | `VALID`; faculty scope ostaje eksplicitno pending |
| 4 | `kristali/07-interakcije.md` | `VALID` |
| 5 | `kristali/08-celija.md` | `VALID + REMEDIATED` — sistemi/Bravais |
| 6 | `kristali/09-simetrija.md` | `VALID` |
| 7 | `kristali/10-difrakcija-kvalitet.md` | `VALID + REMEDIATED` — reciprocal/PXRD |
| 8 | `kristali/11-cvrste-forme.md` | `VALID + REMEDIATED` novom 11A stranom |
| 9 | `osnove/01-atomi-joni-formule.md` | `VALID` |
| 10 | `osnove/02-veze.md` | `VALID` |
| 11 | `osnove/03-geometrija.md` | `VALID` |
| 12 | `osnove/04-organska.md` | `VALID` |
| 13 | `pocetak/dijagnostika.md` | `VALID` |
| 14 | `pocetak/kako-koristiti.md` | `VALID` |
| 15 | `pocetak/mapa-projekta.md` | `VALID` |
| 16 | `pocetak/plan-ucenja.md` | `VALID + UPDATED` — remediation uvrštena u plan |
| 17 | `podaci/12-formati.md` | `VALID + REMEDIATED` novom 12A stranom |
| 18 | `podaci/13-standardizacija.md` | `VALID` |
| 19 | `podaci/14-reprezentacije.md` | `VALID` |
| 20 | `podaci/15-slicnost.md` | `VALID` |
| 21 | `praktikum/laboratorije.md` | `VALID + UPDATED` — L0A/L11 |
| 22 | `praktikum/resenja.md` | `VALID + UPDATED` |
| 23 | `praktikum/zavrsni-projekat.md` | `VALID` |
| 24 | `projekat/16-csd-conquest.md` | `VALID` sa ispravno označenom CQS neizvesnošću |
| 25 | `projekat/17-lokalni-skup.md` | `FALSE → RESOLVED` — jedan denominator bug |
| 26 | `projekat/18-globalna-pretraga.md` | `VALID` |
| 27 | `projekat/19-parovi.md` | `VALID` |
| 28 | `projekat/20-evaluacija.md` | `VALID` |
| 29 | `projekat/21-licence-fair.md` | `VALID` |
| 30 | `referenca/izvori.md` | `VALID` |
| 31 | `referenca/podsetnik.md` | `VALID` |
| 32 | `referenca/recnik.md` | `VALID` |
| 33 | `referenca/registar-tvrdnji.md` | `VALID + UPDATED` |
| 34 | `referenca/zablude.md` | `VALID` |

Naknadne strane 11A, 12A i 22 auditovane su odvojeno; 12A i 22 dobile su 3/3 `RESOLVED` glasova za rupe koje zatvaraju. Ova audit strana nije deo baseline broja 34.

## Pokrivenost svih 15 lokalnih artefakata

Originali ostaju van repoa. Puni hash manifest nalazi se u [registru ključnih tvrdnji](registar-tvrdnji.md#snapshot-lokalnih-artefakata).

| # | Artefakt | Šta je provereno | Gde se uči |
|---:|---|---|---|
| 1 | `CCDC_white_paper_sharpen.pdf` | 22/22 vizuelne strane; hidden text/render konflikt na p.1–2; teme p.3–20; reference/kontakt p.21–22 | [potpuna mapa](../projekat/22-whitepaper-tokovi-fl.md#222-potpuna-mapa-22-strane-dokumenta) |
| 2 | `dve funkcionalnosti.txt` | globalni CIF→baza tok i all-pairs \(n(n-1)/2\) tok | mapa projekta, 18–20 |
| 3 | `cu_n14_a.cif` | formula, cell, `P 21/c`, coordinates, reflection/refinement, quality i embedded sadržaj | 8–13, 17, praktikum |
| 4 | `N14.mol` | 51 atoma/54 bond records i izgubljena crystal/refinement semantika | 12–13, L2 |
| 5 | `N14.mol2` | 51/54, `CRYSIN`, `NO_CHARGES` i unknown bond semantics | 12–13, L2 |
| 6 | `1 - Sifove baze DAP.cqs` | 18-atomski povezani motif, version metadata i ograničenja statičke forenzike | 6, 16–17, L6 |
| 7 | `2 - Kompleksi sa DAP SB.cqs` | isti motif + nepovezani `4M`; presence nije coordination | 5–6, 16–17, L6 |
| 8 | `search1.cif` | 2.110 blokova/refcode-ova, metadata/cell/coordinate coverage | 12, 16–17, L7 |
| 9 | `search1.mol2` | 2.110 record-a, atom/bond/charge typing i `Du` | 12–17, L7 |
| 10 | `search1.sd` | 2.110 V2000 record-a i prazni/matching statusi | 12–17, L7 |
| 11 | `search1.smi` | 1.877 redova i missing coverage | 12–17, L7 |
| 12 | `search2.cif` | 2.038 blokova, 1.954 sa koordinatama, cell/quality statistika | 12, 16–17, L7 |
| 13 | `search2.mol2` | 2.038 record-a, `Du`, bond/charge/metal centri | 5–6, 12–17, L7 |
| 14 | `search2.sd` | 2.038 record-a, 1.954 neprazna; atom/component statistika i denominator korekcija | 17, L7 |
| 15 | `search2.smi` | 1.805 redova, 233 missing i multi-component/charge obrasci | 12–17, L7 |

Deterministički je potvrđeno i da je `search2` strogi, redosledno očuvan podskup `search1` sa 72 uklonjena refcode-a; to je svojstvo ovog snapshot-a, ne univerzalna činjenica o CSD-u.

## Kako sada izgleda ceo CIF bez licencnog rizika

Repo ne sadrži fakultetski `cu_n14_a.cif` niti CSD exporte. Umesto toga sadrži sintetički [`tutorial-minimal.cif`](../assets/open/tutorial-minimal.cif), prikazan u celini i red-po-red objašnjen na [strani 12A](../podaci/12a-anatomija-cif.md).

Fixture:

- ima SHA-256 `A6EEDB8582B90E8A2652DE76394169C506EEA4D06FC1819FB3EF757291D9E7C9`;
- parsira se kao jedan data block sa 25 data items i atom loop-om od šest kolona/dva reda;
- demonstrira komentar, quoted value, semicolon text field, s.u., `?`, `.`, cell/symmetry i atom sites;
- ručno je označen kao sintetički, neeksperimentalni CC0 teaching primer;
- ne sadrži CSD, fakultetske ni korisničke podatke.

To ispunjava nastavni cilj „moram da znam kako CIF izgleda“ bez pretpostavke da privatni GitHub rešava CCDC licencu.

## Otvorene neizvesnosti i dokaz koji bi ih razrešio

### CQS runtime/UI

Statička binarna forenzika podržava opis query grafa, version stringova i nepovezanog `4M` atoma. Ne može dokazati sve version-dependent ConQuest GUI default-e, session stanje ni ponoviti rezultat bez kompatibilnog licenciranog runtime-a.

**Potreban dokaz:** vizuelna/runtime potvrda oba CQS-a u odgovarajućoj ConQuest verziji, sa constraints/filterima, verzijama i ponovljenim refcode rezultatom/hash-om.

### Nameravana DAP definicija

Fajl pouzdano određuje izvršivi 18-atomski podgraf. Ne određuje sam šta naučni tim želi da uključi među supstituisane, parcijalne, protonovane/tautomerne ili koordinaciono pozitivne/granične slučajeve.

**Potreban dokaz:** fakultetski odobrena operational definition, atom mapping i annotation guide sa positive/negative/ambiguous primerima.

### Licenca i lokalne CCDC mogućnosti

Bez institucijskog ugovora i runtime-a nije potvrđeno pravo bulk eksportovanja/redistribucije, raspoloživ product tier ni lokalna dostupnost Mogul, HBP, packing/API/on-site tokova.

**Potreban dokaz:** potvrđena permission/capability odluka data owner/controller-a i licence owner-a, uz lokalni dokaz dostupnosti relevantne funkcije nad odobrenim podacima.

## Istorijske završne kontrole dokumentacije

U auditu od 23. avgusta korišćene su sledeće dokumentacione kontrole:

1. `mkdocs build --strict -f chemistry-foundations/mkdocs.yml` iz korena repozitorijuma;
2. provera internih linkova/assets i da nema horizontalnog overflow-a;
3. browser pregled navigacije, MathJax i svih Mermaid dijagrama;
4. parsiranje sintetičkog CIF-a i provera hash-a/loop cardinality-ja;
5. zabranjeni-asset audit: nijedan lokalni PDF/CQS/MOL/MOL2/SDF/SMI/raw CIF u Git tree-u, osim eksplicitno dozvoljenog sintetičkog fixture-a;
6. `git diff --check` i review svih promena;
7. provera da je GitHub repo i dalje private.

### Rezultat pokretanja 2026-08-23

Sve kontrole su prošle:

- `mkdocs build --strict -f chemistry-foundations/mkdocs.yml`: PASS; jedini ispis van regularnog build loga je opšte upstream upozorenje Material for MkDocs-a o budućem MkDocs 2.0;
- relativni interni linkovi i fragmenti: 3.607 provera, 0 grešaka;
- browser crawl: 38/38 strana na desktop viewport-u i 38/38 na 390×844; bez horizontalnog overflow-a i polomljenih slika;
- Mermaid/MathJax: svih 17 Mermaid kontejnera postalo je SVG, a matematički sadržaj je iscrtan na svim posećenim stranama;
- sintetički CIF: isti SHA-256 kao u registru; nezavisno ga parsiraju PyCifRW 5.0.1 i Gemmi 0.7.5; oba nalaze jedan blok i dve `atom_site` vrste;
- sadržaj Git radnog stabla sa kontrolisanim ekstenzijama: samo `chemistry-foundations/docs/assets/open/tutorial-minimal.cif`; nema lokalnih izvornih PDF/CQS/MOL/MOL2/SD/SDF/SMI/raw CIF fajlova;
- `git diff --check`: PASS;
- remote metadata: repozitorijum `nemper/2cdc-chemistry-foundations` je private.

Ovaj protokol ostaje obavezan i kada se nastavna teorija nije menjala.

## Granica validacije

Ovaj audit daje reproduktivan inženjerski i source-based pregled dostupnog snapshot-a. Ne zamenjuje formalno odobrenje kristalografa, koordinacionog hemičara, statističara privatnosti i vlasnika licence pre produkcije, naučne publikacije ili disertacione tvrdnje. Važna razlika je da su nepoznate stavke sada **vidljive i testabilne**, umesto da budu prećutne pretpostavke.
