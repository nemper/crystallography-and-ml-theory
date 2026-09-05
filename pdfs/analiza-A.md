# Analiza teorijske osnove i plan unapređenja

**Repozitorijum:** `C:\Users\Korisnik\Desktop\crystallography-and-ml-theory`  
**Pregledano stanje:** commit `a5f1ba01dcb57794b39ef37b21798f45fce78ffa`, 5. septembar 2026.  
**Predmet:** razumljivost, redosled preduslova i pedagoška potpunost hemijske i ML/AI teorije.

## 1. Objedinjena procena

Teorija ima veoma dobru metodološku osnovu: dosledno razlikuje hemijski objekat, njegov eksperimentalni model, računarsku reprezentaciju i zaključak koji je na osnovu nje opravdan. Posebno su jaki kontrola identiteta, razdvajanje statusa od rezultata, preciziranje značenja sličnosti i evaluacija bez curenja podataka.

Glavni nedostatak je nesklad između obećane početničke putanje i pojedinih objašnjenja. Tekst ponegde detaljno razmatra ograničenja metode pre nego što čitalac vidi njen osnovni postupak. Na drugim mestima postoji dobra osnova, ali dolazi posle prve zahtevne primene. Posledica može biti čitalac koji ume da nabroji uslove i rizike, ali ne ume da sprovede mali primer ili obrazloži izbor metode.

**Najpre treba popraviti:** Lewisovo elektronsko knjigovodstvo; redosled periodičnih kontakata prema ćeliji i simetriji; prelaz sa periodičnih slika na označene grafove; osnovni račun dodele komponenti; nekoliko uskih grla u difrakciji i termodinamici. Za učenje modela dodatno su potrebni primeri prolaska kroz GNN, računanja loss-a i postupka kalibracije.

Nije potreban novi udžbenik niti ravnomerno proširivanje svih poglavlja. Najveći dobitak doneli bi premeštanje postojećih objašnjenja, nekoliko malih izvedenih primera i jasnije odvajanje osnovne od uslovne napredne putanje.

### Obuhvat i način procene

Pregled obuhvata svih **51 Markdown izvornih dokumenata** u oba teorijska dela: 36 u hemiji i 15 u ML/AI, uključujući planove, dijagnostiku, laboratorije, rešenja, rečnik, mape i izvore. Provereni su i README i navigacioni fajlovi. Pojavljivanje termina proveravano je kroz povezane dokumente, kako kasnije ili ranije postojeće objašnjenje ne bi bilo pogrešno prijavljeno kao potpuno odsutno.

PDF-ovi koji ponavljaju izvorni sadržaj nisu analizirani zasebno. Odsustvo `.cif`, `.mol` i srodnih priloga **nije nijedan od nalaza**. Preporučeni primeri mogu se napraviti iz već odštampanih podataka ili kao jasno označene sintetičke ilustracije.

Ovo je pedagoški i konceptualni pregled, uz ciljanu proveru stručnih definicija u primarnim izvorima. Nije ponovljena empirijska analiza nedostupnih struktura, statistika lokalnog korpusa ili svih radova iz bibliografije. Brojevi linija upućuju na pregledano stanje izvora. Repozitorijum nije menjan.

### Značaj nalaza

- **Kritičan za određeni lanac razumevanja:** nedostaje preduslov bez kog početnik ne može samostalno proći konkretnu osnovnu temu. Ne znači da je čitav projekat tehnički neispravan.
- **Važan:** realno otežava razumevanje ili obrazložen izbor metode; rešiti pre korišćenja te grane.
- **Koristan za poboljšanje:** uklanja lokalnu apstrakciju, neujednačenost ili nepotreban napor.
- **Manja sugestija:** mala terminološka, simbolička ili navigaciona korekcija.

Značaj i projektni prioritet nisu isto: važna dopuna za SOAP ili RAG može sačekati ako ta metoda nije izabrana.

## 2. Zajednički nalazi

### Z01 — Putanja čitanja nije dovoljno jednoznačna

**Mesto:** [ML navigacija, redovi 40–62](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/mkdocs.yml:40); [ML plan, redovi 23–50](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/11-ml-ai-plan-ucenja.md:23); [hemijski plan](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/plan-ucenja.md:15); [Kapija B](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/dijagnostika.md:37).

**Problem i posledica:** navigacija vodi kroz ML 02→03→04, a plan izričito zahteva 04→03→02. Plan već razlikuje obavezno, preporučeno i referentno i predviđa dva čitanja uporedne mape, ali ne određuje dovoljno precizno koje sekcije čine prvi prolaz. Sva hemijska poglavlja 1–22 ostaju obavezna, iako deo završnih tema obrađuje uslovne pravce. Sažeta tabela plana stavlja ML 09 posle hemije 17, dok detaljna razrada u redovima 143–153 deo ML 09 traži već nakon hemije 13. Kapija B, tematski vezana za 3D i koordinaciju, uključuje polimorf bez jasne oznake da taj zahtev čeka obradu u 11. Čitalac ne zna da li sme da preskoči trenutnu tehničku prepreku ili mora da je savlada.

**Prećutno predznanje:** sposobnost samostalnog rekonstruisanja preduslova i procene koje napredne metode su relevantne projektu.

**Konkretna izmena:** usaglasiti navigaciju sa jednom preporučenom putanjom; navesti tačne sekcije za prvo i drugo čitanje. Razdvojiti osnovni deo 04 od SOAP/kernel dodataka koji zavise od 02. U 22 zadržati obavezno kratko razgraničenje naučnih tvrdnji, a detalje uslovnih grana označiti kao takve. Kapije postaviti iza poslednjeg neophodnog preduslova.

**Značaj: važan.** Ne uklanjati postojeći sistem kapija; učiniti ga doslednim.

### Z02 — Matematički početak obećava manje predznanja nego što ubrzo zahteva

**Mesto:** [00a-osnove-ml.md:3, 82–96 i 193–207](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/00a-osnove-ml.md:82).

**Problem i posledica:** uvod kaže da su dovoljni razlomci, a ubrzo koristi logaritam, eksponencijalnu i logističku funkciju, cross-entropy i softmax. Značenje loss-a, gradijenta i softmax-a jeste objašnjeno, ali funkcije od kojih se formule grade nemaju numerički most. Početnik može prihvatiti tvrdnju da se samouverena greška više kažnjava, a da ne ume da je proveri.

**Prećutno predznanje:** ponašanje `log p` kada se p približava nuli; eksponencijalno pretvaranje skorova u pozitivne težine; normalizacija njihovim zbirom.

**Konkretna izmena:** dodati mali okvir: za pozitivnu labelu uporediti p=0,9, 0,5 i 0,1 i odgovarajuće vrednosti −ln(p); definisati prirodni logaritam. Na dva skora pokazati eksponenciranje i deljenje zbirom. Definisati logit pre kasnije kalibracije. Za gradijent zadržati postojeću intuiciju; nije potreban kurs diferencijalnog računa.

**Značaj: važan**, naročito za kasnije M13 i M05. Vektori, norma, skalarni proizvod i osnovna SVD uloga već imaju dovoljan pojmovni uvod.

### Z03 — Nedostaje jedan završen primer koji povezuje oba kursa

**Mesto:** [hemija 15:90–105](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/15-slicnost.md:90), [19:61–113](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/19-parovi.md:61), [20:37–49](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/20-evaluacija.md:37); [ML 09:144–163](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/09-cross-format-eligibility.md:144); [ML 00a:135–147](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/00a-osnove-ml.md:135).

**Problem i posledica:** postoji mnogo korisnih lokalnih primera, uključujući odličan brojčani primer tri nivoa retrieval-a. Ipak, nijedan mali skup ne prolazi ceo lanac: naučno pitanje → objekti i njihove reprezentacije → primenljivost → mapiranje → skorovi → stručna oznaka → kandidati → evaluacija. Zato se isti rečnik može razumeti lokalno, a izgubiti pri prelasku između hemije i ML-a.

**Prećutno predznanje:** povezivanje jedinice analize, imenilaca različitih coverage/recall mera, više zapisa istog objekta i oznake relevantnosti.

**Konkretna izmena:** koristiti jedan sintetički skup od 3–5 objekata kroz odabrane postojeće primere. Pokazati da skup objekata sa bar jednom upotrebljivom granom nije isto što i presek objekata sa svim granama; zatim pratiti jedan propušten kandidat i jedan uspešno ocenjen par. Oznake dati prema kratkoj rubrici, uz konkretno obrazloženje. Ovo je zajednička ilustracija i ne zahteva projektovanje implementacije.

**Značaj: važan za povezivanje celina.** Zameniti deo fragmentisanih ponavljanja tim primerom, umesto dodavanja paralelnog kursa.

### Z04 — Ponavljanje ograda i terminološka gustina povremeno zaklanjaju naučnu ideju

**Mesto:** primeri u [hemiji 13:137](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/13-standardizacija.md:137), [18:55–76](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/18-globalna-pretraga.md:55), [20:170–181](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/20-evaluacija.md:170), [22:124](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/22-whitepaper-tokovi-fl.md:124), [ML planu:9–10, 269](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/11-ml-ai-plan-ucenja.md:269).

**Problem i posledica:** često se ponavlja da tekst nije implementacija, šema ili realizacioni plan. Uz to, dugi pasusi mešaju srpske i engleske stručne izraze. Rečnik postoji i obiman je, ali njegovo postojanje ne uklanja napor stalnog prebacivanja iz objašnjenja u referencu.

**Prećutno predznanje:** stručni engleski iz nekoliko disciplina i sposobnost razlikovanja opšte uredničke ograde od ograničenja konkretnog naučnog zaključka.

**Konkretna izmena:** opštu granicu zadatka navesti centralno i linkovati; lokalno sačuvati ograde koje menjaju dozvoljeno tumačenje rezultata. Pri prvoj upotrebi dati srpsko objašnjenje i originalni termin, a zatim koristiti dosledan naziv. Ne prevoditi nasumično formalne statuse i nazive algoritama. Posebno teške odlomke razložiti na „ideja → mali primer → uslovi → napredna napomena“.

**Značaj: koristan za poboljšanje.** Ovo nije preporuka za uklanjanje naučnih ograničenja ili celog postojećeg rečnika.

## 3. Hemijski deo

### H01 — Lewisov prikaz i valenca nemaju dovoljno početnog elektronskog knjigovodstva

**Mesto:** [01-atomi-joni-formule.md:23–35](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/01-atomi-joni-formule.md:23); [02-veze.md:16–38](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/02-veze.md:16); [Kapija A:28–35](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/dijagnostika.md:28).

**Problem i posledica:** crte i tačke su objašnjene, a formula formalnog naboja i obrađeni primeri postoje. Međutim, oktet je samo imenovan; nema dovoljnog pravila za dobijanje početnog broja valentnih elektrona i sastavljanje jednostavne Lewisove strukture. Kapija potom zahteva valencu i naboj. Čitalac može računati iz gotovog crteža, ali ne i proveriti da li je crtež moguć.

**Prećutno predznanje:** valentni elektroni glavnih grupa, duet vodonika, oktet C/N/O, deljeni i slobodni parovi; razlika valence i naboja.

**Konkretna izmena:** mala tabela H/C/N/O i jedan izveden prelaz NH₃→NH₄⁺ ili H₂O→OH⁻, od ukupnog broja elektrona do veza, slobodnih parova i naboja. Navesti granice tih početnih obrazaca. Zadržati već dobar nitro-primer kao sledeći korak.

**Značaj: kritičan za početnički hemijski lanac**, jer se prenosi na protonaciju, donorstvo i razumevanje grafovske validacije.

### H02 — Hückelovo pravilo nije povezano sa brojanjem π-elektrona

**Mesto:** [02-veze.md:71–79](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/02-veze.md:71); [04-organska.md:80–87](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/04-organska.md:80).

**Problem i posledica:** σ/π i konjugacija jesu uvedeni, ali izraz 4n+2 ne objašnjava jasno šta se broji i šta je n. Kasnije razlikovanje piridinskog i pirolskog N pretpostavlja razumevanje učešća slobodnog para u π-sekstetu. Pravilo donorstva lako postaje činjenica za memorisanje.

**Prećutno predznanje:** brojanje elektrona u zatvorenom konjugovanom π-sistemu i razlikovanje tog broja od svih valentnih elektrona.

**Konkretna izmena:** definisati n kao nenegativan ceo broj, pokazati benzen 6=4·1+2 i nacrtati po jedan piridinski/pirolski prsten sa označenim slobodnim parom. Objasniti koji par je deo π-sistema. Ne širiti u katalog aromatičnih izuzetaka.

**Značaj: važan** za donor/akceptor karakteristike i atom-tipove.

### H03 — Isti termin „donor“ koristi se za dve različite uloge

**Mesto:** [04-organska.md:9–26 i 39–51](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/04-organska.md:9); puna H-veza tek u [07-interakcije.md:91–109](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/07-interakcije.md:91).

**Problem i posledica:** tabela zajedno koristi H-bond donor/acceptor i metalni donor; zatim Lewisova baza postaje donor elektronskog para. Razlika nije naglašena pri prvoj zajedničkoj upotrebi. Čitalac može pogrešno zaključiti da raspoloživ slobodni par znači i H-donorstvo.

**Prećutno predznanje:** H-donor tipično nosi odgovarajuću X–H grupu; koordinacioni donor daje raspoloživ elektronski par metalu.

**Konkretna izmena:** pre tabele uporediti `N:→M` i `D–H···A`. Na karbonilnom O pokazati da H-akceptor/metalni donor nije automatski H-donor. U tabeli dosledno označiti tri uloge. Kasniji odeljak o geometriji vodoničnih veza ostaje.

**Značaj: važan**, jer te uloge kasnije postaju pretraživački uslovi i deskriptori.

### H04 — Ligandno polje dolazi pre dovoljne osnove za popunjavanje orbitala

**Mesto:** [05-kompleksi.md:158–184](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/05-kompleksi.md:158); bilans oksidacionog stanja u [210–242](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/05-kompleksi.md:210).

**Problem i posledica:** minimalni ligand-field most zaista postoji, ali brzo uvodi d-orbitale, t₂g/e_g, d-broj, pairing, high/low spin, degeneraciju i antibonding. D-brojanje prethodi izvedenom bilansu oksidacionog stanja, uz link unapred. Nema jednog popunjavanja koje objašnjava izbor između uparivanja niže i zauzimanja višeg nivoa.

**Prećutno predznanje:** orbitalna popunjenost, nespareni elektroni, energetski nivoi i približno jonsko brojanje d-elektrona.

**Konkretna izmena:** bilans naboja/oksidacionog stanja premestiti pre d-brojanja. Dodati jedan oktaedarski d⁶ high/low-spin dijagram i objasniti konkurenciju razdvajanja nivoa i energije uparivanja; degeneraciju definisati kao jednakost energija. Sačuvati ograničenja zaključivanja o Jahn–Teller efektu. Puna kvantna teorija nije potrebna.

**Značaj: važan**, posebno zato što se ovaj sadržaj pojavljuje u obaveznom ishodu lekcije.

### H05 — Mehanizam Schiffove baze preskače osnovni reakcijski rečnik

**Mesto:** [06-dap-schiff.md:28–51](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/06-dap-schiff.md:28); dodatna upotreba elektrofilnosti u [07:133–135](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/07-interakcije.md:133).

**Problem i posledica:** nukleofilni napad, elektrofilni C, tetraedarski intermedijer i karbinolamin pojavljuju se bez lokalne definicije. Lewisov model iz 04 mogao bi da bude most, ali ta veza nije izrečena. Lista koraka deluje izvedeno iako početnik ne zna šta se tokom „napada“ menja.

**Prećutno predznanje:** pravljenje veze elektronskim parom, polaritet karbonila, adicija, prenos protona i eliminacija.

**Konkretna izmena:** dve definicije povezati sa Lewisovom bazom/kiselinom i dodati jednostavnu šemu karbonil→C(OH)(NHR)→imin. Alternativno mehanistički pasus označiti opcionim, a obavezno zadržati već dobro objašnjenu neto kondenzaciju i bilans atoma.

**Značaj: koristan za poboljšanje.** Nema opravdanja za dodavanje celog kursa organskih mehanizama.

### H06 — Periodični kontaktni račun prethodi ćeliji, simetriji i kvalitetu modela

**Mesto:** [07-interakcije.md:16–33, 165–254](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/07-interakcije.md:16); preduslovi u [08:146–280](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/08-celija.md:146), [09:135–205](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/09-simetrija.md:135) i poglavlju 10.

**Problem i posledica:** eksplicitni „minimalni kristalografski most“ daje notaciju, ali istovremeno pretpostavlja ASU, centriranu ćeliju, specijalna mesta, occupancy, disorder i ekvivalentnost zapisa operacije. Njihova stvarna obrada dolazi kasnije. Čitalac mora da traži više kasnijih objašnjenja pre završetka punog računa u 07.

**Prećutno predznanje:** frakcione/kartezijanske koordinate, metrika kose ćelije, simetrijsko proširenje, jedinstvenost site-a i deduplikacija.

**Konkretna izmena:** podeliti 07 na hemijsku intuiciju interakcija i račun periodičnih kontakata. Drugi deo čitati posle 08/09 i potrebnih objašnjenja occupancy/disorder iz 10. U planu i kapijama pratiti taj red. Formule ostaviti na jednom glavnom mestu, sa povratnim linkovima.

**Značaj: kritičan za kontinuitet kristalografske putanje.** Postojeći N14 račun je koristan; problem je njegovo mesto, ne njegova zahtevnost.

### H07 — Coulombov i Lennard–Jones potencijal nemaju dovoljan rečnik parametara

**Mesto:** [07-interakcije.md:68–89](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/07-interakcije.md:68).

**Problem i posledica:** formule treba da pruže intuiciju, ali nisu neposredno razjašnjeni svi simboli i njihove jedinice. ε u LJ i permitivnosti u Coulombovom izrazu imaju različite uloge. Nije pokazano kako se iz LJ izraza čita privlačenje, odbojnost i optimalni razmak.

**Prećutno predznanje:** potencijalna energija i referentna nula, znak energije, permitivnost i parametri parnog potencijala.

**Konkretna izmena:** definisati q, r i konstante, pa na malom grafiku U(r) označiti odbojni deo, minimum i prilazak nuli. Objasniti ε kao dubinu jame i σ kao LJ razmak nulte energije. Sačuvati postojeće upozorenje da to nije potpuni model kristalne energije; izvod sile nije potreban.

**Značaj: koristan za poboljšanje.** Ako formule nisu ishod učenja, dovoljan je kvalitetan grafički prikaz.

### H08 — L4 traži dokaz dovoljnog opsega susednih slika bez obrađenog obrasca tog dokaza

**Mesto:** [08-celija.md:324–346](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/08-celija.md:324); [laboratorije.md:116–130](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/laboratorije.md:116); [resenja.md:89–91](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/resenja.md:89).

**Problem i posledica:** tekst pravilno kaže da 3×3×3 nije univerzalno dovoljno i L4 zaista zadaje cutoff od 4 Å. Međutim, zahtev „nakon provere dometa“ nije praćen demonstracijom šta predstavlja dovoljnu proveru. Čitalac zna koje pravilo ne sme slepo da koristi, ali nema obrazac prihvatljivog obrazloženja.

**Prećutno predznanje:** geometrijska granica broja translacionih slika ili jasna garancija odabrane procedure pretrage suseda.

**Konkretna izmena:** dati jednu izvedenu dovoljnu granicu za konkretnu ćeliju, npr. pomoću razmaka suprotnih ravni ćelije, i objasniti zašto se obuhvataju sve slike unutar cutoff-a. Navesti očekivani oblik odgovora u L4. Nije potrebna implementacija opšte biblioteke niti novi ulazni fajl.

**Značaj: važan za prohodnost L4**, nižeg opšteg prioriteta od H06.

### H09 — Promena baze i origina ostaje skup formula bez jednog povezanog primera

**Mesto:** [08-celija.md:348–388](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/08-celija.md:348); [09-simetrija.md:239–282](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/09-simetrija.md:239).

**Problem i posledica:** formule promene baze/koordinata i transformacije operacija postoje; unimodularnost takođe nije izostavljena. Nedostaje jedan račun u kome se zajedno menjaju ćelija, koordinate i operacija, uz proveru istog fizičkog ishoda. „Coset representative“ dodatno uvodi apstrakciju bez pomoći prvom primeru.

**Prećutno predznanje:** promena opisa naspram fizičke transformacije, translacione klase i redosled kompozicije.

**Konkretna izmena:** pokazati jednostavnu zamenu osa ili origin shift i proveriti isti položaj pre/posle delovanja simetrije. Za superćeliju dati 2×1×1 primer sa novim koordinatama kopija; apstraktni termin objasniti tek potom. Ne ponavljati već odličan C1 fractional→Cartesian račun. Razlikovanje promene baze i fizičkog pomeranja dosledno je i u [spglib definicijama](https://spglib.readthedocs.io/en/stable/definition.html).

**Značaj: koristan za poboljšanje** i važna priprema za M08.

### H10 — Difrakciona suma koristi hkl i fazu pre njihove fizičke pripreme

**Mesto:** [10-difrakcija-kvalitet.md:31–52](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/10-difrakcija-kvalitet.md:31); hkl u [73–113](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/10-difrakcija-kvalitet.md:73); sistematska odsustva u 123–134.

**Problem i posledica:** Braggov izraz, I∝|F|² i kompleksna suma dolaze pre objašnjenja Millerovih indeksa. Amplituda, faza i interferencija nisu dovoljno pripremljene pre faznog problema. Kasniji ispravan numerički hkl→d→2θ primer ne rešava taj prvi skok.

**Prećutno predznanje:** talasna dužina i ugao, sabiranje talasnih doprinosa, intenzitet naspram amplitude, kompleksni fazor i indeks refleksije.

**Konkretna izmena:** definisati λ/d/θ/n uz Braggovu skicu, a uvod u hkl pomeriti pre strukturnog faktora. Pre opšte sume pokazati dva doprinosa iste i suprotne faze, npr. +1/+1 i +1/−1. Tek tada objasniti zašto intenzitet ne daje sve fazne informacije. Nije potrebno puno Fourierovo izvođenje.

**Značaj: važan** za razumevanje difrakcije i granice između merenja i strukturnog modela.

### H11 — Termodinamički minimum preskače intuiciju pre hemijskog potencijala

**Mesto:** [11-cvrste-forme.md:143–161 i 199–239](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/11-cvrste-forme.md:143); korisna postojeća osnova u [recnik.md:449–456](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/recnik.md:449).

**Problem i posledica:** H/S su u glavnom tekstu uglavnom imenovani, a ubrzo se uvode hemijski potencijal i aktivnost vode. Dobro obrađen račun ΔG=1000−4T može se reprodukovati bez razumevanja fizičke konkurencije doprinosa. Intuicija entalpije/entropije postoji u rečniku, pa nije globalno odsutna; hemijski potencijal i aktivnost nisu dovoljno definisani.

**Prećutno predznanje:** ravnoteža, doprinos energije i dostupnosti mikrostanja slobodnoj energiji, otvoren sistem i razmena vode sa okolinom.

**Konkretna izmena:** kratku H/S intuiciju preneti pre računa, bez svođenja entropije na vidljivi nered. Posle primera istog sastava odvojiti „anhidrat + voda ⇌ hidrat“ i objasniti zašto uslovi okoline ulaze u poređenje. Složenije uslove rastvorljivosti staviti iza osnovne tvrdnje o ravnoteži.

**Značaj: važan** pre tumačenja stabilnosti i polymorph-risk signala. Postojeće ograde uz ΔH/ΔS/ΔCp treba sačuvati.

### H12 — HBP primer počinje izlaznim verovatnoćama pre konkretnog ulaznog opažanja

**Mesto:** [11a-referentne-raspodele-hbp.md:118–164](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/11a-referentne-raspodele-hbp.md:118).

**Problem i posledica:** fitting prilika i pozitivni/negativni ishod jesu definisani, ali odmah slede logistički model i već dobijene vrednosti 0,72/0,61. Nije pokazano šta predstavlja jedan red podataka na kojima se uči. Čitalac razume ograničenja izlaza, ali ne i iz kog tipa opažanja taj izlaz potiče.

**Prećutno predznanje:** jedinica opažanja za H-vezu, obeležja prilike i razlika neopaženog ishoda unutar definisane prilike od proizvoljno neoznačenog para.

**Konkretna izmena:** mala izričito sintetička tabela donora, akceptora, konteksta i ishoda; zatim povezati njen format sa jednim target parom u postojećem primeru. Jasno reći koji događaj p procenjuje. Ne predstavljati nastavnu tabelu kao stvarnu internu CCDC šemu.

**Značaj: koristan za poboljšanje.** Opšti uvod u logističku funkciju već postoji u ML 00a; potreban je domenski međukorak.

### H13 — ECFP postupak nema mali trag od molekulskog grafa do koda

**Mesto:** [14-reprezentacije.md:46–62](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/14-reprezentacije.md:46); primena u [15-slicnost.md:28–44](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/15-slicnost.md:28) i [ML 03:134–193](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:134).

**Problem i posledica:** iteracije, radijus/prečnik, bit/count zapis i kolizije su opisani. Brojčani primeri Tanimoto-a, međutim, počinju već zadatim aktivnim bitovima. Nema kratke ilustracije kako molekul postaje takav niz, pa ostaje praznina između hemijskog i skupovnog razmišljanja.

**Prećutno predznanje:** prikupljanje lokalnog atomskog okruženja, kodiranje njegovih svojstava i sažimanje u ograničen prostor.

**Konkretna izmena:** na C–C–O pokazati radijus 0 i 1, opis jednog okruženja, ilustrativni kod i odgovarajuću aktivnu poziciju. Kodove označiti kao nastavne, a ne stvarni izlaz određene implementacije. Na jednom sudaru povezati sa već objašnjenim ograničenjem, pa linkovati postojeći Tanimoto račun.

**Značaj: važan** za centralni lanac graf→fingerprint→pretraga.

### H14 — Profil sličnosti daje brojeve čije poreklo čitalac ne može da prati

**Mesto:** [15-slicnost.md:90–105](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/15-slicnost.md:90).

**Problem i posledica:** primer prikazuje, između ostalog, mapirani 3D skor 0,71 uz 28/34 atoma i RMSD 0,62 Å, kao i interaction-network skor 0,58. Nije data funkcija koja te podatke pretvara u prikazane skorove. Tekst kasnije kaže da formule treba definisati/kalibrisati, ali primer izgleda kao već izveden rezultat. To zamagljuje inače dobro objašnjenu razliku fizičke mere i skora.

**Prećutno predznanje:** proizvoljno odabrana ilustrativna skala, normalizacija i agregaciona funkcija koja nisu navedene.

**Konkretna izmena:** eksplicitno označiti nedovoljno definisane brojeve kao izmišljene ilustracije formata ili ih zameniti neposredno tumačivim RMSD-om, coverage-om i statusom. Ako je cilj računski primer, dati malu transparentnu nastavnu funkciju uz jasno ograničenje značenja.

**Značaj: koristan za poboljšanje.** Ne predlaže se univerzalni similarity skor niti tvrdnja da su brojevi empirijski pogrešni.

### H15 — MCAR pretpostavci nedostaje neposredna veza sa postojećim statističkim objašnjenjem

**Mesto:** [17-lokalni-skup.md:389–402](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/17-lokalni-skup.md:389); postojeći most u [ML 09:63](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/09-cross-format-eligibility.md:63).

**Problem i posledica:** hemijski pregled lokalnog skupa koristi MCAR i razvija naziv, ali ne daje neposredan pojmovni most do značenja te pretpostavke. ML 09 objašnjava mehanizme nedostajanja, ali može biti pročitan pre ili posle ovog mesta, zavisno od prikaza plana koji čitalac prati. Naziv „potpuno slučajno nedostajanje“ sam ne pokazuje po čemu se pretpostavka razlikuje od malog procenta nedostajućih vrednosti.

**Prećutno predznanje:** nezavisnost mehanizma nedostajanja od relevantnih vrednosti podataka i razlika mehanizma od procenta nedostajanja.

**Konkretna izmena:** uz MCAR dati jednu rečenicu značenja, primer vezan za izvoz i neposredan link ka postojećem ML 09 objašnjenju. Naglasiti da sama tabela nedostajanja ne dokazuje mehanizam. Nije potrebno ovde dodavati zasebnu obradu MAR/MNAR.

**Značaj: manja pedagoška i navigaciona sugestija**, povezana sa Z01. Nova teorijska oblast nije potrebna.

### H16 — Forenzički inventar lokalnog skupa preuzima tok glavne lekcije

**Mesto:** [17-lokalni-skup.md, §17.7:145–234](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/17-lokalni-skup.md:145), [§17.9:282–352](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/17-lokalni-skup.md:282) i [§17.10:354–372](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/17-lokalni-skup.md:354).

**Problem i posledica:** veoma detaljna, 552 reda duga analiza lokalnog skupa nosi mnogo korisnih brojki, identifikatora i poređenja izvoza. Pedagoška poenta — kako razlikovati trag izvoza, pogled na objekat, izbor uzorka i naučni zaključak — teže se prati kroz sve detalje. Tematske sekcije već postoje, ali nije označeno koji detalji pripadaju osnovnom prolazu, a koji služe proveri dokaza. Sama dužina nije problem.

**Prećutno predznanje:** čitalac već ume da prepozna koje stavke inventara dokazuju koji zaključak i šta može da preskoči.

**Konkretna izmena:** glavni tok organizovati oko 2–3 pitanja i završenih slučajeva, npr. N14, search1/search2 i zavisni višestruki pogledi. Potpune inventare, hash identifikatore i distribucione detalje premestiti u povezanu referentnu celinu. Sačuvati trag dokaza i postojeće brojke.

**Značaj: koristan za poboljšanje.** Ovo nije kritika odsutnih priloga niti zahtev za njihovim pribavljanjem.

### H17 — Grupni bootstrap je dobro zahtevan, ali nedovoljno demonstriran

**Mesto:** [20-evaluacija.md:164–166](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/20-evaluacija.md:164); ranija definicija u [ML 00a:189](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/00a-osnove-ml.md:189).

**Problem i posledica:** bootstrap i interval poverenja imaju definiciju u povezanom ML uvodu. Ipak, prelaz na grupno resamplovanje, uparenu razliku metoda i odvojene seed-ove nema primer. Čitalac može ponoviti pravilo „po grupama“, a ipak uzorkovati parove kao da su nezavisni.

**Prećutno predznanje:** jedinica nezavisnosti, uzorkovanje sa vraćanjem, upareno poređenje i različiti izvori varijabilnosti.

**Konkretna izmena:** na tri sintetičke grupe prikazati jednu bootstrap replikaciju sa ponovljenom grupom, iste izabrane grupe za oba modela i račun razlike metrike. Objasniti šta se ponavljanjem procenjuje i povezati sa M05, koji razdvaja interval metrike od intervala nove predikcije. Jedna replikacija služi demonstraciji, ne stvarnoj proceni intervala.

**Značaj: važan pre statističkog poređenja metoda.** Ne treba ponavljati već dobro objašnjene train/test i grupne podele.

## 4. ML/AI deo

### M01 — Tree ensemble porodice imaju više optimizacionih naziva nego objašnjenja učenja

**Mesto:** [02-classical-ml.md:103–109 i 136–157](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/02-classical-ml.md:103).

**Problem i posledica:** stablo i bootstrap imaju početnu definiciju. Extra Trees zatim poredi bias i varijansu, dok boosting brzo prelazi na histogram optimizacije, GOSS/EFB i ordered boosting. Nema zajedničkog primera koji pokazuje prosečavanje različitih stabala naspram sekvencijalnog popravljanja greške. Čitalac pamti porodice bez razloga za njihovo različito ponašanje.

**Prećutno predznanje:** varijabilnost modela između trening uzoraka, sistematska aproksimaciona greška, slab model i rezidual/trenutni gubitak.

**Konkretna izmena:** pokazati nekoliko stabala i njihov agregat, pa dve boosting iteracije na istim malim podacima. Definisati bias/variance u dve rečenice i odvojiti ih od selection bias-a. Bibliotečke optimizacije premestiti u opcioni okvir. Izraz „ceo razvojni uzorak“ za Extra Trees precizirati kao trening deo tekućeg fold-a.

**Značaj: važan** za tabularne referentne modele. Formalna dekompozicija greške nije potrebna.

### M02 — Kernel, Gram/PSD uslov i RBF parametri nisu povezani dovoljnim međukoracima

**Mesto:** [02-classical-ml.md:169–189](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/02-classical-ml.md:169); zavisnost u [04:413](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/04-precise-pairwise.md:413).

**Problem i posledica:** margina i kernel kao skalarni proizvod u transformisanom prostoru jesu uvedeni. Međutim, „pozitivno semidefinitna Gram matrica“ i tuning C/gamma dolaze bez dovoljnog značenja; formalni PSD uslov se pojavljuje tek kasnije uz SOAP. Čitalac ne zna zašto proizvoljan skor ne mora biti validan kernel niti šta hiperparametri menjaju.

**Prećutno predznanje:** matrica svih parnih kernel vrednosti, PSD, širina/lokalnost RBF-a, kazna za greške i SVR tolerisani pojas.

**Konkretna izmena:** mala tabela Kᵢⱼ=K(xᵢ,xⱼ), intuitivno značenje PSD zahteva i kratko značenje C, gamma i SVR tolerancije. Redosled neka bude linearna granica→transformisani prostor→uslov validnosti→parametri. Iz 04 linkovati ovu osnovu; ako se 04 čita prvi, SOAP pomeriti u drugi prolaz.

**Značaj: važan** za zajednički SVM/GPR/SOAP lanac. Ne treba dokaz spektralnih teorema.

### M03 — PCA/PCR/PLS se porede pre objašnjenja komponente

**Mesto:** [02-classical-ml.md:191–207](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/02-classical-ml.md:191), zatim 227–239.

**Problem i posledica:** osnovni mehanizam staje u razliku „varijansa X“ naspram „kovarijansa sa targetom“. Nisu dovoljno uvedeni projekcija, latentna komponenta i dodatni regresioni korak u PCR-u. Čitalac ne vidi koji deo uči samo iz X, a koji koristi y, pa ni zašto izbor broja komponenti pripada validaciji.

**Prećutno predznanje:** linearna kombinacija osobina, projekcija, varijansa/kovarijansa i razlika transformacije ulaza od predikcije.

**Konkretna izmena:** dve povezane kontinuirane kolone sažeti u jednu komponentu i uporediti tokove PCA: X→komponente; PCR: X→PCA→regresija; PLS: X i y→prediktivne komponente→regresija. Razviti pune nazive skraćenica. Takva razlika redukcije dimenzije i naredne upotrebe odgovara [zvaničnom PCA objašnjenju](https://scikit-learn.org/stable/modules/decomposition.html#pca).

**Značaj: važan unutar ove porodice**, ali projektni prioritet je uslovan. Izvođenje sopstvenih vektora nije neophodno.

### M04 — GPR preskače proces prelaska od pretpostavke do predikcije

**Mesto:** [02-classical-ml.md:209–225](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/02-classical-ml.md:209).

**Problem i posledica:** „raspodela nad funkcijama kroz kernel“ odmah prelazi na sredinu/varijansu, veličinu podataka, kubni trošak i Bayesian optimization. Ne vidi se kako posmatrane tačke menjaju skup mogućih funkcija. Upozorenje da model-based neizvesnost nije pouzdanost pod shift-om zato ostaje apstraktno.

**Prećutno predznanje:** prior/posterior, uslovljavanje opažanjima, neizvesnost funkcije i šum merenja.

**Konkretna izmena:** jedna skica mogućih funkcija pre podataka, opaženih tačaka i funkcija posle uslovljavanja. Označiti srednju krivu i raspon i povezati kernel sa pretpostavkom kako ulazi zajednički variraju. Aktivno učenje i Bayesian optimization označiti kao kasniji nastavak.

**Značaj: važan ako se GPR bira ili ozbiljno poredi.** Za deterministički projekat može ostati referentni modul.

### M05 — Kalibracija i conformal imaju dobra ograničenja, ali nemaju dovoljno jasan postupak

**Mesto:** [02-classical-ml.md:241–263](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/02-classical-ml.md:241); [06-metric-learning-and-evaluation.md:375–391](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:375).

**Problem i posledica:** značenje kalibracije, exchangeability i marginalnog coverage-a već postoji. Platt/isotonic/temperature scaling i conformal ipak se uglavnom predstavljaju kroz nazive i uslove. Nije pokazano šta se računa na izdvojenom kalibracionom skupu. Dodatno se lako mešaju verovatnoća klase, interval nove predikcije, interval poverenja metrike i coverage pri uzdržavanju od odluke.

**Prećutno predznanje:** post-hoc mapa skor→verovatnoća, zamrznuti logiti, rezidual/nonconformity, kvantil i razlika nove opservacije od procene uspeha metode.

**Konkretna izmena:** napraviti zajednički blok u 02: zamrznuti model daje skor s, a na posebnom kalibracionom skupu fituje se logistička mapa sigmoid(a·s+b); pokazati ulazne skorove i dobijene verovatnoće. Isotonic objasniti kao fleksibilniju monotonu mapu. Neuralni nastavak u 06 neka pokaže zamrznuti logiti→softmax(logiti/T), sa T fitovanim samo na kalibracionom skupu. Pozitivno T u tom postupku čuva izbor najvećeg logita, iako menja samouverenost; vidi [Guo et al.](https://arxiv.org/html/1706.04599v2). Odvojeno dati mali split-conformal primer prema jasno navedenom protokolu iz [Angelopoulos i Bates](https://arxiv.org/abs/2107.07511), bez obećanja podgrupnog jamstva koje tekst već ograničava. Kratkom tabelom razdvojiti izlaze i njihove imenioce, kao i kalibraciono T od trening temperature τ.

**Značaj: važan pre verovatnosnih i intervalnih tvrdnji.** Metode ne treba uvoditi ako izlaz projekta takav sloj ne zahteva.

### M06 — MinHash/LSH preskače prelaz od skupa okruženja do kandidata

**Mesto:** [03-global-retrieval-ann-ranking.md:306–318](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:306); ranije najave u 163 i 228.

**Problem i posledica:** MHFP6 je razložen do skupa molekulskih okruženja, a zatim se samo kaže da koristi MinHash i omogućava LSH. Potpis i njegovo korišćenje u kandidatskom indeksu nisu objašnjeni. Čitalac teško prati inače ispravno razdvajanje aproksimacije Jaccard-a i propuštanja kandidata.

**Prećutno predznanje:** slučajno hash/rangiranje članova skupa, sažeti potpis i kandidatske kante.

**Konkretna izmena:** mali tok skup→nekoliko MinHash minimuma→potpis→LSH kandidati→preciznije poređenje. Pokazati gde dužina potpisa menja grešku procene, a gde parametri indeksa menjaju izbor kandidata. Ne traži se verovatnosni dokaz ili kompletno izvođenje banding-a.

**Značaj: važan za ovu ANN alternativu**, uslovan dok nije deo izabranog rešenja. Opšte hashiranje i Tanimoto već su definisani.

### M07 — Dodela komponenti nema prvi izračunati primer globalnog uparivanja

**Mesto:** [04-precise-pairwise.md:116–155](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/04-precise-pairwise.md:116); raniji pojmovni oslonac u [hemiji 19:65–69](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/19-parovi.md:65).

**Problem i posledica:** hemijsko značenje cost funkcije i globalnog Hungarian optimuma je dato, ali nema primera zašto pojedinačno najbolji partneri mogu dati loše ukupno rešenje. Odmah slede unmatched trošak, min-cost flow, k-best, simetrične kopije i permutacione orbite. Osnovni problem još nije dovoljno konkretan da bi čitalac pratio njegove komplikacije.

**Prećutno predznanje:** bipartitno uparivanje, jednokratna upotreba partnera, zbirni trošak, dummy opcija i više jednakih optimuma.

**Konkretna izmena:** izračunati mali 2×2/3×3 slučaj sa jednim zabranjenim parom i opcijom neuparenosti. Uporediti lokalni izbor i globalnu mapu, pa tek onda pokazati alternativne optima. Odeliti multiplicitet/neuparenost od naprednog okvira o ekvivalentnim kopijama i Z′.

**Značaj: važan za osnovno poređenje parova**, jer pogrešno shvaćena komponentna mapa kvari tumačenje narednih atomskih i geometrijskih grana.

### M08 — Od periodične slike do quotient/gain grafa nedostaje zajednički obavezni most

**Mesto:** [04-precise-pairwise.md:173–175 i 247–249](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/04-precise-pairwise.md:173); kasniji delovi 325–366 i 464–473; [05-periodic-crystal-encoders.md:128–148](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/05-periodic-crystal-encoders.md:128).

**Problem i posledica:** exact graph matching već zahteva gauge/quotient/gain odnose, a unwrap traži cycle-consistent propagation pre organizovane obrade periodičnog grafa. Hemijski deo dobro uvodi periodične kontakte i promenu baze, ali to samo po sebi ne objašnjava kako beskonačna mreža postaje konačan graf sa translacionim oznakama. U 05 se dodaje opšta transformacija oznake ivice bez jednog malog računa.

**Prećutno predznanje:** predstavnik site-a, označena usmerena ivica, zbir translacija po putanji, izbor ćelijske kopije svakog čvora i broj nezavisnih prostornih pravaca.

**Konkretna izmena:** pre §4.5 napraviti jedan obavezan 1D primer A–B preko granice ćelije, konačan graf i njegov periodični nastavak. Za L=10 Å, sᵢ=0,9, sⱼ=0,1 i n=1 razmak je 2 Å; zapis istog j kao 1,1 uz n′=0 daje isti razmak. Potom u konačnom quotient grafu pokazati ciklus sa nultim i nenultim translacionim zbirom; u drugom slučaju njegova putanja u periodičnom prostoru povezuje različite ćelijske kopije. Definisati rang kao broj nezavisnih pravaca. Opšte formule ostaju; 04 i 05 linkuju isti primer.

**Značaj: kritičan za razumevanje periodičnih grafova, unwrap-a i topologije.** Nije tvrdnja da u tekstu nedostaju PBC, unimodularnost ili sve formule promene zapisa.

### M09 — SOAP/REMatch konstrukcija ostaje kraća od spiska njenih ograničenja

**Mesto:** [04-precise-pairwise.md:398–419](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/04-precise-pairwise.md:398).

**Problem i posledica:** glatka atomska gustina, power spectrum, kernel i entropy-regularized matching uvode se gotovo u jednom koraku. Slede detaljni parametri i opravdana PSD/stereo/Z′ ograničenja. Bez konstrukcionog primera čitalac teško razlikuje lokalni deskriptor, tabelu lokalnih sličnosti i globalni agregator.

**Prećutno predznanje:** glatka prostorna funkcija, približni bazni zapis, rotaciono sažimanje i meko uparivanje skupova okruženja.

**Konkretna izmena:** četiri slike/koraka: atomi→glatki oblaci→lokalni vektori→matrica sličnosti A/B→globalni agregator. Na 2×2 tabeli uporediti prosečavanje, strogo i raspodeljeno uparivanje. Napredne granice REMatch i adapted-average konstrukcija ostaviti posle ovog mosta. Ne izvoditi sferne harmonike ili Sinkhorn iteracije.

**Značaj: važan ako se SOAP bira.** Osnovni packing comparator treba razumeti pre ovog uslovnog dodatka.

### M10 — ANN memorijski detalji razvijeniji su od intuitivne pretrage istog skupa

**Mesto:** [03-global-retrieval-ann-ranking.md:236–304](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:236); postojeći projektni query u [642–664](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:642).

**Problem i posledica:** HNSW/IVF/PQ imaju kratka pojmovna objašnjenja, dok memorijski obračun sadrži mnogo više detalja. Čitalac može računati potrebne gigabajte, a ne pokazati gde se kandidat preskače ili gde se njegov skor približno menja. Tek kasnije dolazi koristan kompletan projektni upit.

**Prećutno predznanje:** kretanje kroz graf bliskosti, centroid/lista, codebook i aproksimativno rastojanje.

**Konkretna izmena:** sažeti postojeći query primer premestiti ranije. Na istom malom vektorskom skupu pokazati Flat proveru svih elemenata, IVF izbor lista, PQ sažimanje brojeva i HNSW obilazak grafa. Označiti mesto mogućeg gubitka kandidata ili promene poretka. Memorijske račune sačuvati kao referentni okvir.

**Značaj: koristan za poboljšanje.** Tekst već pravilno razlikuje IVF-Flat preskakanje lista od PQ kompresije i kaže da rerank ne vraća propuštene kandidate.

### M11 — Od GNN definicije do kataloga arhitektura nedostaje jedan kompletan prolaz

**Mesto:** [05-periodic-crystal-encoders.md:59–70, 98–124 i 235–280](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/05-periodic-crystal-encoders.md:59); raniji uvod u [00a:193–207](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/00a-osnove-ml.md:193).

**Problem i posledica:** message passing, pooling i attention jesu definisani. Specijalizovano poglavlje zatim mnogo detaljnije obrađuje builder, invarijanse i granice CGCNN/ALIGNN/Matformer tvrdnji nego sam prolaz od site/edge osobina do embeddinga. Čitalac može porediti rizike modela, a ne objasniti razliku njihovog unutrašnjeg računanja.

**Prećutno predznanje:** naučena poruka, agregacija, promena stanja čvora kroz sloj, determinističko rastojanje naspram naučene transformacije i konstrukcija line grafa.

**Konkretna izmena:** jedan troatomni ili metal–dva-donora primer: osobine→poruka na ivici→agregat u centru→novo stanje→pooling. Razlikovati zadate brojeve od naučenih parametara. Na istom primeru pokazati da veze postaju čvorovi line grafa, a ugao njegova ivica; attention predstaviti kao ponderisanje poruka. To prati zajednički message-passing okvir iz [Gilmer et al.](https://proceedings.mlr.press/v70/gilmer17a.html), bez tvrdnje da su sve arhitekture identične.

**Značaj: važan pre izbora ili poređenja neuralnih encodera.** Nije potreban ručni backpropagation.

### M12 — Nezavisne transformacije para i parity notacija dolaze pre malog kontraprimera

**Mesto:** [05-periodic-crystal-encoders.md:45–51 i 220–231](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/05-periodic-crystal-encoders.md:45); nastavak u [06:237–246](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:237).

**Problem i posledica:** hemijska hiralnost i osnovna invariansa postoje, ali pasus spaja SE(3)×SE(3), E(3), gauge, cross-attention i stereo gate. Oznake SO/O, SE/E i 0e/0o zahtevaju novi nivo formalizma. Nije odmah jasno zašto zajednička rotacija dva ulaza nije isti uslov kao njihove nezavisne rotacije.

**Prećutno predznanje:** grupe transformacija i njihov proizvod, proper rotacija/refleksija i pseudoskalar/parity.

**Konkretna izmena:** mini-tabela SO(3)/O(3) i SE(3)/E(3); objasniti da „×“ ovde znači nezavisnu promenu A i B. Pokazati da dot product u=v=(1,0,0) iznosi 1, a nakon rotacije samo v na (0,1,0) iznosi 0. Pre parity oznaka reći da ogledanje čuva sve udaljenosti, pa ulaz zasnovan samo na njima ne razlikuje takav ogledalski par. Oznake povezati sa [e3nn objašnjenjem O(3) reprezentacija](https://docs.e3nn.org/en/stable/api/o3/o3_irreps.html).

**Značaj: važan za geometrijsko učenje**, uz očuvanje postojeće stručne preciznosti.

### M13 — Loss formule nisu dovoljno povezane sa ponašanjem trening primera

**Mesto:** [06-metric-learning-and-evaluation.md:99–126 i 170–180](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:99).

**Problem i posledica:** contrastive formula definiše d/y/m, ali nema računsko tumačenje dve grane. Triplet deo daje uslov nad rastojanjima, bez eksplicitne funkcije gubitka i definicije a/p/n. Semi-hard mining i temperatura τ u InfoNCE nisu dovoljno objašnjeni. Čitalac teško povezuje lažan negativ sa konkretnim pomeranjem embeddinga.

**Prećutno predznanje:** anchor/positive/negative, hinge, aktivna margina, izbor negativa prema trenutnim rastojanjima i temperatura softmax-a.

**Konkretna izmena:** definisati oznake i dati L=max(0,d(a,p)²−d(a,n)²+m). Za d(a,p)²=0,2 i m=0,3, negativi sa kvadratnim rastojanjima 0,1/0,4/0,7 daju gubitke 0,4/0,1/0 i ilustruju hard/semi-hard/easy izbor. To je sintetički primer zasnovan na standardnom [FaceNet triplet/mining postupku](https://arxiv.org/html/1503.03832v3). Za InfoNCE definisati τ>0 i odvojiti softmax razlomak od njegovog −log loss-a; pokazati uticaj temperature na nekoliko skorova.

**Značaj: važan pre treninga metric-learning modela.** Postojeća pravila o lažnim negativima i bezbednim augmentacijama ne treba proširivati novim ponavljanjima.

### M14 — PU učenje uvodi više naprednih pretpostavki u jednom pasusu

**Mesto:** [06-metric-learning-and-evaluation.md:183](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:183).

**Problem i posledica:** opravdana opciona mogućnost pozitivno-neoznačenog učenja odmah uvodi SCAR/SAR, propensity, class prior i identifiability. Čitalac razume da nepoznato nije negativno, ali još ne zna kakav novi statistički problem PU rešava i od kojih pretpostavki zavisi.

**Prećutno predznanje:** mešavina pozitivnih/negativnih u neoznačenom skupu, selekcija oznaka i prevalencija klase.

**Konkretna izmena:** u glavnom toku objasniti samo da neoznačeni skup sadrži obe klase i da učenje zahteva pretpostavku o izboru označenih pozitivnih. Akronime premestiti u opcioni okvir sa definicijama. Primer ekspertskog češćeg označavanja poznatih metala dovoljan je da pokaže zašto slučajna selekcija pozitivnih nije podrazumevana.

**Značaj: koristan za poboljšanje**, uslovan pre upotrebe PU-a. Ne treba dodavati obavezni kurs teorije selekcije.

### M15 — Dijagnostika embeddinga navodi mere bez simptoma koje proveravaju

**Mesto:** [06-metric-learning-and-evaluation.md:328–334](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md:328).

**Problem i posledica:** varijansa po dimenziji, effective rank, duplirani vektori, hubness i raspodela normi navedeni su kao kontrolna lista. Bez kratkog tumačenja čitalac može izveštavati brojeve bez razlikovanja kolapsa, malog iskorišćenog prostora i legitimno čestog relevantnog motiva.

**Prećutno predznanje:** efektivna dimenzionalnost, raspodela vektora i neravnomerna učestalost pojavljivanja u listama suseda.

**Konkretna izmena:** tri reda „simptom→mera→tumačenje“: skoro isti vektori→varijansa/duplikati; malo iskorišćenih pravaca→efektivni rang; isti kandidati među susedima mnogih upita→hubness. Reći da alarm nije sam po sebi dokaz naučne greške. Ako je račun efektivnog ranga obavezan, navesti izabranu definiciju; inače ga označiti opcionim.

**Značaj: koristan za poboljšanje** evaluacije naučenih reprezentacija.

### M16 — RAG nema dovoljno povezan put od dokumenta do citirane tvrdnje

**Mesto:** [07-local-slm-rag.md:85–151 i 165–169](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/07-local-slm-rag.md:85).

**Problem i posledica:** osnovni RAG jeste definisan, a BM25/dense/RRF/rerank i grounded odgovor imaju jasne uloge. Ipak, indeksirani odlomak se ne uvodi kroz postupak njegovog nastanka; „chunk“ se kasnije koristi u leakage pravilima. Granice dokumenta, odlomka, konteksta i citata ostaju implicitne.

**Prećutno predznanje:** segmentiranje, jedinica indeksiranja, lokator izvora, ograničen kontekst i razlika relevantnog dokumenta od odlomka koji podržava konkretnu tvrdnju.

**Konkretna izmena:** pre BM25 dati tok odobren dokument+verzija→smisleni odlomci sa lokatorom→kandidati→rerank→kontekst→proverena tvrdnja. Pokazati jedan odlomak kojem treba sačuvati negaciju/uslov. Navesti da qrels/Recall@k označavaju dokument ili passage. Eksplicitna jedinica retrieval-a postoji i u izvornom [RAG radu, Lewis et al.](https://arxiv.org/html/2005.11401v4); njegove konkretne veličine odlomaka ne treba automatski preuzimati.

**Značaj: važan za RAG granu**, koja ne blokira osnovno poređenje kristala.

### M17 — Kontrolisano tumačenje namere nema jedan završen tok razjašnjenja

**Mesto:** [07-local-slm-rag.md:31–43 i 175–177](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/07-local-slm-rag.md:31).

**Problem i posledica:** pet nivoa validacije i primer prisustva metala naspram koordinacije dobro su postavljeni. Nema jednog korisničkog zahteva koji prolazi kroz dva tumačenja, proveru semantike i konačnu dozvoljenu operaciju. Execution equivalence ostaje imenovan, ali nedemonstriran kriterijum.

**Prećutno predznanje:** kontrolisani predikat, parafraze iste namere i razlika sintaksne ispravnosti, semantičke ispravnosti i tačnog naučnog rezultata.

**Konkretna izmena:** tabela za „nađi Cu–DAP primere kao ovaj“: dva tumačenja, potrebno razjašnjenje, prihvaćen pojmovni uslov i razlog odbacivanja formalno validnog pogrešnog uslova. Ekvivalentnost pokazati kao istu nameravanu operaciju; isti slučajan rezultat na jednom korpusu ne predstavlja dokaz opšte semantičke ekvivalencije. JSON ili implementacija nisu potrebni.

**Značaj: koristan za poboljšanje**, posebno ako je prirodni jezik planirani interfejs.

### M18 — API/security rečnik nema kratku mapu aktera i granica

**Mesto:** [08-api-llm-security.md:30–46, 69–81 i 99–138](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/08-api-llm-security.md:30); egress ranije u [07:195](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/07-local-slm-rag.md:195).

**Problem i posledica:** egress, tenant, data-plane, TTL, processor/podprocessor, confused deputy i schema smuggling pojavljuju se u praktičnim pravilima bez jedne osnovne mape sistema. Prompt injection ima korisne primere, ali čitalac bez infrastrukturskog iskustva još teško vidi ko poseduje ovlašćenje i gde podatak prelazi granicu.

**Prećutno predznanje:** izlaz podataka iz sistema, izolacija projekata/korisnika, zadržavanje podataka i delegacija privilegija.

**Konkretna izmena:** mala mapa korisnik→lokalna provera/izvršenje→spoljni obrađivač, sa označenim izlazom podataka. Dodati kratke prevode pri prvoj upotrebi. Confused deputy ilustrovati nepoverljivim dokumentom koji traži izvoz drugog projekta i izvršnim slojem koji pogrešno koristi svoja šira prava. Povezati sa postojećim nezavisnim proverama pristupa.

**Značaj: koristan za poboljšanje**, u trenutku aktiviranja API grane. ACL, fail-closed i minimizacija već imaju osnovu; ne treba ih ponovo širiti.

## 5. Manje lokalne korekcije

Ove stavke ne opravdavaju nove lekcije. Svaka se može rešiti jednom definicijom, oznakom ili malom dopunom postojećeg prikaza.

| Mesto | Problem i zašto otežava čitanje | Pretpostavljeno predznanje | Konkretna korekcija | Značaj |
|---|---|---|---|---|
| [03-geometrija.md:17](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/03-geometrija.md:17) | sp/sp²/sp³ su navedeni bez značenja, iako je VSEPR prethodno dobro uveden. | Oznake hibridizacije. | Kratko povezati oznake sa početnim geometrijskim modelom ili ih odložiti; bez novog kvantnog izvoda. | Manja sugestija. |
| [06-dap-schiff.md:14–23](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/06-dap-schiff.md:14) | Nazivi i SMILES teže pokazuju koji su baš atomi N3 skupa. | Samostalno čitanje strukturnog zapisa i numeracije piridina. | Jedan crtež sa brojevima položaja i obeleženim donorima; može se napraviti iz postojećeg teksta. | Korisno vizuelno poboljšanje. |
| [11-cvrste-forme.md:247–255](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/chemistry-foundations/docs/11-cvrste-forme.md:247) | Instrumentalne skraćenice otežavaju skeniranje već dobre tabele svrha. | SCXRD/PXRD/DSC/TGA/DVS nazivi. | Pri prvoj upotrebi razviti skraćenice i dati srpski naziv. | Manja sugestija. |
| [02-classical-ml.md:72 i 78–83](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/02-classical-ml.md:72) | L1/L2 i kNN oznake ostaju delimično implicitne; formula se teže samostalno proverava. | Oblik kazne, N_k(x), ε i p. | Jedna linija za sumu apsolutnih vrednosti/sumu kvadrata; imenovati skup suseda, stabilizacionu konstantu i eksponent pondera. | Manja sugestija. |
| [04-precise-pairwise.md:194–206](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/04-precise-pairwise.md:194) | Induced/non-induced i incumbent uvode kombinatorni rečnik pre kratkog objašnjenja. | Varijante podgrafa i najbolje trenutno rešenje. | Jedan putanja/triangl primer i srpsko objašnjenje incumbent-a. | Manja sugestija. |
| [03-global-retrieval-ann-ranking.md:569](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md:569) | bpref/condensed kontrola je zahtevana bez lokalnog značenja. | Mere osetljivosti na neocenjene rezultate. | Jedna rečenica o svrsi i direktan link na objašnjenje, ili jasna oznaka napredne evaluacije. | Manja sugestija. |
| [04-precise-pairwise.md:9–18](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/04-precise-pairwise.md:9) | Dijagram ne pokazuje dovoljno jasno ulaz izbora/mapiranja komponenti u packing granu, iako ga tekst kasnije zahteva. | Čitalac sam dopunjava zavisnosti iz proze. | Dodati odgovarajuću strelicu; ne predstavljati lattice mapping kao univerzalni uslov svakog COMPACK poređenja. | Manja sugestija. |
| [07-local-slm-rag.md:153–163](C:/Users/Korisnik/Desktop/crystallography-and-ml-theory/ml-ai-strategy/docs/07-local-slm-rag.md:153) | LoRA ΔW=BA ne daje neposredan osećaj uštede; tema je opciona. | Rang matrice i broj parametara faktorizacije. | Ilustrativno uporediti 1000×1000 sa 1000×4 i 4×1000 treniranih elemenata, bez obećanja istog kvaliteta; mehanizam je opisan u [LoRA radu](https://arxiv.org/html/2106.09685v2). | Manja sugestija. |

## 6. Mapa zavisnosti koje treba popraviti

Ovo su konkretna mesta gde redosled ili dubina objašnjenja utiču na narednu temu. „Postoji“ znači da ne treba pisati novu osnovu od početka.

| Preduslov | Trenutno stanje | Gde je potreban | Minimalna intervencija |
|---|---|---|---|
| Valentni elektroni→Lewis→naboj | Formula naboja postoji; ulazno knjigovodstvo nedovoljno. | Protonacija, donorstvo, grafovska validacija. | H01 pre Kapije A. |
| π-brojanje i dva donorstva | σ/π i oba tipa donacije postoje, ali veza nije dovoljno rana. | Heteroatomi, koordinacija i H-veze. | H02/H03 uz prvu tabelu funkcionalnih grupa. |
| Bilans naboja→OS→d-broj→spin | OS se izvodi posle ligandnog polja. | Tumačenje koordinacione geometrije. | H04: premestiti bilans i dodati jedno popunjavanje. |
| Ćelija→koordinate→simetrija→jedinstveni site | Dobra obrada u 08–10. | Puni kontaktni račun već u 07. | H06: podeliti 07 i odložiti računski deo. |
| Periodične slike→označene ivice→ciklusi | Slike i transformacije postoje; grafovski most nepotpun. | Exact graph, unwrap, topologija, encoder. | M08 na početku periodičnog algoritamskog puta. |
| hkl i interferencija→strukturni faktor | hkl dolazi posle prve sume; fazna intuicija kratka. | Odsustva, fazni problem, kvalitet modela. | H10: promeniti redosled i dodati dva doprinosa. |
| H/S→G→ravnoteža→razmena vode | Račun G postoji; intuicija je delom u rečniku. | Hidrati, stabilnost, polymorph-risk. | H11: preneti osnovu i odvojiti otvoren sistem. |
| Graf→lokalno okruženje→fingerprint | Algoritamski opis postoji bez malog traga. | Tanimoto i 2D kandidati. | H13; Tanimoto račun ostaviti postojećim. |
| Komponente→globalna mapa→atomska mapa | Ograničenja jasna; globalni optimum nema račun. | RMSD, koordinacija i packing. | M07 pre naprednih varijanti mapa. |
| Skalarni proizvod→kernel→PSD | Delimičan uvod u 02, formalniji uslov u 04. | SVM/GPR/SOAP. | M02 i jasno odložen SOAP prvi prolaz. |
| Poruka→agregacija→embedding→loss | Definicije postoje; potpuni mali prolaz ne postoji. | Poređenje i trening encodera. | M11/M13, uz Z02. |
| Model→kalibracioni podaci→izlaz→nezavisna procena | Split i značenje kalibracije dobri; postupak kratak. | Verovatnoće, intervali, uzdržavanje od odluke. | M05/H17 sa različitim jedinicama i imeniocima. |
| Dokument→odlomak→kontekst→tvrdnja | Retrieval porodice objašnjene, nastanak jedinice implicitno. | RAG evaluacija i citiranje. | M16, kada se aktivira ta grana. |

## 7. Predloženi redosled čitanja posle izmene

1. **Orijentacija:** kratki scope i pitanja projekta, hemijski nivoi identiteta, ML 00a sa matematičkim dopunama. Uporednu mapu prvo čitati samo kao pregled objekata, zadataka i izlaza; označiti tačne uvodne sekcije.
2. **Hemijski minimum:** 01→02→03→04→05→06, uz H01–H04. U 05 bilans oksidacionog stanja prethodi ligandnom polju.
3. **Kristalografsko jezgro:** hemijski deo 07→08→09→potrebni deo 10 o eksperimentalnom modelu, occupancy i disorder→računski deo 07. Potom dovršiti difrakciju/kvalitet, 11 i 11A. Po potrebi premestiti kratke definicije occupancy/disorder neposredno pre prvog punog kontaktnog računa, umesto nametanja cele lekcije 10 unapred.
4. **Podatak i reprezentacija:** hemija 12/12A→13→14→15→16→sažeti nastavni tok 17; zatim 21 i ML 09. Detaljni inventari 17 koriste se kao povezani dokazi.
5. **Determinističko poređenje:** hemija 19→osnovni ML 04: primenljivost, komponentna/atomska mapa, periodični grafovski most, mapirani 3D, koordinacija, osnovni packing. SOAP i druge napredne kernel grane ostaviti za kasnije.
6. **Retrieval i evaluacija, prvi prolaz:** hemija 18/20→delovi ML 03 o reprezentacijama, indeksima, determinističkim referencama i evaluaciji, uz rani primer kompletnog upita. Odeljke o učenom rangiranju čitati tek posle odgovarajućih linearnih/tree/kernel osnova iz 02.
7. **Klasični ML i drugi prolaz:** ML 02, prvo linearni/tree/kernel mehanizmi i kalibracija; zatim selektivni PCA/PLS/GPR. Vratiti se učenom rangiranju iz ML 03, SOAP delu 04 i punoj uporednoj mapi. Primer učenja ranga treba da koristi već poznatu stručnu relevantnost i grupisanje po upitu.
8. **Učenje kristalnih reprezentacija:** ML 05→06 tek kada čitalac razume periodičnu ekvivalentnost, target, mapiranje, oracle i split. Dodati GNN i loss primer pre poređenja arhitektura.
9. **Uslovne grane:** SLM/RAG, spoljni API, FL i pojedinačni napredni property zadaci čitaju se kada za njih postoji konkretna projektna potreba. Kratko razgraničenje dokaznih tvrdnji iz 22 ostaje deo opšte pismenosti; puna razrada svake opcije ne mora biti zajednički preduslov.

Ovo je predlog putanje po sekcijama, ne zahtev da se sav sadržaj fizički prebroji. Ključno je da navigacija, kapije i interne veze pokazuju isti red.

## 8. Plan izmena po prioritetu i kriterijum završetka

| Prioritet | Zahvat i nalazi | Zašto tada | Dokaz da je dopuna dovoljna |
|---|---|---|---|
| **P0 — pre oslanjanja na osnovnu početničku putanju** | Uskladiti putanju i kapije; Lewisovo knjigovodstvo; podeliti kontaktno poglavlje; dodati mali log/exp primer u 00a. **Z01, Z02, H01, H06.** | To su stvarni prekidi redosleda ili osnovne procedure. | Čitalac sam nacrta jednostavnu Lewisovu strukturu, protumači osnovni loss primer i završi kontaktni račun bez neoznačenog čitanja nekoliko budućih lekcija. |
| **P1 — pre pouzdanog determinističkog poređenja** | Dva donorstva i aromatično brojanje; globalna dodela komponenti; periodični grafovski most; ECFP trag; kriterijum dometa L4. **H02, H03, H08, H13, M07, M08.** | Ovi pojmovi direktno određuju šta se mapira, meri i pretražuje. | Čitalac obrazloži atomsku ulogu, izračuna malu globalnu mapu, očuva fizičku ivicu pri promeni zapisa i objasni nastanak jednog fingerprint koda. |
| **P1 — pre naučnog tumačenja koordinacije, kvaliteta i stabilnosti** | Orbitalno popunjavanje, difrakciona faza/hkl i H/S/voda. **H04, H10, H11.** | Pogrešno ili površno tumačenje ovde menja značenje kasnijih signala. | Čitalac objasni dva d⁶ popunjavanja, poništavanje talasnih doprinosa i zašto okolina ulazi u poređenje hidrata. |
| **P2 — pre klasičnog ML-a i statističkih tvrdnji o uspehu** | Tree/kernel mehanizmi prema izabranoj metodi, odgovarajući kalibracioni postupak i grupni bootstrap. **M01, M02, M05, H17.** | Izbor i evaluacija modela treba da budu obrazloženi. | Čitalac objasni izabrani model i pokaže šta se uzorkuje, eventualno kalibriše i nezavisno ocenjuje. |
| **P2 — pre izabrane neuralne/metric-learning grane** | GNN prolaz, geometrijske transformacije, loss/mining i neuralna kalibracija ako je potrebna. **M11–M13 i neuralni deo M05.** | Ti preduslovi postaju obavezni za ovu granu, ne za RF/Ridge ili čisto geometrijsko poređenje. | Čitalac sprovede jedan forward/loss račun, objasni nezavisnu rotaciju ulaza i razlikuje trening i kalibracionu temperaturu. |
| **P2 — povezivanje i preglednost osnovnog teksta** | Zajednički mali slučaj; transparentni skorovi; ranije missingness definicije; raspored inventara i ANN primera. **Z03, H14–H16, M10.** | Omogućava prenos lokalnog znanja kroz ceo projekat. | Isti primer može da se prati od objekta do konačnog izveštaja; svaki prikazani broj ima definisan izvor, funkciju ili oznaku da je ilustrativan. |
| **P3 — neposredno pre izbora konkretne napredne grane** | PCA/PCR/PLS, GPR, MinHash/LSH, SOAP, PU, embedding dijagnostika, RAG/API. **M03, M04, M06, M09, M14–M18.** | Važnost zavisi od stvarnog izbora metode. | Čitalac može da objasni ulaz, osnovni postupak, izlaz i uslove samo odabrane metode. |
| **P4 — završno uredničko čišćenje** | Reakcijski rečnik, potencijali, basis/origin primer, HBP ulazni red, ponavljanja i male oznake. **H05, H07, H09, H12, Z04 i odeljak 5.** | Poboljšava tok bez odlaganja važnijih preduslova; H09 može ranije ako je odmah potreban M08. | Tekst se čita bez nepotrebnog traganja po rečniku; nijedna nova strana ne ponavlja već izvedenu istu ideju. |

Prioriteti nisu ocena vrednosti oblasti: P3 tema može postati obavezna odmah ako projekat izabere baš tu metodu. Ne treba čekati da se prepišu sve opcione grane da bi se nastavilo sa dobro definisanim determinističkim jezgrom.

### Delovi kojima stvarno nedostaje osnova

Najjasnije nedostaju elementarno Lewisovo knjigovodstvo, lokalno brojanje za Hückelovo pravilo, orbitalno popunjavanje, talasna fazna intuicija, objašnjenje hemijskog potencijala/aktivnosti vode i prelaz od periodičnih slika na označeni graf. U ML-u osnovu dodatno traže projekcija/komponenta, Bayesian proces GPR-a, MinHash potpis, postupak kalibracije, semi-hard izbor i temperatura loss-a. Za te stavke nije dovoljan samo još jedan link ka literaturi ako ostaju u početničkom obaveznom toku.

### Delovi koji su nepotrebno teški u sadašnjem rasporedu

To su pre svega periodični račun u 07 pre preduslova, deo ligandnog polja pre bilansa oksidacionog stanja, gauge/quotient/cycle-sum pasusi pre prvog označenog grafa, SOAP/REMatch pasus sa mnogo konstrukcionih pojmova odjednom, SE(3)×SE(3)/parity pasusi i forenzički inventar 17 u glavnoj putanji. Problem se rešava malim prethodnim primerom ili slojevima čitanja. Precizne uslove ne treba brisati.

### Preporučeni obim intervencije

Za početak je dovoljno napraviti nekoliko zajedničkih nastavnih blokova: Lewis/naboj; periodični zapis i graf; globalna komponentna mapa; difrakciona interferencija; H/S i voda; GNN→embedding→loss; kalibracija i jedinica evaluacije. Svaki blok treba da ima kratku intuiciju, jedan izveden primer i jednu novu proveru razumevanja. Postojeće kapije i laboratorije već obezbeđuju strukturu; ne treba praviti paralelan sistem vežbi.

## 9. Šta je već dovoljno dobro i ne treba dodatno proširivati

### Hemija

- **Formula, sastav i identitet:** dobro se razlikuju sastav, povezanost, metal u formuli i metal kao koordinacioni centar; primer Cu Kα dodatno sprečava konkretnu zabunu.
- **σ/π, konjugacija i nitro-rezonanca:** veza između crteža, naboja i reprezentacije već je dovoljno razrađena. H01/H02 dopunjuju prethodne korake, ne zahtevaju ponovno pisanje rezonance.
- **VSEPR, geometrija i stereo:** domeni naspram oblika, konfiguracija/konformacija, E/Z i osnovna chirality imaju dobru podlogu. Dužina, ugao i puna atan2 torzija već imaju formule, izuzetke i numerički primer.
- **Koordinaciona semantika:** CN naspram broja liganada, potencijalni/opaženi denticitet, τ₅ račun, DAP donor set i više nivoa dokaza metala među najboljim su delovima.
- **Ćelija i simetrija:** opšta matrica ćelije, puni C1 fractional↔Cartesian račun, operacije, ASU/specijalna mesta, Z/Z′ i gustina već su konkretni. H06/H09 popravljaju redosled i prelaz između zapisa; ne traže novo izvođenje istih računa.
- **Kvalitet eksperimentalnog modela:** constraint/restraint, measured/unique/refined, simulirani/izmereni PXRD, standardna neizvesnost i višedimenzionalni kvalitet obrađeni su pažljivo. Univerzalni „dobar R“ prag bio bi lošije pojednostavljenje.
- **Čvrste forme i referentne raspodele:** identitet soli/hidrata/solvata, postojeći ΔG primer, percentili/MAD, MAD=0, multimodalnost i kružne torzije imaju primerenu preciznost. H11/H12 ne opravdavaju širenje cele taksonomije ili statistike.
- **Formati i standardizacija:** 12/12A daju koristan sintetički CIF, loop strukturu i razliku `?`, `.`, nule i naučne validnosti. U 13 jasno su odvojeni parsiranje, validacija, normalizacija, standardizacija i kuriranje, uz očuvanje izvornog pogleda.
- **Sličnost i evaluacija:** Tanimoto račun, mapiranje pre RMSD-a, coverage uz geometriju, obuhvat all-pairs zadatka, stručna rubrika i razlika score/status već su dobri. Provenance i uslovnost prava takođe su jasno postavljeni.

### ML/AI

- **00a kao pojmovni uvod:** uzorak/feature/target/labela, graf/fingerprint/embedding, norma/cosine, fit/predict, parametri/hiperparametri i train/validation/calibration/test već daju dobar okvir. Z02 je uska matematička dopuna.
- **Granice reprezentacije:** isti 2D ulaz ne može razotkriti različito pakovanje; property benchmark nije dokaz retrieval uspeha. Te ograde ne treba ponavljati još opširnije.
- **Tanimoto i retrieval evaluacija:** binary/count varijante, exact oracle, ANN recall, stručni candidate recall i finalni ranking imaju jasnu semantiku i konkretne račune. Posebno je dobro što različiti imenitelji nisu poistovećeni.
- **Neocenjeno i neuspešno nisu negativno:** unjudged, timeout, ambiguous, unavailable i neprimenljivo odvojeni su od naučne labele. Pravila zero-hit, ties i filter-aware evaluacije opravdano su detaljna.
- **Mapiranje i RMSD:** uloga Kabsch-a, reflection policy, coverage, degeneracija i periodični unwrap uslovi dobro su postavljeni. Nije potrebno izvoditi celu SVD optimizaciju da bi se koristilo objašnjenje.
- **Target i split:** relation registry, smer relacije, warm/cold i cold/cold, vremensko odvajanje, zavisni parovi i grupisanje imaju dobru osnovu. Zamena jednim random split-om bila bi gubitak kvaliteta.
- **Cross-format pogled i lifecycle:** jasno je da više fajlova jednog objekta nisu nezavisni glasovi, da nedostajući kanali imaju različita značenja i da prava, kvalitet i dostupnost predstavljaju odvojene uslove.
- **Naučna uloga jezičkog modela:** SLM/RAG/API ne dobijaju autoritet da samostalno potvrđuju hemijsku činjenicu. Odvajanje retrieval-a, interpretacije, izvršenja, retention-a i prava već je dobro. M16–M18 traže primer toka, ne novu listu zabrana.
- **Uslovni FL deo:** postojeći FedAvg primer sa definisanim ponderima i razdvajanje privatnosti, agregacije i prava dovoljno su dobri za orijentaciju. Povećavanje obima te teme nema prioritet bez konkretnog FL cilja.

## 10. Završna urednička odluka

Preporuka je **ciljana dorada postojećeg materijala**, uz zadržavanje njegove metodološke preciznosti. Prvi paket izmena treba da popravi početničke preduslove i periodični lanac; drugi da omogući samostalno praćenje jedne kompletne putanje od hemijskog objekta do poređenja i evaluacije; treći da razradi samo stvarno izabrane ML/AI metode.

Uspeh se ne meri brojem dodatih strana. Posle dorade čitalac treba da ume da objasni odakle dolazi svaki ulaz, sprovede mali primer, navede značenje izlaza i prepozna koji prethodni korak taj izlaz omogućava. Tamo gde tekst to već postiže, proširivanje nije potrebno.
