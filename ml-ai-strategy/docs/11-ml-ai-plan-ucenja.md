# Plan učenja ML/AI dela za 2CDC

Ovo je putanja kroz kurs hemije i ML/AI teoriju, dostupna i čitaocu bez predznanja iz obe oblasti. Početnik prvo prolazi [ML/AI od nule](00a-osnove-ml.md); iskusan ML inženjer može taj modul koristiti kao dijagnostiku i preći dalje tek kada ume da reši njegove primere. Plan određuje **redosled, preduslove, projektantske vežbe i dokaze razumevanja**; nije pretpostavka da čitalac već zna da trenira i validira model.

Osnovna putanja organizovana je kao niz tematskih celina povezanih preduslovima i kapijama razumevanja. Nema kalendarski raspored niti procenu trajanja: napredovanje zavisi isključivo od savladanih preduslova i prolaska odgovarajućih kapija. Putanja ne uključuje implementiranje dve aplikacije, treniranje modela niti kompletno čitanje svake spoljne reference.

Ovaj plan usklađuje [sažeti plan učenja hemije](https://github.com/nemper/crystallography-and-ml-theory/blob/main/chemistry-foundations/docs/plan-ucenja.md). Hemijski plan daje redosled domenskog gradiva; ova strana govori kada je to gradivo dovoljno savladano za određenu ML/AI odluku.

!!! info "Granica ovog plana"
    Tokom učenja pišeš kratke obrazložene skice, uporedne tabele i očekivane ishode na ilustrativnim primerima. Plan ostaje na pojmovima, pretpostavkama i dokazima; ne projektuje konkretan sistem niti izvodi praktične sistemske probe.

## Pravila rada

1. **Napredovanje je zasnovano na dokazu, ne na datumu.** Ako kapija ne prolazi, ponovi ciljanu vežbu; nemoj samo nastaviti čitanje.
2. **Svaki score prvo dobija semantiku.** Pre poređenja metoda napiši objekat, target, primenljivost, reprezentaciju, metriku i značenje neuspeha.
3. **Determinističko jezgro prethodi ML-u.** Parser, standardizacija, hard filteri, atom/component mapping i periodična geometrija nisu poslovi za generativni model.
4. **`UNKNOWN` nije nula.** Dvosmisleno, odsutno, neprimenljivo, blokirano kvalitetom, isteklo i neuspešno nisu ista stanja i nijedno automatski ne postaje negativna labela ili similarity `0`.
5. **Restricted podaci ostaju u odobrenom data-plane-u.** Raw CSD i fakultetski sadržaj ne kopira se radi vežbe; primer mora biti otvoren, sintetički ili eksplicitno dozvoljen za tu svrhu.
6. **Ne preskači osnovne ML međukorake.** Najpre razjasni uzorak, reprezentaciju, target, loss, učenje, split i metrike u uvodnom modulu. Linearne modele, tree ensemble-e, GNN, metric learning i kalibraciju zatim poveži sa 2CDC targetima. Ranije znanje može skratiti ponavljanje, ali ne zamenjuje proveru razumevanja.

## Prioriteti i tačan redosled čitanja

Ovo je **merodavna početnička putanja kroz oba dela**. Navigacija i kratki hemijski plan prikazuju isti redosled preduslova. Oznake: **O — obavezno jezgro**, **U — uslovna grana**, **R — referentni detalji**. Uslovna grana postaje obavezna kada izabereš njen metod ili tvrdnju; njena ograničenja važe i kada je čitaš samo radi orijentacije.

| Red | Čitanje | Prioritet | Preduslov i izlaz |
|---:|---|---|---|
| 0 | [ML/AI od nule](00a-osnove-ml.md), §1–7 i samoprovera osnovnih pojmova | O | bez ML predznanja; račun, target, učenje, split i osnovne metrike; neuralne §8–9 ostavi za kasnije |
| 1 | početne strane, hemijska mapa projekta i dijagnostika; [scope](00-scope.md), [pipeline mapa](01-pipeline-decision-map.md) i uvod [uporedne mape](10-optimal-stack-roadmap.md) | O, samo orijentacija | imenuj dva problema i nivoe tvrdnji; katalozi algoritama se još ne polažu |
| 2 | hemija 1–6 | O | veze, geometrija i donorstvo pre koordinacije; Kapija A nakon4 |
| 3 | hemija7 prvi prolaz →8 →9 →10 →7 drugi prolaz | O | intuicija kontakta pre ćelije; pun periodični račun i njegova kapija tek nakon simetrije, occupancy i disorder-a |
| 4 | hemija11; 11A osnovno značenje referentnih signala | O; tehnički11A je U/R | polimorf, stabilnost, kinetika i granice propensity/outlier tvrdnji; Kapije B i C iza11 |
| 5 | hemija12,12A,13–17; [povezani primer](https://github.com/nemper/crystallography-and-ml-theory/blob/main/chemistry-foundations/docs/povezani-primer.md) do mapa i geometrije | O; inventari17 su R | formati, namenski pogled, periodični graf, sličnost i pouke lokalnog preseka |
| 6 | hemija21 i [cross-format/lifecycle](09-cross-format-eligibility.md) | O; detalji R | granice prava, identiteta i primenljivosti pre evaluacije |
| 7 | hemija19 i osnovni mapping/3D deo [pairwise lekcije](04-precise-pairwise.md) | O | komponentna i atomska mapa pre RMSD-a; napredni SOAP i enumeraciju odloži |
| 8 | hemija18 i mehanika exact/ANN u [retrieval lekciji](03-global-retrieval-ann-ranking.md) | O | prvi prolaz do kandidata; učenje rangiranja još preskoči |
| 9 | hemija20: stručne ocene, split, metrike, kalibracioni tok i grupno poređenje | O | osnovna evaluacija bez neuralnih modela; imenioce proveri na Q/B/C/D |
| 10 | [Klasični ML](02-classical-ml.md): linearne reference, stabla/boosting, kernel i kalibracija | O | učenje i evaluacija prethode izboru modela; boosting prethodi LambdaMART-u; kernel prethodi SOAP-u |
| 11 | povratak na [pairwise](04-precise-pairwise.md) pakovanje/evidence i [retrieval](03-global-retrieval-ann-ranking.md) učenje rangiranja | O za osnovno poređenje; pojedinačne porodice U | SOAP/REMatch prvo kroz numerički primer u02; MCS enumeracija, PQ/LSH detalji prema izabranoj grani |
| 12 | PCA/PCR/PLS, GPR, SOAP/REMatch ili split-conformal iz02 | U | produbi samo izabranu porodicu; svaki blok ima sopstveni račun i granice |
| 13 | povratak na00a neuralne osnove → [periodični encoderi](05-periodic-crystal-encoders.md) → [metric learning](06-metric-learning-and-evaluation.md) | U | periodični graf, grupe, evaluacija, log/softmax i negativi pre trening gubitaka |
| 14 | hemija22 i cela uporedna mapa, drugi prolaz | O za granice tvrdnji; property/FL razrada U | pregled dopuštenih naučnih tvrdnji posle osnovnih metoda; FL samo uz dodatne preduslove |
| 15 | [SLM/RAG](07-local-slm-rag.md), [spoljni API](08-api-llm-security.md) | U | zasebno jezičko pitanje; njegov izbor ne menja naučni autoritet geometrije |
| 16 | [Metod dokaza](evidence-method.md), rečnik, zablude, izvori i referentni okviri | R | otvaraj uz konkretnu proveru; rešenja vežbi posle sopstvenog pokušaja |

Obavezno jezgro čuva razgraničenja sastava, grafa, konformacije, pakovanja, svojstva i kvaliteta dokaza. Ne zahteva računanje svake algoritamske porodice ni čitanje svakog primarnog rada u celosti. Detalj postaje preduslov tek za odgovarajuću uslovnu granu.

## Hemijski preduslovi po ML/AI temi

| ML/AI odluka | Hemija koju moraš završiti | Šta treba da razumeš pre kasnije realizacije |
|---|---|---|
| CIF ingest i izdvajanje polja | 1–2, 8–10, 12 i 12A | Razliku između ?, ., 0, standardne neizvesnosti, ASU, ćelije i simetrijskih operacija; filename nije hemijski sastav. |
| Molekulski graf, ECFP i Tanimoto | 1–6, 12–15 | Kako bond order, aromatičnost, naboj, tautomerija, stereohemija i politika komponenti menjaju fingerprint i rang. |
| Exact graph, subgraph, VF2 i MCS | 2, 4–6, 11–15 | Node/edge ograničenja, smer containment-a, coverage obe strane, timeout i ambiguity politiku. |
| Dodela komponenti | 4–6, 11–13 | Razliku između liganda, coordination entity-ja, counterion-a, solventa i coformer-a; pravilo „najveći fragment“ nije dovoljno. |
| Kabsch, mapirani 3D i stereo | 3–4, 8–9, 12–15 | Atom mapping prethodi RMSD-u, refleksija zavisi od stereo profila, a coverage mora stajati uz RMSD. |
| Koordinacioni deskriptori i graf | 5–10, 12–15 | Prisustvo metala nije isto što i direktno donor mapiranje; CN, donor set, geometrija/CSM i neodređenost su različiti izlazi. |
| Periodični graf i crystal encoder | 7–10, 12A–14 | Koje fizički ekvivalentne promene zapisa ne smeju promeniti rezultat i zašto se čuva provenance periodične slike. |
| Packing, polimorfi i interakcije | 7–11A, 13–15 | Isti molekulski graf nije nužno ista čvrsta forma; packing, PXRD, HBP i Mogul su odvojeni signali sa ograničenjima. |
| Retrieval, reranking i qrels | 5–6, 11–18, 20 | Razliku između hard filtera, candidate recall-a, semantic recall-a i finalnog ranga; postojeće search grupe nisu automatski gold. |
| Kalibracija, abstention i analiza grešaka | 10–15 i 20 | Raw score nije verovatnoća, kalibracija ne koristi finalni test, a risk–coverage opisuje cenu abstention-a. |
| Structure–property i polymorph-risk target | 10–11A, 20–22 | Target se vezuje za material/solid form, uslove, metod, vreme i neizvesnost; indikator nije oracle. |
| Federativno učenje | 21–22 | FL nije zamena za licencu niti automatska privatnost; bez opravdanog multi-site targeta odluka je **DEFER**. |

## Tematske celine po redosledu preduslova

### Početnički most: od podataka do procene uspeha

**Čitaj:** [ML/AI od nule](00a-osnove-ml.md), §1–7, pa samoproveru osnovnog računa; §8–9 čitaj pre izabrane neuralne ili jezičke grane. Istovremeno počni hemijske osnove; za prve ML proračune nije potrebno detaljno znanje kristalografije.

**Fokus:** uzorak naspram feature-a i labele, deterministički algoritam naspram učenja, skalar/vektor/matrica, loss i parametri, trening/validation/kalibracija/test, precision/recall/nDCG i značenje uzdržavanja.

**Vežba:** bez gledanja rešenja ponovi Tanimoto primer, izračunaj 45 parova za 10 ulaza i objasni zašto candidate miss ne može ispraviti reranker. Nacrtaj četiri odvojene grupe podataka i smesti sve formate istog primera u jednu grupu.

**Kapija:** umeš da čitaš oznake u osnovnim formulama i da razlikuješ izračunatu geometriju, procenu verovatnoće i rang. Ako ne umeš, vrati se relevantnoj celini uvoda pre detaljnog algoritamskog modula.

### Problem pre algoritma

**Čitaj:** početne strane oba dela dokumentacije, hemijsku mapu projekta i dijagnostiku; zatim ML/AI scope, pipeline mapu i uvodne delove uporedne algoritamske mape.

**Fokus:** za oba proizvoda odredi objekat, korisničku odluku, target, cenu greške, evidence i ono što ostaje blokirano bez CSD prava ili gold podataka.

**Projektantska vežba:** frazu „sličan kristal“ razloži na najmanje pet različitih claim-ova. Uz svaki napiši dovoljan input i uslov za **UNKNOWN** ili **not_applicable**.

**Kapija:** umeš da objasniš zašto App 1 nije samo klasifikator, App 2 nije jedna univerzalna matrica score-a i LLM nije parser.

### Od atoma do stereo-svesnog grafa

**Čitaj:** hemija 1–4.

**Fokus:** formula naspram grafa, formalni/parcijalni naboj i oksidaciono stanje, konfiguracija naspram konformacije, nepoznata stereo oznaka naspram ahiralnosti.

**Projektantska vežba:** na pet malih nacrtanih primera napravi node/edge tabelu i obrazloži očekivani uticaj promene aromatičnosti, tautomerije, protonacije i stereo politike na fingerprint.

**Kapija:** prolaziš hemijsku Kapiju A i ne pretvaraš nepoznato polje u podrazumevanu vrednost.

### DAP, metali i koordinaciona semantika

**Čitaj:** hemija 5–6.

**Fokus:** tri DAP N donora, potential naspram observed denticity, metal u entry-ju naspram metala u istoj komponenti i direktne N3 koordinacije.

**Projektantska vežba:** napiši kriterijume za pozitivan, težak negativan i reprezentaciono neodređen slučaj; posebno objasni tvrdnju „isti metal je direktno vezan za sva tri mapirana DAP N“.

**Kapija:** nijedan kriterijum se ne svodi samo na formulu, filename, SMILES tačku ili pripadnost staroj search grupi.

### 3D, ćelija i periodični susedi

**Čitaj:** hemija7 samo [prvi prolaz](https://github.com/nemper/crystallography-and-ml-theory/blob/main/chemistry-foundations/docs/07-interakcije.md#prvi-prolaz), zatim8. Periodične kontakte i L4 odloži do sledeće celine.

**Fokus:** frakcione i Cartesian koordinate, metric tensor, PBC i činjenica da fizički objekat ne prestaje na ivici nacrtane ćelije.

**Projektantska vežba:** pretvori jednostavne frakcione koordinate u kartezijanske i objasni fizički smisao ponavljanja ćelije. Iz prvog prolaza7 protumači D–H···A ugao bez enumeracije simetrijskih slika.

**Kapija prvog prolaza:** razlikuješ hemijsku ulogu i geometriju kontakta i umeš da preračunaš koordinate u zadatoj ćeliji. Potpuna kapija periodičnih suseda dolazi nakon9–10.

### Simetrija, kvalitet i neizvesnost

**Čitaj:** hemija 9–10.

**Fokus:** ASU, ćelija i supercell; setting/origin promena naspram fizičke razlike; measured naspram simulated PXRD; profil kvaliteta naspram jednog R praga.

**Projektantska vežba:** opiši jednu ekvivalentnu promenu zapisa i jednu stvarnu promenu strukture, pa za nekoliko problema kvaliteta odredi očekivani status.

**Kapija:** ekvivalentan zapis ne tretiraš kao novi kristal, a odsutan ili loš input ne pretvaraš u score 0.

### Povratak na periodične kontakte

**Čitaj:** [drugi prolaz hemije7](https://github.com/nemper/crystallography-and-ml-theory/blob/main/chemistry-foundations/docs/07-interakcije.md#drugi-prolaz), nakon8–10.

**Fokus:** simetrijska slika, translacija, metrika kose ćelije, zauzeće mesta i nered u modelu pre brojanja suseda.

**Vežba i kapija:** prođi sačuvani periodični račun i L4; objasni zašto promena predstavnika ne menja fizički kontakt i zašto alternativna disorder mesta nisu nezavisno prisutni puni atomi.

### Polimorfi, packing i referentni signali

**Čitaj:** hemija 11 i 11A.

**Fokus:** parent compound, solid form, polymorph, solvate/hydrate/co-crystal i redetermination; granice Mogul, HBP, packing i PXRD signala.

**Projektantska vežba:** obrazloži slučaj sa istim molekulskim grafom i različitim packing-om i navedi kakva bi nezavisna potvrda bila potrebna za jaču tvrdnju.

**Kapija:** prolaziš hemijsku Kapiju C i umeš da predvidiš očekivanja za origin, wrap, setting/basis, supercell, stereo i disorder slučajeve.

### Formati i loss-aware ingest

**Čitaj:** hemija 12, 12A i 13; zatim prvi deo cross-format/lifecycle modula.

**Fokus:** šta CIF, MOL, MOL2, SDF i SMILES čuvaju, gube, dodeljuju ili ostavljaju nepoznatim; original i purpose-specific view nisu isto.

**Projektantska vežba:** napravi matricu gubitaka i obrazloži koje vrste provenance-a su potrebne da bi se razlikovali izvor, verzija, konflikt, raspoloživost i transformacija.

**Kapija:** lossy format ne prepisuje bogatiji izvor, uspešan parse nije isto što i validan crystal model i nijedan entry ne nestaje bez accounting-a.

### Eligibility, reprezentacije i lokalni bias

**Čitaj:** hemija 14–17 i 21; dovrši cross-format/lifecycle ugovor.

**Fokus:** declared, curated i geometry-neighbor graf; granice 2D, isolated-3D i periodic reprezentacije; identity, family, lifecycle i rights pre splita.

**Projektantska vežba:** na malom zamišljenom primeru nacrtaj union inventar, channel coverage, međusobno isključiv exclusion waterfall i proveru očuvanja broja zapisa.

**Kapija:** isti entry u svim formatima/verzijama pripada istoj split grupi, a missing SMILES nije ni missing graph ni negativna labela.

### Deterministički App 2: mapping i 3D

**Čitaj:** hemija 19 i pairwise modul 4.1–4.8.

**Fokus:** comparison profile, dodela komponenti sa unmatched opcijom, exact/subgraph/MCS semantika, automorfizmi, Kabsch posle mapping-a i koordinacioni evidence.

**Projektantska vežba:** za 4–6 ilustrativnih struktura ručno odredi broj parova i očekivano ponašanje grana pri timeout-u, unknown bond-u, missing cell-u i neodređenom donor assignment-u. Ne gradi engine.

**Kapija:** razumeš zašto svaki par i svaka grana moraju imati stanje i zašto smer A→B može menjati coverage, ali ne i simetrične veličine.

### App 1: exact i višekanalni candidate retrieval

**Čitaj:** hemija 18 i retrieval modul 3.1–3.12.

**Fokus:** eligibility/hard filter, 2D, coordination, shape i periodic kanal; exact ECFP/Tanimoto baseline, exact Flat oracle i ANN kao infrastrukturna optimizacija.

**Projektantska vežba:** na jednostavnim bit-vektorima ručno izračunaj Tanimoto za nekoliko kandidata i nacrtaj trag hard filter → kanali → unija kandidata. Zabeleži koje parametre i provenance bi budući sistem morao vezati za rang.

**Kapija:** umeš da objasniš set-equality zahtev za hard filter i zašto ANN evaluacija mora imati exact oracle iste reprezentacije i metrike.

### Split, baseline-i, kalibracija i analiza grešaka

**Čitaj:** hemiju20 u celosti i osnovni evaluacioni račun iz00a. Sekcije6.8–6.12 su kasnija detaljna referenca; nisu preduslov ovog bloka.

**Fokus:** estimand pre splita; query/family grouping, 1D warm/cold, 2D cold/cold i temporal holdout; nezavisne grupe naspram broja parova.

**Projektantska vežba:** nacrtaj leakage-safe train/validation/calibration/test podelu, tabelu budućih baseline-a i odluka, pa protumači zamišljene rezultate za intervale, worst slice, kalibraciju i risk–coverage. Ne treniraš modele.

**Kapija:** model, prag i calibrator se ne biraju na finalnom testu, raw score nije verovatnoća i **KEEP BASELINE** je ispravan ishod kada nema praktičnog dobitka.

### Klasični ML pre učenog rangiranja i kernela nad okruženjima

**Čitaj:**02 linearne reference, stablo i prosečavanje, dva boosting koraka, kernel/Gram uvod i kalibraciju zamrznutog modela.

**Preduslov:** loss, split i evaluacione metrike iz prethodnog bloka. **Vežba:** ponovi račun reziduala, sastavi malu Gram matricu i odvoji fit kalibratora od izbora praga.

**Kapija:** umeš da objasniš šta uči sledeće stablo i zašto proizvoljna sličnost nije automatski validan kernel. Tek sada čitaj LambdaMART i, ako biraš SOAP, njegov numerički uvod u02. PCA/PLS, GPR i conformal razrada su uslovni nastavci.

### Deterministički App 2: packing i evidence

**Čitaj:** posle kernel uvoda u02 dovrši pairwise modul4.9–4.21; SOAP/REMatch prvo prati kroz njegov mali primer u02. Specifične metode produbljuj po izabranoj grani.

**Fokus:** uloge i granice COMPACK/PAC, CrystalCMP, SOAP–REMatch, PXRD i interaction networks; primenljivost i licencna dostupnost.

**Projektantska vežba:** skiciraj predložak evidence-rich izveštaja i ručno popuni nekoliko normalnih, failure i ambiguous slučajeva. Ako metoda nije dostupna ili validirana, predviđeni izlaz je precizan status, ne improvizovani rezultat.

**Kapija:** drugi inženjer iz tvoje skice može nedvosmisleno razumeti budući pair universe, mapping, parametre, statuse i evidence.

### Reranking, qrels i retrieval evaluacija

**Čitaj:** posle stabala i boostinga u02 retrieval modul3.13–3.22; osnova evaluacije iz hemije20 već je preduslov.

**Fokus:** infrastructure Recall@N, expert candidate Recall@N i end-to-end nDCG/Recall; pool, unjudged primeri, hard negatives i granica candidate/reranker greške.

**Projektantska vežba:** na malom zamišljenom skupu napravi vodič za slepu graded-relevance anotaciju i ručno obrazloži jedan tok exact → candidate → rerank, uključujući izgubljen relevantan kandidat.

**Kapija:** candidate miss ne pripisuješ rerankeru, stare search grupe nisu gold i novi neocenjeni vrh rezultata zahteva dopunu pool-a.

### Periodični graf i encoder contract

**Čitaj:** periodične crystal encodere.

**Fokus:** site features, edge vrste, image/lattice podaci, cell/global state, occupancy/disorder i invariance/equivariance ugovor; crystal encoder, pair model i property model nisu isto.

**Projektantska vežba:** uporedi input i invariance zahteve nekoliko opisanih encoder porodica i napiši očekivane metamorphic provere koje bi prethodile bilo kakvom treningu.

**Kapija:** znaš koje transformacije ne menjaju target semantiku, kako stereo profil utiče na refleksiju i zašto nevalidan periodic input nije zero-filled pseudo-kristal.

### Metric learning bez lažnih parova

**Čitaj:** ceo metric learning i evaluacioni modul.

**Fokus:** equivalence, relation i query-conditioned relevantnost; granice contrastive/triplet/InfoNCE pristupa; dual encoder naspram exact evidence-a i cross-graph comparator-a.

**Projektantska vežba:** napravi uporednu tabelu descriptor+GBDT, CGCNN i Matformer/ALIGNN porodica, sa istim targetom i splitom, potrebnim ablation-om, false-negative pitanjima i uticajem label budžeta.

**Kapija:** umeš da objasniš praktičnu korist, critical-slice non-inferiority, kalibraciju, abstention, resurse, licence i reproduktivnost bez pretpostavke da deep model mora pobediti.

### Governance, white paper i uslovne teme

**Čitaj:** hemija 22 i celu uporednu mapu po drugi put; zatim teorijske granice lokalnog SLM/RAG-a i spoljnog API-ja.

**Fokus:** white-paper pojmovi naspram state, property i evidence semantike; polymorph-risk indikator naspram tvrdnje; naučni, pravni i bezbednosni uslovi za SLM, API i FL.

**Projektantska vežba:** usmeno odbrani jedan search query, pair rezultat, **UNKNOWN** slučaj, leakage incident i licence stop. Za FL prođi preduslove i nacrtaj threat model na konceptualnom nivou.

**Kapija:** umeš da objasniš zašto FL zahteva zakonit zajednički multi-site supervised target, a SLM/API ne postaju naučni autoritet time što su jezički sposobni.

## Kapije prelaza

Kapije ispituju tek pročitane preduslove. G4 u prvom prolazu proverava mapping/3D; specifični kernel/packing dokazi dodaju se nakon02. G5 prvo proverava dohvat kandidata, a učeno rangiranje tek posle boostinga i G6. G7 i G8 važe samo za izabrane uslovne grane.

| Kapija | Prelaziš kada razumeš i možeš da obrazložiš | Ne prolazi ako |
|---|---|---|
| G−1 — ML i matematički minimum | uzorak/feature/labelu, normu i skalarni proizvod, fitting/split, Tanimoto i recall na malom primeru | brojevi 0–1 se automatski nazivaju verovatnoćom ili se ista struktura u više formata broji kao nezavisni skup |
| G0 — claim i prava | objekat, target, scope, evidence, rights pitanja, abstention i stop-uslov za svaki output | nepoznata licenca se prećutno tretira kao dozvola |
| G1 — hemijski graf i koordinacija | DAP motif, stereo, charge, component i donor mapping na ilustrativnom primeru | formula, filename ili samo prisustvo metala glume povezanost |
| G2 — crystal i 3D | očekivano PBC/symmetry/setting/basis i stereo ponašanje | RMSD prethodi atom mapping-u ili cell/space group glume packing dokaz |
| G3 — data core | union inventar, lineage, purpose view, lifecycle i denominator accounting na malom primeru | silent overwrite, inner-join drop ili missing status postaje vrednost |
| G4 — deterministički App 2, posle hemije19 i osnovnog04 | pair universe, branch state, evidence, simetriju i usmereni coverage | non-assessed grana nestaje, postaje nula ili dobija relation labelu |
| G5 — osnovni App 1, posle exact/ANN mehanike | exact filter/oracle, multichannel coverage i tri nivoa retrieval evaluacije | ANN brzina glumi hemijsku tačnost ili reranker skriva candidate miss |
| G6 — evaluacija, posle hemije20 i osnovnog02 | leakage-safe gold/qrels, split, kalibraciju i error-analysis plan | stare grupe, duplikati ili finalni test utiču na trening i tuning |
| G7 — deep modeli | fer poređenje za critical slice, invarijanse, resurse i licence | jedan random split, seed ili label budžet se smatra dovoljnim dokazom |
| G8 — uslovne teme | koje dodatno pitanje rešavaju SLM, API, polymorph-risk ili FL i koje pretpostavke zahtevaju | sama oznaka „AI“, „LLM“ ili „FL“ služi kao opravdanje |

## Minimalni paket beležaka svake nastavne celine

Za učenje je dovoljno da beleška sadrži:

- pitanje ili claim i populaciju na koju se odnosi;
- hemijski objekat, target i relevantnu reprezentaciju;
- relevantne izvore, status prava i ono što još nije poznato;
- ilustrativan primer i očekivani ishod;
- missing, ambiguous, not-applicable i failure slučajeve;
- buduće zahteve za validaciju, metrike i stop-uslov;
- poznate granice i odluku šta treba čitati ili proveravati sledeće;
- vezu sa rečnikom i čestim zabludama iz hemijskog dela.

Plan učenja beleži pojmove, pretpostavke i načine dokazivanja. Ne definiše tehničke artefakte, konkretne modele, servise ili operativne izveštaje.

## Uslovni nastavak posle osnovnih blokova

Ovo nisu automatske obaveze osnovnog 2CDC scope-a.

### Lokalni SLM i dokumentacioni RAG

Pročitaj lokalni SLM/RAG modul i uporedi formulare/rečnike, kontrolisanu međureprezentaciju, BM25, constrained decoding, dense retrieval, RRF i reranking. Objasni kako intent/paraphrase grupe, višejezični i rare-token slučajevi utiču na evaluaciju, bez menjanja determinističkog naučnog rezultata.

**Ishod učenja:** uporedna beleška o ulozi, ograničenjima i evaluaciji lokalnog jezičkog sloja.

### Spoljni API

Pročitaj API/security modul. Objasni razliku između izvorne licence, minimizacije, processor/region uslova, retention-a, cache/state-a, audit-a i prompt-injection odbrane. Projektni podaci se ne šalju radi vežbe.

**Ishod učenja:** obrazložena procena koje činjenice bi morale biti poznate pre razmatranja spoljne obrade, bez izbora providera ili modela.

### Federativno učenje

Ponovo pročitaj FL delove hemijskog poglavlja 22 i uporedne mape. Uporedi centralizovano, local-only, shared-public-pretraining i federativno učenje, pa objasni kako threat model određuje secure aggregation, diferencijalnu privatnost i robust aggregation.

**Ishod učenja:** konceptualno objašnjenje uslova pod kojima FL ima smisla. Bez stvarnog multi-site targeta koji se zakonito ne može centralizovati, FL ostaje samo teorijska porodica.

## Završni kriterijum spremnosti

Integrisano razumevanje imaš kada možeš da odbraniš ceo lanac:

**odobren izvor → loss-aware purpose view → hemijski i periodični objekat → deterministički exact evidence → candidate retrieval i/ili pair comparison → leakage-safe gold/qrels i split → kalibrisana target-specific learned metoda sa abstention-om → reproduktivnost i licencna dozvoljenost → objašnjiv rezultat ili precizan UNKNOWN**

Ako bilo koja strelica nema jasno značenje, teorijsko opravdanje i plan buduće provere, složeniji model još nije sledeći korak.
