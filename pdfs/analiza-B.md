# Pedagoška analiza teorijske osnove projekta 2CDC

**Datum pregleda:** 5. septembar 2026.  
**Pregledana kopija:** `C:\Users\Korisnik\Desktop\crystallography-and-ml-theory-2`  
**Predmet:** kvalitet objašnjenja, redosled preduslova i kontinuitet između hemije i ML/AI.  
**Način rada:** čitanje izvornog sadržaja; repozitorijum nije menjan.

## Objedinjena procena

Teorijska osnova je obimna, projektno relevantna i naročito dobra u razdvajanju onoga što podatak zaista pokazuje od zaključka koji tek treba potvrditi. Hemijski deo uspešno povezuje sastav, molekulski graf, konformaciju, kristalno pakovanje i eksperimentalni model. ML/AI deo ozbiljno tretira definiciju cilja, primenljivost reprezentacije, nezavisnost evaluacije i ograničenja naučenih modela.

Glavni nedostatak je **neujednačen odnos između objašnjenja postupka i objašnjenja njegovih ograničenja**. Na više mesta čitalac sazna mnogo o tome kada metodu ne sme nekritički primeniti, a znatno manje o jednostavnom primeru njenog rada. To posebno pogađa deklarisanu putanju „od nula predznanja“. Iskusan ML inženjer će deo praznina sam popuniti; početnik u obe oblasti ima znatno veći teret.

Drugi problem je **raspored stvarno postojećih objašnjenja**. Rečnik, planovi učenja i uvod u ML zaista pokrivaju mnoge termine. Ipak, lokalna lekcija ponekad zahteva sposobnost koja se sistematski razvija tek kasnije. Najočigledniji primer je operativna analiza periodičnih kontakata u hemijskom poglavlju 7, pre poglavlja o ćeliji i simetriji. U naprednom ML delu sličan obrazac postoji kod periodičnih grafova, promena njihovog zapisa i matematičke notacije za simetriju.

Preporučujem ciljanu reviziju: nekoliko kratkih pojmovnih mostova, nekoliko potpuno izvedenih sintetičkih primera i jasno razdvajanje osnovne lekcije od napredne reference. Nije potrebno pisati novu knjigu, pojednostavljivati opravdano složenu kristalografiju niti dodatno širiti svaki nabrojani algoritam.

## Obuhvat i kriterijum procene

Pregled obuhvata **51 izvorni Markdown dokument: 36 u hemijskom i 15 u ML/AI delu, ukupno 13.047 linija**, uz README i obe MkDocs konfiguracije. Pomoćni materijali — planovi, dijagnostika, rečnik, zablude, laboratorije, rešenja, završni projekat i bibliografske strane — korišćeni su za proveru da li objašnjenje zaista nedostaje ili se nalazi drugde. Detaljan popis pokrivenosti nalazi se na kraju.

PDF kopije nisu analizirane ponovo. Odsustvo originalnih fakultetskih/CSD materijala, uključujući CIF/MOL izvoze i white paper, **nije tretirano kao nedostatak**. Lokalni brojevi i primeri ocenjeni su kao deo izlaganja u dokumentaciji; ovaj pregled ne tvrdi da su ponovo izračunati iz nedostupnih podataka. Sintetički primeri preporučuju se radi objašnjenja postupaka, a ne kao zamena za te originalne materijale.

Analiza je prvenstveno pedagoška. Spoljni primarni i zvanični izvori proveravani su ciljano kada su pomagali da se razgraniči značenje metode ili opravdanost preporučenog međukoraka. Nije urađen novi pregled celokupne literature, reprodukcija algoritama, benchmark nad CSD-om niti pravna provera licenci. Pedagoška ocena zasniva se na stvarnom tekstu i njegovim zavisnostima; sama činjenica da je složen koncept prisutan nije nalaz protiv njega.

Za svaki nalaz odvojeni su lokacija, problem, posledica za čitaoca, implicitni preduslov, konkretna intervencija i značaj. „Nedostaje primer“ koristim samo tamo gde primer popunjava određeni misaoni korak koji se kasnije zahteva.

| Značaj | Značenje u ovom izveštaju |
|---|---|
| Kritičan za razumevanje | Nepopunjen preduslov može zaustaviti deklarisanog početnika ili preneti pogrešno razumevanje kroz više narednih tema. Ne znači automatski da je naučna tvrdnja netačna. |
| Važan | Čitalac može pratiti opštu poruku, ali nema dovoljno osnove za traženu samostalnu procenu ili proračun. |
| Koristan za poboljšanje | Osnovna poruka je dostupna; intervencija smanjuje nepotreban napor ili priprema određenu naprednu granu. |
| Manja pedagoška/stilska sugestija | Terminologija, navigacija ili ponavljanje otežavaju čitanje, bez bitne teorijske praznine. |

Prioritet izmene i značaj nisu isto: kratak dodatak legende može biti brz prvi zahvat, a dublji opcioni metod ne mora blokirati osnovnu putanju. Linije se odnose na pregledanu kopiju i promeniće se posle uređivanja.


## Nalazi: hemija i kristalografija

### H01 — Od valentnih elektrona do Lewisovog crteža nedostaje jedan osnovni postupak

- **Gde:** [hemija/02-veze.md:7–38](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/02-veze.md:7), §2.1–2.3; provera [hemija/02-veze.md:112–125](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/02-veze.md:112) i zahtev kapije A [hemija/dijagnostika.md:28–35](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/dijagnostika.md:28).
- **Problem:** crte, tačke i formalni naboj jesu definisani. Pravilo okteta je imenovano, ali nije objašnjeno kako početnik određuje broj valentnih elektrona i raspoređuje ih u crtežu. Spoljni OpenStax link postoji; rečnik daje definicije. Nedostaje lokalni međukorak ili jasna oznaka da je konkretno spoljno čitanje obavezno.
- **Zašto je teško:** čitalac može ubaciti već date V, N i B u formulu, a ne znati kako ih sam odrediti za neutralni ili protonovani azot. Na tome kasnije počivaju slobodni parovi, donori i ocena nedoslednog izvoza veza.
- **Implicitno znanje:** valentni elektroni H/C/N/O, oktet i izuzetak za H, razlika broja elektrona, broja veza i valence.
- **Konkretna izmena:** mala tabela H/C/N/O i potpuno izveden par NH₃/NH₄⁺ ili H₂O/OH⁻, sa tačkama, ukupnim brojem elektrona i proverom formalnog naboja. Zadržati postojeći nitro-primer kao sledeći nivo. Alternativno, označiti odgovarajući deo [OpenStax lekcije](https://openstax.org/books/chemistry-2e/pages/7-3-lewis-symbols-and-structures) kao obavezan pre kapije A.
- **Značaj:** **važan** — osnovni preduslov koji utiče na više narednih poglavlja.

### H02 — Aromatično elektronsko brojanje ostaje implicitno

- **Gde:** [hemija/02-veze.md:50–79](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/02-veze.md:50), naročito §2.5; primena na piridin/pirol u [hemija/04-organska.md:80–87](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/04-organska.md:80).
- **Problem:** σ/π veze i konjugacija jesu uvedene. Kod pravila 4n+2 nije izričito objašnjeno šta se broji i šta predstavlja n. Kasniji „π sekstet“ i različita uloga slobodnog para dva aromatična N atoma nemaju prikazan elektronski račun.
- **Zašto je teško:** čitalac može zapamtiti da je piridinski N raspoloživ donor, a pirolski nije na isti način, bez razloga koji bi preneo na novi ligand.
- **Implicitno znanje:** π elektronsko brojanje i razlika slobodnog para koji pripada π sistemu od para van njega.
- **Konkretna izmena:** uz postojeća ograničenja pravila definisati n i π elektrone; dodati označen benzen i uporedni prikaz piridina/pirola sa doprinosima elektrona i slobodnim parom. Nije potrebna derivacija molekulskih orbitala niti katalog antiaromatičnih sistema. [OpenStax primer piridina i pirola](https://openstax.org/books/organic-chemistry/pages/15-5-aromatic-heterocycles-pyridine-and-pyrrole) daje odgovarajući nivo osnove.
- **Značaj:** **važan** — neposredan most ka DAP donorima i digitalnim donor/akceptor etiketama.

### H03 — Dva značenja reči „donor“ treba razdvojiti pre tabele funkcionalnih grupa

- **Gde:** [hemija/04-organska.md:9–37](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/04-organska.md:9); kasnija objašnjenja u [hemija/05-kompleksi.md:7–18](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/05-kompleksi.md:7) i [hemija/07-interakcije.md:91–109](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/07-interakcije.md:91).
- **Problem:** tabela već koristi H-bond donor/acceptor, a odmah zatim N-donor prema metalu. Pojedinačne tvrdnje su uglavnom jasne i tačne; zajednički ključ za razlikovanje dolazi rasuto kroz kasnija poglavlja.
- **Zašto je teško:** doniranje slobodnog elektronskog para može se pomešati sa doniranjem vodonične veze. Atom koji donira par metalu može u drugom kontekstu biti akceptor H-veze.
- **Implicitno znanje:** razlika Lewisove baze prema metalu i uloga D–H/A u vodoničnoj vezi, uz protonaciju i prisustvo vezanog H.
- **Konkretna izmena:** pre §4.1 okvir sa dva prikaza, `N: → M` i `D–H···A:`, i po jednom rečenicom o značenju donora. Neutralni piridinski N je dovoljan zajednički primer. Linkovati kasnija detaljna objašnjenja i zadržati postojeće nijanse o amidu. Terminološki oslonac je [IUPAC definicija H-veze](https://goldbook.iupac.org/terms/view/H02899).
- **Značaj:** **važan** — mala dopuna sprečava zabunu koja se prenosi do HBP-a.

### H04 — Obavezno ligandno polje dolazi pre potrebnog orbitalnog minimuma

- **Gde:** [hemija/05-kompleksi.md:158–187](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/05-kompleksi.md:158), „Minimalni ligand-field most“; prethodni uvod [hemija/02-veze.md:7–12](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/02-veze.md:7); denticitet i oksidaciono stanje dolaze tek u [hemija/05-kompleksi.md:190–245](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/05-kompleksi.md:190).
- **Problem:** pet d-orbitala, t₂g/e_g, energija sparivanja, degeneracija i antivezni karakter koriste se kao sažetak poznatog gradiva. Nisu prethodno pokazani kapacitet orbitale, upareni/nespareni elektroni ni izbor između sparivanja i zauzimanja višeg nivoa. Direktan link ka kasnijem bilansu oksidacionog stanja postoji, pa taj deo predstavlja problem redosleda.
- **Zašto je teško:** početnik može memorisati obrazac Cu(II)/d⁹/izduženje, a ne razumeti zašto d¹⁰ Zn predstavlja drugi slučaj. Upravo se takvo obrazloženje traži kao ishod.
- **Implicitno znanje:** orbitala kao energetsko stanje, do dva elektrona suprotnog spina, popunjavanje nivoa i konkurencija cepanja i sparivanja.
- **Konkretna izmena:** najpre ligand/donor → CN i denticitet → bilans oksidacionog stanja → dⁿ → elektronsko tumačenje geometrije. Pre tabele dati kutije/strelice za jedan d⁶ primer u dva idealizovana oktaedarska polja. Objasniti Δ i cenu sparivanja; bez multipleta i kvantnomehaničkih izvođenja. [OpenStax koordinaciona hemija](https://openstax.org/books/chemistry-2e/pages/19-3-spectroscopic-and-magnetic-properties-of-coordination-compounds) podržava takav uvod. Ograde o nedovoljnosti jedne dužine za dokaz mehanizma treba sačuvati.
- **Značaj:** **kritičan za razumevanje ove obavezne celine kod početnika**; osnovni deo o CN-u i CAPHEK-u ostaje dobar.

### H05 — Mehanizam nastanka imina koristi nekoliko neuvedenih termina

- **Gde:** [hemija/06-dap-schiff.md:30–50](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/06-dap-schiff.md:30), §6.2; prethodna Lewisova kiselina/baza u [hemija/04-organska.md:39–53](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/04-organska.md:39).
- **Problem:** „nukleofilni napad“, „elektrofilni C“, „intermedijer“ i eliminacija sažeti su u četiri koraka, bez veze sa već poznatim elektronskim parom i polaritetom karbonila.
- **Zašto je teško:** ukupan reakcioni bilans može biti razumljiv, a reč „napada“ ostaje mehanistička metafora bez jasnog značenja.
- **Implicitno znanje:** nukleofil/elektrofil, privremena reakcijska vrsta i premeštanje protona.
- **Konkretna izmena:** kratko prevesti nukleofilni N u prethodno uvedenu Lewisovu bazu i elektrofilni C u mesto koje prima elektronski par; intermedijer definisati kao privremeni proizvod koraka. Druga prihvatljiva opcija je označiti mehanističku listu kao produbljivanje, dok obavezni ostaju reakcija i postojeći atomski bilans. Ne dodavati čitav kurs mehanizama.
- **Značaj:** **koristan za poboljšanje**.

### H06 — Periodični kontakt se zahteva pre lekcija koje omogućavaju njegovo razumevanje

- **Gde:** ishodi i „most“ [hemija/07-interakcije.md:5–33](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/07-interakcije.md:5), račun [hemija/07-interakcije.md:165–205](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/07-interakcije.md:165) i završna kapija [hemija/07-interakcije.md:350–356](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/07-interakcije.md:350); osnova se razvija u [hemija/08-celija.md:146–190](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/08-celija.md:146) i [hemija/09-simetrija.md:34–77](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/09-simetrija.md:34).
- **Problem:** poglavlje 7 već traži periodične susede, simetrijske operacije i kontaktni graf. Kratak most daje jednačine, ali istovremeno uvodi bazu ćelije, frakcione koordinate, ASU, centriranje, occupancy i deduplikaciju. To prevazilazi najavu buduće teme: kasnije se zahteva reprodukcija računa.
- **Zašto je teško:** čitalac mora otići u poglavlja 8 i 9 da bi prošao kapiju poglavlja 7, iako plan propisuje napredovanje nakon savladanog ishoda.
- **Implicitno znanje:** ćelija/baza, ASU, konverzija koordinata, simetrijsko proširenje, periodične slike i identitet kristalografskog mesta.
- **Konkretna izmena:** putanja **7A fizičke interakcije → 8 ćelija → 9 simetrija → 7B periodični kontakti**. U prvom prolazu ostaviti fizičku intuiciju i jednostavnu D–H···A geometriju; formalno proširenje, periodični račun i odgovarajuću kapiju pomeriti u drugi. To može biti podela postojećeg fajla na dva čitalačka prolaza, bez obaveznog stvaranja novih fajlova. Uskladiti navigaciju, plan i kapije.
- **Značaj:** **kritičan za kontinuitet početničke putanje**. Sama objašnjenja iz 8–9 ne zahtevaju dupliranje.

### H07 — Coulombova i Lennard–Jonesova formula nemaju potpunu legendu

- **Gde:** [hemija/07-interakcije.md:68–89](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/07-interakcije.md:68), „Šta drži molekulski kristal“.
- **Problem:** nisu objašnjeni ε₀, εᵣ, ε i σ. Slična slova u uzastopnim jednačinama imaju različite fizičke uloge, dok tekst od formula očekuje da daju intuiciju o znaku i optimalnom razmaku.
- **Zašto je teško:** čitalac ne zna koja veličina određuje energijsku, a koja dužinsku skalu; može pomešati σ sa položajem minimuma ili ε sa permitivnošću.
- **Implicitno znanje:** permitivnost, potencijalna energija, jedinice parametara i čitanje oblika potencijala.
- **Konkretna izmena:** dodati legendu svih simbola i jedinica. Uz LJ dati jednu označenu krivu sa nulom i minimumom, ili tri vrednosti na malom/srednjem/velikom rastojanju. Objasniti da ε određuje dubinu minimuma, a σ nulu tog izraza; [zvanična LAMMPS dokumentacija](https://docs.lammps.org/pair_lj.html) eksplicitno razlikuje te uloge. Zadržati postojeća fizička ograničenja; ne uvoditi derivaciju sile ako nije potrebna.
- **Značaj:** **važan**, uz vrlo malu potrebnu intervenciju.

### H08 — Superćelija i promena baze traže jedan konstruktivan primer

- **Gde:** [hemija/08-celija.md:348–378](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/08-celija.md:348), naročito podrešetka i „coset representative“; nastavak [hemija/09-simetrija.md:239–282](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/09-simetrija.md:239).
- **Problem:** matematički zapis promene ćelije jeste potreban, ali pre pojma klase translacija nije prikazano gde zaista završavaju nove kopije motiva. Vežba sa V/Z/gustinom proverava skaliranje, ne konstrukciju koordinata.
- **Zašto je teško:** udvostručenje zapremine je intuitivno, a prelaz na predstavnike podrešetke nepotrebno apstraktan bez jednog atomskog primera.
- **Implicitno znanje:** promena baze naspram deformacije, podrešetka i predstavnici translacionih klasa.
- **Konkretna izmena:** primer 2×1×1: nakon udvostručenja a, stare kopije x i x+1 imaju nove frakcione koordinate x/2 i (x+1)/2. Pokazati očuvanje fizičkih položaja. Tek potom dati opšti matrični zapis; termin koset može ostati u opcionoj napomeni. U 9 dodati jednu proveru promene origina ako je potrebna za povezivanje R′/t′.
- **Značaj:** **koristan za poboljšanje**, posebno pre periodičnih ML modela.

### H09 — Pre PXRD poređenja nedostaje fizički uvod u praškasti eksperiment

- **Gde:** [hemija/10-difrakcija-kvalitet.md:73–134](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/10-difrakcija-kvalitet.md:73) i [hemija/10-difrakcija-kvalitet.md:147–170](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/10-difrakcija-kvalitet.md:147); kasnija primena [hemija/11-cvrste-forme.md:243–257](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/11-cvrste-forme.md:243).
- **Problem:** hkl→d→2θ i razlika simulirano/izmereno dobro su obrađeni. Nije prvo jasno prikazano šta razlikuje merenje jednog kristala od praha i kako nastaje tipična jednodimenzionalna kriva intenzitet–2θ.
- **Zašto je teško:** preklapanje pikova, preferentna orijentacija i reprezentativnost celog uzorka pojavljuju se bez eksperimentalne slike koja ih povezuje.
- **Implicitno znanje:** kristalit, raspodela orijentacija, powder prstenovi i svođenje podatka na 1D obrazac.
- **Konkretna izmena:** kratak uvod „jedan kristal → mnogo kristalita“ i šema tačkastih refleksija/prstenova/1D krive. U tom okviru objasniti preklapanje i mogućnost više faza u uzorku, pa nastaviti postojećom tabelom. Dovoljna je osnova opisana u [IUCr klasifikaciji eksperimentalnih tehnika](https://xrpp.iucr.org/Cc/wf5156/wf5156.html); Rietveldova analiza i rešavanje strukture iz praha nisu potrebni.
- **Značaj:** **važan** za kasniju validaciju čvrstih formi i tumačenje PXRD signala.

### H10 — Račun ΔG ima više osnove od fizičkog značenja H i S

- **Gde:** [hemija/11-cvrste-forme.md:143–194](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/11-cvrste-forme.md:143); kratka rečnička osnova [hemija/recnik.md:450–465](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/recnik.md:450).
- **Problem:** formula, jedinice, predznak i numerički primer su pažljivi. Entalpija i entropija u samoj lekciji prvenstveno dobijaju imena; odmah zatim se uvode hemijski potencijal i aktivnost vode. Deo osnove postoji u rečniku, pa je problem fragmentacija i nedovoljno povezivanje.
- **Zašto je teško:** čitalac računa 1000−4T, ali ne vidi zašto dva pakovanja imaju različite H/S i zašto promena temperature menja njihov odnos.
- **Implicitno znanje:** kvalitativna veza interakcija i entalpije, dostupnih stanja/kretanja i entropije, razlika ravnoteže i kinetičke barijere.
- **Konkretna izmena:** preneti prilagođene definicije u lekciju i na postojećem primeru protumačiti zašto B postaje povoljnija pri većem T. Aktivnost/hemijski potencijal vode kratko objasniti samo koliko zahteva promena sastava, uz link za produbljivanje. [OpenStax slobodna energija](https://openstax.org/books/chemistry-2e/pages/16-4-free-energy) daje prikladan pojmovni okvir. Ne širiti već dobar numerički račun i ograničenje enantiotropnog zaključka.
- **Značaj:** **važan** za razumevanje stabilnosti.

### H11 — HBP primer ne prikazuje oba grupna izlaza koja traži kriterijum prolaza

- **Gde:** [hemija/11a-referentne-raspodele-hbp.md:118–163](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/11a-referentne-raspodele-hbp.md:118) i [hemija/11a-referentne-raspodele-hbp.md:194–209](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/11a-referentne-raspodele-hbp.md:194); vežba [hemija/laboratorije.md:236–247](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/laboratorije.md:236).
- **Problem:** individual propensity, observed status, grouping i coordination score konceptualno su razdvojeni. Numerički primer ipak prikazuje samo individualne verovatnoće i intervale, dok se tumačenje HBP chart-a traži na izlazu. Dodatna grupna demonstracija nije nađena u drugim poglavljima ili rešenjima.
- **Zašto je teško:** čitalac zna da grouping nije polimorf i da HBP coordination nije CN metala, ali ne vidi dve mreže sa različitim donorskim/akceptorskim ishodima.
- **Implicitno znanje:** kombinovanje mogućih ivica, broj doniranih/prihvaćenih H-veza i sažimanje njihovih ocena.
- **Konkretna izmena:** proširiti postojeći primer sa dva nacrtana grouping-a, njihovim ivicama i jednom označenom observed tačkom. Grupne vrednosti dati kao jasno sintetičke, ili ih izračunati po imenovanoj konvenciji [CCDC propensity groupings dokumentacije](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/hbond_propensities.html#propensity-groupings). Ne izmišljati univerzalnu agregacionu formulu i ne dodavati novi opšti kurs logističke regresije.
- **Značaj:** **koristan za poboljšanje**, posle osnovnih hemijskih i kristalografskih mostova.

## Nalazi na prelazu iz hemije u algoritme

### D01 — Globalno uparivanje komponenti nije demonstrirano na maloj matrici

- **Gde:** [hemija/19-parovi.md:61–85](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/19-parovi.md:61), §19.4–19.5; [ML/04-precise-pairwise.md:116–155](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/04-precise-pairwise.md:116), §4.4; rubrika [hemija/resenja.md:123–140](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/resenja.md:123).
- **Problem:** hemija navodi „globalno konzistentno uparivanje“, a ML daje cost formulu, Hungarian metod, unmatched čvorove i napredne multiplicitet/orbit slučajeve. Nema izvedenog primera koji pokazuje šta globalno rešenje dodaje izboru najboljeg partnera pojedinačno.
- **Zašto je teško:** čitalac može pogoditi ligand–ligand/voda–voda slučaj, ali ne vidi kako izbor jedne komponente ograničava druge. Sledeći atom mapping i RMSD zavise od tog izbora.
- **Implicitno znanje:** bipartitno uparivanje, ukupni trošak, one-to-one ograničenje i mogućnost neuparenog objekta.
- **Konkretna izmena:** 2×2 sintetička matrica `[[1,2],[2,100]]`: pohlepno biranje prvog reda može dati zbir 101, dok druga potpuna dodela daje 4. Brojevi samo demonstriraju globalnost, ne predstavljaju hemijsku metriku. Dodati odvojenu tabelu hemijske dozvoljenosti, jedan unmatched slučaj i prenos izabranog rešenja u malu atom-map tabelu. Napredne orbite/multiplicitete ostaviti posle tog primera.
- **Značaj:** **važan** za App 2. Ovo je jedan zajednički nalaz oba kursa.

### D02 — Grupna i uparena evaluacija nemaju izvedeni primer

- **Gde:** [hemija/20-evaluacija.md:95–109](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/20-evaluacija.md:95) i [hemija/20-evaluacija.md:160–166](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/20-evaluacija.md:160); [ML/06-metric-learning-and-evaluation.md:302–311](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:302); osnovna definicija bootstrap-a već postoji u [ML/00a-osnove-ml.md:185–189](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/00a-osnove-ml.md:185).
- **Problem:** razlog za grupisanje i izbor jedinice uzorkovanja jesu objašnjeni. Nedostaje ceo prelaz od rezultata po grupama do macro/micro procene, zajedničkog resample-a i uparene razlike metoda. Ne nedostaje definicija bootstrap-a kao takva.
- **Zašto je teško:** „ne uzorkuj nezavisno redove parova“ ostaje pravilo bez prikaza šta se zapravo ponavlja i šta se ponovo računa. Završni zahtev za intervalom može se ispunjavati mehanički.
- **Implicitno znanje:** procenitelj, ponderisanje grupa, zavisna opažanja, uzorkovanje sa vraćanjem i raspodela razlike dva procenitelja.
- **Konkretna izmena:** dva query-ja za razliku macro/micro; zatim nekoliko sintetičkih nezavisnih familija sa rezultatima oba metoda, dve ili tri resample liste i račun jedne uparene razlike. Objasniti da mali primer ilustruje postupak, a ne dokazuje pouzdan interval. Za App 2 pokazati deljenje endpoint-a i upućivati na postojeći dyadic/endpoint okvir; obični query bootstrap ne prenositi slepo na sve parove. Jedan zajednički statistički most linkovati iz hemije i ML-a.
- **Značaj:** **važan** pre naučnog tumačenja poređenja modela.

### D03 — Od hemijskog grafa do fingerprint-a nedostaje jedan vidljiv korak

- **Gde:** [hemija/14-reprezentacije.md:46–62](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/14-reprezentacije.md:46), [hemija/15-slicnost.md:28–44](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/15-slicnost.md:28) i [ML/03-global-retrieval-ann-ranking.md:134–155](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:134).
- **Problem:** ECFP, radijus, bit/count, kolizija i Tanimoto imaju objašnjenja. Ipak, računski primeri počinju gotovim skupovima bitova; nije prikazan jedan korak kojim se lokalno atomsko okruženje kodira.
- **Zašto je teško:** posledica promene protonacije ili bond typing-a na rang ostaje uglavnom verbalna tvrdnja.
- **Implicitno znanje:** objedinjavanje oznaka atoma i suseda, kodiranje okruženja i preslikavanje koda u ograničen vektor.
- **Konkretna izmena:** graf od 3–4 atoma → radius-0 oznake → jedna iteracija susedstva → izmišljena tabela kod/bit. Promeniti jednu vezu i pokazati promenjeni bit, pa upotrebiti već uvedeni Tanimoto. Jasno označiti da didaktički hash nije stvarni izlaz RDKit-a. Ne objašnjavati ponovo sve parametre koji već imaju definiciju.
- **Značaj:** **koristan za poboljšanje** veze hemija–cheminformatika.

### D04 — Standardizaciji treba jedan zaokružen primer dva namenska pogleda

- **Gde:** [hemija/13-standardizacija.md:17–52](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/13-standardizacija.md:17) i [hemija/13-standardizacija.md:108–137](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/13-standardizacija.md:108); završni zahtev [hemija/13-standardizacija.md:144–154](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/13-standardizacija.md:144).
- **Problem:** razlika originala, crystal i parent pogleda, očekivanih invarijanti i promene naboja već je dobro postavljena. Nema jednog celog pre/posle primera koji sve te odluke povezuje.
- **Zašto je teško:** čitalac može ponoviti „sačuvaj poreklo“, a ne jasno odrediti koja tvrdnja nakon uklanjanja komponente više ne važi.
- **Implicitno znanje:** task-specific transformacija, očuvani podgraf, namerno promenjen sastav i opseg uporedivosti.
- **Konkretna izmena:** hipotetički L·H₂O: prikaz originala i parent-only pogleda, očuvanih atoma L, uklonjene vode i veze ka originalu. U poređenju sa bezvodnim L, parent graf može biti isti dok puna forma time nije izjednačena. Ako se demonstrira neutralizacija, zasebno prikazati očekivani Δcharge; nije potrebno dodati sve varijante.
- **Značaj:** **koristan za poboljšanje**. Primer može biti početak zajedničkog slučaja koji se nastavlja kroz D01/D03.


## Nalazi: ML/AI osnove i metode

### M01 — Matematički uvod prelazi granicu deklarisanog početnog znanja

- **Gde:** [ML/00a-osnove-ml.md:3–5](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/00a-osnove-ml.md:3), [ML/00a-osnove-ml.md:46–98](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/00a-osnove-ml.md:46) i [ML/00a-osnove-ml.md:191–207](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/00a-osnove-ml.md:191).
- **Problem:** skalar, vektor, matrica, suma, norma i skalarni proizvod dobro su uvedeni. Ipak, od obećanja da su dovoljni razlomci brzo se prelazi na log/exp, SVD, gradijent i softmax. Naziv i kratka definicija nisu uvek dovoljni da se prati račun.
- **Zašto je teško:** čitalac prepoznaje simbol, ali ne ume da objasni kako promena njegovog argumenta menja gubitak, težinu ili koordinatu.
- **Implicitno znanje:** logaritmi/eksponencijale, matrično množenje, ortogonalnost i lokalna promena funkcije. Hemijska torzija dodatno pretpostavlja vektorski proizvod i trigonometrijsku notaciju.
- **Konkretna izmena:** osnovni blok zadržati za uzorak, reprezentaciju, jednostavan loss, split i prve metrike. Matematičke mostove otvarati pred konkretnom primenom: tabela −ln(p) za nekoliko p, dve softmax težine, jedno 2×2 množenje i link za vektorsku geometriju. SVD predstaviti kao alat za kasnije poravnanje; potpuna derivacija nije potrebna. Alternativa je jasnije navesti potrebna predznanja i precizno obavezno čitanje.
- **Značaj:** **važan** za deklarisanu početničku putanju.

### M02 — Treniranje modela nema mali primer stvarne promene parametra

- **Gde:** [ML/00a-osnove-ml.md:72–102](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/00a-osnove-ml.md:72) i [ML/02-classical-ml.md:55–74](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/02-classical-ml.md:55).
- **Problem:** model, loss, minimizacija i parametri jesu definisani. Primer klasičnog ML-a nabraja ulaze i target, ali ne pokazuje kako podaci određuju bolju vrednost parametra. Takav izvedeni primer nije nađen ni u detaljnim modulima 03–06.
- **Zašto je teško:** razlika između ručno postavljenog score-a i naučenog modela ostaje apstraktna. Kasniji metric-learning loss-evi naslanjaju se upravo na nju.
- **Implicitno znanje:** optimizacija na fiksnim trening podacima, primena zamrznute funkcije i razlika parametra od hiperparametra.
- **Konkretna izmena:** sintetički y≈wx sa 2–3 reda, dve težine i izračunatim prosečnim kvadratnim greškama. Zatim jedan korak promene w i odvojena test tačka. Ako se uvodi gradijent, može biti dat kao već izračunat broj uz objašnjenje smera; nije potrebno izvoditi diferencijalni račun. Na istom primeru odvojiti w od veličine koraka ili jačine regularizacije.
- **Značaj:** **važan** — jedan od prvih ML zahvata, sa velikim uticajem na naredne teme.

### M03 — Kod ansambala detalji biblioteka dolaze pre dovoljne intuicije osnovnog postupka

- **Gde:** [ML/02-classical-ml.md:103–167](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/02-classical-ml.md:103), posebno §2.5–2.6.
- **Problem:** stablo, bootstrap i OOB imaju kratka objašnjenja. Boosting dobija jednu uvodnu rečenicu, pa odmah slede histogrami, GOSS/EFB i ordered boosting. Bias/variance razlika RF/ExtraTrees ostaje nedemonstrirana.
- **Zašto je teško:** moguće je zapamtiti prednosti biblioteka bez razumevanja razlike između prosečavanja više stabala i sekvencijalne korekcije greške.
- **Implicitno znanje:** list i predikcija stabla, agregacija, rezidual i promenljivost modela pri promeni trening uzorka.
- **Konkretna izmena:** malo stablo sa dva uslova, predikcije tri stabla i njihov prosek; zatim, za kvadratni loss, red trenutna predikcija → rezidual → korekcija sledećeg stabla. Optimizacije biblioteka premestiti u opcioni okvir ili ih kratko definisati posle mehanike. [Zvanični scikit-learn prikaz ansambala](https://scikit-learn.org/stable/modules/ensemble.html) podržava ovu osnovnu podelu; nisu potrebne izvedene specifikacije tri biblioteke.
- **Značaj:** **važan** za argumentovan izbor klasične ML porodice.

### M04 — Kernel i latentne metode traže jasno označen dodatni matematički nivo

- **Gde:** [ML/02-classical-ml.md:169–225](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/02-classical-ml.md:169); uslov pozitivne semidefinitnosti već postoji i u [ML/04-precise-pairwise.md:413–419](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/04-precise-pairwise.md:413).
- **Problem:** kernel kao skalarni proizvod i PSD uslov nisu odsutni. Ipak, Gram matrica, varijansa/kovarijansa, projekcija i „raspodela nad funkcijama“ pretpostavljaju više od osnovnog uvoda. PCA→PCR i target-usmereni PLS sažeti su gotovo na naziv razlike.
- **Zašto je teško:** uslovi primenljivosti mogu se čitati kao reference, ali ne daju početniku dovoljno osnove da sam izabere kernel, latentnu komponentu ili protumači GP varijansu.
- **Implicitno znanje:** projekcija i latentni prostor, kovarijansa, Gram matrica, prior/posterior i modelna prediktivna varijansa.
- **Konkretna izmena:** za osnovnu putanju ove stavke jasno označiti kao referentne alternative. Pre njihove dublje obrade ponuditi mali zajednički most: 2–3 vektora i matrica skalarnih proizvoda; jedna 2D projekcija i PCA→regresija; za GPR skica funkcija pre/posle opažanja. PSD uslov povezati sa tom matricom. Ne zahtevati dokaz PSD-a, izvođenje GP posteriora ili novo obavezno poglavlje o svakoj metodi.
- **Značaj:** **koristan za osnovnu putanju; važan pre konkretne kernel/SOAP/GPR obrade**.

### M05 — Kalibracija objašnjava cilj, ali ne pokazuje nastanak kalibracione mape

- **Gde:** [ML/02-classical-ml.md:241–250](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/02-classical-ml.md:241), [ML/00a-osnove-ml.md:185–189](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/00a-osnove-ml.md:185) i [ML/06-metric-learning-and-evaluation.md:373–391](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:373).
- **Problem:** razlika score/verovatnoća/kalibracija i razdvajanje skupova vrlo su dobri. Platt, isotonic i temperature scaling uglavnom se pojavljuju kroz nazive i ograničenja; nije pokazan osnovni tok učenja dodatne mape nad izlazom zamrznutog modela.
- **Zašto je teško:** čitalac može objasniti zašto 0,8 nije dokaz dobre kalibracije, a ipak pomešati kalibrator sa izborom klasifikacionog praga.
- **Implicitno znanje:** drugi model nad izlazom prvog, empirijska učestalost, monotona transformacija i odluka na osnovu praga.
- **Konkretna izmena:** mala tabela score+label, ilustracija učestalosti i šema model → izdvojeni kalibracioni podaci → g(score) → finalni test. Pokazati imenovanu kalibracionu mapu ili jasno sintetičku ilustraciju njenog dejstva. Dve grupe empirijskih učestalosti same nisu demonstracija fitovanja Platt/isotonic modela. Posebno odvojiti podešavanje verovatnoće od odluke preko praga. [Zvanična dokumentacija o kalibraciji](https://scikit-learn.org/stable/modules/calibration.html) daje osnovu za taj tok.
- **Značaj:** **važan** pre upotrebe kalibracije i uzdržavanja u evaluacionom zaključku.

### M06 — Conformal predikcija je predstavljena kroz garanciju pre mehanizma

- **Gde:** [ML/02-classical-ml.md:254–263](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/02-classical-ml.md:254) i [ML/06-metric-learning-and-evaluation.md:389–391](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:389).
- **Problem:** exchangeability i marginalni coverage jesu navedeni. Nedostaje pokazivanje kako kalibracione greške postaju interval ili prediction set. Kratak opis je dovoljan za mapu alternativa, ali ne i za operativno tumačenje predloženog conformal sloja.
- **Zašto je teško:** interval za novu predikciju, interval poverenja prosečne metrike i coverage uzdržavanja mogu ostati pomešani.
- **Implicitno znanje:** kvantil, nonconformity mera i razlika neizvesnosti predikcije od neizvesnosti procene uspeha.
- **Konkretna izmena:** označiti temu kao uslovni nastavak. Pre stvarne obrade dati jedan split-conformal regresioni primer sa apsolutnim rezidualima, deklarisanim konačno-uzoračkim kvantilom i intervalom nove predikcije. Uz njega kratko razgraničiti pomenute intervale i coverage. Sačuvati pretpostavke i ograničenja iz teksta; [Shafer–Vovk tutorijal](https://jmlr.org/papers/v9/shafer08a.html) služi kao metodski oslonac, bez zahteva da se u kurs prenese dokaz teoreme.
- **Značaj:** **koristan za opštu putanju; važan ako se conformal sloj zaista razmatra**.

### M07 — Gain/gauge i zatvaranje putanje uvode novi periodični grafovski jezik bez mosta

- **Gde:** [ML/04-precise-pairwise.md:173–175](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/04-precise-pairwise.md:173), [ML/04-precise-pairwise.md:247–249](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/04-precise-pairwise.md:247) i [ML/04-precise-pairwise.md:464–473](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/04-precise-pairwise.md:464); potrebne formule tek u [ML/05-periodic-crystal-encoders.md:126–148](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/05-periodic-crystal-encoders.md:126).
- **Problem:** hemija već objašnjava ćeliju, wrapping i promenu baze. Novi pojmovi quotient/gain graf, vertex-wise gauge i cycle/path-sum nisu samo druga imena za tu osnovu. Njima se u §4.5–4.6 već obrazlažu matching i sastavljanje konačnog molekula, pre celovitog periodičnog modela u §4.8.
- **Zašto je teško:** običan ciklus u konačnom nacrtanom grafu može predstavljati fizički prsten ili put do periodične kopije. Bez te razlike čitalac ne razume finite-molecule unwrap i dimenzionalnost mreže.
- **Implicitno znanje:** orijentisana periodična ivica, izbor predstavnika čvora, zbir translacija duž putanje i rang nezavisnih translacionih pravaca.
- **Konkretna izmena:** pre §4.5 uvesti 1D ćeliju dužine L=1 u izabranoj jedinici: sᵢ=0,9, sⱼ=0,1 i n=1 daju displacement 0,2 u istoj jedinici; izbor s′ⱼ=1,1 zahteva n′=0 za isti kontakt. Prikazati tabelu ivica pre/posle, zatim ciklus sa zbirom 0 i putanju sa zbirom 1. Tek tada dati opštu formulu i 3D rang. Ne ponavljati kompletnu kristalografiju.
- **Značaj:** **kritičan za razumevanje periodične grafovske grane**, uključujući determinističko poređenje, a ne samo deep modele.

### M08 — Notacija grupa i pariteta dolazi pre kratkog pojmovnika

- **Gde:** [ML/05-periodic-crystal-encoders.md:45–51](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/05-periodic-crystal-encoders.md:45) i [ML/05-periodic-crystal-encoders.md:220–231](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/05-periodic-crystal-encoders.md:220); nastavak [ML/06-metric-learning-and-evaluation.md:235–246](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:235).
- **Problem:** invariansa i ekvivarijansa imaju početne definicije. Ipak, SE(3)×SE(3), E(3), O(3), 0e/0o i pseudoskalar uvode se naglo, bez jedne mape notacije.
- **Zašto je teško:** nije očigledno zašto zajednička rotacija oba ulaza predstavlja slabiji zahtev od nezavisne promene njihovih koordinatnih sistema. Specijalistička notacija može zakloniti jednostavniji stereo princip.
- **Implicitno znanje:** grupa transformacija, proper/reflection razlika, nezavisni izbor dve transformacije, paritet i pseudoskalar.
- **Konkretna izmena:** tabela O/SO/E/SE sa rotacijama, refleksijama i translacijama; objasniti da × ovde znači nezavisan izbor transformacije A i B. Jedan vektorski primer pokazuje kako rotacija samo A menja sirovi skalarni proizvod. Detalje 0e/0o i tenzorskih reprezentacija izdvojiti kao napredan okvir uz [e3nn definicije](https://docs.e3nn.org/en/stable/api/o3/o3_irreps.html). Ne izvoditi teoriju grupa.
- **Značaj:** **važan za geometrijsku/deep putanju**, bez blokiranja tabularne osnove.

### M09 — MCS varijante menjaju značenje, ali ostaju lista opcija

- **Gde:** [ML/04-precise-pairwise.md:183–217](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/04-precise-pairwise.md:183); osnovna razlika zadataka već postoji u [hemija/15-slicnost.md:17–24](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/15-slicnost.md:17).
- **Problem:** induced/non-induced, connected/disconnected i complete-rings/ring-fusion navode se kao obavezne odluke bez minimalnog objašnjenja njihovog efekta. Osnovni exact/subgraph/MCS pojmovi i timeout ograničenje jesu pokriveni.
- **Zašto je teško:** opcije mogu izgledati kao podešavanja brzine, iako menjaju samo pitanje i dopušteni zajednički podgraf.
- **Implicitno znanje:** indukovani podgraf, povezanost, očuvanje prstena i ekvivalentnost različitih mapiranja.
- **Konkretna izmena:** tabela „odluka → dopušteno podudaranje → posledica“ i dva mala crteža: dodatna ivica između mapiranih čvorova i povezano/nepovezano jezgro. Završiti jednim mapiranjem i pokrivenošću obe strane. Naprednu enumeraciju i granice optimuma premestiti iza tog primera; ne uvoditi implementaciju VF2.
- **Značaj:** **važan**, jer pripada semantici centralne determinističke metode.

### M10 — SOAP/REMatch preskače put od lokalnog okruženja do globalne sličnosti

- **Gde:** [ML/04-precise-pairwise.md:398–419](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/04-precise-pairwise.md:398), §4.10.
- **Problem:** jedna uvodna celina prelazi od glatke atomske gustine i power spectrum-a do entropijski regularizovanog matching-a i Sinkhorn metode. Potom slede vrlo precizna ograničenja PSD-a i adapted-average konstrukcije. Nije prethodno nacrtano šta se lokalno kodira, a šta globalno agregira.
- **Zašto je teško:** čitalac može znati parametre i zabrane, a ne razlikovati prosečavanje lokalnih sličnosti od mekog uparivanja okruženja.
- **Implicitno znanje:** zaglađivanje, lokalni descriptor, kernel, matrica sličnosti, meka dodela i regularizacija entropijom. PSD uslov već postoji; potrebno je pravovremeno povezivanje sa M04.
- **Konkretna izmena:** šema okruženje → lokalni vektor → matrica sličnosti svih centara → globalna agregacija. Dve strukture sa po dva centra i izmišljena 2×2 matrica dovoljne su da se objasni razlika agregatora. [Zvanični DScribe opis SOAP-a](https://singroup.github.io/dscribe/latest/tutorials/descriptors/soap.html) daje osnovu za lokalni deo. Sinkhorn iteracije ne treba izvoditi, a posebna ograničenja adapted-average rada treba sačuvati u naprednom delu.
- **Značaj:** **važan pre obrade ove opcione porodice**; nije razlog da se odlaže rad sa drugim validnim metodama poređenja.

### M11 — Mehanika ANN aproksimacije kraća je od njenih memorijskih i audit detalja

- **Gde:** [ML/03-global-retrieval-ann-ranking.md:236–318](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:236), §3.7–3.9.
- **Problem:** HNSW ima vrlo kratak opis kretanja po grafu; IVF/PQ brzo uvode centroid, inverted list, codebook i residual; MinHash/LSH potpis i izbor kandidata ostaju sažeti. Memorija i validacija su znatno detaljniji. Definicija ANN-a i njegova razlika od stručne relevantnosti već su dobre.
- **Zašto je teško:** čitalac može računati bajtove ili menjati nprobe, a ne jasno objasniti u kom koraku pravi sused nestaje iz rezultata.
- **Implicitno znanje:** particionisanje prostora, predstavnik vektora, rezidual, potpis skupa i hash-bucket izbor.
- **Konkretna izmena:** jedna zajednička slika sa malim skupom tačaka: exact pregleda sve; HNSW prati veze; IVF otvara grupe; PQ menja vektor predstavnikom. Ako se MinHash/LSH obrađuje, dodati samo mali skup i nekoliko unapred zadatih permutacija za potpis, pa odvojiti izbor kandidata. [Izvorni MHFP rad](https://link.springer.com/article/10.1186/s13321-018-0321-8) podržava tu razliku. Ne dodavati katalog novih indeksa.
- **Značaj:** **važan za izbor infrastrukture globalne pretrage**; postojeće oracle i recall objašnjenje treba očuvati.

### M12 — „Pairwise“ označava različite jedinice u poređenju i rangiranju

- **Gde:** [ML/03-global-retrieval-ann-ranking.md:435–464](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:435) i [ML/06-metric-learning-and-evaluation.md:134–143](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:134); početna osnova [ML/00a-osnove-ml.md:16–28](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/00a-osnove-ml.md:16).
- **Problem:** tekst tačno razlikuje query–candidate red i preferenciju P(i≻j|q). Ipak, nema zajedničkog malog prikaza tri značenja: par kristala u App 2, jedan kandidat uz query i dva kandidata poređena za isti query.
- **Zašto je teško:** labele neuređenih parova mogu se pogrešno smatrati gotovim ranking preferencijama; termini su slični, a jedinica supervizije drugačija.
- **Implicitno znanje:** query grupa, preferencija, lista i razlika gubitka po redu od gubitka poretka.
- **Konkretna izmena:** isti Q i A/B/C sa ocenama 2/1/0 prikazati kao tri pointwise reda, tri preferencije i jednu listu. Navesti ulaz u loss i izlaz modela za svaku varijantu. Poređenje A–B iz App 2 označiti zasebno. Pre LambdaMART-a linkovati osnovu boostinga.
- **Značaj:** **koristan za poboljšanje**; definicija već postoji, potrebno je pokazati prelaz jedinice podatka.

### M13 — Katalog crystal modela prethodi jednom praćenom GNN prolazu

- **Gde:** [ML/00a-osnove-ml.md:191–207](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/00a-osnove-ml.md:191), [ML/05-periodic-crystal-encoders.md:59–72](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/05-periodic-crystal-encoders.md:59) i [ML/05-periodic-crystal-encoders.md:233–292](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/05-periodic-crystal-encoders.md:233).
- **Problem:** message passing, pooling i attention imaju definicije. Nije prikazan jedan mali tok čvor/ivica → poruka → agregacija → readout, kojim bi poređenje distance-only, angle-aware i line-graph porodica dobilo zajedničku osnovu.
- **Zašto je teško:** katalog modela i benchmarka može se zapamtiti bez jasne predstave koji deo reprezentacije svaka porodica menja.
- **Implicitno znanje:** lokalno stanje, domet poruke, readout i konstrukcija grafa čiji su čvorovi prethodne ivice.
- **Konkretna izmena:** mali metal sa tri donora, jednostavne ručno zadate osobine i jedan obrazovni korak poruke/sabiranja. Potom dve metal–donor ivice prikazati kao čvorove line grafa povezane uglom. Jasno označiti da to nije reprodukcija CGCNN/ALIGNN-a. Uz svaku arhitekturu referencirati korak koji ona menja, umesto novih formula svih originalnih modela.
- **Značaj:** **važan za deep putanju**; nije obaveza za čitaoca koji se zadržava na tabularnim metodama.

### M14 — Loss formule nemaju prvi izvedeni primer, a deo oznaka ostaje neobjašnjen

- **Gde:** [ML/06-metric-learning-and-evaluation.md:95–143](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:95) i [ML/06-metric-learning-and-evaluation.md:168–183](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:168).
- **Problem:** contrastive loss definiše marginu kratko; triplet prikazuje uslov, bez samog hinge gubitka i lokalne legende a/p/n. Semi-hard se koristi bez prikaza, a τ u InfoNCE formuli nije imenovano na mestu upotrebe. Nijedan od ova tri postupka nema mali numerički račun.
- **Zašto je teško:** čitalac može pratiti zabranu lažnih negativa, a ne znati kada je kazna nula ili kako temperatura menja raspodelu težina.
- **Implicitno znanje:** aktivna margina, anchor/positive/negative, kvadrirano rastojanje, softmax temperatura i izbor teških negativa prema trenutnom modelu.
- **Konkretna izmena:** po jedan mali positive/negative račun; triplet oblik `max(0,d(a,p)²−d(a,n)²+m)` sa legendom i easy/semi-hard/hard prikazom; mali InfoNCE batch uz dve τ>0 vrednosti. Razlikovati trening temperaturu od kasnije kalibracione temperature. Osnovu daju [FaceNet](https://arxiv.org/html/1503.03832v3) i [CPC/InfoNCE rad](https://arxiv.org/html/1807.03748v2). Zadržati postojeće pažljivo pravilo denominatora; ne izvoditi celu mrežu.
- **Značaj:** **važan pre samostalnog obrazlaganja metric-learning metode**.

### M15 — „Metric-consistency audit“ nema objašnjen minimalni postupak

- **Gde:** [ML/06-metric-learning-and-evaluation.md:31–48](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:31), [ML/06-metric-learning-and-evaluation.md:128–143](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:128) i [ML/06-metric-learning-and-evaluation.md:85–91](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:85).
- **Problem:** opravdano se traži provera da target odgovara globalnom prostoru rastojanja, ali naziv audita ne govori koje odnose čitalac treba da proveri. Posebno treba razdvojiti ekvivalencijske klase od pragovske relevantnosti.
- **Zašto je teško:** iz opreza prema netranzitivnoj relevantnosti može se izvesti prejak zaključak da svaka takva relacija isključuje metričko rangiranje. Na pravoj sa tačkama 0, 0,6 i 1,2 i pragom 1, bliskost je netranzitivna iako je rastojanje metričko. To je ilustracija razlike pojmova, ne tvrdnja da tekst daje pogrešnu teoremu.
- **Implicitno znanje:** ekvivalencija, tranzitivnost, trougaona nejednakost, prag, preferencija i kompatibilnost ograničenja.
- **Konkretna izmena:** tri mala primera: dosledne klase, query-zavisna preferencija i pragovska bliskost. Minimalna kontrola: imenovati target i smer; proveriti simetriju; kod klasa proveriti zatvaranje/tranzitivnost; kod distance/margina proveriti sukob ograničenja. Objasniti da ovo nije opšti dokaz postojanja embedding-a željene dimenzije. Pair/query model zatim postaje obrazložena alternativa.
- **Značaj:** **važan za izbor između globalnog embedding-a i direktnog modela odnosa**.

### M16 — PU learning je uveden kroz pretpostavke pre osnovnog modela označavanja

- **Gde:** [ML/06-metric-learning-and-evaluation.md:168–183](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:168), naročito poslednji pasus; nagoveštaj [ML/03-global-retrieval-ann-ranking.md:496–506](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:496).
- **Problem:** „neocenjeno nije negativno“ odlično je objašnjeno. Ponuđena PU alternativa odmah koristi SCAR/SAR, selection propensity, class prior i identifikabilnost, bez razdvajanja stvarne klase od činjenice da je labela uopšte dobijena.
- **Zašto je teško:** verovatnoća relevantnosti može se pomešati sa verovatnoćom da je ekspert izabrao zapis za anotaciju.
- **Implicitno znanje:** indikator anotacije, selekcioni mehanizam, prevalenca i uslovi identifikacije.
- **Konkretna izmena:** osnovnom toku ostaviti uslovnu mogućnost PU učenja. U naprednom okviru uvesti dve promenljive — stvarna relevantnost i dostupna anotacija — razvezati SCAR/SAR i dati primer da su eksperti birali pretežno visok Tanimoto. Ako se taj nivo neće obrađivati, dati precizno spoljašnje čitanje umesto neobjašnjene obaveze.
- **Značaj:** **koristan za poboljšanje**, uslovna grana koja ne treba da blokira osnovnu teoriju.

### M17 — bpref i condensed evaluacija pojavljuju se bez objašnjenja efekta

- **Gde:** [ML/03-global-retrieval-ann-ranking.md:559–571](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:559), deo o nepotpunim qrels.
- **Problem:** pool, slepa anotacija, relevantni i neocenjeni kandidati dobro su razdvojeni. Zatim se zahteva bpref/condensed analiza osetljivosti bez definicije šta se tim računom menja.
- **Zašto je teško:** čitalac ne zna da li neocenjeni rezultat ostaje na listi, izostavlja se pri računu ili dobija nulu, i kakav zaključak zavisi od te politike.
- **Implicitno znanje:** selektovane relevance ocene, kondenzovanje liste i analiza osetljivosti na nepoznate oznake.
- **Konkretna izmena:** jedna rang-lista sa relevantnim, nerelevantnim i neocenjenim kandidatom; pokazati efekat dve politike. Jednom rečenicom definisati svrhu bpref-a i condensed varijante, uz ograničenje da ne rekonstruišu nepoznatu punu relevantnost. Alternativno ih označiti kao naprednu referencu, umesto osnovne obaveze.
- **Značaj:** **koristan za poboljšanje**, naročito pri stvarnom radu sa nepotpunim anotacijama.

## Nalazi: organizacija oba kursa

### J01 — Postojeće putanje treba usaglasiti i obeležiti lokalne preduslove

- **Gde:** [ML/11-ml-ai-plan-ucenja.md:31–48](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/11-ml-ai-plan-ucenja.md:31), detaljnije [ML/11-ml-ai-plan-ucenja.md:161–209](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/11-ml-ai-plan-ucenja.md:161), [hemija/plan-ucenja.md:3–25](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/plan-ucenja.md:3) i navigacija obe knjige.
- **Problem:** plan za početnika i O/P/R nivoi već postoje. Sidebar, glavna tabela i detaljni odeljci ipak ne pokazuju svuda isti redosled. Glavna tabela čita kompletan pairwise i retrieval/LTR pre klasičnog ML-a; detaljni plan na liniji 203 već izvlači §6.8–6.12 evaluacije pre encodera. Rani „orijentacioni“ prolaz kroz algoritamsku mapu nema uvek tačno označen kraj. Hemijska putanja ima opšti link, ali nema dosledne lokalne povratne mostove ka ML uvodu.
- **Zašto je teško:** čitalac koji prati meni mora sam razlikovati pojmove koje sada samo prepoznaje od postupaka koje već treba da ume da izvede.
- **Implicitno znanje:** samostalno usklađivanje nastavne putanje, reference i preskakanja po prethodnom znanju.
- **Konkretna izmena:** jedan kanonski početnički sled sa tačnim odeljcima; brza putanja za iskusnog ML čitaoca. U ranoj mapi označiti „samo orijentacija“. Pre supervised LTR-a linkovati osnovu učenja i boostinga; pre SOAP-a kernel most. U glavnu tabelu preneti već postojeći raniji korak grupne evaluacije. U hemiji 14/18/20/22 dodati po jednu konkretnu liniju ML preduslova. Sa H06 uskladiti i dve kapije poglavlja 7.
- **Značaj:** **važan** za povezanu celinu; ne zahteva novi plan od početka.

### J02 — Razdvojiti lekciju, referentni inventar i napredne kontrolne liste

- **Gde:** [hemija/17-lokalni-skup.md:1–6](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/17-lokalni-skup.md:1) i [hemija/17-lokalni-skup.md:536–538](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/17-lokalni-skup.md:536), [hemija/22-whitepaper-tokovi-fl.md:63–126](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/22-whitepaper-tokovi-fl.md:63), [ML/03-global-retrieval-ann-ranking.md:666–738](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:666), [ML/06-metric-learning-and-evaluation.md:501–556](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:501); primer metateksta [hemija/18-globalna-pretraga.md:55–74](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/18-globalna-pretraga.md:55).
- **Problem:** obavezno gradivo uključuje detaljan lokalni inventar i uslovne teme, dok završne matrice, anti-patterni i kriterijumi često ponavljaju iste zahteve. Više puta se ponavlja i urednička ograda da primer nije data schema, implementacija ili rollout plan. Kontrole jesu korisne; neujednačena je pažnja koju dobijaju naspram samog mehanizma metode.
- **Zašto je teško:** dužina može delovati kao dubina objašnjenja. Početnik troši pažnju na ponovljene ograde i podatke konkretnog snapshot-a, dok assignment ili loss još nije izveo ni jednom. Tekst ne traži memorisanje svih brojeva; problem je nedovoljno vidljiva razlika nivoa.
- **Implicitno znanje:** ekspertno selektivno čitanje i prepoznavanje šta je trajni princip, a šta referenca.
- **Konkretna izmena:** na početku 17 izdvojiti ključne pouke, a numeričke inventare označiti kao referencu. U 22 razdvojiti razumevanje razloga za uslovni FL od njegovog naprednog statističkog/bezbednosnog nastavka. U ML lekciji pratiti pitanje → primer → mehanizam → specifična granica; završnu kontrolnu listu povezati linkovima umesto ponavljanja. Opštu ogradu „nije implementaciona specifikacija“ zadržati jednom, a lokalno samo gde primer zaista može biti pogrešno shvaćen.
- **Značaj:** **koristan za poboljšanje**; samo uklanjanje suvišnog metateksta je manja redakcijska izmena.

### J03 — Višeznačni coverage treba dosledno kvalifikovati

- **Gde:** [hemija/19-parovi.md:99–110](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/19-parovi.md:99), [hemija/20-evaluacija.md:143–158](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/20-evaluacija.md:143); već dobro opšte razgraničenje [ML/00a-osnove-ml.md:185–189](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/00a-osnove-ml.md:185).
- **Problem:** ista reč može značiti pokrivenost mapiranih atoma, dostupnost reprezentacije ili udeo slučajeva na koje sistem odgovara. Definicije zaista postoje, ali kvalifikator nije dosledan pri svakoj promeni jedinice analize.
- **Zašto je teško:** visok atom coverage ne znači visok udeo odgovorenih upita niti nizak rizik među odgovorima.
- **Implicitno znanje:** praćenje promene brojioca, imenioca i jedinice analize iz samog konteksta.
- **Konkretna izmena:** koristiti „pokrivenost mapiranja“, „dostupnost reprezentacije“ i „udeo odgovorenih slučajeva“, uz kratku tabelu brojilac/imenilac u rečniku. Pri mapiranju izričito navoditi obe strane kada su različite veličine. Nije potrebno novo poglavlje o coverage-u.
- **Značaj:** **manja pedagoška/terminološka sugestija**.

## Šta zaista nedostaje od osnove, a šta prvenstveno treba premestiti

| Vrsta praznine | Konkretna mesta | Potrebna intervencija |
|---|---|---|
| Osnovni misaoni korak nije lokalno izveden | Lewis/valentni elektroni (H01), π brojanje (H02), treniranje (M02), graf→fingerprint (D03) | Po jedan kratki proračun; jasno obavezno spoljno čitanje prihvatljivo je tamo gde daje baš taj ishod. |
| Novi stručni jezik nema dovoljnu uvodnu osnovu | orbitalni minimum (H04), gain/gauge/cycle sums (M07), MCS varijante (M09) | Mali pojmovnik vezan za nacrtan primer pre upotrebe. |
| Formula postoji, a fizičko ili algoritamsko značenje ostaje tanko | LJ/Coulomb (H07), H/S/G (H10), ansambli (M03), loss (M14) | Legenda i tumačenje promene ulaza/parametra; postojeće formule uglavnom sačuvati. |
| Objašnjenje postoji kasnije ili rasuto | periodični kontakti (H06), donor značenja (H03), kernel/PSD (M04/M10), grupna evaluacija u planu (J01) | Promena redosleda i precizni linkovi, bez kopiranja celih blokova. |
| Pravila su dobra, ali nema kompletne demonstracije | standardizacija (D04), assignment (D01), grupna evaluacija (D02), kalibracija (M05), HBP grouping (H11) | Jedan slučaj sa ulazom, međukorakom i ograničenim zaključkom. |
| Napredna alternativa može ostati kratka ako je tako označena | GPR/PLS/kernel produbljivanje (M04), conformal (M06), PU (M16), bpref (M17), specijalistički paritet (M08) | Referentni nivo i tačni preduslovi; dublji most tek kada se bira ta grana. |

## Gde je tekst nepotrebno težak

Nepotrebna težina ne potiče iz same teme, već iz rasporeda i gustine novih pojmova. Posebno su opterećeni:

| Segment | Šta otežava čitanje | Šta sačuvati i kako rasteretiti |
|---|---|---|
| Hemija 5, ligandno polje | stručna tabela prethodi orbitalnim kutijama i OS bilansu | Sačuvati elektronske razlike; uvesti minimum i promeniti redosled. |
| Hemija 7, kristalografski most | više novih objekata i matrica pre intuicije ćelije | Sačuvati puni periodični račun posle 8–9. |
| Hemija 8–9, promene ćelije | koseti/podrešetka pre primera atomskih kopija | Sačuvati opšti formalizam posle 2×1×1 primera. |
| ML 04, assignment/gain/SOAP | mnogo naprednih pravila pre prvog kompletnog elementarnog primera | Sačuvati uslove primenljivosti kao drugi nivo čitanja. |
| ML 05, simetrijske reprezentacije | grupa, gauge, paritet i tensor notacija u kratkim pasusima | Najpre fizička transformacija i očekivani rezultat; notaciju vezati za nju. |
| ML 06, loss/PU/kalibracija | slični statistički nazivi imaju različite uloge | Pokazati ulaz, ono što se uči i izlaz; napredne alternative obeležiti. |
| Završeci više poglavlja | ponavljanje inventara, ograda i kontrolnih lista | Jedna pregledna referenca sa preciznim vezama ka objašnjenjima. |

Ne preporučujem uklanjanje razlika između ASU i ćelije, proper rotacije i refleksije, molekula i periodične mreže, tri nivoa retrieval evaluacije ili različitih split režima. Ta složenost je potrebna da bi projektni zaključci imali jasno značenje.

## Povezana mapa preduslova

Sledeći sled opisuje učenje, ne redosled implementacije proizvoda:

1. **Hemijski jezik:** atom/formula → valentni elektroni i Lewis → formalni naboj, σ/π i rezonanca → organsko okruženje i dva značenja donora.
2. **Koordinaciona osnova:** ligand/komponenta → CN i denticitet → bilans oksidacionog stanja → dⁿ i orbitalni minimum → geometrija/distorzija → DAP motiv i dokaz direktne koordinacije.
3. **Periodični objekat:** fizičke interakcije → ćelija/koordinate → simetrija/ASU → periodični kontakti → difrakcija i kvalitet → čvrste forme i referentni signali.
4. **Digitalni pogled:** formati → namenska standardizacija → graf → fingerprint → sličnost. Pre algoritamskog dela uvesti osnovni ML uzorak, target, loss, split i metrike iz 00a.
5. **Precizni dokaz:** uloge komponenti → globalni assignment → atom mapping/MCS → konačni ili periodični grafovski status → mapirana geometrija → packing/interakcioni dokaz. Kernel/SOAP je jasno označena napredna grana.
6. **Pretraga i učenje:** isti graf/fingerprint → exact oracle → ANN mehanika → više kanala → stručne query ocene → jedinica ranking supervizije → jednostavno učenje/boosting pre LTR-a.
7. **Naučna procena:** target i nezavisne grupe → split prema tvrdnji → metrike i uparena procena → kalibracija/uzdržavanje. Ovaj blok treba da prethodi završnim tvrdnjama i izboru složenijeg modela, kako detaljni plan delimično već nalaže.
8. **Uslovni deep nastavak:** periodični graf → jedan message-passing primer → nezavisne transformacije/stereo → odnos targeta i metrike → loss/mining → poređenje encodera. SLM/RAG, spoljni API i FL dolaze prema njihovoj zasebnoj ulozi.

Od čitaoca se ne traži da u najranijem prolazu savlada svaku stavku kasnijeg bloka. Rane mape služe orijentaciji; precizne kapije treba vezati za već uvedene preduslove.

## Konkretan plan izmena po prioritetu

U izveštaju je **35 jedinstvenih nalaza**. Preklapanja iz hemije i ML-a objedinjena su: assignment, statistički most, nastanak fingerprint-a i navigacija nisu brojani dvaput. Tri nalaza označena su kao kritična za odgovarajuću početničku granu: H04, H06 i M07. To nisu tri dokazane naučne greške.

| Red | Paket izmena | Nalazi | Konkretan izlaz | Provera da je promena uspela |
|---:|---|---|---|---|
| 1 | Uskladiti preduslove i obavezne kapije | H04, H06, M07, J01 | orbitalni minimum i raniji OS; dva prolaza kroz 7; periodični grafovski most pre 4.5; usaglašen plan | Početnik može da prati sekvencu bez obaveznog skakanja u neoznačeno buduće poglavlje. |
| 2 | Popuniti osnovne hemijske i ML međukorake | H01, H02, H03, H07, M01, M02, M03 | Lewis primer; π brojanje; dva donora; legende potencijala; mali primer učenja i ansambla | Čitalac rešava novu malu varijantu, a ne samo ponavlja gotovu definiciju. |
| 3 | Dovršiti centralni dokaz i evaluaciju | D01, D02, M05, M09, M12 | assignment matrica i atom-map; MCS varijante; grupna/uparena procena; kalibrator; query-jedinice | Za isti sintetički skup ume da objasni izbor mapiranja, uzorak, labelu, procenu i granicu zaključka. |
| 4 | Povezati fizičke i reprezentacione primere | H08, H09, H10, H11, D03, D04, M11 | superćelija sa atomskim kopijama; SCXRD/PXRD uvod; H/S intuicija; grouping; graf→bit; pre/posle pogled; ANN slika | Ume da predvidi šta se menja, a šta ostaje isto pri jednoj kontrolisanoj promeni. |
| 5 | Pripremiti napredne grane samo prema potrebi | M04, M06, M08, M10, M13, M14, M15, M16, M17 | označeni preduslovi i kratki kernel/GNN/loss primeri; referentni PU/conformal/qrels nastavci | Čitalac obrazlaže izabranu porodicu i njene pretpostavke; ne mora znati sve alternative napamet. |
| 6 | Završna redakcija i provera usklađenosti | H05, J02, J03 | prevod mehanističkih termina ili opcioni okvir; uklonjen suvišan metatekst; kvalifikovan coverage | Novi primeri nisu udvostručeni, kapije odgovaraju gradivu, a pojmovi zadržavaju isto značenje. |

Prva tri paketa daju najveći doprinos pre nastavka teorijskog rada koji treba samostalno da koristi početnik. Ako projekat u određenoj fazi ne koristi deep, SOAP, PU ili conformal pristup, razrada tih opcija ne treba da odlaže razumevanje i upotrebu osnovnih metoda. M07, za razliku od većeg dela deep bloka, potreban je i za determinističku periodičnu grafovsku analizu.

## Jedan zajednički primer može zameniti više nepovezanih dopuna

Umesto dodavanja nove priče uz svaki nalaz, predlažem mali jasno sintetički skup od 4–6 zapisa sa imenovanim molekulskim/komponentnim odnosima: isti parent u dva zapisa, jedna promena koordinacije, jedan primer sa vodom i jedna promena pakovanja. Ne treba izmišljati eksperimentalne podatke niti predstavljati te zapise kao stvarne forme.

| Korak primera | Šta prikazati | Koji jaz zatvara |
|---|---|---|
| Original i namenski pogled | koji atomi/komponente ostaju i koje tvrdnje se ograničavaju | D04 |
| Graf i jedan fingerprint korak | promena lokalnog okruženja → promena koda/bita | D03 |
| Dve višekomponentne strukture | matrica dozvoljenosti/troška → assignment → atom mapping | D01, M09 |
| Jedan query i kandidati | reference, kandidati, stručne ocene i izgubljen relevantan rezultat | M11, M12; oslonac na već dobre recall primere |
| Zamrznuti dokaz i naučeni model | ulazni feature nije isto što i target; mala promena parametra | M02, M03 |
| Zaseban mali skup grupa za evaluaciju | isto resamplovanje oba metoda i tumačenje razlike | D02, M05 |

Za statistički deo koristiti jasno izmišljene rezultate po grupama. Mali broj struktura/parova iz nastavne priče **nije dovoljan da demonstrira stvarnu statističku pouzdanost intervala ili kalibracije**. Primer pokazuje račun i logiku; validna procena u projektu zahteva odgovarajuće nezavisne podatke i protokol.

Zajednički primer treba da ima jednu matičnu stranu, a lekcije da upućuju na odgovarajući korak. Tako se smanjuje, umesto povećava, količina ponavljanja.

## Delovi koji su već dovoljno dobro objašnjeni

| Oblast | Konkretna mesta | Šta vredi očuvati bez dodatnog opšteg proširivanja |
|---|---|---|
| Sastav, graf i digitalna dodela | hemija 1–2 i 5 | Ime fajla nije sastav; formula nije graf; formalni i parcijalni naboj nisu ista veličina. Nitro-primer dobro vezuje rezonancu i problem izvoza. |
| Molekulska geometrija | hemija 3 | VSEPR domen/oblik, konstitucija/konfiguracija/konformacija, torziona konvencija i degenerisani slučaj. Ne treba puna derivacija SVD-a. |
| Koordinacija i DAP | hemija 5–6, ML 01/03/04 | CN nije broj liganada; potencijalni donor nije dokazana koordinacija; 4M u zapisu nije M–DAP veza. Orbitalna dopuna ne poništava ovaj kvalitet. |
| Koordinate i kristalografija | hemija 8–9, 12A | CIF→Cartesian račun, jedinice, ASU, četiri simetrijska položaja, specijalne pozicije i Z/Z′. Dopuniti konstruktivnu transformaciju, ne ponavljati postojeći račun. |
| Kvalitet eksperimentalnog modela | hemija 10 | R/wR/GoF, podskupovi refleksija, s.u., occupancy, constraint/restraint i checkCIF granice. Pojednostavljenje jednim quality pragom bilo bi pogoršanje. |
| Čvrste forme i referentni signali | hemija 11–11A | Identiteti se razlikuju i kategorije kombinuju; ΔG račun ima uslove; percentil/MAD i kružnost imaju primere; outlier/propensity nisu energija ili dokaz polimorfa. |
| Formati i izvorni/purpose pogledi | hemija 12/12A/13/17; ML 09 | Sintetički CIF, scalar/loop/missing tokeni, gubici veza i periodičnog konteksta, autoritet po polju, status naspram nule. Ne dodavati još jedan opšti CIF uvod. |
| Osnovne mere i retrieval granice | hemija 15/18/20; ML 00a/03 | Tanimoto, normalizacija, nulti denominator, nDCG primer; exact oracle naspram stručnog gold-a; reranker ne vraća izgubljenog kandidata. |
| Pairwise naučni dokaz | hemija 19; ML 04 | Mapping pre RMSD-a, pokrivenost obe strane, refleksija, status svake grane i full all-pairs naspram candidate-pruned režima. |
| Split i lažne labele | ML 00a/02/06/09 | Isti objekat u više formata, endpoint leakage, cold/cold i warm/cold, legitimni warm/warm, temporalni odnos i pretraining overlap; preširoki split može ukloniti sve pozitivne. Nedostaje ilustracija, ne novo opšte pravilo. |
| Nedostajući podaci | ML 00a/09 i hemija 17 | Train-only transformacije, one-hot/scaling razlika, MCAR/MAR/MNAR ograničenja, dostupnost nije naučna labela i source/missingness prečice. |
| Jezički sloj | ML 07–08 | Text RAG nije crystal embedding; BM25/RRF imaju legende; schema-valid nije semantički tačno; model objašnjava proverljive rezultate. Ne treba katalog novih LLM providera ili potpuna LoRA derivacija za ovu ulogu. |
| FAIR, poreklo i uslovni FL | hemija 21–22; ML evidence-method/08/09/10 | FAIR nije automatski otvoreno; prava, kvalitet i lifecycle su različite ose; vendor okvir nije projektni dokaz; FedAvg već ima formulu, legendu i primer. Dalja ponavljanja tih ograda malo bi doprinela. |

Procena tih oblasti znači da su dovoljno objašnjene za deklarisanu ulogu u teorijskom okviru. Ne predstavlja potvrdu svih empirijskih podataka, benchmark tvrdnji ili promenljivih uslova spoljnih alata.

## Kriterijumi za završenu reviziju teorije

Revizija je uspešna kada novi čitalac, uz označene preduslove, može da:

1. izvede jednostavan hemijski ili numerički primer koji nije identičan datom rešenju;
2. objasni šta svaki korišćeni simbol, objekat i imenilac znače na mestu prve ozbiljne upotrebe;
3. prati isti objekat kroz originalni podatak, namenski pogled, izračunati dokaz, feature i ciljnu ocenu;
4. razlikuje izmenu zapisa od fizičke promene i prikaže očekivani ishod jednog takvog primera;
5. obrazloži izbor mapiranja, trening jedinice i evaluacionog skupa pre izbora složenijeg modela;
6. prepozna šta mora da zna sada, a šta je referentna ili uslovna napredna tema.

Svaku dopunu treba proveriti i naspram rešenja, rečnika i kapija. Ako se uvede novi primer, a kriterijum i dalje traži drugu, neobjašnjenu sposobnost, problem nije završen. Ako je potreban međukorak već negde dobro napisan, najpre promeniti redosled ili link umesto dodavanja njegove druge verzije.


## Popis pregledanog izvornog sadržaja

Popis označava pokrivenost čitanjem, ne broj nađenih grešaka. Osnovni pregledi urađeni su paralelno po celinama; zajednički preduslovi i preklopljeni nalazi zatim su provereni i objedinjeni. Bibliografske strane su pročitane kao deo dokumentacije; svi spoljni radovi nisu ponovo pregledani u celosti.

### Hemijski deo

| Izvorni fajl | Linije | Tema |
|---|---:|---|
| [hemija/01-atomi-joni-formule.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/01-atomi-joni-formule.md:1) | 107 | 1. Atomi, elementi, joni i formule |
| [hemija/02-veze.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/02-veze.md:1) | 127 | 2. Elektroni i hemijske veze |
| [hemija/03-geometrija.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/03-geometrija.md:1) | 141 | 3. Molekulska geometrija i konformacija |
| [hemija/04-organska.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/04-organska.md:1) | 132 | 4. Organska hemija koja nam treba |
| [hemija/05-kompleksi.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/05-kompleksi.md:1) | 366 | 5. Metali, ligandi i kompleksi |
| [hemija/06-dap-schiff.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/06-dap-schiff.md:1) | 299 | 6. DAP Schiff-base motiv u ovom skupu |
| [hemija/07-interakcije.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/07-interakcije.md:1) | 367 | 7. Intermolekulske interakcije |
| [hemija/08-celija.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/08-celija.md:1) | 570 | 8. Kristal, rešetka i jedinična ćelija |
| [hemija/09-simetrija.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/09-simetrija.md:1) | 532 | 9. Simetrija, prostorne grupe i periodičnost |
| [hemija/10-difrakcija-kvalitet.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/10-difrakcija-kvalitet.md:1) | 456 | 10. Difrakcija, refiniranje i kvalitet |
| [hemija/11-cvrste-forme.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/11-cvrste-forme.md:1) | 384 | 11. Polimorfi i druge čvrste forme |
| [hemija/11a-referentne-raspodele-hbp.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/11a-referentne-raspodele-hbp.md:1) | 217 | 11A. Referentne raspodele, Mogul i hydrogen-bond propensity |
| [hemija/12-formati.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/12-formati.md:1) | 175 | 12. CIF, MOL, MOL2, SDF i SMILES |
| [hemija/12a-anatomija-cif.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/12a-anatomija-cif.md:1) | 164 | 12A. Anatomija jednog CIF fajla |
| [hemija/13-standardizacija.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/13-standardizacija.md:1) | 154 | 13. Standardizacija bez gubitka značenja |
| [hemija/14-reprezentacije.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/14-reprezentacije.md:1) | 154 | 14. Molekul kao graf i skup deskriptora |
| [hemija/15-slicnost.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/15-slicnost.md:1) | 142 | 15. Sličnost nije jedna veličina |
| [hemija/16-csd-conquest.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/16-csd-conquest.md:1) | 122 | 16. CSD i ConQuest tok podataka |
| [hemija/17-lokalni-skup.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/17-lokalni-skup.md:1) | 552 | 17. Forenzika dostavljenog skupa |
| [hemija/18-globalna-pretraga.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/18-globalna-pretraga.md:1) | 111 | 18. Globalna pretraga: teorijski okvir |
| [hemija/19-parovi.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/19-parovi.md:1) | 188 | 19. Precizno poređenje parova |
| [hemija/20-evaluacija.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/20-evaluacija.md:1) | 198 | 20. Evaluacija i naučna validacija |
| [hemija/21-licence-fair.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/21-licence-fair.md:1) | 236 | 21. Licence, FAIR i poreklo podataka |
| [hemija/22-whitepaper-tokovi-fl.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/22-whitepaper-tokovi-fl.md:1) | 147 | 22. White paper tokovi i federativno učenje |
| [hemija/dijagnostika.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/dijagnostika.md:1) | 76 | Dijagnostika i kriterijumi prolaza |
| [hemija/index.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/index.md:1) | 66 | Hemija koju 2CDC zaista traži |
| [hemija/izvori.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/izvori.md:1) | 413 | Izvori i metod validacije |
| [hemija/kako-koristiti.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/kako-koristiti.md:1) | 74 | Kako se koristi ova knjiga |
| [hemija/laboratorije.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/laboratorije.md:1) | 259 | Opcione nastavne laboratorijske vežbe |
| [hemija/mapa-projekta.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/mapa-projekta.md:1) | 87 | Šta projekat zapravo traži |
| [hemija/plan-ucenja.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/plan-ucenja.md:1) | 81 | Plan učenja |
| [hemija/podsetnik.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/podsetnik.md:1) | 136 | Brzi pojmovni podsetnik |
| [hemija/recnik.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/recnik.md:1) | 763 | Rečnik pojmova |
| [hemija/resenja.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/resenja.md:1) | 162 | Rešenja i rubrike |
| [hemija/zablude.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/zablude.md:1) | 215 | Opasne zablude |
| [hemija/zavrsni-projekat.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/chemistry-foundations/docs/zavrsni-projekat.md:1) | 151 | Završna projektantska analiza — bez implementacije |

### ML/AI deo

| Izvorni fajl | Linije | Tema |
|---|---:|---|
| [ML/00-scope.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/00-scope.md:1) | 50 | Scope i teorijska pravila poređenja |
| [ML/00a-osnove-ml.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/00a-osnove-ml.md:1) | 250 | ML/AI od nule: pojmovi, matematika i prvi proračuni |
| [ML/01-pipeline-decision-map.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/01-pipeline-decision-map.md:1) | 132 | Mapa pipeline-a i algoritamskih odluka |
| [ML/02-classical-ml.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/02-classical-ml.md:1) | 341 | Klasični ML: baseline-i koji zaista imaju smisla |
| [ML/03-global-retrieval-ann-ranking.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:1) | 738 | Globalna pretraga: candidate generation, ANN i learning-to-rank |
| [ML/04-precise-pairwise.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/04-precise-pairwise.md:1) | 707 | Precizno poređenje parova: algoritmi, dokazi i granice |
| [ML/05-periodic-crystal-encoders.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/05-periodic-crystal-encoders.md:1) | 405 | Periodični crystal encoderi: GNN, transformer i equivariant modeli |
| [ML/06-metric-learning-and-evaluation.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:1) | 556 | Metric learning, pair modeli i evaluacija |
| [ML/07-local-slm-rag.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/07-local-slm-rag.md:1) | 234 | Lokalni SLM, kontrolisana interpretacija i RAG |
| [ML/08-api-llm-security.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/08-api-llm-security.md:1) | 212 | Spoljni LLM API-ji, granica podataka i bezbednost |
| [ML/09-cross-format-eligibility.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/09-cross-format-eligibility.md:1) | 224 | Cross-format reconciliation i eligibility podataka |
| [ML/10-optimal-stack-roadmap.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/10-optimal-stack-roadmap.md:1) | 297 | Uporedna mapa algoritamskih porodica i uslova primene |
| [ML/11-ml-ai-plan-ucenja.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/11-ml-ai-plan-ucenja.md:1) | 299 | Plan učenja ML/AI dela za 2CDC |
| [ML/evidence-method.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/evidence-method.md:1) | 42 | Metod dokaza i validacije |
| [ML/index.md:1](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-2/ml-ai-strategy/docs/index.md:1) | 36 | 2CDC ML/AI Strategy |

Dodatno su pregledani `README.md`, `chemistry-foundations/mkdocs.yml` i `ml-ai-strategy/mkdocs.yml` radi publike, načina upotrebe i redosleda navigacije. Distribuirani JavaScript/font resursi i serverska skripta nisu predmet pedagoškog audita. Sintetički CIF korišćen je kao sadržaj objašnjen u lekciji 12A; nije rađena nova validacija eksperimentalnih ulaza.

Provera SHA-256 sa početnim inventarom potvrđuje da pregledani izvorni fajlovi nisu izmenjeni tokom ovog rada. Sve predložene promene u ovom izveštaju ostaju preporuke za narednu uredničku reviziju.
