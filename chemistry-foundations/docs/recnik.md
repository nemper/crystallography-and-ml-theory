# Rečnik pojmova

Rečnik je namenjen ML inženjeru koji kreće od nule. Definicije su dovoljno precizne za projektovanje dve 2CDC aplikacije, ali nisu zamena za puni IUPAC/IUCr rečnik. Kada termin ima više značenja, ovde je navedeno značenje koje mora stajati u data contract-u ili izveštaju.

!!! warning "Najopasnija reč je „struktura“"
    Može označavati molekulski graf, jednu 3D konformaciju, kristalnu strukturu, eksperimentalni model ili zapis u bazi. U zahtevima i šemi koristi precizniji termin.

## Kako čitati oznake

| Oznaka | Značenje |
|---|---|
| Å | ångström, \(10^{-10}\ \mathrm{m}\); tipična jedinica atomskih rastojanja |
| ° | stepen; koristi se za uglove i torzije |
| K | kelvin; apsolutna temperatura |
| s.u. | standard uncertainty, standardna neizvesnost |
| ASU | asymmetric unit, asimetrična jedinica |
| CN | coordination number, koordinacioni broj |
| \(F\), \(F^2\), \(I\) | strukturna amplituda, njen kvadrat i izmereni intenzitet |
| \((hkl)\) | Millerovi indeksi refleksije/ravni |
| \(R\), wR, GoF | različiti pokazatelji slaganja modela i difrakcionih podataka |
| \(Z\), \(Z'\) | formula units u ćeliji; nezavisne formula units u ASU u jednostavnom slučaju |

## Osnovni hemijski jezik

### Atom, element i čestice

**Atom**  
Najmanja elektroneutralna jedinica elementa koja zadržava njegov hemijski identitet: jezgro sa protonima i neutronima i elektronski omotač. U molekulskom grafu je čvor, ali „atom site“ u kristalografiji je model položaja/populacije, ne nužno jedna trajno označena čestica.

**Proton / neutron / elektron**  
Proton ima pozitivno elementarno naelektrisanje, neutron je neutralan, elektron negativan. Broj protona određuje element; promena broja elektrona daje jon; promena broja neutrona daje izotop.

**Atomski broj \(Z_{\mathrm{atom}}\)**  
Broj protona u jezgru. Ne mešati ga sa kristalografskim \(Z\), brojem formula units u ćeliji.

**Element**  
Vrsta atoma sa istim atomskim brojem. Simbol `Cu` znači bakar samo kada je hemijski element u odgovarajućem polju; `Cu Kα` opisuje rendgensko zračenje sa bakarne mete.

**Izotop**  
Atomi istog elementa sa različitim brojem neutrona. Izotopska oznaka može uticati na masu i ponekad svojstva; exact-match politika mora reći da li je razlikuje.

**Jon / katjon / anjon**  
Jon ima neto električno naelektrisanje; katjon je pozitivan, anjon negativan. Poliatomski jon sadrži više povezanih atoma sa ukupnim nabojem.

### Jedinke, sastav i količina

**Hemijska vrsta (chemical species)**  
Skup hemijski identičnih molekulskih entiteta u definisanom kontekstu. U praksi treba navesti charge, izotopsko i stereo stanje kada utiču na identitet.

**Molekulski entitet**  
Pojedinačna konstitucionalno ili izotopski određena jedinka koja može biti molekul, jon, radikal i slično. Precizniji termin od svakodnevnog „molekul“ kada su uključeni joni.

**Molekul**  
Elektroneutralna jedinka sa više atoma povezanih dovoljno snažno da se tretiraju kao celina. Jonski kristal poput NaCl nema diskretne `NaCl molekule` u istom smislu; koristi se formula unit.

**Jedinjenje**  
Čista supstanca sastavljena od dva ili više elemenata u određenom odnosu. Ne govori automatski da li su osnovne jedinke diskretni molekuli, joni ili mreža.

**Komponenta / fragment**  
Povezana ili funkcionalno izdvojena celina u zapisu. U soli su katjon i anjon odvojene komponente; u solvatu je rastvarač posebna komponenta. „Fragment“ može biti tehnički rezultat cepanja grafa i ne sme automatski dobiti hemijsku ulogu.

**Formula unit**  
Najmanji stehiometrijski odnos sastojaka koji predstavlja sastav nemolekulskog/jonskog materijala ili se koristi kao računovodstvena jedinica kristala. \(Z\) broji formula units u ćeliji, prema formuli prijavljenoj u CIF-u.

**Empirijska formula**  
Najjednostavniji celobrojni odnos elemenata. Ne daje povezanost, oblik, naboj po komponenti ni čvrstu formu.

**Molekulska formula**  
Stvarni broj atoma svakog elementa u molekulu, ali i dalje ne određuje graf: \(\mathrm{C_2H_6O}\) može biti etanol ili dimetil-etar.

**Formula sum / formula moiety**  
CIF polja za ukupni sastav i opis komponenti. Treba ih proveriti prema atom sites, occupancy, symmetry multiplicity i \(Z\); nisu nepogrešiva etiketa.

**Stehiometrija**  
Kvantitativni odnos sastojaka. U kokristalu 1:1 i 2:1 nisu ista forma; occupancy i disorder ne smeju pokvariti račun.

**Mol**  
SI jedinica količine supstance, tačno \(6{,}02214076\times10^{23}\) navedenih jedinki. Ne mešati sa `.mol` molekulskim formatom.

**Relativna molekulska masa / molarna masa**  
Prva je bezdimenziona relativna veličina; druga je masa po količini supstance, tipično \(\mathrm{g\,mol^{-1}}\). CIF formula weight ulazi u račun kristalne gustine.

### Elektroni, naboji i veze

**Valentni elektron**  
Elektron u spoljašnjem delu elektronske strukture koji najviše učestvuje u hemijskom vezivanju. Jednostavna pravila grupa dobro rade za glavne elemente, manje univerzalno za prelazne metale.

**Lewisova struktura**  
2D računovodstveni prikaz valentnih elektrona, veza i slobodnih parova. Koristan model; nije slika elektronske gustine i često je nedovoljan za metale/delokalizaciju.

**Slobodni elektronski par (lone pair)**  
Par valentnih elektrona formalno nevezan u Lewisovom prikazu. Može omogućiti baznost, H-bond prihvatanje ili koordinaciju metalu, ali dostupnost zavisi od protonacije, rezonance i geometrije.

**Formalni naboj**  
Celobrojna knjigovodstvena dodela elektrona unutar izabrane Lewisove strukture. Nije isto što i oksidaciono stanje ili parcijalni naboj.

**Oksidaciono stanje**  
Formalni broj dobijen jonskom aproksimacijom raspodele veznih elektrona. Koristan je za metalnu hemiju, ali se ne čita pouzdano samo iz oznake elementa ili koordinacionog broja.

**Parcijalni naboj**  
Modelom dodeljena necela raspodela elektronskog naboja na atomima. Zavisi od metode; `NO_CHARGES` u MOL2 znači da takav model nije dodeljen, ne da su atomi nepolarni.

**Hemijska veza**  
Stabilizujuća interakcija koja drži atome u hemijskoj celini. Granice između „jonske“, „kovalentne“ i „koordinacione“ nisu tri nepovezana fizička prekidača.

**Kovalentna veza**  
Vezivanje povezano sa deljenjem elektronske gustine između atoma. Jednostruka/dvostruka/trostruka oznaka je koristan model reda veze.

**Jonsko vezivanje**  
Elektrostatičko privlačenje suprotno naelektrisanih jedinki u široj strukturi. Jonski kristal je periodična mreža, ne nužno zbir izolovanih parova.

**Koordinaciona (dativna) veza**  
U Lewisovom formalizmu zajednički par potiče od donora/liganda i veže se za centralni atom. Posle formiranja nije univerzalno posebna vrsta `bond type` koju svaki format čuva.

**Red veze (bond order)**  
Model multiplicitetа/delokalizacije veze. Integer `1/2/3`, aromatični ili `unknown` tip zavise od representation modela; rendgenska difrakcija ga ne meri direktno kao etiketu.

**Rezonanca / delokalizacija**  
Više Lewisovih crteža deli isti raspored jezgara, a prava elektronska struktura nije smenjivanje tih crteža već delokalizovan hibrid.

**Aromatičnost**  
Stabilizovana ciklična delokalizacija definisana određenim hemijskim kriterijumima. Aromaticity perception je algoritamski model; različiti alati mogu dati različite `ar` oznake.

**Elektronegativnost**  
Relativna tendencija atoma u vezi da privlači elektronsku gustinu. Koristi se kvalitativno; postoji više skala.

**Polarna veza / dipolni moment**  
Polarna veza ima neravnomernu raspodelu naboja. Molekulski dipol je vektorski zbir doprinosa i zavisi od 3D geometrije; polarne veze mogu dati nepolaran molekul ako se vektori ponište.

**Intermolekulska interakcija**  
Privlačna/odbojna interakcija između hemijskih jedinki: disperzija, dipol–dipol, H-veza, halogena veza, jon–dipol i druge. Geometrijski kontakt je kandidat, ne automatski dokaz energetski dominantne „veze“.

**Vodonična veza**  
Usmerena privlačna interakcija u kojoj H vezan za donor učestvuje sa prihvataocem, uz hemijske i geometrijske dokaze. Nije svaki kratak H···X kontakt H-veza.

**Halogena veza**  
Privlačna interakcija u kojoj elektrofilni region halogenog atoma tipično usmereno interaguje sa nukleofilnim regionom. Potrebni su kontekst i geometrija.

## Organska, stereo i acid–base hemija

**Funkcionalna grupa**  
Prepoznatljiv atomski motiv koji daje tipično hemijsko ponašanje: karbonil, imin, hidroksil, piridin i slično. Ista grupa u drugačijem charge/rezonantnom okruženju može imati drugu donor/acceptor ulogu.

**Scaffold**  
Izabrano osnovno molekulsko jezgro za poređenje. Nema jednu univerzalnu definiciju; algoritam, prstenovi, side-chain pravila i metal handling moraju biti verzionisani.

**DAP**  
U ovom projektu: 18-atomsko 2,6-diacetilpiridinsko query jezgro sa dve `C=N` veze iz lokalnih ConQuest upita. Sama podstrukturna podudarnost ne dokazuje da je pogodak bis-imin ili Schiffova baza; to zahteva proveru neposrednog supstituenta na svakom `C=N` azotu u kompletnoj strukturi. Tačan pozitivni opseg (supstituenti, protonacija, donor set, bridging) mora potvrditi naučni tim.

**Schiffova baza / imin**  
Schiffova baza se uobičajeno odnosi na iminski proizvod kondenzacije primarnog amina i karbonilnog jedinjenja; ključni motiv je C=N. Iminski N može biti donor, ali protonacija i supstitucija menjaju ponašanje.

**Kiselina/baza po Brønsted–Lowryju**  
Kiselina donira proton; baza prima proton. Acid–base stanje menja formalni naboj, H-bond uloge, komponente i često čvrstu formu.

**Lewisova kiselina/baza**  
Lewisova kiselina prihvata elektronski par, a baza ga donira. Metalni centar i ligandni donor se često opisuju tim jezikom.

**pKa**  
Logaritamska mera ravnoteže disocijacije kiseline u određenom rastvaraču, temperaturi i standardnom stanju. Nije nepromenljiva etiketa samog CIF-a.

**Protomer**  
Jedna od struktura koje se razlikuju položajem dodatog/uklonjenog protona pri datom ukupnom sastavu/naboju. Protonation standardization može promeniti query rezultat.

**Tautomer**  
Konstitucioni izomeri koji se tipično razlikuju položajem protona i dvostruke veze i mogu međusobno da se pretvaraju. Brzina i ravnoteža zavise od rastvarača, pH, temperature, katalize i energetske barijere; u čvrstoj fazi tautomer može biti stabilizovan ili kinetički zarobljen. „Tautomer canonicalization“ je projektna politika, ne neutralno formatiranje.

**Izomer**  
Jedno od jedinjenja sa istom molekulskom formulom, ali različitim rasporedom atoma ili prostornim uređenjem.

**Konstitucioni izomeri**  
Imaju istu formulu, ali različitu povezanost atoma. Formula filter ih ne razlikuje.

**Stereoizomeri**  
Ista povezanost, različit prostorni raspored koji nije samo rotacija celog objekta.

**Enantiomeri / dijastereoizomeri**  
Enantiomeri su nesuperponibilne ogledalske slike; dijastereoizomeri nisu ogledalski par. Racemat sadrži jednake količine enantiomera, ali kristalno ponašanje zavisi od forme.

**Hiralnost**  
Osobina objekta koji se ne može superponirati sa ogledalskom slikom. Centar hiralnosti je čest, ali nije jedini izvor hiralnosti.

**Konfiguracija**  
Stereo raspored čija promena zahteva prekid/rekonstrukciju veze ili drugi diskretan stereo događaj; npr. R/S ili E/Z.

**Konformacija / konformer**  
3D raspored dostupan rotacijama i fleksijom bez promene povezanosti; konformer je jedna takva geometrija. Kristalna konformacija i generisana low-energy konformacija imaju različit provenance.

**Torzioni (diedarski) ugao**  
Orijentacija četiri uzastopna atoma. Periodičan je; razliku treba računati kružno, ne običnim oduzimanjem blizu \(-180^\circ/180^\circ\).

**Rotabilna veza**  
Algoritamski definisana veza oko koje je relevantna konformaciona rotacija. Amidi, prstenovi i terminalne veze se tretiraju različito po definiciji alata.

## Koordinaciona hemija

**Centralni atom / metalni centar**  
Atom, često metal, oko koga su ligandi uređeni u koordinacionoj jedinki. Jedan entry može imati više centara.

**Ligand**  
Atom, jon ili molekulska grupa vezana za centralni atom; u ovom projektu obično organska komponenta koja donira jedan ili više atomskih parova metalu.

**Donorni atom**  
Konkretan ligandni atom koji je direktno koordinisan centralnom atomu, npr. iminski ili piridinski N. Prisustvo N u ligandu ne dokazuje da je taj N donor u konkretnoj strukturi.

**Koordinaciona jedinka (coordination entity)**  
Centralni atom sa okolnim ligandima tretiranim kao celina. Nije isto što i ceo kristalni entry: counterioni i solventi mogu biti izvan jedinke.

**Koordinacioni kompleks**  
Uobičajen naziv za coordination entity/jedinjenje koje je sadrži. U specifikaciji navedi da li porediš jedinku, neutralni kompleks, so ili punu kristalnu formu.

**Koordinacioni broj (CN)**  
Broj direktno koordinisanih donor-atoma centralnom atomu prema eksplicitnom neighbor/bond modelu. Nije broj liganada: jedan tridentatni ligand daje tri donora.

**Denticitet**  
Broj donor-atoma jednog liganda koji se istovremeno vezuju za isti centralni atom: mono-, bi-, tri- itd. Zapisuje se uz mapping, ne procenjuje iz imena liganda.

**Helat**  
Prstenasta coordination arrangement nastala kada polidentatni ligand veže isti metal preko više donora.

**Mostni ligand (bridging ligand)**  
Ligand koji povezuje dva ili više centara. Algoritam koji svaku komponentu dodeli tačno jednom metalu gubi ovu informaciju.

**Haptičnost \(\eta^n\)**  
Broj susednih atoma delokalizovanog ligandnog segmenta koji zajedno koordiniraju metalu. Nije isto što i denticitet.

**Koordinaciona geometrija**  
3D raspored donor-atoma oko centra, npr. linearna, tetraedarska, kvadratno-planarna, trigonalno-bipiramidalna ili oktaedarska. CN sam ne određuje geometriju.

**Distortion measure / shape measure**  
Numeričko odstupanje realnog coordination polyhedron-a od idealne geometrije. Definicija, mapping i referentni ideal moraju pratiti vrednost.

**Koordinacioni polimer / mreža**  
Periodična struktura u kojoj coordination veze šire jedinku u 1D, 2D ili 3D. „Izdvoji najveći molekul“ može biti besmisleno jer nema konačne diskretne jedinke bez presecanja mreže.

**Metal-organic**  
Široka kategorija struktura sa metalom i organskim delom. Ne znači nužno organometalno u užem smislu sa direktnom metal–ugljenik vezom.

**Ligandno polje**  
Model cepanja energija metalnih orbitala usled usmerenog okruženja liganada. U ovom kursu koristi se kvalitativno da bi se razumeli spin-zavisne distance, square-planar/tetrahedral grananje i elektronske distorzije; duboki multipletni/spektroskopski račun nije deo uvodnog nivoa kursa.

**High-spin / low-spin**
Različiti načini popunjavanja split \(d\)-orbitala kada se nadmeću ligand-field splitting i pairing energija. Etiketa se ne izvodi samo iz coordination number-a ili jedne distance.

**Jahn–Teller efekat**
Distorzija nelinearnog sistema koja uklanja elektronsku degeneraciju i može sniziti energiju. Pseudo-octahedral Cu(II), \(d^9\), često pokazuje aksijalnu elongaciju; isti geometrijski obrazac sam nije dokaz uzroka.

## Kristal, ćelija i simetrija

**Kristal**  
Čvrst materijal sa dugodometnim uređenjem koje daje diskretan difrakcioni obrazac. Realni kristali imaju defekte, termalno kretanje i mogući disorder.

**Kristalna struktura**  
U operativnom scope-u ove knjige: konvencionalna 3D periodična malomolekulska struktura opisana rešetkom, motivom i simetrijom. Nije sinonim za jedan molekul niti za CIF fajl. Širi kristalografski pojam obuhvata i aperiodične kristale, pa ovu projektnu definiciju ne treba predstavljati kao univerzalnu.

**Rešetka (lattice)**  
Matematički periodičan skup translaciono ekvivalentnih tačaka. Svaki rešetkasti vektor je celobrojna kombinacija vektora primitivnog bazisa; kod centriranog konvencionalnog bazisa njegove celobrojne kombinacije daju podrešetku, a centrirajući vektori daju preostale tačke. Atomi nisu „rešetka“; kristalna struktura nastaje vezivanjem motiva za rešetku.

**Motiv / basis**  
Skup atoma/jedinki pridružen svakoj rešetkastoj tački da bi se izgradila struktura. Ne mešati sa basis vektorima ćelije.

**Jedinična ćelija**  
Paralelepiped definisan vektorima \(\mathbf a,\mathbf b,\mathbf c\) kojim se opisuje periodičnost rešetke. Kod primitivne ćelije njihove celobrojne translacije dosežu sve rešetkaste tačke; centrirana konvencionalna ćelija sadrži dodatne centrirajuće tačke. Nije jedinstven izbor; ista struktura može imati ekvivalentne ćelije/settings.

**Parametri ćelije**  
Dužine \(a,b,c\) i uglovi \(\alpha,\beta,\gamma\). Zapremina za opšti slučaj potiče iz determinantе cell matrix/metric tensor-a; slični parametri ne dokazuju isti packing.

**Primitivna / konvencionalna ćelija**  
Primitivna ima jednu rešetkastu tačku po ćeliji; konvencionalna je standardno izabrana radi jasne simetrije i može biti centrirana.

**Redukovana/standardizovana ćelija**  
Kanonskiji opis metrike dobijen definisanim algoritmom, koristan za candidate search. Rezultat zavisi od tolerancija i ne dokazuje strukturni identitet.

**Kristalni sistem / Bravaisova rešetka**  
Sedam kristalnih sistema grupišu space groups po point-group simetriji. Sedam rešetkastih sistema razlikuju se u hexagonal familiji: koriste rhombohedral umesto trigonal kategorije. Četrnaest Bravaisovih tipova (`aP`–`cF`) klasifikuju translacione rešetke i centriranje; to nisu similarity score-evi. Trigonalni kristal može imati `hP` ili `hR` rešetku.

**Frakciona koordinata**  
Koeficijenti \((x,y,z)\) u osnovi ćelije: \(\mathbf r=x\mathbf a+y\mathbf b+z\mathbf c\). Vrednosti koje se razlikuju za ceo broj predstavljaju periodično ekvivalentne položaje.

**Kartezijanska koordinata**  
Koordinata u ortogonalnom 3D sistemu, tipično u ångströmima. Pretvaranje iz frakcionih zahteva punu cell matrix, ne samo množenje sa \((a,b,c)\) kod neortogonalne ćelije.

**Periodični granični uslovi (PBC)**  
Suprotne strane ćelije predstavljaju susedne kopije periodičnog prostora. Najkraći kontakt može prelaziti granicu ćelije.

**Operacija simetrije**  
Transformacija koja ostavlja strukturu ekvivalentnom: translacija, rotacija, screw, refleksija/glide, inverzija i kombinacije.

**Prostorna grupa (space group)**  
Grupa svih simetrijskih operacija periodične strukture. Postoji 230 tipova u 3D; oznaka poput \(P\,2_1/c\) ne određuje hemijski identitet ni packing sama po sebi.

**Setting / origin choice**  
Konvencija osa, baze i koordinatnog početka za isti space-group type. Ekvivalentni \(P\,2_1/c\) i \(P\,2_1/n\) zapisi mogu opisivati istu strukturu u drugom setting-u.

**Asimetrična jedinica (ASU)**  
Minimalni nezavisni deo iz kog simetrijske operacije generišu ceo kristalni sadržaj. Nije nužno jedan ceo molekul niti cela ćelija.

**Opšta / specijalna pozicija**  
Opšta pozicija nema dodatnu site simetriju i obično ima punu multiplicity; specijalna leži na elementu simetrije i ima manju multiplicity. To utiče na occupancy i broj atoma u ćeliji.

**Multiplicity**  
Broj simetrijski ekvivalentnih mesta generisanih iz jednog atom site-a u ćeliji. Nije isto što i occupancy.

**\(Z\)**  
Broj prijavljenih formula units u jediničnoj ćeliji. Zavisi od izabrane formule i ćelije; nije atomski broj.

**\(Z'\) („Z prime“)**  
U jednostavnom molekulskom slučaju broj kristalografski nezavisnih formula units u ASU. Za specijalne pozicije, polimere, disorder i složene višekomponentne forme zahteva pažljiviju definiciju.

**Kristalno pakovanje (packing)**  
Periodični način rasporeda i orijentacije molekula/komponenti. Isti molekul može imati različit packing; ista ćelija/space group nije dovoljan dokaz istog packing-a.

**Kristalni habit**  
Spoljašnji oblik kristala uslovljen relativnim brzinama rasta lica. Različit habit ne mora značiti različitu unutrašnju kristalnu strukturu.

**Mreža kontakata / interaction graph**  
Graf periodičnih suseda prema navedenim definicijama H-veza, koordinacije ili kontakta. Rezultat zavisi od cutoffs, uglova, H položaja i disorder-a.

## Difrakcija, model i kvalitet

**Rendgenska difrakcija**  
Elastično rasipanje rendgenskih talasa na elektronskoj gustini kristala. Meri se obrazac intenziteta; atomski model se rešava i refinira iz podataka.

**Braggov zakon**  
Uslov konstruktivne difrakcije \(2d\sin\theta=n\lambda\), gde je \(d\) razmak familije ravni, \(\theta\) ugao, \(\lambda\) talasna dužina, a \(n\) red.

**Recipročna rešetka**  
Matematički prostor u kome se periodične ravni i difrakcione refleksije prirodno opisuju. U konvenciji bez \(2\pi\), \(\mathbf g_{hkl}=h\mathbf a^*+k\mathbf b^*+l\mathbf c^*\) i \(d(hkl)=1/\lVert\mathbf g_{hkl}\rVert\).

**Millerovi indeksi \((hkl)\)**  
Celobrojne oznake familija rešetkastih ravni/refleksija. Nisu atomske koordinate.

**Refleksija**  
Jedna tačka/meren intenzitet u difrakcionom skupu vezan za \((hkl)\). Symmetry-equivalent merenja mogu se spojiti u jedinstvenu refleksiju.

**Systematic absence / extinction**
Refleksija zabranjena translacionim delom space-group simetrije, npr. centriranjem, screw ili glide operacijom. Razlikuje se od dozvoljene, ali slabe/neopažene refleksije.

**Simulirani / izmereni PXRD**
Simulirani pattern je deterministički derivat crystal model-a pod navedenim wavelength/profile settings-ima. Izmereni PXRD dolazi iz bulk uzorka i instrumenta; može podržati fazni identitet ili mešavinu, ali sam ne potvrđuje svaki SCXRD atom/refinement detalj.

**Strukturni faktor \(F_{hkl}\)**  
Kompleksna amplituda izračunata kao zbir rasipanja svih atoma sa fazama određenim položajima. Intenzitet je približno proporcionalan \(\lvert F\rvert^2\).

**Fazni problem**  
Detektor meri intenzitete, ali ne direktno faze strukturnih faktora. Rešavanje strukture mora proceniti faze/model pre refiniranja.

**Rešavanje strukture**  
Dobijanje početnog atomskog modela iz difrakcionih podataka i hemijskog znanja. Razlikuje se od kasnijeg refiniranja.

**Refiniranje**  
Optimizacija parametara modela (položaji, displacement, occupancy…) da bi izračunati podaci bolje odgovarali opaženim, uz restraints/constraints i težine.

**Least squares**  
Optimizacija zbira težinskih kvadrata ostataka. Mala vrednost ciljne funkcije ne garantuje da je model jedinstven ili hemijski ispravan.

**R faktor**  
Konvencionalni ostatak zasnovan na razlikama opaženih i izračunatih amplituda. Mora se navesti skup refleksija, npr. all ili `gt`; univerzalni quality cutoff nije validan.

**wR**  
Težinski ostatak, često na \(F^2\). Zbog druge formule i težina obično nije direktno uporediv sa konvencionalnim R.

**GoF / \(S\)**  
Goodness of fit: odnos težinskih ostataka prema broju stepeni slobode. Vrednost blizu 1 ima smisla samo uz realistične weights/uncertainties; nije sertifikat tačnosti.

**\(R_{\mathrm{int}}\)**  
Mera međusobnog slaganja symmetry-equivalent refleksija pre/pri spajanju. Govori o konzistentnosti merenja/obrade, ne direktno o potpunosti atomskog modela.

**Completeness**  
Udeo očekivanih jedinstvenih refleksija izmerenih do određenog ugla/rezolucije prema definisanoj geometriji. Mora se navesti rezolucioni opseg.

**Resolution / \(d_{\min}\)**  
Najmanji razmak ravni obuhvaćen podacima; manje \(d_{\min}\) znači višu prostornu rezoluciju. „Visok broj“ i „visoka rezolucija“ mogu jezički zbuniti.

**Redundancy**  
Prosečan broj ponovljenih merenja iste/jednake refleksije. Viša redundancija može poboljšati procenu, ali nije zamena za kvalitet ili completeness.

**Standardna neizvesnost (s.u.)**  
Neizvesnost izražena kao jedna standardna devijacija. `12.7138(3)` znači \(12.7138\pm0.0003\) u istoj jedinici, pod pretpostavkama procene.

**Restraint**  
Meki dodatni cilj koji preferira hemijski razumnu geometriju/displacement, ali dozvoljava odstupanje uz cenu. Broji se u objective-u.

**Constraint**  
Tvrdo smanjenje slobode: parametar je fiksiran ili algebrajski vezan za drugi. Ne mešati sa restraint-om.

**Occupancy**  
Udeo populacije atomskog mesta u modelu, uz multiplicity i symmetry kontekst. Vrednost 0,5 može opisivati alternativu/disorder, ne „pola atoma u svakom kristalu“.

**Disorder**  
Model više lokalnih položaja/orijentacija ili sastava koji se prosečno vide u kristalu. Alternative imaju povezane occupancy vrednosti; disorder nije automatski ni greška ni zanemarljiv.

**ADP / \(U_{\mathrm{iso}}\) / \(U_{\mathrm{ani}}\) / B faktor**  
Atomic displacement parameter opisuje prosečnu raspodelu položaja usled termalnog kretanja i/ili statičkog nereda. Izotropni model je sfera, anizotropni elipsoid; konverzije \(B\leftrightarrow U\) moraju biti eksplicitne.

**Rezidualna elektronska gustina**  
Razlika opažene i modelovane gustine posle refiniranja. Pikovi/rupе mogu ukazati na propušten atom, apsorpciju, disorder ili druge efekte; tumače se prostorno i hemijski.

**Apsorpciona korekcija**  
Korekcija za različito slabljenje rendgenskog zraka kroz kristal pri različitim orijentacijama. Posebno važna za jače apsorbujuće elemente/geometrije.

**Twinning**  
Kristal/dataset koji sadrži dve ili više domena povezane određenom transformacijom, čiji se difrakcioni doprinosi preklapaju. Zahteva model twin law/fractions i utiče na quality metrics.

**checkCIF / alert**  
IUCr validacioni servis i skup testova. Alert je strukturisan signal za proveru/objašnjenje, ne automatska presuda; odsustvo alert-a ne dokazuje hemijsku istinu.

**CIF**  
Crystallographic Information Framework: samopisujući tekstualni format zasnovan na data names, blokovima, loop tabelama i rečnicima. Može sadržati koordinatni model, eksperiment, strukture faktora i ugrađene tekstualne blokove.

## Čvrste forme i termodinamika

**Faza**  
Makroskopski homogena oblast sa ujednačenim fizičkim/hemijskim svojstvima. Jednofazni kristal i fizička mešavina dve faze nisu isto.

**Čvrsta forma**  
Operativni krovni termin za određenu kristalnu ili amorfnu realizaciju supstance, uključujući polymorph, salt, solvate/hydrate ili cocrystal klasifikacije. Uvek navedi taksonomiju.

**Polimorf**  
Jedna od različitih kristalnih struktura iste supstance/hemijskog sastava, uz definisanu terminološku konvenciju. Razlika u solventu ili proton transfer-u tipično nije „samo polimorf“.

**Polimorfizam**  
Sposobnost supstance da postoji u više kristalnih formi. Jedan pronađen kristal ne dokazuje da drugih nema.

**So**  
Jonska čvrsta forma sa suprotno naelektrisanim komponentama, često nastala proton transfer-om acid/base para. Položaj H i charge evidence mogu biti nejasni.

**Solvat / hidrat**  
Kristal koji uključuje molekule rastvarača; hidrat je solvat sa vodom. Gubitak rastvarača može promeniti strukturu; solvat nije samo „nečistoća“.

**Anhidrat**  
Forma bez kristalne vode. Ne znači da uzorak nikada nije bio izložen vodi ili da je jedina moguća forma.

**Kokristal (co-crystal)**  
Jednofazni kristalni materijal sa dve ili više različitih komponenti u određenom odnosu, pod stručnom definicijom koja ga razlikuje od prostog solvata/soli. Granica salt–cocrystal može zahtevati dokaz protonacije.

**Amorfno stanje**  
Čvrsto stanje bez dugodometnog kristalnog periodičnog uređenja. Nema jednu crystal cell/space group; lokalno uređenje ipak postoji.

**Kristalni pseudopolimorf**  
Stariji/nejednoznačan izraz često korišćen za solvate/hydrates. Bolje je eksplicitno reći solvat/hidrat.

**Termodinamička stabilnost**  
Niža odgovarajuća Gibbsova slobodna energija pri konkretnim \((T,p)\), sastavu i hemijskim potencijalima. Nije apsolutna etiketa forme za sve uslove.

**Metastabilna forma**  
Lokalni minimum slobodne energije koji može dugo opstati zbog kinetičke barijere iako druga forma ima niži \(G\). Nije automatski greška ili bezvredna forma.

**Gibbsova slobodna energija**  
\(G=H-TS\); pri konstantnim \((T,p)\), razlika \(\Delta G\) određuje termodinamički smer/ravnotežu pod datim uslovima. Kristalni \(G\) nije samo izolovana molekulska energija.

**Entalpija / entropija**  
Entalpijski doprinos obuhvata energetiku/interakcije; entropijski doprinos broji dostupnost stanja i disorder/dinamiku. Stabilnost forme zavisi od oba i od temperature.

**Energija rešetke**  
Energetska mera kohezije kristala prema definisanom referentnom stanju. Nije puna Gibbsova slobodna energija i ne uključuje automatski sve termalne/entropijske efekte.

**Nukleacija**  
Nastanak kritičnog jezgra nove faze. Zavisna je od supersaturacije, interfejsa, nečistoća, površina, mešanja i vremena; kinetika može izabrati metastabilnu formu.

**Rast kristala**  
Dodavanje jedinki postojećem jezgru/licu. Uslovi rasta utiču na habit, defekte, veličinu i koja forma preživi.

**Supersaturacija**  
Stanje u kome koncentracija/hemijski potencijal prelazi ravnotežnu vrednost za određenu formu, dajući pokretačku silu za nukleaciju/rast. Vezana je za konkretnu formu i uslove.

**Enantiotropija / monotropija**  
Enantiotropni polimorfi menjaju relativnu stabilnost na temperaturi tranzicije pre topljenja; kod monotropnih jedan je stabilniji kroz relevantan opseg. Eksperimentalna klasifikacija zahteva termalne/ravnotežne dokaze.

**Rastvorljivost**  
Ravnotežna količina supstance koja se rastvara pri definisanim uslovima i specijaciji. Razlikuje se po formi i nije isto što i brzina rastvaranja.

**Brzina rastvaranja (dissolution rate)**  
Kinetika prelaska materijala u rastvor; zavisi i od površine, habit-a, veličine čestica, mešanja i forme.

**Talište / entalpija topljenja**  
Temperatura prelaza i toplotni efekat pod definisanim uslovima. Više talište samo po sebi ne daje univerzalni poredak stabilnosti bez pune termodinamičke analize.

## Digitalni hemijski podaci i formati

**Parser**  
Softver koji sintaksu fajla pretvara u strukturisan objekat. Uspešan parse znači da je nešto pročitano, ne da je hemija tačna.

**Schema / data dictionary**  
Formalna definicija polja, tipova, jedinica, odnosa i dozvoljenih vrednosti. CIF rečnik daje semantiku data name-ova; proizvoljno SDF property ime nema automatski tu snagu.

**MOL**  
MDL connection-table format za jedan molekulski zapis: atomi, veze i opcione koordinate/properties. Ne čuva periodičnost kristala.

**MOL2**  
Tripos format sa atom/bond tipovima, substructure i opcionalnim charges. Tipovi poput `C.ar` ili `N.3` su dodela modela/izvoznika.

**SDF**  
Structure Data File: niz MOL zapisa razdvojenih sa `$$$$`, uz property polja. Zahteva eksplicitnu dataset schemu i missing/unit pravila.

**SMILES**  
Linijski zapis molekulskog grafa. Isti graf ima više validnih SMILES; canonical SMILES zavisi od implementacije i ne čuva crystal cell/packing.

**SMARTS**  
Jezik za strukturne obrasce/upite, sa wildcard i logičkim uslovima. SMARTS nije identifikator molekula.

**InChI / InChIKey**  
Standardizovani IUPAC linijski identifikator i njegov sažeti hash-like ključ. Layers/policy su važni; ne kodiraju pun kristalni packing ili eksperimentalni entry.

**CSD**  
Cambridge Structural Database: CCDC-ova kurirana, licencirana baza malih organskih i metal-organskih kristalnih struktura. Nije isto što i CCDC organizacija/portfolio.

**CSD entry**  
Jedan bazni zapis o konkretnom strukturnom određivanju i metapodacima. Nije nužno jedinstven molekul, compound family ili čvrsta forma.

**CCDC refcode**  
Identifikator CSD entry/family konvencije. Sličan prefiks može povezivati određivanja, ali sam string nije dovoljan ground truth za identitet forme.

**ConQuest / `.cqs`**  
CCDC alat za strukturne i metadata upite; `.cqs` je binarni query/session objekat. Dostavljeni lokalni fajlovi sadrže i sačuvano stanje/rezultate, ali nisu obične prenosive result-liste. Naziv upita izražava nameru, dok stvarni atom/bond/filter constraints određuju semantiku.

**Mercury / Mogul / CSD Python API**  
CCDC alati: vizuelizacija/analiza kristala; distribucije geometrije iz CSD-a; programski pristup funkcijama i podacima u granicama licence. „API“ ovde znači application programming interface, ne active pharmaceutical ingredient.

**Hydrogen-bond propensity (HBP)**
Statistički model zasnovan na funkcionalnim grupama, fitting evidence-u i logističkoj regresiji za potencijalne donor–acceptor ishode. Individual propensity, observed H-veza, network grouping i coordination score su različiti output-i; nijedan sam nije polymorph probability ili lattice energy.

**API (active pharmaceutical ingredient)**  
Farmaceutski aktivna supstanca. U dokumentaciji uvek razjasni da li `API` znači aktivni sastojak ili programski interfejs.

**Raw / canonical / derived**  
Raw je netaknut izvor/parsiran dokaz; canonical je kurirana task-specific verzija; derived su fingerprints, embeddings, izveštaji i modeli. Ne prepisivati jedan sloj drugim.

**Normalizacija**  
Kontrolisana promena zapisa u dosledniji oblik, npr. jedinice ili whitespace. Mora se razlikovati od hemijske standardizacije koja menja reprezentaciju identiteta.

**Standardizacija**  
Verzionisana pravila za components, charges, bonds, aromaticity, tautomers, coordinates i crystal setting. Nije neutralna; rezultat zavisi od zadatka.

**Kanonski zapis**  
Deterministički izabrana reprezentacija unutar definisanog algoritma/verzije. „Kanonski“ ne znači univerzalno jedini istinit zapis.

**Lossless / lossy transformacija**  
Lossless omogućava rekonstrukciju svih relevantnih informacija; lossy odbacuje ili sažima deo. CIF→SMILES je namerno lossy za crystal context.

**Missing / unknown / not applicable**  
Nedostaje, nije poznato i nije primenljivo nisu nula. U CIF-u `?` i `.` imaju posebna značenja; u ML šemi moraju ostati odvojeni statusi.

**Provenance / lineage**  
Provenance beleži poreklo, alat, osobu, vreme i okolnosti artefakta; lineage povezuje izvedeni rezultat sa tačnim ulazima i transformacijama.

**Hash**  
Deterministički sažetak bajtova, npr. SHA-256. Detektuje promenu konkretnog fajla; ne potvrđuje naučnu istinu, vlasništvo ili licencu.

**Representation version**  
Identifikator pravila/softvera koji su proizveli graf, fingerprint, ćeliju, embedding ili drugi prikaz. Bez njega se score-ovi ne smeju mešati.

## Cheminformatika i sličnost

**Molekulski graf**  
Graf čiji su čvorovi atomi, a ivice veze prema definisanom bond modelu. Ne sadrži automatski periodičnost, crystal packing ili eksperimentalni quality.

**Atom/bond typing**  
Dodela hemijskih kategorija atomima/vezama radi pretrage ili modela. Kod aromatičnosti i metala može biti višeznačna; čuvaj alat, verziju i confidence.

**Atom mapping**  
Eksplicitno uparivanje atoma između dve reprezentacije/reakcije. Mora prethoditi RMSD-u i objašnjenju lokalnih razlika.

**Exact graph match**  
Izomorfizam grafova pod pravilima za element, bond order, charge, isotope i stereo. Exact zavisi od tog policy-ja.

**Podstrukturna pretraga**  
Pita da li target sadrži query podgraf. Asimetrična je: mali query može biti u velikom target-u, ne obrnuto.

**MCS**  
Maximum common substructure: najveći zajednički podgraf prema pravilima. Može imati više jednakih mapiranja i biti računski skup.

**Deskriptor**  
Numerička ili kategorijska karakteristika, npr. masa, broj H-bond donora, koordinacioni broj ili cell volume. Svaki deskriptor ima definiciju i scope.

**Fingerprint**  
Skup/vektor hemijskih feature-a, često binarni, napravljen za brzu pretragu. Kolizije i gubitak informacije su očekivani.

**Morgan/ECFP fingerprint**  
Circular fingerprint koji iterativno kodira lokalna atomska okruženja do radius-a. Parametri, chirality, bit length/count mode i standardizacija menjaju rezultat.

**Tanimoto koeficijent**  
Za binarne skupove \(T=\frac{\lvert A\cap B\rvert}{\lvert A\rvert+\lvert B\rvert-\lvert A\cap B\rvert}\). Vrednost ima smisla samo uz identičnu fingerprint definiciju i task kontekst.

**Embedding**  
Naučena ili projektovana kontinuirana vektorska reprezentacija. Blizina u embedding prostoru odražava cilj/podatke treninga; nije univerzalna hemijska istina.

**RMSD**  
Korenska srednja kvadratna udaljenost mapiranih koordinata posle definisanog poravnanja. Bez mapping-a, coverage-a i symmetry/policy parametara može biti obmanjujuća.

**Packing similarity**  
Poređenje periodičnih molekulskih okruženja, često preko klastera suseda i RMSD-a. Broj matched molecules, shell, tolerancije i component policy su deo rezultata.

**Similarity profile**  
Verzionisan paket definicija: objekti, standardizacija, metrike, parametri, težine, missing/abstention pravila i evidence schema.

**Candidate generation / reranking**  
Prva faza brzo vraća širok kandidatni skup sa visokim recall-om; druga primenjuje skuplje, preciznije metode. Candidate recall je obavezna metrika.

**ANN**  
Approximate nearest-neighbor pretraga. Brža je od exact pretrage, ali može propustiti susede; indeks i parametri moraju biti evaluirani.

**Coverage**  
Udeo objekta/podataka koji je zaista poređen ili ocenjen. Nizak RMSD na tri atoma može imati loš coverage.

**Score / distance / probability**  
Score je vrednost određene funkcije; distance meri razdvojenost prema metric/semi-metric definiciji; probability je kalibrisana verovatnoća događaja. Ne koristiti reči kao sinonime.

## ML, evaluacija i privatnost

**Feature / label / target**  
Feature je ulazna karakteristika; label je referentna oznaka; target je ono što model predviđa. Polje nastalo posle događaja ili iz ekspertske odluke ne sme slučajno u features.

**Klasifikacija / regresija / rangiranje / retrieval**  
Klasifikacija bira kategoriju, regresija broj, rangiranje uređuje kandidate, retrieval pronalazi kandidate iz velike kolekcije. Zahtev određuje metrike.

**Ground truth / referentna anotacija**  
Operacionalizovana ekspertska ili eksperimentalna odluka sa pravilima, evidence-om i confidence-om. Naziv fajla, ConQuest query ime ili model score nisu ground truth.

**Train / validation / test skup**  
Train uči parametre; validation bira modele/thresholds; test se koristi tek za finalnu nepristrasnu procenu. Promena nakon gledanja testa čini ga delom razvoja.

**Data leakage**  
Informacija nedostupna u realnoj primeni ili skoro duplikat prelazi iz test/ budućnosti u trening. U CSD-u su rizični redeterminations, ista compound family/publikacija i derivati istog entry-ja.

**Random / scaffold / group / temporal split**  
Random deli zapise nasumično; scaffold grupiše hemijska jezgra; group čuva familije/izvore zajedno; temporal odvaja buduće podatke. Split se bira prema claim-u.

**Baseline**  
Jednostavna transparentna metoda protiv koje se meri složeni model: formula filter, substructure, ECFP+Tanimoto, metal/donor pravilo, RMSD ili reduced-cell kandidat.

**Ablation**  
Eksperiment uklanjanja jedne komponente sistema da bi se procenio njen doprinos, uz isti evaluation protokol.

**Class imbalance**  
Velika razlika u učestalosti klasa. Accuracy može biti visoka predviđanjem većinske klase; koristi odgovarajuće precision/recall i PR metrike.

**Precision / recall**  
Precision (=TP/(TP+FP)): koliko predviđenih pozitivnih je tačno. Recall (=TP/(TP+FN)): koliko stvarno pozitivnih je pronađeno.

**F1**  
Harmonijska sredina precision-a i recall-a. Jedan F1 i dalje može sakriti različite threshold trade-offe i slice greške.

**ROC-AUC / PR-AUC**  
Površine ispod ROC i precision–recall krivih kroz pragove. PR-AUC je često informativniji za retku pozitivnu klasu; nijedna ne zamenjuje operativni threshold.

**Recall@k / precision@k**  
U retrieval-u, recall@k meri udeo relevantnih objekata pronađenih u prvih \(k\), precision@k udeo relevantnih među prvih \(k\). Oba zavise od potpunosti relevantnog seta.

**MRR / MAP / nDCG**  
MRR naglašava rank prvog relevantnog rezultata; MAP prosečnu precision kroz relevantne pogodke; nDCG podržava graded relevance i jače vrednuje vrh rangiranja.

**Calibration**  
Saglasnost predviđene verovatnoće sa empirijskom učestalošću. Score 0,9 nije 90% verovatnoća bez kalibracije za taj domen.

**Brier score / calibration error**  
Brier meri kvadratnu grešku probabilističkih prognoza; calibration error grupisano odstupanje confidence-a od učestalosti. Navedi implementaciju/binning.

**Uncertainty / evidence confidence**  
Uncertainty opisuje neizvesnost predikcije/parametra; evidence confidence pouzdanost ulaza i reprezentacije. Visok model score može imati nizak evidence confidence.

**Abstention**  
Svesna odluka sistema da ne da claim kada nema potreban input, objekat je ambiguous/out-of-domain ili je rizik previsok.

**Applicability domain / out-of-domain**  
Oblast hemijskog i podatkovnog prostora za koju je model evaluiran; out-of-domain slučaj nema isti dokaz performansi.

**Domain shift / concept drift**  
Menja se raspodela ulaza/uslova ili veza feature–target tokom vremena, institucija ili CSD release-a. Monitoring mora pratiti slice i release verzije.

**Hard positive / hard negative**  
Težak pozitivan je relevantan uprkos površinskoj razlici; težak negativan je nerelevantan uprkos velikoj površinskoj sličnosti, npr. isti ligand ali druga koordinaciona geometrija.

**Invariance / metamorphic test**  
Invariance zahteva isti rezultat posle semantički neutralne transformacije; metamorphic test proverava poznat odnos između izlaza kada nema jednostavnog oracle-a.

**p50 / p95 latencija**  
Medijana i 95. percentil vremena odziva. Prosek može sakriti spor dugi rep.

**Federativno učenje (FL)**  
Učenje zajedničkog modela uz lokalno zadržavanje podataka i razmenu update-a prema protokolu. Ne znači automatski privatnost, dozvolu ili zaštitu IP-a.

**FedAvg**  
Federated Averaging: agregacija lokalno treniranih model update-a težinski prema količini podataka, pod određenim pretpostavkama. Non-IID klijenti mogu otežati konvergenciju i pravednost.

**Non-IID**  
Lokalni skupovi nisu nezavisno i isto distribuirani: različite laboratorije imaju različitu hemiju, instrumente, kuraciju i property protokole.

**Secure aggregation**  
Kriptografski protokol kojim server uči agregat update-a bez uvida u pojedinačni update, pod modelom pretnji. Ne sprečava sve inferencije iz konačnog modela/agregata.

**Differential privacy (DP)**  
Formalna statistička garancija ograničenog uticaja jednog zapisa/učesnika, uz parametre \(\varepsilon,\delta\), clipping i noise. Privatnost ima kumulativni budžet i utility trade-off.

**Gradient/model leakage**  
Mogućnost rekonstrukcije ili inferencije o podacima iz gradients, update-a, modela ili izlaza. „Nismo poslali raw CIF“ nije dokaz bezbednosti.

## Upravljanje, licence i FAIR

**Metadata**  
Podaci o podacima: identitet, schema, units, source, uslovi, quality, licenca i veze. Metadata mogu biti dostupni i kada je sadržaj restricted.

**Identifikator / verzija**  
Identifikator kaže koji je logički objekat; verzija koji tačno snapshot/representation. Filename nije dovoljan persistent ID.

**Licenca / ugovor / policy**  
Licenca/ugovor pravno određuju dozvoljenu upotrebu; policy je njihova izvršiva tehnička interpretacija. Tehnička mogućnost pristupa nije dozvola.

**Open data / public domain**  
Open data imaju dozvolu za pristup i ponovnu upotrebu pod navedenim uslovima; public domain je druga, šira pravna kategorija. Javno vidljivo nije automatski open.

**FAIR**  
Findable, Accessible, Interoperable, Reusable. Accessible može zahtevati autentikaciju/autorizaciju; FAIR ne znači nužno open, free, public ili quality-certified.

**Ontology / controlled vocabulary**  
Formalno definisani koncepti i relacije / dozvoljen skup termina. Sprečavaju da `solvent`, `coformer` i `counterion` postanu slobodni, nedosledni stringovi.

**Claim ledger**  
Verzionisan registar naučnih, tehničkih i licencnih tvrdnji: precizan claim, scope, izvor, lokalni test, confidence, datum provere, rok revalidacije i status.

**Audit trail**  
Neizmenjiv ili kontrolisano verzionisan dnevnik događaja: pristup, transformacija, pregled, eksport, opoziv i brisanje.

**Fail closed**  
Kada dozvola ili potreban dokaz nedostaju, operacija je blokirana. Suprotno, fail open bi pretpostavio dozvolu/uspeh.

**Derivative**  
Artefakt izveden iz izvora: standardized record, fingerprint, embedding, indeks, model ili izveštaj. Nije automatski slobodan od licence izvora.

**Karantin**  
Stanje u kome se raw evidence čuva, ali se sadržaj ne pušta u canonical indeks/trening/eksport dok se konflikt ne pregleda.

## Termini koji se često pogrešno poistovete

| Nije isto | Kratka razlika |
|---|---|
| CCDC / CSD | organizacija i portfolio / konkretna strukturna baza |
| entry / molekul | zapis jednog određivanja / hemijska jedinka |
| formula / graf | broj elemenata / povezanost atoma |
| graf / konformer | povezanost / jedan 3D raspored |
| molecule / crystal | konačna jedinka / periodični raspored |
| cell / packing | izbor translacione kutije / raspored sadržaja kroz periodični prostor |
| \(Z\) / \(Z'\) | formula units u ćeliji / nezavisni sadržaj ASU u jednostavnom slučaju |
| occupancy / multiplicity | populacija mesta / broj symmetry-equivalent mesta |
| formal charge / oxidation state / partial charge | Lewis knjigovodstvo / jonska formalizacija / modelovana necela raspodela |
| salt / cocrystal | jonske komponente/proton transfer / višekomponentna jednofazna forma po konvenciji |
| solvat / polymorph | promenjen sastav rastvaračem / drugi arrangement iste supstance |
| solubility / dissolution rate | ravnotežna količina / kinetika rastvaranja |
| R / wR / GoF | različite objective/statističke veličine |
| restraint / constraint | meko pravilo / tvrda algebrajska veza |
| missing / 0 | nema poznate vrednosti / poznata nulta vrednost |
| score / probability / confidence | vrednost metrike / kalibrisana učestalost / pouzdanost dokaza |
| similar / same | task-specific blizina / identitet po eksplicitnoj definiciji |
| FAIR / open | upravljivost i ponovna upotreba / prava javnog pristupa-upotrebe |
| private repo / licence | kontrola pristupa hostu / pravna dozvola kopiranja i deljenja |

## Autoritativne tačke za proveru definicija

- [IUPAC Gold Book](https://goldbook.iupac.org/) — hemijska terminologija; posebno [ligand](https://goldbook.iupac.org/terms/view/L03518), [coordination entity](https://goldbook.iupac.org/terms/view/C01330), [polymorph](https://goldbook.iupac.org/terms/view/15225) i [standard uncertainty](https://goldbook.iupac.org/terms/view/S05928).
- [IUCr Online Dictionary of Crystallography](https://dictionary.iucr.org/) — kristalografija; posebno [unit cell](https://dictionary.iucr.org/Unit_cell), [asymmetric unit](https://dictionary.iucr.org/Asymmetric_unit), [space group](https://dictionary.iucr.org/Space_group), [Bragg's law](https://dictionary.iucr.org/Bragg%27s_law) i [refinement](https://dictionary.iucr.org/Refinement).
- [IUCr CIF dictionaries](https://www.iucr.org/resources/cif/dictionaries) — formalno značenje CIF data names.
- [OpenStax Chemistry 2e](https://openstax.org/details/books/chemistry-2e) — početničko objašnjenje atoma, veza, geometrije, interakcija, čvrstih struktura i termodinamike.
- [CCDC CSD Python API dokumentacija](https://downloads.ccdc.cam.ac.uk/documentation/API/) — ponašanje CCDC alata i task-specific pojmovi; verziju i licencu proveravati iznova.
