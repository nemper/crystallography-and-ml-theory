# Zajednički predlozi za poboljšanje repozitorijuma crystallography-and-ml-theory

Poređenjem celog sadržaja fajlova `analiza-A.md`, `analiza-B.md` i `analiza-C.md` izdvojio sam **30 sigurnih zajedničkih predloga**. Ispod su njihovi objedinjeni opisi. Samostalne izmene koje rešavaju različite probleme brojane su odvojeno, čak i kada ih neka analiza obrađuje zajedno. Poređenje je zasnovano isključivo na ta tri fajla.

1. **Uskladiti putanju čitanja, navigaciju, preduslove i kapije znanja.**

   Uspostaviti jednu merodavnu početničku putanju i usaglasiti početne stranice, navigaciju, sažete tabele, detaljna uputstva i provere znanja. Precizno označiti koje sekcije služe samo orijentaciji, šta treba savladati u prvom prolazu i kada se čitalac vraća naprednim delovima. Uz poglavlja navesti kratke, konkretne preduslove. Osnove učenja i boostinga treba da prethode učenom rangiranju, kernel osnova SOAP-u, a osnovna evaluacija treba da bude dostupna bez prethodnog čitanja celog neuralnog dela. Kapije postaviti iza svih potrebnih preduslova. Razlikovati obavezno jezgro od uslovnih grana, uz očuvanje osnovnih razgraničenja naučnih tvrdnji.

2. **Razdvojiti osnovno objašnjenje od stručnih ograničenja i smanjiti ponavljanje metateksta.**

   Najgušće odeljke urediti redom: pitanje → intuicija → mali primer → definicija ili formula → ograničenja → detalji za stručnu proveru. Zahteve za potpunost, tolerancije, verzije i reproduktivnost zadržati u jasno izdvojenom referentnom sloju, kako bi osnovni postupak bio vidljiv pre njegovih komplikacija. Opšte napomene da dokument nije implementaciona specifikacija ili šema navesti centralno i povezivati linkovima; lokalno zadržati napomene koje utiču na tumačenje konkretnog rezultata. Stručne termine pri prvom korišćenju kratko objasniti na srpskom, uz originalni naziv, a zatim koristiti doslednu terminologiju.

3. **Preurediti poglavlje o lokalnom skupu oko prenosivih pouka.**

   Sintezu nalaza postaviti pre dugih inventara, tako da čitalac najpre vidi odnos „nalaz → posledica → dokaz“. Osnovni tok organizovati oko nekoliko pitanja i završenih slučajeva, kao što su N14, razlika search1/search2 i zavisni višestruki pogledi istog objekta. Naglasiti šta primeri pokazuju o značenju upita, gubicima pri izvozu, izboru uzorka i granicama zaključivanja. Potpune brojnosti, hash identifikatore, distribucije i druge podatke konkretnog preseka izdvojiti ili jasno označiti kao referentne. Sačuvati postojeće brojke i trag dokaza.

4. **Napraviti jedan nastavljen sintetički primer koji povezuje hemiju, poređenje i ML evaluaciju.**

   Koristiti mali skup imenovanih objekata kroz više postojećih poglavlja, sa jednom matičnom stranom i vezama ka odgovarajućim koracima. Primer treba da poveže naučno pitanje, izvorni i namenski pogled na objekat, dostupne reprezentacije, primenljivost metoda, komponentno i atomsko mapiranje, geometrijske mere, stručnu ocenu, izbor kandidata i evaluaciju.

   U strukturnom delu prikazati glavnu i dodatnu komponentu, dozvoljene dodele, nekoliko nekolinearnih mapiranih atoma, centriranje, poznatu rotaciju, ručni RMSD i pokrivenost obe strane. Razlikovati isti objekat zapisan drugačije od stvarno drugačije strukture, a molekulsku geometriju od pakovanja susednih molekula. Pratiti i jedan propušten relevantan kandidat i jedan uspešno ocenjen par, uz jasne imenioce različitih mera obuhvata. Sve podatke i pojednostavljenja označiti kao nastavne; prikaz pakovanja ne predstavljati kao stvarni COMPACK rezultat, niti mali skup kao dokaz statističke pouzdanosti.

5. **Dopuniti matematički uvod objašnjenjem logaritma, eksponencijalne funkcije i njihove upotrebe u ML formulama.**

   Pre zahtevnih formula napraviti kratak numerički most koji objašnjava kako promena argumenta menja gubitak ili težinu. Definisati prirodni logaritam i, za pozitivnu labelu, uporediti vrednosti −ln(p) za p=0,9, 0,5 i 0,1. Na dva skora pokazati eksponenciranje i normalizaciju zbirom, tako da nastanak softmax težina bude proverljiv. Povezati to sa logističkom funkcijom i definisati logit pre kalibracije. Dopune povezati sa prvim mestima ozbiljne upotrebe; postojeću intuiciju gradijenta zadržati bez zahteva za celim kursom diferencijalnog računa.

6. **Dodati početni postupak konstrukcije Lewisove strukture iz formule.**

   Uvesti malu tabelu valentnih elektrona H/C/N/O, duet vodonika, osnovno pravilo okteta i razliku između elektrona, elektronskih parova, broja veza, valence i naboja. Potpuno izvesti primer NH₃/NH₄⁺ ili H₂O/OH⁻: ukupan broj elektrona, raspored veza, preostale slobodne parove i proveru formalnog i ukupnog naboja. Time omogućiti da čitalac sam odredi ulaze u formulu formalnog naboja. Primer povezati sa protonacijom, geometrijom i donorstvom, a postojeći nitro-primer zadržati kao sledeći nivo. Ako se koristi spoljašnja lekcija, njen konkretan odlomak jasno označiti kao obavezan preduslov.

7. **Povezati Hückelovo pravilo sa konkretnim brojanjem π-elektrona.**

   Objasniti šta se broji u izrazu 4n+2 i definisati n kao nenegativan ceo broj. Na benzenu prikazati šest π-elektrona, a zatim uporediti piridin i pirol sa označenim elektronskim doprinosima i položajem slobodnog para azota. Pokazati koji par učestvuje u aromatičnom sistemu, a koji ostaje izvan njega, i povezati tu razliku sa donorskim i akceptorskim ulogama. Dopuna treba da se nadoveže na postojeće objašnjenje σ/π veza i konjugacije, bez širenja u katalog aromatičnih izuzetaka.

8. **Razjasniti različita značenja donorstva pre tabele funkcionalnih grupa.**

   Uporedno predstaviti doniranje elektronskog para metalu, donorstvo i akceptorstvo vodonične veze i doniranje protona. Koristiti prikaze `N: → M` i `D–H···A`, uz jasno objašnjenje šta se u svakom slučaju podrazumeva. Na piridinu i piridinijumu pokazati kako protonacija menja raspoloživost slobodnog para i mogućnost H-donorstva; karbonilni kiseonik može dodatno pokazati da H-akceptor ili metalni donor nije automatski H-donor. Posebno razjasniti da vodonična veza ne podrazumeva nužno prenos protona. U tabelama dosledno razlikovati ove uloge, uz veze ka kasnijim geometrijskim kriterijumima.

9. **Postaviti oksidacioni bilans pre d-brojanja i dodati orbitalni primer ligandnog polja.**

   Redosled urediti kao ligand i donor → koordinacioni broj i denticitet → bilans naboja i oksidaciono stanje → dⁿ → elektronsko tumačenje geometrije. Pre stručnih tabela objasniti orbitalni kapacitet, sparene i nesparene elektrone, energetske nivoe i degeneraciju. Dodati jedan idealizovani oktaedarski d⁶ dijagram sa visokim i niskim spinom, prebrojanim elektronima, oznakama t₂g/e_g i razdvajanjem Δ. Pokazati konkurenciju zauzimanja višeg nivoa i energije sparivanja. Sačuvati postojeća ograničenja zaključivanja o distorzijama i Jahn–Teller efektu na osnovu pojedinačnih rastojanja.

10. **Pripremiti reakcijski rečnik za mehanizam nastanka Schiffove baze.**

    Nukleofilni azot povezati sa već uvedenim donorom elektronskog para, a elektrofilni ugljenik karbonila sa mestom koje taj par prima. Kratko objasniti intermedijer, prenos protona i eliminaciju, tako da „nukleofilni napad“ dobije konkretno značenje. Ako mehanizam ostaje u osnovnom toku, dodati jednostavnu strukturnu šemu od karbonila, preko karbinolaminskog međuproizvoda, do imina. Prihvatljiva alternativa je označiti mehanističku razradu kao opcionu, dok neto kondenzacija i postojeći bilans atoma ostaju obavezni.

11. **Premestiti kvantitativne periodične kontakte iza ćelije i simetrije.**

    Poglavlje o interakcijama podeliti na dva čitalačka prolaza: najpre fizička i hemijska intuicija interakcija i jednostavna geometrija vodonične veze, zatim ćelija i koordinate, simetrija i ASU, pa povratak na periodične kontakte. Pre punog računa obezbediti potrebna objašnjenja zauzeća mesta i nereda u modelu. Periodični algoritam, postojeći N14 proračun i odgovarajuću kapiju postaviti u drugi prolaz. Ažurirati plan i navigaciju, a formule zadržati na jednom glavnom mestu sa povratnim vezama. Postojeće račune i upozorenja o kosim ćelijama sačuvati.

12. **Dopuniti legende i fizičko tumačenje Coulombovog i Lennard–Jonesovog potencijala.**

    Uz formule navesti značenje svih simbola, njihove jedinice i referentnu nulu energije. Razlikovati permitivnosti u Coulombovom izrazu od parametra ε u LJ potencijalu. Na označenoj krivoj prikazati odbojni deo, privlačni deo, minimum i približavanje nuli pri velikom rastojanju. Za prikazani LJ izraz objasniti da je σ rastojanje nulte energije, a ε dubina minimuma; minimum je na r=2^(1/6)σ, sa energijom −ε. Tako pokazati zašto kraći kontakt nije nužno povoljniji. Sačuvati ograničenje da ove formule nisu potpuni model kristalne energije.

13. **Objasniti superćeliju kroz konstrukciju atomskih kopija.**

    Pre podrešetki, koseta i opšteg determinantnog računa izvesti primer superćelije 2×1×1, uz nepromenjen origin. Pokazati da udvostručenjem ose a stare kopije sa koordinatama x i x+1 dobijaju nove frakcione koordinate x/2 i (x+1)/2. Povezati to sa zapisom A′=AP i P=diag(2,1,1), uz proveru očuvanja fizičkih položaja. Time razjasniti razliku promene koordinatnog opisa od fizičkog istezanja strukture. Opšti matrični formalizam izložiti nakon primera, a termin koset ostaviti za naprednu napomenu.

14. **Ojačati fizičko značenje termodinamičkih veličina pre naprednih ograničenja.**

    Kratke definicije entalpije i entropije preneti iz rečnika u glavnu lekciju i povezati ih sa interakcijama i dostupnim stanjima ili kretanjima. Na postojećem primeru ΔG=1000−4T objasniti zašto promena temperature menja povoljniju formu, bez svođenja entropije na vidljivi „nered“. Razlikovati ravnotežnu stabilnost od kinetičke barijere pomoću slike minimuma i prelaza. Zatim posebno obraditi „anhidrat + voda iz okoline ⇄ hidrat“, uz minimum značenja aktivnosti i hemijskog potencijala vode. Rastvorljivost izlagati od osnovne ravnoteže ka očuvanju ili promeni faze tokom merenja, pa tek zatim detaljnim ograničenjima.

15. **Demonstrirati globalnu dodelu komponenti na maloj matrici.**

    Pre unmatched opcija, multipliciteta i napredne enumeracije izračunati jednostavno globalno uparivanje. Matrica `[[1,2],[2,100]]` pokazuje da pohlepni izbor može dati ukupan trošak 101, dok ukrštena potpuna dodela daje 4. Brojeve označiti kao nastavnu ilustraciju globalnosti. Odvojeno prikazati hemijsku dozvoljenost parova, zabranu pojedinog uparivanja i mogućnost da komponenta ostane neuparena. Pokazati kako izabrana komponentna mapa određuje naredno atomsko mapiranje. Tek potom obraditi alternativne optima, ekvivalentne kopije, orbite i k-best rešenja.

16. **Pokazati kako izbor MCS varijante menja dozvoljeno podudaranje.**

    Na malim grafovima objasniti razliku induced/non-induced podgrafa, posebno preko dodatne ivice između mapiranih čvorova, kao u poređenju putanje i trougla. Dopuniti povezano/nepovezano jezgro i relevantna pravila očuvanja prstenova, uz tabelu „odluka → dopušteno podudaranje → posledica“. Završiti konkretnim mapiranjem i pokrivenošću obe strane. Jasno pokazati da ove opcije menjaju pitanje koje se postavlja grafovima. Pojam incumbent kratko objasniti kao najbolje trenutno pronađeno rešenje, a naprednu enumeraciju i granice optimuma postaviti posle osnovnog primera.

17. **Uvesti zajednički most od periodičnih slika do označenog konačnog grafa.**

    Pre periodičnog matching-a i unwrap-a prikazati jednodimenzionalni lanac sa dva predstavnika čvorova, njegov konačan graf i periodični nastavak. Na primeru ćelije dužine 10 Å, koordinata 0,9 i 0,1 i translacione oznake 1 pokazati kontakt od 2 Å; izbor drugog predstavnika na 1,1 zahteva oznaku 0 za isti kontakt. Zatim objasniti kako se oznake ivica menjaju pri promeni predstavnika, uz očuvanje fizičkog pomeraja.

    Uporediti ciklus sa ukupnom translacijom nula i put koji završava u drugoj ćelijskoj kopiji. Rang mreže objasniti kroz nezavisne pravce lanca, sloja i prostorne mreže. Opšte formule dati posle primera i povezati isti osnovni blok iz determinističkog i neuralnog dela.

18. **Objasniti učenje ansambala kroz zajednički primer stabala i boostinga.**

    Na maloj tabeli pokazati jednostavno stablo, predikcije nekoliko stabala i njihov prosek. Zatim na istim podacima izvesti dva koraka regresionog boostinga uz kvadratni gubitak: trenutna predikcija → rezidual → korekcija sledećeg stabla. Time učiniti vidljivom razliku prosečavanja modela i sekvencijalnog popravljanja greške. Kratko objasniti bias i varijansu, uz razlikovanje od pristrasnosti izbora uzorka. Bibliotečke optimizacije, kao što su histogrami, GOSS/EFB i ordered boosting, postaviti iza osnovne mehanike ili u opcioni okvir.

19. **Izgraditi numerički most od skalarnog proizvoda do kernela i Gram matrice.**

    Iz nekoliko vektora formirati malu matricu Kᵢⱼ=K(xᵢ,xⱼ), tako da čitalac vidi šta predstavlja tabela svih parnih kernel vrednosti. Objasniti vezu sa skalarnim proizvodom u transformisanom prostoru i intuitivno značenje pozitivne semidefinitnosti, uključujući razlog zbog kojeg proizvoljan skor sličnosti nije automatski validan kernel. Uvesti osnovno značenje C, širine odnosno lokalnosti RBF-a kroz gamma i tolerisanog pojasa u SVR-u. Ovaj blok postaviti pre prve ozbiljne kernel primene i povezati ga sa SVM, GPR i SOAP delovima.

20. **Objasniti latentnu komponentu i razliku PCA, PCR i PLS postupaka.**

    Na dve povezane kontinuirane osobine prikazati projekciju i sažimanje u komponentu. Uporediti pravac najvećeg rasipanja podataka sa pravcem korisnim za predikciju cilja. Jasno razdvojiti tokove PCA: X→komponente; PCR: X→PCA→regresija; PLS: X i y→prediktivne komponente→regresija. Pokazati koji korak koristi samo ulaze, a koji i ciljnu promenljivu, i zašto izbor broja komponenti pripada validaciji. Razviti pune nazive skraćenica. Dublju obradu označiti kao preduslov izabrane porodice metoda.

21. **Prikazati GPR kao promenu raspodele mogućih funkcija nakon opažanja.**

    Dodati skicu nekoliko mogućih funkcija pre podataka, opaženih tačaka i funkcija nakon uslovljavanja tim opažanjima. Označiti srednju predikciju i raspon neizvesnosti, a kernel povezati sa pretpostavkom o zajedničkom variranju ulaza. Kratko razlikovati prior i posterior, neizvesnost funkcije i šum opažanja. Tek nakon tog prikaza razmatrati računarski trošak i napredne nastavke, poput aktivnog učenja i Bayesove optimizacije. Sačuvati ograničenje da modelna neizvesnost nije sama po sebi potvrda pouzdanosti pri promeni distribucije podataka.

22. **Objasniti SOAP/REMatch od lokalnog okruženja do globalne sličnosti.**

    Prikazati tok atomsko okruženje → zaglađena atomska gustina → lokalni deskriptor → matrica sličnosti između centara dve strukture → globalna agregacija. Na sintetičkoj matrici 2×2 uporediti prosečavanje, strogo uparivanje i meko, raspodeljeno uparivanje. Time razdvojiti ono što lokalni deskriptor kodira od onoga što globalni agregator radi sa skupovima okruženja. Detalje bazne ekspanzije i regularizovanog računanja postaviti u napredni sloj. Očuvati razliku REMatch/adapted-average konstrukcija i njihove uslove validnosti, uz prethodno dostupan kernel uvod.

23. **Demonstrirati mehaniku exact, HNSW, IVF i PQ pre memorijskih računa.**

    Na istom malom skupu tačaka pokazati da exact pretraga proverava sve elemente, HNSW prati put kroz graf, a IVF otvara samo izabrane particije. PQ prikazati kroz vektor podeljen na delove i njihovu zamenu codebook predstavnicima ili identifikatorima. Obeležiti gde nastaje propuštanje kandidata, a gde približno rastojanje može promeniti poredak. Povezati parametre poput efSearch i nprobe sa obuhvatom postupka. Sažeti postojeći primer kompletnog upita premestiti ranije, a memorijske i audit detalje zadržati nakon mehanizma.

24. **Pokazati nastanak MinHash potpisa i njegovu vezu sa izborom LSH kandidata.**

    Krenuti od malog skupa molekulskih okruženja i nekoliko zajedničkih permutacija ili hash rangiranja. Pokazati izbor minimuma, sastavljanje potpisa i njegovu upotrebu za izdvajanje kandidata, nakon čega sledi preciznije poređenje. Razdvojiti grešku procene sličnosti koja zavisi od potpisa od propuštanja kandidata koje zavisi od indeksnog postupka. Tako objasniti različite uloge dužine potpisa i parametara kandidatskog indeksa. Detaljniji LSH postupak može ostati jasno označena alternativna grana.

25. **Prikazati učenje rangiranja na jednom upitu i stručno ocenjenim kandidatima.**

    Koristiti isti upit i tri kandidata sa ocenama 2/1/0, pa ih predstaviti kao pointwise redove, parove preferencija i jednu rang-listu. Za svaki zapis navesti jedinicu supervizije, šta ulazi u gubitak i šta model predviđa. Razlikovati te uzorke od para kristala u App 2, tako da binarne oznake parova ne budu automatski shvaćene kao gotove query-grupisane preferencije. Primer vezati za već poznatu stručnu relevantnost, pokazati značaj zamene mesta pri vrhu liste za izabrani nDCG i obezbediti boosting osnovu pre LambdaMART-a.

26. **Povezati notaciju transformacionih grupa i pariteta sa geometrijskim primerima.**

    Dati kratku legendu SO(3), O(3), SE(3) i E(3), sa jasno označenim rotacijama, refleksijama i translacijama. Objasniti da proizvod grupa za par ulaza znači nezavisan izbor transformacije svakog ulaza. Prikazati rotaciju samo A, samo B, oba nezavisno i ogledanje jednog objekta. Jedan vektorski primer treba da pokaže promenu sirovog skalarnog proizvoda pri rotaciji samo jednog ulaza. Paritet povezati sa promenom znaka orijentisane tetraedarske zapremine i objasniti zašto očuvane udaljenosti same ne razlikuju ogledalski par. Formalnu teoriju reprezentacija ostaviti naprednoj referenci.

27. **Izvesti male račune triplet i InfoNCE gubitka.**

    Definisati anchor, positive, negative i marginu, pa dati eksplicitni triplet gubitak `max(0,d(a,p)²−d(a,n)²+m)`. Pokazati aktivan i nulti gubitak i povezati ih sa hard, semi-hard i easy izborom negativa. Primer sa d(a,p)²=0,2, marginom 0,3 i negativnim kvadratnim rastojanjima 0,1/0,4/0,7 daje gubitke 0,4/0,1/0.

    Za InfoNCE definisati τ>0, odvojiti softmax razlomak od njegovog negativnog logaritma i na malom skupu skorova pokazati uticaj temperature i sastava denominatora. Razlikovati trening temperaturu od kasnije kalibracione temperature i povezati izbor negativa sa konkretnim dejstvom na gubitak.

28. **Pokazati kako se kalibraciona mapa uči nad izlazom zamrznutog modela.**

    Dodati malu tabelu skorova i labela i tok zamrznuti model → izdvojeni kalibracioni podaci → naučena transformacija → nezavisni završni test. Na imenovanom postupku pokazati šta se fituje, na primer logističku mapu sigmoid(a·s+b); isotonic objasniti kao fleksibilniju monotonu mapu. Za neuralni nastavak prikazati zamrznute logite, softmax(logiti/T) i izbor T samo na kalibracionom skupu. Objasniti da pozitivno T menja samouverenost uz očuvanje izbora najvećeg logita. Jasno razdvojiti promenu verovatnosne prognoze od podešavanja praga odluke.

29. **Objasniti mehanizam split-conformal predikcije i razgraničiti vrste intervala i pokrivenosti.**

    Pre razmatranja garancije izvesti mali regresioni primer: apsolutni kalibracioni reziduali kao nonconformity skorovi → sortiranje → eksplicitno definisan konačno-uzorački kvantil → interval nove predikcije. Navesti pretpostavke, uključujući exchangeability i značenje marginalne pokrivenosti, uz očuvanje ograničenja podgrupnih tvrdnji. Kratkom tabelom razlikovati interval evaluacione metrike, interval novog cilja, skup klasnih oznaka i modelnu varijansu. Razjasniti i razliku pokrivenosti predikcije od udela slučajeva na koje sistem odgovara. Ovu obradu označiti kao uslovni nastavak za conformal granu.

30. **Demonstrirati grupno resamplovanje i upareno statističko poređenje metoda.**

    Na nekoliko sintetičkih nezavisnih grupa prikazati uzorkovanje sa vraćanjem, uključujući ponovljenu grupu. Za oba modela koristiti iste izabrane grupe i izračunati uparenu razliku metrike. Objasniti šta raspodela tih razlika procenjuje i razlikovati varijabilnost hemijskih uzoraka od varijabilnosti seed-ova.

    Razdvojiti query/family jedinicu pretrage od App 2 parova koji mogu deliti bilo koji endpoint; mali graf parova treba da pokaže zašto grupisanje samo po prvom članu nije dovoljno. Povezati primer sa postojećim odgovarajućim ML objašnjenjem. Tumačenje intervala dopuniti razlikom tačkaste prednosti, dokazane superiornosti, unapred definisane neinferiornosti i preširokog intervala za odluku. Mali broj demonstracionih replikacija ne predstavljati kao pouzdanu procenu intervala.

U sigurne rezultate nisam uključio sledeće **granične slučajeve**:

- **Dopuna difrakcije:** uvod u praškasti eksperiment i nastanak PXRD krive razlikuje se od pripreme faze, interferencije i strukturnog faktora. Zajednička oblast nije dovoljna za jednu istovetnu preporuku.
- **Dopuna HBP primera:** prikaz ulaznog opažanja i podataka za individualnu procenu razlikuje se od prikaza grupisanja H-veza i mrežnih izlaza. To su različiti koraci postupka.
- **Zaseban primer učenja linearnog modela:** nije dovoljno jednoznačno zajednički svim analizama. Pouzdano zajednički deo jeste demonstracija učenja stabala i ansambala, obuhvaćena stavkom 18.

**Ukupan broj sigurnih predloga zajedničkih za sve tri analize: 30.**
