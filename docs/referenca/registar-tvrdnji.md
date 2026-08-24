# Registar ključnih tvrdnji

Ovo je audit sloj knjige: najvažnije projektne tvrdnje povezane su sa tačnim lokalnim snapshot-om, načinom provere, confidence-om i granicom važenja. Datum poslednje provere ovog registra je **2026-08-23**. Metod, tri nezavisna pregleda, glasovi i remediation odluke nalaze se u [validacionom auditu](validacioni-audit-2026-08-23.md).

## Kako se čita

| Oznaka | Vrsta tvrdnje |
|---|---|
| O | direktno opaženo/pročitano iz izvora |
| D | izvedeno determinističkim proračunom ili poređenjem |
| A | dodeljeno hemijskim/softverskim modelom |
| I | interpretacija/inferencija koja zahteva jasno naveden scope |
| E | eksterni autoritativni ili primarni izvor |

`High` znači da je dokaz reproduktivan za navedeni snapshot. Ne znači da je tvrdnja univerzalna za sve CSD verzije, formate ili hemijska jedinjenja. Gde namera naučnog tima nije eksplicitno dokumentovana, ona ostaje `pending faculty confirmation` čak i ako je file-level forenzika sigurna.

## Snapshot lokalnih artefakata

Raw fajlovi nisu u ovom repou. Hash omogućava proveru da vežba koristi iste bajtove bez njihove redistribucije.

| Relativni izvor | SHA-256 |
|---|---|
| `CCDC_white_paper_sharpen.pdf` | `3A4D2597158505C0B4956BB967B7DFA294FF7E8804AB29450444C9157D23C612` |
| `dve funkcionalnosti.txt` | `990A5BDD4006D49A275C645204BACBA61C725527FA98F887033D83C6FB6345C3` |
| `cu_n14_a.cif` | `43C166DE6379E98AA120FA2C09425793F9E03BE7EF6FA0B677764D1660B5FC02` |
| `N14.mol` | `8BDF68228DEE990519CD6BE831F72C82EE0DAC4F1C156F6E1C325F1B525E1135` |
| `N14.mol2` | `A6E9870506DCB08B3F7C600DE0FF7D9816017AC4CA28196EC705C23FED99C59B` |
| `1 - Sifove baze DAP.cqs` | `1E64C48E266C8E6194C93386F0E3EFC27472180005140D5EEA60CCF870C00905` |
| `2 - Kompleksi sa DAP SB.cqs` | `065C31C2669BCA2FB087A58650E1A9B8C71EA6BB8F87050B8CAB6BD79416AAA5` |
| `search1.cif` | `28BEFFDC4E53DED5291DE936FB07E8C4F83474B36901F9C99061D5673AA2F159` |
| `search1.mol2` | `989E9A4C9173D07F48BF8AB633FB97CDDBDD48984ED66C904BC6F904C0DC54F6` |
| `search1.sd` | `0097E16CD9516A071C4C7741C4799A4E235CD3B830907AD2A8A6F83AE6E3D68C` |
| `search1.smi` | `0BE89D6C1FE0D59A88727CD550E1AFDFF205A67018A59E6D3E9112A3C5ABC720` |
| `search2.cif` | `B8EE968FA8E98F485B8389C0A89002D40951CC946CFD538DA79AEDF4BDD0E1AB` |
| `search2.mol2` | `F6B92A27CA4F8570FC29E439DED525A3E925E0328109EB5ABA49018D744D1977` |
| `search2.sd` | `DFF75F66F43827FC5D08E453DFB2C1FF86C7945C7B8B5CB1D0A5C67914D48781` |
| `search2.smi` | `49F89091D28DAEE5102CE771316EA1AB4204A01FF91F9CD5B350B15800745F4D` |

Repo-generated `docs/assets/open/tutorial-minimal.cif` nije jedan od 15 izvora. Njegov SHA-256 je `A6EEDB8582B90E8A2652DE76394169C506EEA4D06FC1819FB3EF757291D9E7C9`; to je sintetički CC0 teaching fixture čiji je sadržaj u celini pregledljiv.

## Kritične lokalne tvrdnje

| ID | Tvrdnja | Tip | Dokaz/provera | Confidence | Granica |
|---|---|---|---|---|---|
| L-01 | Dostavljeno je 15 izvornih fajlova | O | filesystem inventar + hash manifest | high | navedeni folder/snapshot |
| L-02 | `cu_n14_a.cif` ima formulu C25H20N3O2P i ne sadrži Cu atom site | O | formula i atom-site petlja | high | ovaj data block |
| L-03 | `Cu` u istom CIF-u označava Cu Kα zračenje, λ=1,54178 Å | O/I | radiation type/wavelength; formula cross-check | high | ne tumačiti svaki filename prefiks isto |
| L-04 | ćelija je monoklinska, P 21/c (#14), Z=4, T=100 K | O | CIF cell/symmetry/experiment tags | high | navedeno određivanje |
| L-05 | formula, Z=4, M=425,41 g mol⁻¹ i V=2073,51 Å³ daju ρ≈1,363 g cm⁻³ | D | gustina iz \(ZM/(N_\mathrm{A}V)\) uz konverziju jedinica | high | rounded input values |
| L-06 | N14 MOL i MOL2 imaju 51 atom i 54 bond records, ali različitu/siromašnu bond semantiku | O/D | counts i bond-type audit | high | ova dva exporta; bond record nije fizičko merenje |
| L-07 | dve N–O distance su obe oko 1,2273 Å | D | distance iz CIF koordinata | high | određivanje/uncertainty; resonance je hemijska interpretacija |
| L-08 | `search1` ima 2.110, `search2` 2.038 CIF/MOL2/SD records | O | nezavisni record counts i refcode liste | high | navedeni exports |
| L-09 | `search2` je ordered strict subset `search1`; razlika je 72 | D | set i sequence comparison refcode-ova | high | navedeni exports |
| L-10 | SMI ima samo 1.877/1.805 redova; istih 233 entries nema SMILES | O/D | identifier coverage diff | high | navedeni SMILES exporter/snapshot |
| L-11 | prvi CQS kodira povezani 18-atomski DAP-derived bis-iminski motiv | O/I | serializovani atom/bond constraints | high za graf; medium-high za naziv DAP | značenje skraćenice potvrditi sa fakultetom |
| L-12 | drugi CQS dodaje nepovezani `4M` atom; nema metal–DAP bond/contact constraint | O/E | query connectivity + CCDC definicija `4M` | high | dokazuje metal presence u entry-ju, ne koordinaciju |
| L-13 | CQS navodi ConQuest 2022.2.0 i CSD 5.43 sa March/June 2022 segmentima; temp-path timestamp je samo trag search/save događaja 2026-06-06 | O | CQS metadata/segment manifest + generisana temp putanja | high za verzije/cutoff; medium za semantiku timestamp-a | timestamp nije autoritativan datum pokretanja pretrage; nije savremeni full-CSD snapshot |
| L-14 | query quality filteri nisu bili uključeni | O | CQS filter flags | high | njihov downstream uticaj je task-dependent |
| L-15 | 2.023/1.954 CIF records imaju atom coordinates, pa 87/84 nemaju | O/D | atom-site presence po record-u | high | metadata/2D može i dalje biti upotrebljiv |
| L-16 | CQS sadrži pickle objekte i lokalne putanje | O | binary/printable/serialization audit | high | ne izvršavati untrusted pickle; ne redistribuirati bez pregleda |
| L-17 | CAPHAG je metal-free DAP-derived ligand; CAPHEK je ZnN3Cl2 positive coordination primer sa solventima | O/A | formula, graph/components i local geometry | high za navedeni export | full chemical review i dalje poželjan |
| L-18 | postoje `search2` kontraprimeri gde metal nije vezan za ciljni DAP N3 džep | D/A | component/metal–N graph i geometry review | high za jasan exported graph | ambiguous cases ostaju odvojeni |
| L-19 | PDF embedded-text ekstrakcija na stranama 1–2 sadrži nevidljivi, tematski nepodudarni docking tekst | O/D | text extraction naspram rendera svih 22 strana | high | parser/PDF snapshot; poreklo teksta ostaje inferencija |
| L-20 | među 1.954 neprazna `search2.sd` record-a atom count ima median/prosek/max 92/108,61/646, a connected components 2/2,93/36 | D | V2000 counts i connected components iz bond tabele; tri auditorske provere | high | ne mešati sa statistikama svih 2.038 record-a, gde 84 prazna menjaju prosek/medijanu |
| L-21 | sintetički CIF ima 1 block, 25 items i atom loop od 6 kolona × 2 reda; \(V=179.406144\ \text{Å}^3\) i \(\rho\approx2.164\ \text{g cm}^{-3}\) | O/D | SHA-256 + dva CIF parsera + ručni račun | high | teaching model, nije eksperiment ni CSD zapis |

## Ključne eksterne tvrdnje

| ID | Tvrdnja | Izvor | Status i datum | Granica |
|---|---|---|---|---|
| E-01 | `4M` obuhvata metalne grupe u ConQuest-u | zvanični CCDC ConQuest vodič | verified 2026-08-22 | verzija/alatom definisana semantika |
| E-02 | CIF data names imaju značenje definisano rečnicima | IUCr CIF standard/core dictionary | verified 2026-08-22 | koristiti odgovarajući dictionary/version |
| E-03 | FAIR ne znači nužno open; access može zahtevati autentikaciju/autorizaciju | originalni FAIR rad | verified 2026-08-22 | FAIR nije quality/licence sertifikat |
| E-04 | H-veza se ne definiše samo jednim distance cutoff-om | IUPAC Recommendation 2011 | verified 2026-08-22 | geometrija ostaje evidence, ne energija |
| E-05 | CCDC packing comparison vraća matched molecules i RMSD pod zadatim parametrima | CCDC API docs + COMPACK rad | verified 2026-08-22 | licenca/product availability; nije univerzalni metric |
| E-06 | CSD Portfolio i izvedeni podskupovi podležu CCDC uslovima/licenci | zvanični CCDC Conditions of Use | verified 2026-08-22 | konkretni institucijski ugovor je merodavan |
| E-07 | 2026 CCDC summary navodi 1.431.347 CSD entries | zvanični 2026 statistics PDF | verified 2026-08-22 | dinamička snapshot vrednost, ne konstanta |
| E-08 | razlikuje se sedam kristalnih i sedam rešetkastih sistema; 14 Bravaisovih tipova imaju standardne IUCr oznake | IUCr nomenklatura i Online Dictionary | verified 2026-08-23 | metrics same ne dokazuje crystal system; trigonal/rhombohedral razlika je bitna |
| E-09 | CCDC HBP tok koristi fitting data/evidence, logističku regresiju, individual propensity i zasebne grouping/coordination rezultate | CCDC API docs + Galek et al. 2007 | verified 2026-08-23 | output zavisi od baze, settings-a, coverage-a i licence; nije polymorph oracle |
| E-10 | powder-diffraction metadata razlikuje merenje od izračunatog obrasca i čuva radiation/instrument/profile podatke | IUCr pdCIF dictionary + CCDC simulation docs | verified 2026-08-23 | simulacija iz istog CIF-a nije nezavisna potvrda modela |

## Tvrdnje koje namerno nisu potvrđene

- da „DAP“ u naučnom timu nema nijedno drugo operativno značenje;
- da svih 2.038 `search2` pogodaka predstavlja koordinisane komplekse;
- da lokalni query subset predstavlja ceo CSD;
- da je jedna konkretna ML arhitektura već propisana white paper-om;
- da je `cu_n14_a.cif` jedina ili najstabilnija čvrsta forma jedinjenja;
- da je svaki missing SMILES greška iste vrste;
- da private GitHub sam po sebi daje dozvolu za CSD redistribuciju;
- da se svaki izvedeni feature/model sme objaviti.

## Princip verzionisanja dokaza

Promena source hash-a, CSD release-a, query-ja, parsera, standardization profila ili autoritativne definicije može promeniti važenje nalaza. Stari i novi rezultat zato se ne smeju nevidljivo spojiti: moraju ostati razdvojeni po verziji, uz vidljiv uticaj na pogođene tvrdnje i odgovarajući stručni review interpretativnih promena. Ovo je epistemološki princip registra, ne plan buduće implementacije ili release procedura.

Ovaj registar je inženjerska verifikacija, ne zamena za formalni review kristalografa, koordinacionog hemičara i vlasnika licence pre naučne publikacije ili produkcionog puštanja.
