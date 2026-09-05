# Pedagoška recenzija teorijske osnove za 2CDC

**Pregledana kopija:** `C:\Users\Korisnik\Desktop\crystallography-and-ml-theory-3`  
**Datum:** 5. septembar 2026.  
**Verzija pri pregledu:** `a5f1ba01dcb57794b39ef37b21798f45fce78ffa`  
**Obuhvat:** 36 hemijskih i 15 ML/AI Markdown stranica, README i obe MkDocs navigacije.

## Objedinjena ocena

Dokumentacija je sadržajno bogata i pažljiva u razdvajanju onoga što podaci pokazuju, što algoritam izračunava i što tek treba naučno potvrditi. Posebno dobro objašnjava zašto sastav, molekulski graf, konformacija, kristalno pakovanje i ekspertska relevantnost nisu isto. Nema razloga da se ceo teorijski okvir prepisuje ili da se svako poglavlje proširuje.

**Glavni nedostatak je što je materijal trenutno ujednačeniji kao stručna projektna referenca nego kao samostalan put „od nule“.** Na više mesta precizni zahtevi za validaciju, ograničenja metoda i izuzeci dolaze pre dovoljno jasnog objašnjenja osnovnog mehanizma. Čitalac može naučiti šta ne sme da zaključi, a da još ne ume samostalno da izvede jednostavan ispravan zaključak.

Hemijski deo uglavnom ima prirodan makroredosled, ali mu nedostaju pojedini mali temelji u elektronskom knjigovodstvu, orbitalnoj slici, termodinamici i difrakciji. Najvidljiviji problem redosleda je kvantitativna periodična geometrija u poglavlju 7 pre punog uvođenja ćelije i simetrije u 8–9. ML/AI deo ima dobar novi početnički uvod, ali detaljna poglavlja povremeno preskaču nekoliko nivoa matematičkog i algoritamskog objašnjenja.

Pre nastavka projekta najviše koristi donose: usklađivanje putanje čitanja; ciljane dopune preduslova; jedan zajednički razrađen primer strukturnog poređenja; nekoliko kratkih računskih primera u učenju i evaluaciji; izdvajanje specijalističkih detalja iz osnovnog toka uz njihovo očuvanje u referentnim odeljcima.

## Kako je pregled sproveden

Čitani su izvorni teorijski tekstovi i pomoćne nastavne stranice. Za potencijalni problem proveravano je da li preduslov postoji ranije, kasnije, u drugom kursu, u rečniku ili u rešenjima. Sam pomen napredne metode u orijentacionoj mapi nije tretiran kao nedostatak. Problem je označen kada se od čitaoca traži razumevanje, račun ili odluka za koju taj pomen nije dovoljna priprema.

PDF duplikati nisu ponovo analizirani. Odsustvo referenciranih `.cif`, `.mol`, CSD izvoza i drugih pratećih projektnih materijala nije računato kao nedostatak. Predloženi mali primeri služe učenju; nisu zahtev da se pribave ti materijali. Izvorni repozitorijum nije menjan.

Ocena se odnosi na čitaoca opisanog samom dokumentacijom: hemijski uvod obećava put od nula hemijskog predznanja, a integrisani ML plan izričito uključuje početnika bez predznanja iz obe oblasti. Za iskusnog ML inženjera deo matematičkih dopuna može biti preskočiva dijagnostika. Ovo je pedagoška i konceptualna recenzija, a ne sertifikacija svake bibliografske, softverske ili lokalno izmerene tvrdnje. Primarni spoljni izvori proveravani su ciljano tamo gde pomažu preciznoj preporuci.

**Značaj nalaza:** „važan“ znači da problem otežava obavezan ishod ili može dovesti do pogrešne upotrebe pojma; „koristan“ znači da je osnova prisutna, ali tok može biti znatno jasniji; „manji“ označava lokalnu terminološku ili nastavnu korekciju. Oznaka prioriteta u završnom planu govori kojim redom menjati tekst. Kratka izmena može imati visok prioritet. Oznaka „kritičan“ rezervisana je za preduslov bez kog deklarisana početnička putanja ne može da se prati samostalno.

Brojevi linija odnose se na pregledanu verziju izvora. Link uz nalaz otvara njegovu početnu lokaciju; raspon relevantnih linija naveden je u tekstu.

## Zajednički problemi strukture i zavisnosti

### Z01 — Postoji više konkurentnih redosleda čitanja

**Gde:** [ML plan, redosled čitanja](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/11-ml-ai-plan-ucenja.md:31), linije 31–47 i 161–209; [ML navigacija](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/mkdocs.yml:49), linije 49–54; [ML početna](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/index.md:5), linije 5 i 18–28.

**Problem:** početna već pravilno upućuje početnika na uvod i plan. Ipak, njen „prvi detaljni modul“ i navigacija predstavljaju klasični ML → retrieval → pairwise, dok precizan integrisani plan nalaže pairwise → retrieval → klasični ML. Unutar drugog redosleda čitalac dolazi do LambdaMART-a i drugih naučenih rankera pre detaljne obrade boosting-a. Plan već razlikuje orijentaciono i potpuno čitanje uporedne mape, što je dobro; ta razlika nije dovoljno konkretna na drugim ulaznim stranicama.

**Zašto otežava razumevanje:** čitalac koji prati bočni meni dobija drugačije preduslove od čitaoca koji prati plan. Mora sam da odluči šta je trenutno samo najava, šta mora razumeti i kada da se vrati.

**Implicitno predznanje:** poznavanje zavisnosti između determinističkog poređenja, osnovnog učenja, rangiranja i statističke evaluacije.

**Konkretna izmena:** proglasiti jednu početničku putanju merodavnom i uskladiti meni ili jasno označiti meni kao tematski indeks. Uz svako veliko poglavlje dodati „Pre ovoga“ sa najviše tri precizna odeljka i „U prvom prolazu“. Osnovno objašnjenje stabala/boosting-a pročitati pre retrieval §3.13; napredne detalje klasičnog ML-a ostaviti za kasniji prolaz. Osnovnu evaluaciju izdvojiti iz zavisnosti od čitanja celog deep modula.

**Značaj:** važan. Rešava se prvenstveno reorganizacijom, bez novog teorijskog poglavlja.

### Z02 — Matematički minimum nije usklađen sa obećanjem „dovoljni su razlomci“

**Gde:** [ML uvod](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/00a-osnove-ml.md:3), linije 3, 46–96, 163–170 i 191–205; [hemijska geometrija](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/03-geometrija.md:31), linije 31–54; [promena baze i origina](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/09-simetrija.md:239), linije 239–282; [difrakcija](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/10-difrakcija-kvalitet.md:31), linije 31–50; [rang pri poravnanju](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/04-precise-pairwise.md:253), linije 253–257.

**Problem:** uvod zaista objašnjava skalar, vektor, matricu, normu, skalarni proizvod, transponovanje i ideju gradijenta. Zato nije tačno da matematike nema. Međutim, sledeći obavezni odeljci koriste logaritme i eksponencijalnu funkciju, trigonometriju, vektorski proizvod, matrični inverz i determinant, a zatim kompleksnu fazu; za njih ne postoji odgovarajući operativni most. Jedna rečenica o SVD-u ne priprema čitaoca za rang i singularne vrednosti u Kabsch ograničenjima.

**Zašto otežava razumevanje:** početnik može prepisati formulu, ali ne zna koju operaciju da izvrši ili zašto se njome čuva fizička veličina. Iskusnom inženjeru isti tekst deluje dovoljan, pa se praznina lako previdi.

**Implicitno predznanje:** srednjoškolske funkcije i trigonometrija, osnovna linearna algebra i najosnovnija slika kompleksnog broja.

**Konkretna izmena:** dodati kratak, preskočiv matematički most u tri celine: log/exp i verovatnoće; vektori i promene koordinata; amplituda i faza. Svaka celina treba jedan numerički primer i tačan link sa prvog mesta upotrebe. Ne uvoditi ceo kurs analize niti dokazivati SVD. Ako autori ne žele taj most, moraju eksplicitno podići zahtevano predznanje i dati konkretan pripremni put; to bi promenilo sadašnje obećanje kursa.

**Značaj:** važan; blokira samostalno izvođenje pojedinih obaveznih računa pri doslovno deklarisanom početku od razlomaka. Iskusnom ML inženjeru dovoljan je preskočiv podsetnik.

### Z03 — Osnovno objašnjenje i uslovi stručne validacije često imaju isti vizuelni rang

**Gde:** [component assignment](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/04-precise-pairwise.md:127), naročito linije 139–155; [ANN](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:236), linije 236–318; [hemijski plan](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/plan-ucenja.md:7), linije 7–25; [ML evaluacione odluke](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:406), linije 406–430.

**Problem:** objašnjenje metode često brzo prerasta u gust niz uslova za tolerancije, verzije, potpunost pretrage, poreklo i statističku odbranu. Ti uslovi imaju naučnu svrhu; problem je njihov položaj i gustina pre prvog jednostavnog primera rada samog algoritma. HNSW, na primer, već ima dobar memorijski račun. Naročito duge rečenice sa više engleskih termina skrivaju glavnu ideju.

**Zašto otežava razumevanje:** čitalac pokušava istovremeno da shvati objekat, osnovni algoritam, izuzetke i standard naučne odbrane. Ne vidi šta je konceptualno jezgro odeljka.

**Implicitno predznanje:** iskustvo čitanja metodoloških specifikacija i sposobnost da se iz liste kontrola rekonstruiše algoritam.

**Konkretna izmena:** u najgušćim odeljcima koristiti isti red: pitanje → intuicija → mali primer → definicija/formula → ograničenja → detalji za stručnu proveru. Poslednji sloj može ostati u izdvojenoj referentnoj podsekciji. Termin prvi put navesti kao „dodela komponenti (assignment)“, a potom koristiti dosledan oblik. Ne prevoditi svaku standardnu skraćenicu niti svuda ponavljati iste opšte uslove.

**Značaj:** važan u ML §4.4–4.10; koristan kao opšte uredničko pravilo.

### Z04 — Nedostaje jedan do kraja razrađen primer koji povezuje dva kursa

**Gde:** [hemijsko poređenje parova](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/19-parovi.md:61), §19.4–19.9, linije 61–137; [ML pairwise](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/04-precise-pairwise.md:116), §4.4–4.9; [laboratorije](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/laboratorije.md:199), L9, linije 199–216; [rešenja](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/resenja.md:123), L9, linije 123–140.

**Problem:** pojedinačne definicije i provere postoje, ali nisu spojene u jedan vođeni tok sa konkretnim komponentama, atomskom mapom, koordinatama, računanjem odstupanja i odvojenim zaključkom o pakovanju. Ovo nije odsustvo Kabsch/COMPACK teorije niti problem nedostupnih fajlova.

**Zašto otežava razumevanje:** čitalac može ponoviti da mapiranje prethodi RMSD-u, ali još ne vidi kako izbor komponente i atomskog mapiranja menja broj koji na kraju dobije, niti zašto isti molekulski rezultat može pratiti različito pakovanje.

**Implicitno predznanje:** prethodno iskustvo u stvarnom strukturnom poređenju ili sposobnost da se više odvojenih definicija samostalno pretvori u postupak.

**Konkretna izmena:** napraviti jedan mali sintetički nastavni primer i nastavljati ga kroz postojeća poglavlja: dve strukture sa glavnom komponentom i dodatnom komponentom; tabela dozvoljenih dodela; 3–4 mapirana nekolinearna atoma; centriranje i poznata rotacija; ručni RMSD i dvostrani coverage; šematsko poređenje susednih molekula. Dodati A′ kao isti objekat sa promenjenim zapisom i B kao stvarno drugačiji objekat. Za packing ne izmišljati rezultat COMPACK-a: pokazati izabrani mali klaster i jasno označiti nivo pojednostavljenja. Izvesti rezultat, pa tek onda prikazati završnu karticu dokaza.

**Značaj:** važan; ovo je pojedinačna nastavna dopuna sa najvećim dometom kroz oba kursa.

## Hemija: konkretni nalazi

### H01 — Od formule do Lewisove strukture nedostaje prvi samostalan račun

**Gde:** [atomi i periodni sistem](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/01-atomi-joni-formule.md:21), linije 21–35; [veze, §2.1–2.3](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/02-veze.md:5), linije 5–38.

**Problem:** valentni elektroni, oktet i simbolika Lewisovog crteža jesu pomenuti, ali nije pokazan postupak kojim se iz formule dobiju veze, slobodni parovi i formalni naboj. Formula za naboj pretpostavlja da čitalac već ume da odredi njene ulaze. Kasniji nitro-primer daje dobar rezultat, ali ne nadomešta najjednostavniji početni postupak.

**Zašto otežava:** isti nedostajući korak prenosi se na VSEPR, protonaciju, donorstvo i koordinaciju; čitalac pamti koliko parova azot ima umesto da to proveri.

**Implicitno predznanje:** valentni elektroni H/C/N/O, elektroni naspram parova, oktet i očuvanje ukupnog broja elektrona.

**Konkretna izmena:** mala tabela valentnih elektrona i jedan ceo primer NH₃ + H⁺ → NH₄⁺: broj elektrona, veze, preostali par, formalni i ukupni naboj. Isti primer koristiti u geometriji i donorstvu. Spoljni Lewisov udžbenički link već postoji; osnovni postupak treba uvesti u glavnu putanju ili taj konkretan odlomak izričito označiti kao obavezan preduslov.

**Značaj:** kritičan za samostalnu hemijsku putanju od nule; mali obim dopune, veoma širok uticaj.

### H02 — Hückelovo pravilo nije povezano sa konkretnim brojanjem π elektrona

**Gde:** [aromatičnost, §2.5](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/02-veze.md:71), linije 71–79; [piridinski i pirolski N](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/04-organska.md:80), linije 80–91.

**Problem:** izraz 4n+2 nije izričito razložen kao broj π elektrona sa značenjem n. Kasnija razlika dva tipa azota zavisi upravo od toga koji slobodni par ulazi u aromatični sistem. Postojeći σ/π i konjugacioni uvod je dobar; nedostaje primena.

**Zašto otežava:** donorska sposobnost postaje zapamćena etiketa, a veza između elektronskog modela i funkcionalne grupe ostaje skrivena.

**Implicitno predznanje:** doprinos π elektrona i slobodnog para aromatičnom krugu; razlika para u tom sistemu i para izvan njega.

**Konkretna izmena:** nacrtati benzen sa šest π elektrona, zatim piridin i pirol sa obeleženim doprinosima azota. Definisati n kao nenegativan ceo broj u ovom osnovnom pravilu. Nije potrebna puna teorija molekulskih orbitala.

**Značaj:** važan za DAP donorstvo i aromatičnost.

### H03 — „Donor“ ima tri značenja koja se susreću pre zajedničkog razjašnjenja

**Gde:** [organske grupe i kiseline/baze](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/04-organska.md:9), linije 9–26, 39–56 i 119–120; puna H-veza u [poglavlju 7](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/07-interakcije.md:91), linije 91–109.

**Problem:** tabela koristi H-bond donor/acceptor i metalni donor, pa zatim Brønstedovo doniranje protona i Lewisovo doniranje elektronskog para. Nema kratke uporedne legende, iako provera već zahteva razlikovanje tih uloga.

**Zašto otežava:** piridinski N može biti metalni donor i H-bond akceptor. Bez razjašnjenja to zvuči protivrečno. H-bond donorstvo se takođe može pogrešno poistovetiti sa stvarnim prenosom protona.

**Implicitno predznanje:** D–H···A, raspoloživ elektronski par, kovalentno vezan H i protonaciono stanje.

**Konkretna izmena:** pre tabele dati tri reda „šta se donira / šta termin znači / primer“. Uporediti isto N mesto u piridinu i piridinijumu: slobodni par omogućava tipičnu HBA/Lewisovu donorsku ulogu; protonacijom taj par više nije raspoloživ na isti način, a N–H omogućava HBD ulogu. HBD ne znači da se proton nužno prenosi. Geometrijske kriterijume H-veze ostaviti u poglavlju 7.

**Značaj:** važan; neposredno utiče na razumevanje hemijskih deskriptora i koordinacije.

### H04 — Ligandno polje dolazi pre oksidacionog bilansa i bez prikaza popunjavanja orbitala

**Gde:** [minimalni ligand-field most](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/05-kompleksi.md:158), linije 158–188; preduslovi u istom fajlu, §§5.6–5.7, linije 190–242.

**Problem:** račun dⁿ koristi oksidaciono stanje pre postupka njegovog određivanja. Link ka kasnijem bilansu postoji, pa preduslov nije prećutan, ali je redosled obrnut. Zatim se u kratkom prostoru uvode t₂g/e_g, cepanje, sparivanje, spin, degeneracija i Jahn–Teller, bez jednog popunjenog energetskog dijagrama.

**Zašto otežava:** čitalac može zapamtiti obrazac Cu(II), a da ne razume lanac naboj → elektronski broj → raspored elektrona → moguća strukturna posledica.

**Implicitno predznanje:** energetski nivoi, spareni/nespareni elektroni, cena sparivanja, degeneracija i kvalitativno antivezno ponašanje.

**Konkretna izmena:** završiti ligand, CN, denticitet i oksidacioni bilans pre elektronskog objašnjenja geometrije. Dodati jednu skicu oktaedarskog d⁶ sa visokim i niskim spinom, prebrojanim elektronima i označenim Δ. Imena t₂g/e_g tretirati kao oznake grupa nivoa. Postojeće ograde o Zn(II), jednom rastojanju i granicama modela zadržati.

**Značaj:** važan. Ne zahteva multiplete, spektroskopiju ili izvođenje teorije grupa.

### H05 — Reakcijski mehanizam DAP/Schiff baze koristi neobjašnjen jezik

**Gde:** [DAP, §6.2](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/06-dap-schiff.md:28), linije 28–45.

**Problem:** „nukleofilni napad“, elektrofil, karbinolamin, transfer protona i eliminacija služe kao intuitivni opis, iako te reči prethodno nisu dovoljno uvedene.

**Zašto otežava:** neto nastanak imina je čitljiv, ali objašnjenje mehanizma uvodi više nepoznanica nego što ih zatvara.

**Implicitno predznanje:** polarizacija karbonila, donor/primalac elektronskog para i reakcijski međuproizvod.

**Konkretna izmena:** dve rečenice povezati sa Lewisovim jezikom i prikazati neto promenu R₂C=O + H₂N–R′ ⇄ R₂C=N–R′ + H₂O. Četvorokoračni mehanizam označiti kao opcioni ili mu dodati jednu strukturnu skicu međuproizvoda. Ne širiti kurs organskim mehanizmima koji se dalje ne koriste.

**Značaj:** koristan za poboljšanje.

### H06 — Kvantitativni deo interakcija zahteva ćeliju i simetriju pre njihovog uvođenja

**Gde:** [poglavlje 7](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/07-interakcije.md:7), linije 7–33, 165–254 i 354–356; [plan zavisnosti](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/plan-ucenja.md:36), linije 36–40.

**Problem:** cilj i kriterijum poglavlja 7 traže frakcione koordinate, matricu ćelije, ASU, simetrijske kopije i reprodukciju periodičnog kontakta. Kratki most daje formule, ali puna značenja slede tek u poglavljima 8–9. Plan istovremeno zahteva prolaz prethodne kapije pre nastavka.

**Zašto otežava:** učenik mora da čita unapred da bi završio trenutno poglavlje. Bez ASU/ćelija razlike teško razume zašto traženi sused nije u izvornoj atomskoj tabeli.

**Implicitno predznanje:** ćelija, njena metrika, ASU, simetrija naspram translacije, specijalne pozicije i periodične slike.

**Konkretna izmena:** zadržati hemijsku intuiciju i vrste interakcija pre 8–9, a periodični algoritam, N14 proračun i odgovarajuću proveru postaviti posle 9. Alternativa je eksplicitno označen drugi prolaz kroz 7. Ažurirati i plan i kriterijume. Postojeći račun i upozorenja o kosim ćelijama treba sačuvati.

**Značaj:** važan, najviši prioritet među izmenama redosleda.

### H07 — Energetske formule imaju nedovoljnu legendu

**Gde:** [Coulomb i Lennard–Jones](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/07-interakcije.md:56), linije 56–89; dipol u [organskim grupama](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/04-organska.md:17), linije 17–24, i [rečniku](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/recnik.md:127), linije 127–128.

**Problem:** značenje parametara i nultog nivoa energije nije dovoljno eksplicitno. Posebno nisu razjašnjeni ε i σ u LJ potencijalu. Molekulski dipol se oslanja na kratke ranije najave i rečnik.

**Zašto otežava:** σ može biti pogrešno pročitan kao ravnotežno rastojanje, a ε pomešan sa dielektričnim oznakama iz prethodne formule. Veoma kratak kontakt tada deluje nužno povoljnije.

**Implicitno predznanje:** potencijalna energija u odnosu na razdvojene partnere, dubina minimuma i vektorsko sabiranje dipola veza.

**Konkretna izmena:** legenda uz formule; kod prikazanog LJ izraza, za ε>0, σ>0 i U(∞)=0, navesti da je nula na r=σ, a minimum na r=2^(1/6)σ sa energijom −ε. Jedna kriva može zameniti nekoliko opisnih rečenica. Kratak CO₂/H₂O primer povezuje polarnost veze i ukupan dipol.

**Značaj:** koristan za poboljšanje; dopuna čitanju postojećih formula, ne novi kurs energetike.

### H08 — Taksonomija je prerana, a opštoj superćeliji nedostaje mali konstrukcioni primer

**Gde:** [ćelija](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/08-celija.md:67), linije 67–97, 146–196 i 348–388.

**Problem:** crystal/lattice system, hP/hR, centriranja i metrička specijalizacija obrađuju se pre dovršene veze frakcionih i kartezijanskih koordinata. Kasnije se superćelija opisuje preko indeksa podrešetke i predstavnika koseta bez malog konstrukcionog primera.

**Zašto otežava:** čitalac se bavi klasifikacijom pre nego što sigurno razume šta koordinata meri. Kod superćelije vidi promenu Z i zapremine, ali ne i kako nastaju kopije atoma bez fizičkog istezanja strukture.

**Implicitno predznanje:** tačkasta/prostorna grupa, konvencionalno centriranje, indeks podrešetke i promena koordinatne baze.

**Konkretna izmena:** prvo završiti rešetka/motiv → koordinate → udaljenost/wrap; zatim dati klasifikaciju. Superćeliju početi sa A′=AP i P=diag(2,1,1), uz nepromenjen origin. Predstavnik atoma f iz već rekonstruisane početne ćelije tada daje kopije P⁻¹f i P⁻¹(f+(1,0,0)). Tek potom izložiti opšti determinantni račun. Termin koset može ostati u naprednoj napomeni.

**Značaj:** važan za ekvivalenciju zapisa; taksonomiju ne treba uklanjati.

### H09 — Strukturni faktor i fazni problem dolaze pre dovoljno jasne refleksije i faze

**Gde:** [difrakcija](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/10-difrakcija-kvalitet.md:31), linije 31–52, 73–134 i 172–228.

**Problem:** kompleksna suma F(hkl) prethodi punom hkl objašnjenju. Tvrdnja da detektor ne meri fazu nema mali primer sabiranja talasnih doprinosa. R/wR se zatim oslanjaju na isti nedovršeni most.

**Zašto otežava:** pik, atomski raspored, intenzitet i kvalitet refiniranja mogu ostati četiri odvojene formule, umesto povezanog eksperimentalnog lanca.

**Implicitno predznanje:** amplituda/faza, interferencija, intenzitet kao kvadrat modula amplitude i observed/calculated veličine.

**Konkretna izmena:** već dobar hkl → d → 2θ primer staviti pre formule F. Dodati jednodimenzionalni nastavni model jednakih rasipača sa jednakim zauzećem na x=0 i x=1/2: F(h00)=fₕ[1+exp(πih)], pa se za h=1 doprinosi poništavaju, za h=2 sabiraju. To nije pravilo za proizvoljna dva atoma. Dodati legendu n, λ, d, θ, Fₒ/Fc i povezati sliku sa sistematskim odsustvima. Ovaj nivo objašnjenja podržava [IUCr uvod u strukturne faktore](https://www.iucr.org/what-we-do/education/pamphlets/introduction-calculation-of-structure-factors); nije potrebno izvoditi celu Fourierovu rekonstrukciju.

**Značaj:** važan. Matematička priprema iz Z02 i ovaj fizički primer rešavaju različite delove iste teškoće.

### H10 — Termodinamičke veličine su imenovane pre nego što dobiju dovoljno fizičkog značenja

**Gde:** [čvrste forme](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/11-cvrste-forme.md:143), linije 143–239.

**Problem:** uz G=H−TS uglavnom se daju nazivi H i S, a potom hemijski potencijal, aktivnost vode, ΔCp i precizne ograde o metastabilnoj rastvorljivosti. Račun promene stabilnosti je koristan, ali fizička osnova je kraća od naprednih izuzetaka.

**Zašto otežava:** čitalac može izračunati znak ΔG, a ne objasniti uticaj temperature, razliku stabilnosti i brzine prelaza ili zašto hidrat zahteva bilans vode.

**Implicitno predznanje:** energetski i entropijski doprinos, ravnoteža, lokalni minimum/barijera, zasićenje rastvora i hemijski potencijal.

**Konkretna izmena:** kratak fizički opis H i S, slika dva minimuma i barijere i bilans „anhidrat + voda iz okoline ⇄ hidrat“. Rastvorljivost izložiti redom: rastvaranje/kristalizacija → merenje uz očuvanu fazu → transformacija tokom merenja. Ograde o toplotnom kapacitetu i metastabilnosti zadržati posle osnove. Ne proširivati celu termodinamiku rastvora.

**Značaj:** važan za čvrste forme i tumačenje rizika.

### H11 — Ilustrativna statistika nije dovoljno povezana sa imenovanim Mogul izlazom

**Gde:** [referentne raspodele i Mogul](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/11a-referentne-raspodele-hbp.md:23), linije 23–116.

**Problem:** percentil i robustni MAD račun jasno su označeni kao sintetički, što je dobro. Ipak, nedostaje kratka mapa od tih nastavnih veličina do vrsta izlaza alata pomenutog u naslovu. Nije izričito tvrđeno da je robustni z standardni Mogul rezultat, ali čitalac treba sam da razreši tu razliku.

**Zašto otežava:** može razumeti „neobično u datoj populaciji“, a ipak ne znati kako da protumači prikaz podrške, generalizacije upita i geometrijske dijagnostike.

**Implicitno predznanje:** geometrijska biblioteka, exact/generalized pogodak i izbor dijagnostike za dužinu, ugao i torziju.

**Konkretna izmena:** četiri reda „geometrijska veličina → šta se poredi → naziv izlaza konkretne verzije → podrška/generalizacija“. Povezati sa [zvaničnim opisom geometrijske analize](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/molecular_geometry_analysis.html). Jasno reći da gornji percentil/MAD objašnjava princip, a ne reprodukuje određenu implementaciju. Ne uvoditi nove univerzalne pragove.

**Značaj:** koristan; viši prioritet tek za samostalno tumačenje ovog alata.

### H12 — HBP primer ne dovršava prelaz od pojedinačne veze do mreže

**Gde:** [HBP tok i primer](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/11a-referentne-raspodele-hbp.md:118), linije 118–163 i kriterijum u 209.

**Problem:** primer naslovljen „četiri output-a“ numerički prikazuje propensity i opaženost pojedinačnih veza. Grouping i coordination score ostaju verbalni, bez dve eksplicitne mreže i njihovih donorskih/akceptorskih ishoda.

**Zašto otežava:** nije dovoljno vidljivo zašto dobra pojedinačna veza i dobro ukupno zadovoljenje donornih/akceptorskih mesta nisu isti kriterijum. Tekst već pravilno razlikuje ovaj coordination score od metalnog CN-a; to nije prijavljeni problem.

**Implicitno predznanje:** kompatibilni skupovi H-veza, broj doniranja/prihvatanja po mestu i agregacija pojedinačnih procena.

**Konkretna izmena:** na postojećim D1/A1/A2 prikazati dva ilustrativna, kombinatorno kompatibilna groupinga i tabelu „ko donira/prihvata koliko puta“. Coordination score nije izvodljiv samo iz individualnih propensity vrednosti ili broja veza: potrebne su zasebne modelske procene donornih/akceptorskih ishoda. Za numeričko agregiranje navesti pravilo iz konkretne verzije [HBP dokumentacije](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/hbond_propensities.html), uz sintetičku oznaku. Grouping sam ne dokazuje ostvarivo kristalno pakovanje. Logistički model i AUC povezati sa preciznim odeljkom ML uvoda.

**Značaj:** važan za završni HBP ishod; kasniji prioritet ako je trenutni fokus samo strukturna sličnost.

### H13 — U primeru se pojavljuje 3D skor 0,71 bez definicije

**Gde:** [hibridni rezultat, §15.7](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/15-slicnost.md:86), linije 88–99; suštinska prethodna napomena u 65.

**Problem:** posle ispravnog objašnjenja da RMSD u Å nije skor 0–1, primer daje `mapped 3D core 0.71 (28/34 heavy atoms; RMSD 0.62 Å)`. Transformacija do 0,71 nije navedena. Slična neodređenost postoji za interaction score 0,58.

**Zašto otežava:** čitalac može pretpostaviti standardnu konverziju iz 0,62 Å u 0,71, čime primer podriva prethodno objašnjenje.

**Implicitno predznanje:** zasebna, zadatkom definisana funkcija koja udaljenost ili mrežni odnos preslikava u skor.

**Konkretna izmena:** ukloniti neobjašnjene skorove i ostaviti izvornu meru, jedinicu i coverage obe strane. Ako skor ostaje, dati eksplicitnu ilustrativnu funkciju i njenu skalu; ne izmišljati univerzalnu transformaciju. Označiti brojke kao nastavne.

**Značaj:** važan; vrlo mala izmena koja treba da ide u prvi paket popravki.

### H14 — Macro/micro agregacija zahteva jedan nastavak postojećeg računa

**Gde:** [evaluacija, §20.7](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/20-evaluacija.md:107), linije 107–109.

**Problem:** recall i precision jednog upita imaju dobre formule i primer. Sledeći pasus zahteva query-macro i pooled-micro, ali ne pokazuje šta prosečavaju niti zašto se razlikuju. To ne dopunjuju ni postojeći rečnik ni nDCG primer iz ML uvoda.

**Zašto otežava:** dva različita procenta mogu delovati kao računska greška, umesto odgovora na različita pitanja o uspehu sistema.

**Implicitno predznanje:** prosek razlomaka naspram količnika zbirova; jedinica ponderisanja.

**Konkretna izmena:** dva upita: prvi pronalazi 1 od 1 relevantnog, drugi 1 od 9. Macro recall je (1+1/9)/2≈0,556; pooled micro je (1+1)/(1+9)=0,20. Prvi ravnopravno ponderiše upite, drugi ukupne relevantne slučajeve. Dodati ove dve formule i link iz ML evaluacije. Ne pretvarati nDCG u neobjašnjeni „micro nDCG“.

**Značaj:** važan za evaluacionu pismenost; vrlo kratka dopuna.

### H15 — Bootstrap u App 2 nije dovoljno povezan sa zavisnošću oba člana para

**Gde:** [hemijska evaluacija](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/20-evaluacija.md:164), linije 164–166, uz raniju dobru osnovu u 79; postojeće detaljnije rešenje u [ML evaluaciji](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:302), linije 302–311.

**Problem:** hemija pravilno upozorava da parovi nisu nezavisni, ali preporuku resamplinga formuliše preko upita ili familije. App 2 nema prirodan jedinstveni query i parovi mogu deliti oba endpoint-a. ML deo tu razliku već eksplicitno obrađuje; problem je neusaglašenost nivoa objašnjenja i nedostajuća veza.

**Zašto otežava:** grupisanje samo po prvom članu može delovati dovoljno, iako (A,B) i (C,B) i dalje dele B.

**Implicitno predznanje:** retrieval lista naspram grafa parova i resampling osnovnih struktura/familija naspram redova rezultata.

**Konkretna izmena:** prikazati parove (A,B), (A,C), (B,C), razdvojiti App 1 query-family jedinicu od App 2 postupka koji uvažava obe strane, i dati direktan link na postojeći ML odeljak. Ne propisivati jedan univerzalni bootstrap za sve ciljeve niti u hemiji izvoditi celu teoriju zavisnih parova.

**Značaj:** važan za samostalnu evaluaciju; prvenstveno povezivanje postojeće teorije.

### H16 — U poglavlju o lokalnom skupu prenosive pouke dolaze iza dugog inventara

**Gde:** [forenzika lokalnog skupa](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/17-lokalni-skup.md:20), linije 20–49, 114–232 i 282–372; sinteza u 438–456.

**Problem:** veličine fajlova, zbirni brojevi atoma/veza, elementne brojnosti i CQS detalji imaju sličnu težinu kao ključne pouke o query značenju, gubicima formata, missingness-u i familijama. Ceo odeljak nosi obavezni prioritet.

**Zašto otežava:** čitalac može pokušati da memorise snapshot statistiku umesto da prepozna pravilo primenljivo na sledeći skup.

**Implicitno predznanje:** čitanje inventara podataka i razlikovanje dokaza, prenosivog zaključka i referentne numerike.

**Konkretna izmena:** postojeću sintezu pomeriti napred kao tabelu „nalaz → posledica → dokaz“. U osnovnom toku zadržati po jedan primer za svaku glavnu pouku, a detaljne tabele jasno označiti kao referentne. Sačuvati sve dokumentovane dokaze. Ovo nema veze sa dostupnošću originalnih fajlova.

**Značaj:** koristan za poboljšanje i skraćivanje prvog prolaza.

## ML/AI: konkretni nalazi

Matematičke praznine iz Z02 i zajednički strukturni primer iz Z04 ovde se ne broje ponovo. Kod Kabsch-a treba na njih nadovezati samo dimenzije R, x, y i t i kratak redosled: izabrana atomska mapa → neprekinuta molekulska geometrija → centriranje → optimalna rotacija → translacija i odstupanje. Nije potrebno ručno izvoditi SVD. Sledeći nalazi odnose se na dodatne, zasebne nastavne korake.

### M01 — Postoji definicija treninga, ali nema jednog dovršenog primera učenja

**Gde:** [ML uvod, trening](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/00a-osnove-ml.md:74), linije 74–102; [klasični ML](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/02-classical-ml.md:55), linije 55–74, 105–144 i 280–304.

**Problem:** linearni model, loss, regularizacija i trening jesu definisani. „Primer modela“ potom uglavnom nabraja ulazne osobine; ne pokazuje izbor parametara i predikciju novog primera. RF i boosting imaju osnovni opis, ali njihove različite načine učenja ne demonstrira zajednička mala tabela.

**Zašto otežava:** početnik može pomešati ručno postavljen skor i naučeni model ili prosečavanje stabala i sekvencijalno popravljanje predikcije.

**Implicitno predznanje:** empirijski izbor parametara, list stabla, trening greška i nezavisna greška predikcije.

**Konkretna izmena:** na 4–6 sintetičkih redova uporediti dva ponuđena linearna modela prema prosečnom loss-u i izračunati predikciju jednog izdvojenog primera. Na istoj tabeli pokazati malo stablo i dva koraka regresionog boosting-a uz kvadratni gubitak. To su ručni teorijski primeri, saglasni sa planom koji ne zahteva implementaciju. Optimizacije pojedinih biblioteka mogu ostati u referentnoj napomeni.

**Značaj:** važan; najveća pojedinačna dopuna za čitaoca bez ML iskustva.

### M02 — Kernel, latentne komponente i GPR imaju uslove primene pre dovoljno jasne osnove

**Gde:** [SVM, PCA/PLS i GPR](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/02-classical-ml.md:171), linije 171–225; [SOAP uslov za kernel](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/04-precise-pairwise.md:413).

**Problem:** kernel kao skalarni proizvod jeste definisan. Gram matrica i pozitivna semidefinitnost nisu operativno objašnjene. PCA/PLS se oslanjaju na jednu rečenicu o varijansi/kovarijansi, a GPR na „raspodelu nad funkcijama“ bez osnovne slike pre i posle opažanja. Po planu SOAP može doći i pre ovog kratkog kernel uvoda.

**Zašto otežava:** ne može se jasno razlikovati proizvoljna sličnost od validnog kernela, niti razumno objasniti šta nova komponenta ili prediktivna varijansa znače.

**Implicitno predznanje:** projekcija, kovarijansa, Gram/PSD, prior/posterior i prediktivna raspodela.

**Konkretna izmena:** mali most pre prve kernel metode: iz nekoliko vektora izračunati Kᵢⱼ, pa rečima objasniti zašto kvadrat dužine ne može biti negativan. Za PCA/PLS uporediti pravac najvećeg rasipanja sa pravcem korisnim za y. GPR prikazati kroz nekoliko mogućih funkcija pre i posle opažanja, uz srednju predikciju i neizvesnost; [autorski GPML, poglavlje 2](https://gaussianprocess.org/gpml/chapters/RW2.pdf) daje osnovu za takav sažeti most. Ne tražiti kompletan Bayesov izvod.

**Značaj:** važan pre kernel/SOAP/GPR grana; referentna dopuna za ostale čitaoce.

### M03 — Assignment i MCS preskaču jednostavan primer problema koji rešavaju

**Gde:** [dodela komponenti i grafovi](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/04-precise-pairwise.md:127), linije 127–217.

**Problem:** od simboličke cost matrice brzo se prelazi na unmatched čvorove, kapacitete, k-best rešenja, orbite, granice optimuma i enumeraciju. MCS uvodi induced/non-induced i connected/disconnected izbore bez malih grafova koji pokazuju posledicu. To su opravdani zahtevi, ali njihov zajednički jednostavni problem nije demonstriran.

**Zašto otežava:** nije očigledno zašto najbolji pojedinačni izbor komponente ne mora dati najbolje ukupno uparivanje, niti kako mala promena MCS definicije menja rezultat.

**Implicitno predznanje:** globalna kombinatorna optimizacija, bijekcija, povezanost, ekvivalentne permutacije i dokaz optimuma.

**Konkretna izmena:** pre naprednog odeljka dati matricu troškova [[1,2],[2,100]]: pohlepni izbor dijagonale daje 101, ukršteno uparivanje 4. Potom dodati mogućnost neuparene komponente. Na dva mala grafa pokazati razliku exact/containment/MCS i objasniti četiri MCS izbora. Orbite/k-best/bounds izdvojiti u „potpunost i neizvesnost pretrage“. Ovaj primer može biti početak zajedničke studije Z04.

**Značaj:** važan za osnovno poređenje parova.

### M04 — Periodični grafovi zahtevaju poseban most od ćelije do oznaka ivica i ciklusa

**Gde:** [periodično mapiranje i unwrap](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/04-precise-pairwise.md:173), linije 173–175, 249 i 464–473; kasnija formula u [periodičnom encoderu](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/05-periodic-crystal-encoders.md:126), linije 128–148.

**Problem:** quotient/gain/gauge, promena predstavnika čvora, zbir translacija oko ciklusa i rang mreže traže se pre objašnjenja. Hemijska PBC i promena baze daju deo osnove, ali ne objašnjavaju konačan graf koji predstavlja beskonačnu mrežu. Formula transformacije tek je u kasnijoj, uslovnoj deep lekciji.

**Zašto otežava:** čitalac zna da wrapping ne menja kristal, ali ne razume zašto integer oznaka ivice mora da se promeni ili zašto zatvoren put na crtežu jedne ćelije ne mora biti fizički prsten.

**Implicitno predznanje:** periodični graf i njegov konačni prikaz, orijentisani pomeraji ivica, izbor predstavnika čvora i linearna nezavisnost translacija.

**Konkretna izmena:** pre §4.5 uvesti 1D lanac sa dva predstavnika. Pokazati sᵢ′=sᵢ+kᵢ i n′=n+kᵢ−kⱼ, tako da sⱼ′−sᵢ′+n′ ostaje isti frakcioni pomeraj, a time i fizički pomeraj a·(sⱼ′−sᵢ′+n′) za dužinu ćelije a. Zatim uporediti ciklus sa ukupnom translacijom 0 i put do kopije u sledećoj ćeliji. Rang 1/2/3 objasniti pomoću nezavisnih pravaca lanca/sloja/mreže. Opštu formulu baze sačuvati kao nastavak i iz encodera linkovati nazad.

**Značaj:** važan, visok prioritet za periodično poređenje. Ovo je nova konceptualna veza, ne samo dodatna matematička oznaka iz Z02.

### M05 — SOAP/REMatch detaljnije objašnjava ograničenja nego prelaz od lokalnih okruženja do globalnog skora

**Gde:** [SOAP i agregacija](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/04-precise-pairwise.md:398), linije 398–419.

**Problem:** glatka gustina, power spectrum i entropijski regularizovano uparivanje dobijaju vrlo kratak opis. Potom dolaze truncation, alchemical kernel, PSD i domenska ograničenja različitih agregacija.

**Zašto otežava:** bez lokalnog deskriptora i matrice lokalnih sličnosti čitalac ne vidi šta se prosečava ili uparuje, ni zašto globalne konstrukcije nisu međusobno zamenljive.

**Implicitno predznanje:** zaglađena atomska gustina, kernel, matrica uparivanja i meka/regularizovana dodela.

**Konkretna izmena:** dati četiri koraka: atomsko okruženje → zaglađena gustina → lokalni deskriptor → matrica sličnosti dva skupa okruženja. Na matrici 2×2 kvalitativno uporediti prosek, strogo uparivanje i meko uparivanje. Detalje bazne ekspanzije ostaviti u naprednom dodatku. Očuvati postojeću razliku REMatch/adapted-average i njihove uslove.

**Značaj:** važan kada se proučava ova porodica; nije preduslov osnovnog toka koji je ne koristi.

### M06 — ANN parametri i memorija dolaze pre dovoljne intuicije samih algoritama

**Gde:** [HNSW, IVF/PQ i MinHash](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:236), linije 236–318.

**Problem:** osnovni ANN/exact odnos je dobro objašnjen. Međutim, HNSW dobija vrlo kratak mehanizam pre parametara i memorije; IVF podrazumeva centroid/particionisanje, PQ codebook/residual, a MinHash konstrukciju potpisa.

**Zašto otežava:** čitalac može izračunati RAM, ali ne objasniti gde nastaje propušten kandidat ili kako efSearch/nprobe utiču na obuhvat pretrage.

**Implicitno predznanje:** obilazak grafa, centroid, kvantizacija, rezidual i hash potpis.

**Konkretna izmena:** jedan skup 8–10 tačaka koristiti za exact pregled, HNSW put i IVF preskočenu particiju. PQ pokazati na četvorokomponentnom vektoru podeljenom na dva dela sa codebook ID-jevima. MinHash-u dati kratku ideju minimuma pod zajedničkom permutacijom; detalje LSH-a ostaviti kao alternativnu granu. Postojeće korisne memorijske račune pomeriti posle mehanizma.

**Značaj:** važan za samostalno poređenje indeksnih porodica; nije zahtev za implementacijom indeksa.

### M07 — „Pairwise“ znači i par kristala i preferenciju dva kandidata za isti upit

**Gde:** [učenje rangiranja](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:435), linije 435–464; [primer pair relevance](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/02-classical-ml.md:280), linije 280–288.

**Problem:** definicije pointwise/pairwise/LambdaMART postoje i ograničenja labela su ispravno navedena. Ipak, ista reč se koristi za dva različita uzorka bez jedne zajedničke demonstracije: (A,B,labela) i (query,kandidat₁,kandidat₂,preferencija).

**Zašto otežava:** lako je zaključiti da bilo koje binarne oznake parova već predstavljaju query-grupisanu ranking superviziju. LambdaMART dodatno zavisi od boosting osnove koju plan obrađuje kasnije.

**Implicitno predznanje:** razlika jedinice podataka, jedinice gubitka i uslovljene preferencije.

**Konkretna izmena:** jedan upit i tri kandidata sa ocenama 2/1/0 pretvoriti u tri pointwise reda, parove preferencija i jednu rang-listu. Prikazati zašto zamena mesta pri vrhu jače utiče na izabrani nDCG. Povezati sa kratkim boosting uvodom i koristiti opisni naslov „preferencija dva kandidata za isti upit“.

**Značaj:** važan za rangiranje; mala dopuna koja rešava terminološku i konceptualnu zabunu.

### M08 — Triplet i InfoNCE formule nemaju sve ključne definicije i prvi račun

**Gde:** [loss porodice](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:99), linije 99–143; pair head u 223–229.

**Problem:** pair contrastive loss definiše d/y/m. Triplet potom daje samo željenu nejednakost, bez eksplicitnog a/p/n i samog loss-a. Semi-hard izbor nije razložen. InfoNCE τ nema objašnjenje, a kasniji ⊙ nema legendu.

**Zašto otežava:** nije jasno kada trojka doprinosi gubitku, kako se bira semi-hard primer niti zašto promena τ ili skupa kandidata menja rezultat istog para.

**Implicitno predznanje:** anchor/positive/negative, hinge gubitak, mining, softmax temperatura i množenje po komponentama.

**Konkretna izmena:** definisati a/p/n i dodati max(0,d(a,p)²−d(a,n)²+m), sa aktivnim i nultim primerom. Semi-hard objasniti uslovom d(a,p)²<d(a,n)²<d(a,p)²+m, saglasno [originalnom FaceNet radu](https://openaccess.thecvf.com/content_cvpr_2015/html/Schroff_FaceNet_A_Unified_2015_CVPR_paper.html). Za τ>0 dati intuiciju oštrine softmax-a i mini-primer promene denominatora; ne preuzimati hiperparametre drugog domena. ⊙ znači množenje odgovarajućih komponenti.

**Značaj:** važan pre metric-learning grane.

### M09 — Grupe transformacija i parity oznake zahtevaju geometrijsku legendu

**Gde:** [periodični encoderi](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/05-periodic-crystal-encoders.md:45), linije 45–51, 148 i 193–231; [pair modeli](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:237), linije 237–246.

**Problem:** osnovna invarijansa/ekvivarijansa je već objašnjena. Zatim se prelazi na SO(3), O(3), SE(3), E(3), njihov proizvod, 0e/0o i pseudoskalar bez kratkog pregleda šta koja oznaka dozvoljava.

**Zašto otežava:** čitalac može proveravati samo zajedničku rotaciju dva ulaza, iako njihovi nezavisni koordinatni sistemi zahtevaju jači uslov; ili pogrešno zaključiti da svaka ekvivarijantna mreža automatski razlikuje ogledalske parove.

**Implicitno predznanje:** proper rotacija, refleksija, transformaciona grupa, parity i orijentisana zapremina.

**Konkretna izmena:** mala legenda četiri grupe i slika četiri slučaja: rotiran samo A, samo B, oba nezavisno, ogledalski preslikan A. Za 0o dovoljno je pokazati znak orijentisane tetraedarske zapremine pod rotacijom i refleksijom. Formalni račun reprezentacija grupa ostaviti specijalističkoj referenci.

**Značaj:** važan za geometrijske neuronske i cross-graph modele; uslovna napredna dopuna.

### M10 — Kalibracija, prag i prediktivni interval nemaju zajednički prikaz postupka

**Gde:** [kalibracija i conformal](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/02-classical-ml.md:243), linije 243–263; [napredna kalibracija](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:375), linije 375–391.

**Problem:** značenje kalibracije i primer procene 0,8 već postoje. Detaljni moduli uglavnom opisuju kada Platt/isotonic/temperature metode rade i koje pretpostavke ograničavaju conformal. Nije jasno prikazano šta se fituje i kako se konstruiše skup/interval. Interval evaluacione metrike, modelna varijansa i prediktivni interval pojavljuju se odvojeno.

**Zašto otežava:** čitalac može pomešati promenu praga sa promenom verovatnosne prognoze ili sve intervale shvatiti kao istu vrstu „confidence-a“.

**Implicitno predznanje:** rezidual, kvantil, transformacija score-a i marginalna naspram uslovne pokrivenosti.

**Konkretna izmena:** dodati tok zamrznuti model → kalibracioni podaci → naučena transformacija → netaknuti test. Pored njega tabelu „interval metrike / interval novog targeta / skup klasnih oznaka“. Za opcioni simetrični regresioni split-conformal primer pokazati sortirane apsolutne reziduale |y−ŷ| kao nonconformity score, eksplicitan konačno-uzorački kvantil i novi interval, uz pretpostavke. [Shafer–Vovk tutorial](https://jmlr.org/papers/v9/shafer08a.html) daje primarnu osnovu i numeričke primere. Ne ponavljati postojeću definiciju 0,8 bez ovog narednog koraka.

**Značaj:** važan za naučene odluke sa uzdržavanjem; conformal nije obavezna metoda.

### M11 — Statistički uslovi prihvatanja modela nemaju dovršen primer zaključivanja

**Gde:** [kriterijumi fer poređenja](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/01-pipeline-decision-map.md:124), linije 124–127; [evaluacione odluke](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:406), linije 406–430, uz resampling u 302–311.

**Problem:** bootstrap, interval i non-inferiority imaju osnovne definicije, ali kapije zahtevaju uparene intervale, donju granicu, praktičnu marginu i procenu nedovoljne snage uzorka bez jednog kompletnog primera. Dobre 1D/2D split sheme već postoje; one nisu problem.

**Zašto otežava:** čitalac može ponoviti „ne birati model na testu“, a ipak pogrešno proglasiti pobednika iz male tačkaste razlike ili brojati seed-ove kao nove hemijske uzorke.

**Implicitno predznanje:** raspodela procene, uparena razlika, klasterska zavisnost, margina i statistička snaga.

**Konkretna izmena:** na nekoliko query grupa dati rezultate oba sistema i pokazati da isti resample bira iste grupe za oba. Definisati Δ = metrika novog modela − metrika reference, pri čemu je veća metrika bolja. Ilustrativni interval za Δ [−0,01;0,03] ne dokazuje superiornost; može podržati unapred definisanu marginu neinferiornosti δ=0,02 jer je donja granica iznad −δ, uz odgovarajući nivo intervala, protokol i ostale uslove. Dodati i slučaj u kome je interval preširok za odluku. Macro/micro račun preuzeti iz H14, a zavisnost parova povezati sa H15. Ne izvoditi svu dyadic statistiku u osnovnom toku.

**Značaj:** važan, prioritet pre širenja liste modela.

### M12 — Otvorene kapije učenja nemaju dovoljno povratne informacije za samostalnog početnika

**Gde:** [plan i kapije](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/11-ml-ai-plan-ucenja.md:163), linije 163–254.

**Problem:** vežbe uglavnom traže da polaznik sam osmisli primer, pravila ili izveštaj, a zatim proceni sopstvenu spremnost. Kriterijumi poput „drugi inženjer može nedvosmisleno razumeti“ nisu dovoljna povratna informacija bez tutora. Hemijske rubrike i ML00a samoprovera jesu korisne, ali ne pokrivaju sve nove ML kapije.

**Zašto otežava:** učenik može preći dalje memorisanjem termina ili ostati zaglavljen jer ne zna očekivani nivo formalizma.

**Implicitno predznanje:** stručni audit i samostalna procena kvaliteta otvorenog metodološkog odgovora.

**Konkretna izmena:** za G3–G7 dodati po jedan mali zadatak sa fiksnim činjenicama, rubriku „mora sadržati“ i sklopivi uzor odgovora. Početnički ishod treba da proverava značenje i izbor potrebnog postupka; napredni može proveravati punu reproduktivnu definiciju. Koristiti iste primere iz Z04, M01 i M11, bez novih implementacionih projekata.

**Značaj:** važan za samostalno učenje; manji problem u mentorskom radu.

### M13 — „Ceo razvojni uzorak“ kod ExtraTrees-a terminološki se sukobljava sa podelom podataka

**Gde:** [Extra Trees](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/02-classical-ml.md:138), linija 138; relevantna razlika skupova u [ML uvodu](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/00a-osnove-ml.md:106), linije 106–113.

**Problem:** formulacija može značiti da se pri gradnji koristi i validation deo. Ostatak dokumentacije pravilno insistira na trening-only učenju, pa ovo nije tvrdnja da kurs namerno propisuje curenje podataka.

**Zašto otežava:** ista reč „razvojni“ označava različite skupove u susednim metodološkim objašnjenjima.

**Implicitno predznanje:** razlika kompletnog razvojnog skupa, trening dela pojedinačnog fold-a i redova prosleđenih operaciji fit.

**Konkretna izmena:** napisati „tipično koristi ceo trening deo konkretnog fold-a, bez bootstrap uzorkovanja“. [Zvanični ExtraTrees opis](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html) navodi bootstrap=False i korišćenje celog prosleđenog skupa za stablo; to nije dozvola za uključivanje nezavisne validacije.

**Značaj:** manja terminološka korekcija sa važnom preventivnom posledicom; uraditi odmah.

### M14 — Netranzitivna „bliskost“ ne treba da bude pročitana kao automatski dokaz protiv metrike

**Gde:** [relacije i metric learning](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:130), linije 130–143; [uporedna mapa](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/10-optimal-stack-roadmap.md:195), linije 195–199.

**Problem:** upozorenje da „povezano“ ne treba pretvarati u klase ekvivalencije je opravdano. Blizina tog upozorenja širim tvrdnjama o kompatibilnosti metričkog prostora može se preširoko pročitati: kao da svaka netranzitivnost isključuje metriku. Tekst to ne tvrdi kao strogu teoremu; treba sprečiti takvo čitanje.

**Zašto otežava:** može se nepotrebno odbaciti validan prostor udaljenosti zbog svojstva koje ima i obična pragovana euklidska bliskost.

**Implicitno predznanje:** metrika, relacija ekvivalencije i binarni odnos dobijen pragovanjem rastojanja nisu isti objekti.

**Konkretna izmena:** dodati kontraprimer tačaka 0,1,2 na pravoj uz prag 1,5: A je blisko B, B je blisko C, A nije blisko C; rastojanje je i dalje validna metrika. Zatim precizirati da problem mogu biti neusaglašene klase, asimetričan target ili međusobno nekompatibilni zahtevi, što treba posebno proveriti.

**Značaj:** koristan za konceptualnu preciznost; dovoljan je jedan kratak pasus.

## Mapa najvažnijih zavisnosti

Ova tabela pokazuje zašto izmene treba raditi u paketima. Jedna dopuna često popravlja više kasnijih poglavlja. Ne treba istu definiciju dopisivati na svakom mestu korišćenja.

| Lanac koji čitalac treba da prati | Trenutno slabo mesto | Potrebna veza |
|---|---|---|
| valentni elektroni → Lewis → slobodni par → VSEPR/protonacija/koordinacija | H01, H03 | jedan elektronski račun i uporedna donor legenda |
| σ/π i konjugacija → aromatični elektroni → piridinski/pirolski N → DAP | H02 | konkretno prebrojavanje, uz očuvanje postojećeg σ/π uvoda |
| naboj liganada i jedinke → oksidaciono stanje → dⁿ → spin/geometrija | H04 | preurediti redosled i pokazati jedno popunjavanje orbitala |
| ćelija i koordinate → ASU/simetrija → periodični kontakt | H06, H08 | kvalitativni i kvantitativni prolaz kroz interakcije |
| periodični kontakt → označena ivica → promena predstavnika → ciklus/mreža | M04 | mali periodični graf pre naprednog mapiranja i encodera |
| hkl → d i položaj pika → fazno sabiranje → F/I → refiniranje/kvalitet | H09, Z02 | talasni primer i priprema oznaka; sačuvati postojeći hkl račun |
| H/S i ravnoteža → ΔG → barijera → metastabilnost/rastvorljivost | H10 | fizička slika pre detaljnih ograničenja merenja |
| izabrana populacija → statistički signal → HBP pojedinačna procena → mreža | H11–H12, Z02, M01 | razlikovati nastavni skor, modelski izlaz i agregaciju |
| komponente → atomska mapa → unwrapped koordinate → poravnanje → RMSD/coverage → packing | Z04, M03–M04 | jedan nastavljen primer, sa odvojenim fizičkim zaključcima |
| podaci/loss → izbor parametara → predikcija → query-grupisano rangiranje | M01, M07, Z01 | ručni trening pre naprednog rankera; jasno razlikovati uzorke |
| lokalni deskriptor → kernel matrica → globalna agregacija | M02, M05 | osnovni kernel most pre SOAP/REMatch/GPR |
| nezavisna jedinica → split → agregacija → interval razlike → odluka | H14–H15, M11 | sačuvati dobre split sheme i dodati račun/tumačenje |
| naučeni score → verovatnosna prognoza → kalibracija/prag → rizik i obuhvat | M10 | prikazati različite postupke i objekte intervala |
| invarijansa → nezavisni sistemi dva ulaza → rotacija/refleksija → parity | M09 | legenda grupa i četiri geometrijska slučaja |

## Šta zaista treba dopuniti, a šta prvenstveno premestiti

**Nedovoljna teorijska osnova u glavnoj početničkoj putanji:** elektronski račun i π brojanje; minimum orbitalnog popunjavanja; log/exp i potrebna linearna algebra; amplituda/faza; fizičko značenje termodinamičkih veličina; periodični graf sa pomerajima ivica. Za kernel, GPR, conformal i parity metode potrebni su posebni mali mostovi pre tih grana, ne pre svakog osnovnog zadatka.

**Osnova postoji, ali nedostaje izvedena primena:** učenje modela, globalni assignment, molekulsko naspram kristalnog poređenja, HBP grouping, macro/micro agregacija, upareni statistički zaključak i pointwise/pairwise/listwise supervizija. Najveći dobitak ovde dolazi iz nekoliko rešenih primera.

**Osnova postoji, ali je putanja do nje loša:** periodične interakcije pre ćelije/simetrije; oksidacioni bilans posle dⁿ; SOAP pre osnovnog kernela; statistički preduslovi u hemijskom delu bez neposrednog linka; formula periodičnog gain-a tek u kasnijem deep modulu; neusaglašen meni i integrisani plan.

**Delovi koji su nepotrebno teški u prvom prolazu:** rana klasifikaciona gustina u ćeliji; assignment orbite i potpuna enumeracija pre jednostavnog problema; SOAP ograničenja pre lokalno-globalnog mehanizma; ANN konfiguracija pre puta pretrage; inventarska numerika pre pouka o lokalnom skupu. Potrebno je promeniti slojeve izlaganja, a ne obrisati stručne detalje.

Ponovljene metanapomene poput „ovo nije schema/implementacija“ mogu se sažeti u zajedničko uputstvo. Reprezentativna mesta su [globalna pretraga](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/18-globalna-pretraga.md:55), linije 55–74, i [licence/provenance](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/21-licence-fair.md:150), linije 150–162. To je konkretna primena Z03: uklanja se ponavljanje o vrsti dokumenta, dok granice naučnog zaključka i prava ostaju.

## Plan izmena po prioritetu

P0/P1/P2 ispod su urednički prioriteti za unapređenje teorije. Ne propisuju arhitekturu ili redosled razvoja aplikacije. Sve oznake nalaza upućuju na šestodelni opis iznad.

| Red i prioritet | Paket | Nalazi | Konkretan rezultat izmena | Kako proveriti da je dovoljno |
|---|---|---|---|---|
| 1 — P0 | Putanja i male kontradikcije | Z01, H06, H13, M13 | usklađen vodič/meni; drugi prolaz kroz periodične interakcije; uklonjeni neobjašnjeni skorovi; precizan trening skup | početnik zna sledeći korak; svaki broj primera ima značenje, jedinicu ili definisanu funkciju |
| 2 — P0 | Temelji za obavezno gradivo | Z02, H01–H04, H09–H10 | kratak matematički most; Lewis/protonacija i π primer; orbitalna skica; talasni i termodinamički primer | polaznik izvodi jednostavan novi slučaj, ne samo prepričava rešenje |
| 3 — P0 | Povezano strukturno poređenje | Z04, H08, M03–M04 | jedna studija component→atom→3D→packing; mali supercell i periodični graf primer | razlikuje promenu zapisa od promene strukture, dozvoljenu mapu od povoljnog ali pogrešnog RMSD-a |
| 4 — P0 pre modelskih zaključaka | Učenje i evaluacija | M01, H14–H15, M10–M11 | ručni trening; macro/micro; jedinica resamplinga; kalibracioni tok; interval i odluka | bira model samo na razvojnom delu, navodi denominator i nezavisnu jedinicu, pravilno tumači neodlučan rezultat |
| 5 — P1 | Retrieval i rangiranje | M06–M07 | jedna zajednička ilustracija pretrage i tri zapisa ranking supervizije | objašnjava gde nastaje candidate miss i razlikuje App 2 par od ranking preferencije |
| 6 — P1 pre odgovarajuće grane | Specijalistički mostovi | M02, M05, M08–M09, M14, H11–H12 | kernel/SOAP skica, dva loss računa, legenda transformacija, Mogul/HBP interpretacija | ume da objasni ulaz→postupak→izlaz izabrane metode i njene granice; ne mora izvoditi sve metode |
| 7 — P2, delom paralelno | Uredničko rasterećenje i povratna informacija | Z03, H05, H07, H16, M12 | osnovni i referentni sloj, kraće metanapomene, legende, fiksni zadaci i rubrike | prvi prolaz je kraći; ključne provere imaju proverljiv uzor odgovora; tehnički dokazi ostaju dostupni |

Paket 1 može odmah da se uradi i nezavisno proveri. Paketi 2 i 3 popravljaju glavne konceptualne zavisnosti. Paket 4 treba završiti pre izvođenja naučnih zaključaka iz modelskih rezultata. Paket 6 nije razlog da se odlaže svaki osnovni korak: obrađuje se pre konkretne metode, a HBP dobija raniji prioritet ako je polimorfni rizik centralna projektna tema. Rubrike iz M12 treba dopunjavati uz svaki paket, iako je završna provera nastavne ujednačenosti u poslednjem redu.

Za prve četiri grupe izmena nisu potrebne nove liste algoritama, dodatni bibliografski katalozi niti proširivanje svih poglavlja. Premeštanjem postojećih objašnjenja i sažimanjem ponovljenih metanapomena može se osloboditi značajan prostor za predložene primere.

## Predloženi redosled čitanja posle izmena

Ovo je uređena nastavna ruta kroz postojeće celine. Nije potrebno fizički preimenovati sve fajlove; precizne putanje i oznake prvog/drugog prolaza mogu postići isti cilj.

1. **Orijentacija:** naslovne strane, mapa projekta i scope; detaljne algoritamske tabele za sada služe prepoznavanju tema.
2. **Osnovni jezik:** hemija 1–4 i ML00a §1–5, sa matematičkim mostom i malim primerom treninga. Hemijski i ML pojmovi mogu se učiti paralelno.
3. **Koordinacija:** hemija 5–6, sa nabojem i oksidacionim bilansom pre dⁿ/ligandnog polja.
4. **Od interakcije do periodičnosti:** kvalitativni deo 7 → osnovni koordinatni deo 8 → simetrija 9 → povratak na kvantitativne kontakte i njihov kriterijum u 7. Kratko značenje occupancy/s.u. uvesti uz primer, a puno tumačenje ostaviti poglavlju 10.
5. **Eksperiment i čvrste forme:** hemija 10–11, sa hkl/talasnim i termodinamičkim međukoracima.
6. **Empirijske reference:** ML00a §6–7 i logistički minimum iz ML02 §2.2 → hemija 11A. To priprema statistički i HBP jezik bez čitanja svih klasičnih modela unapred.
7. **Digitalni objekat:** hemija 12/12A/13 → 14–15. Annotirani CIF može i ranije da se pregleda radi orijentacije, bez uslova da se odmah razume svaki tag.
8. **Populacija i uslovi upotrebe:** hemija 16–17 i 21 + ML09; glavni tok poglavlja 17 čita se pre referentnih tabela.
9. **Determinističko poređenje:** hemija 19 + ML04, sa zajedničkom studijom Z04 i periodičnim grafom uvedenim pre njegove upotrebe. SOAP i slične alternative imaju posebno označen preduslov.
10. **Osnovna evaluacija:** hemija 20 i odgovarajući evaluacioni delovi ML06, naročito §6.8–6.12. Oni treba da budu dostupni bez pretpostavke da je pročitan ceo deep deo.
11. **Modeli i pretraga:** preostali osnovni klasični ML02 → hemija 18 i ML03; boosting prethodi naprednom learning-to-rank objašnjenju.
12. **Napredni strukturni ML:** ML00a §8 kao podsetnik → ML05 → preostali ML06, uz kernel/transformacioni/loss most potreban izabranoj porodici.
13. **Završna teorijska sinteza:** hemija 22 i kompletna ML10 uporedna mapa. Osnovne granice structure–property, polimorfnog rizika i FL-a ostaju deo razumevanja izvora; detaljne metode se proučavaju kada postanu relevantne.
14. **Uslovni jezički sloj:** ML00a §9 → ML07; ML08 kao prateća bezbednosna/pravna referenca. Na kraju kapije sa fiksnim sintetičkim zadacima i završna konceptualna odbrana.

## Oblasti koje su već dovoljno dobro objašnjene

| Oblast | Zašto sada funkcioniše | Šta sačuvati |
|---|---|---|
| Sastav, graf, konformer, kristal i eksperimentalni model | jasno se razlikuju objekti i posledice gubitka informacije | uvodne mape i poređenje pet nivoa; ne dodavati nove varijante iste liste |
| Rezonanca i digitalno tipovanje | nitro-primer razdvaja fizičku delokalizaciju od neispravnog zapisa | konkretan primer u hemiji 2, posle dopune Lewisove osnove |
| VSEPR domen naspram oblika molekula | CH₄/NH₃/H₂O daju jasnu zajedničku osnovu | postojeća tabela i razlika domena i vezanih atoma |
| Konfiguracija/konformacija i granice RMSD-a | objašnjeni su mapiranje, refleksija, okvir i vremenska skala | hemiju 3; dodati primenu, ne novu opštu definiciju |
| Prisustvo metala naspram stvarne DAP koordinacije | pozitivni primeri, kontraprimeri i nepovezani 4M uslov imaju različite jasne uloge | hemiju 5–6 i 16–17; ponavljanje ovde ima nastavnu svrhu |
| CN, denticitet i τ₅ | postoje definicije i konkretan račun geometrijske mere | ne uvoditi katalog svih oblika i indeksa samo radi potpunosti |
| Frakcione/kartezijanske koordinate, gustina, ASU i specijalne pozicije | postoje razrađeni računi i smisleno brojanje | sačuvati sadržaj hemije 8–9, popraviti raspored |
| Kvalitet kristalografskog modela | R/wR/GoF, s.u., occupancy i constraint/restraint se ne poistovećuju | ne pojednostavljivati u univerzalan quality prag |
| Simulirani naspram izmerenog PXRD-a | eksplicitno je odvojena izvedena simulacija od nezavisne eksperimentalne potvrde | postojeću epistemološku granicu |
| Formati, annotirani CIF i standardizacija | jasno je šta format čuva, gubi, dodeljuje i ostavlja nepoznatim | hemiju 12/12A/13; ne dopunjavati sintetički CIF izmišljenim eksperimentom |
| Referentna populacija, MAD i kružne torzije | postoje brojčani primer, MAD=0 i granice interpretacije outlier-a | dopuniti samo vezu sa alatima/mrežom, ne nova opšta upozorenja |
| Feature/target/label, skaliranje i Tanimoto | ML00a sadrži razumljive definicije i dobre male račune | ne prijavljivati ih kao odsutne niti ponavljati iste račune |
| Tri nivoa retrieval uspeha | jasno se razlikuju exact susedi, kandidati po ekspertu i konačni rang | naročito primer candidate miss-a koji reranker ne može popraviti |
| nDCG i IDCG | postoji gain funkcija i numerički račun nad jasno opisanim korpusom | nije potrebna nova uvodna nDCG lekcija |
| Naučna relacija naspram statusa računanja | missing/ambiguous/not-applicable/timeout se ne pretvaraju u negativnu labelu | dosledan statusni model kroz ML04/06/09 |
| Identiteti, familije, splitovi i cross-format populacija | 1D/2D sheme i problem zajedničkih endpoint-a konkretno su opisani | dopuniti resampling i zaključivanje, ne duplirati objašnjenje leakage-a |
| Jezički sloj i dokumentacioni retrieval | RAG nije kristalna pretraga; BM25/RRF imaju definicije i granice | nema potrebe širiti SLM/LLM deo u opšti kurs transformera |
| Poreklo podataka, FAIR, prava i uslovne teme | odvojene su naučna validnost, dopuštena upotreba i vendor tvrdnje | sažeti ponovljene metanapomene, a sačuvati sadržaj i uslovnost FL-a |

Nisu potrebne dodatne obavezne lekcije o svim 230 prostornim grupama, punoj kvantnoj hemiji, svim organskim mehanizmima, izvođenju svakog encodera ili celokupnoj kriptografiji FL-a. Takav dodatak ne rešava identifikovane nedostatke.

## Kriterijum da je teorijska dorada završena

Revidirana dokumentacija je dovoljno unapređena kada samostalan čitalac na novom malom primeru može da:

- iz formule izvede jednostavan elektronski račun i objasni donorsku ulogu;
- pronađe periodičnog suseda tek nakon razumevanja ćelije i simetrije;
- razlikuje istu strukturu u drugom zapisu od stvarno drugačije strukture;
- objasni izbor komponenti i atoma, izračuna mali RMSD i odvoji ga od packing zaključka;
- pokaže koji parametar model uči i kako se ocenjuje na novom primeru;
- razlikuje candidate miss, loš rang i pogrešnu naučnu labelu;
- navede šta ulazi u denominator, šta je nezavisna jedinica i šta interval dozvoljava da se zaključi;
- obrazloži kada su dodatna metoda, dodatni podatak ili uzdržavanje potrebni.

To se može proveriti kroz nekoliko fiksnih sintetičkih zadataka i kratkih rubrika. Merilo uspeha je prenos razumevanja na novi primer, a ne veći broj stranica ili više stručnih termina.

## Evidencija obuhvata

Sve sledeće Markdown stranice pregledane su u izvornom obliku. Rečnik, podsetnik, izvori, zablude, vežbe i rešenja korišćeni su i za proveru da li glavni tekst već ima potrebnu potporu. Spoljni izvori navedeni u njima nisu svi zasebno revidirani.

### chemistry-foundations — 36 stranica

- [01-atomi-joni-formule.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/01-atomi-joni-formule.md)
- [02-veze.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/02-veze.md)
- [03-geometrija.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/03-geometrija.md)
- [04-organska.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/04-organska.md)
- [05-kompleksi.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/05-kompleksi.md)
- [06-dap-schiff.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/06-dap-schiff.md)
- [07-interakcije.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/07-interakcije.md)
- [08-celija.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/08-celija.md)
- [09-simetrija.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/09-simetrija.md)
- [10-difrakcija-kvalitet.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/10-difrakcija-kvalitet.md)
- [11-cvrste-forme.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/11-cvrste-forme.md)
- [11a-referentne-raspodele-hbp.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/11a-referentne-raspodele-hbp.md)
- [12-formati.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/12-formati.md)
- [12a-anatomija-cif.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/12a-anatomija-cif.md)
- [13-standardizacija.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/13-standardizacija.md)
- [14-reprezentacije.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/14-reprezentacije.md)
- [15-slicnost.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/15-slicnost.md)
- [16-csd-conquest.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/16-csd-conquest.md)
- [17-lokalni-skup.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/17-lokalni-skup.md)
- [18-globalna-pretraga.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/18-globalna-pretraga.md)
- [19-parovi.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/19-parovi.md)
- [20-evaluacija.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/20-evaluacija.md)
- [21-licence-fair.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/21-licence-fair.md)
- [22-whitepaper-tokovi-fl.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/22-whitepaper-tokovi-fl.md)
- [dijagnostika.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/dijagnostika.md)
- [index.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/index.md)
- [izvori.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/izvori.md)
- [kako-koristiti.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/kako-koristiti.md)
- [laboratorije.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/laboratorije.md)
- [mapa-projekta.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/mapa-projekta.md)
- [plan-ucenja.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/plan-ucenja.md)
- [podsetnik.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/podsetnik.md)
- [recnik.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/recnik.md)
- [resenja.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/resenja.md)
- [zablude.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/zablude.md)
- [zavrsni-projekat.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/chemistry-foundations/docs/zavrsni-projekat.md)

### ml-ai-strategy — 15 stranica

- [00-scope.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/00-scope.md)
- [00a-osnove-ml.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/00a-osnove-ml.md)
- [01-pipeline-decision-map.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/01-pipeline-decision-map.md)
- [02-classical-ml.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/02-classical-ml.md)
- [03-global-retrieval-ann-ranking.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md)
- [04-precise-pairwise.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/04-precise-pairwise.md)
- [05-periodic-crystal-encoders.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/05-periodic-crystal-encoders.md)
- [06-metric-learning-and-evaluation.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md)
- [07-local-slm-rag.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/07-local-slm-rag.md)
- [08-api-llm-security.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/08-api-llm-security.md)
- [09-cross-format-eligibility.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/09-cross-format-eligibility.md)
- [10-optimal-stack-roadmap.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/10-optimal-stack-roadmap.md)
- [11-ml-ai-plan-ucenja.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/11-ml-ai-plan-ucenja.md)
- [evidence-method.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/evidence-method.md)
- [index.md](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory-3/ml-ai-strategy/docs/index.md)

Dodatno su provereni README i obe MkDocs konfiguracije radi predviđenog toka čitanja. Generisani PDF-ovi, aplikacioni runtime resursi i nedostupni projektni podaci nisu bili predmet duplog sadržajnog pregleda.
