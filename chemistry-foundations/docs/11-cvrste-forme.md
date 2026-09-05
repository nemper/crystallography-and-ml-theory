# 11. Polimorfi i druge čvrste forme

**Preduslov:** razlikuješ hemijske komponente, protonaciju i jonske forme iz [poglavlja 4](04-organska.md), a kristalni raspored, simetriju i kvalitet modela iz [8](08-celija.md), [9](09-simetrija.md) i [10](10-difrakcija-kvalitet.md). [Interakcije](07-interakcije.md) daju fizički most; entalpija i entropija uvode se ovde pre termodinamičkog računa.

## Šta treba da umeš posle ovog poglavlja

Posle ovog poglavlja treba da možeš da:

- razlikuješ hemijski entitet, čvrstu formu, kristalnu strukturu i pojedinačno eksperimentalno određivanje;
- razdvojiš polimorf od soli, hidrata, solvata i kokristala;
- objasniš zašto ista aktivna supstanca može imati različitu solubilnost, melting point i stabilnost;
- koristiš Gibbsovu slobodnu energiju kao minimalni termodinamički model;
- objasniš zašto kinetika kristalizacije može dati metastabilnu formu;
- formiraš solid-form familije bez oslanjanja samo na SMILES, formulu ili CSD refcode;
- prevedeš čvrstu formu u filtere, reprezentacije i ground truth za obe aplikacije.

## Intuicija: isti molekul, drugačiji materijal

Zamisli jednake kockice koje možeš da složiš u više stabilnih zidova. Kockice su iste, ali raspored kontakata, gustina i način na koji se zid lomi nisu isti. Kod molekulskih kristala „kockice“ mogu i da promene konformaciju, pa različiti kristalni rasporedi imaju različite intermolekulske interakcije i slobodne energije.

Zbog toga isti molekulski graf ne određuje jedinstven čvrsti materijal. Promena forme može promeniti:

- equilibrium solubility i brzinu rastvaranja;
- melting point i toplotu topljenja;
- fizičku i hemijsku stabilnost;
- higroskopnost;
- gustinu, tvrdoću i crystal habit;
- tok praha, filtraciju, mlevenje i druge proizvodne osobine.

[IUPAC definicija polymorph-a](https://goldbook.iupac.org/terms/view/15225) upravo naglašava različite kristalne vrste istog solidnog materijala i mogućnost različitih fizičkih svojstava.

## Četiri nivoa identiteta

U farmaceutskim primerima **API** znači *active pharmaceutical ingredient*, odnosno aktivna farmaceutska supstanca. To je drugo značenje skraćenice od programskog API-ja (*application programming interface*) u ML/AI delu projekta.

| Nivo | Pitanje | Primer identifikatora |
|---|---|---|
| hemijski entitet | koji su povezanost atoma, stereokemija i protonaciono stanje? | InChI, standardizovani molekulski graf |
| sastav čvrste forme | koje su komponente, naboji i stehiometrija? | API:HCl:H2O = 1:1:1 |
| faza/polimorf | kako su komponente konformisane i periodično upakovane? | forma I, forma II |
| određivanje | kojim uzorkom, metodom, temperaturom i publikacijom je model izmeren? | jedan CIF/deposition/refcode |

Jedan hemijski entitet može imati više formi. Jedna forma može imati više redeterminations pri različitim temperaturama. Jedan CIF data block može sadržati jednu određenu strukturu, ali to nije dokaz da je ona jedina moguća forma.

## Precizne definicije

### Polimorf

Polimorfi su različite kristalne strukture istog hemijskog materijala, uz isti sastav. U molekulskom slučaju sama jednakost sumarne formule nije dovoljna: različiti konstitucioni izomeri nisu time postali polimorfi; moraju se proveriti identitet komponenti, stereokemija i stehiometrija. Razlika između polimorfa može biti:

- samo u pakovanju gotovo iste konformacije;
- u molekulskoj konformaciji i pakovanju;
- u mreži vodoničnih i drugih interakcija;
- u space group, jediničnoj ćeliji ili broju nezavisnih molekula.

Uska kristalografska definicija zahteva isti sastav. Zato dodavanje vode, rastvarača, counterion-a ili koformera stvara drugu vrstu čvrste forme, ne samo novi polimorf originalne bezvodne neutralne supstance.

### So

So je višekomponentna jonska forma. U farmaceutskom primeru proton se može preneti sa kiseline na bazni API, pa kristal sadrži kation i anion. „API hydrochloride“ nije isti hemijski sastav kao neutralni API.

Granica između soli i kokristala ponekad nije potpuno oštra samo iz formalnog 2D crteža: položaj protona može zahtevati kvalitetne strukturne i spektroskopske podatke. Razlika pKa može biti koristan trag, ali nije nepogrešiva presuda.

### Hidrat

[IUPAC hydrate](https://goldbook.iupac.org/terms/view/15195) u ovom kontekstu definiše kao kristalnu formu u kojoj su molekuli vode deo kristalne strukture. Voda može biti stehiometrijska, parcijalno zauzeta ili podložna gubitku pri promeni temperature i relativne vlažnosti.

### Solvat

[IUPAC solvate](https://goldbook.iupac.org/terms/view/15234) je kristalna forma u kojoj su jedan ili više molekula rastvarača deo strukture. Hidrat je poseban slučaj u kome je taj rastvarač voda.

Solvent u kristalnoj šupljini, kanalima ili kao deo mreže interakcija može biti teško modelovan. Desolvacija može ostaviti novu fazu, kolaps rešetke ili amorfni materijal.

### Kokristal

[IUCr Online Dictionary](https://dictionary.iucr.org/Co-crystal) opisuje kokristal kao jednofazni kristalni materijal sa dva ili više različitih molekulskih i/ili jonskih jedinjenja u uglavnom stehiometrijskom odnosu, koji nije prost solvat ili so. U farmaceutskom kontekstu često su to neutralni API i neutralni koformer u istoj rešetki.

[FDA guidance za farmaceutske kokristale](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/regulatory-classification-pharmaceutical-co-crystals) koristi regulatornu definiciju i zahteva dokaz da klasifikacija zaista odgovara materijalu. Terminologija zato mora biti verzionisana i vezana za naučni/regulatorni kontekst. Klasična stručna diskusija je [Aitipamula et al., “Polymorphs, Salts, and Cocrystals: What’s in a Name?”](https://doi.org/10.1021/cg3002948).

## Kategorije mogu da se kombinuju

Nazivi nisu uvek međusobno isključivi:

- so može biti hidrat;
- so može biti solvat;
- kokristal može imati vodu ili drugi solvent;
- jedna konkretna so ili kokristal može imati sopstvene polimorfe;
- višekomponentna forma može sadržati i neutralne i jonske komponente.

Zato jedan enum sa vrednostima <code>POLYMORPH | SALT | HYDRATE | SOLVATE | COCRYSTAL</code> nije dovoljan. Razumniji model čuva:

1. listu komponenti;
2. formalne naboje i protonaciona stanja;
3. stehiometriju;
4. uloge: API, counterion, water, solvent, coformer;
5. fazni identitet unutar istog sastava;
6. dokaz i confidence ljudske klasifikacije.

## Primer iz projekta: šta znamo iz cu_n14_a.cif

Lokalni CIF navodi:

- <code>_chemical_formula_moiety 'C25 H20 N3 O2 P'</code>;
- istu sumarnu formulu;
- \(Z=4\);
- jednu potpuno zauzetu listu atomskih mesta;
- nema eksplicitne water/solvent komponente;
- nema deklarisanih disorder grupa;
- <code>_chemical_melting_point ?</code>.

Najoprezniji zaključak glasi:

> Fajl modeluje jednu, naizgled jednokomponentnu kristalnu strukturu sastava C25H20N3O2P, izmerenu na 100 K, bez eksplicitno modelovanog kristalnog solvata ili hidrata.

!!! example "Ime fajla nije hemijski dokaz"
    Prefiks <code>cu</code> u nazivu fajla ne znači da struktura sadrži bakar: navedena formula nema Cu. Kompoziciju izvodi iz validiranog sadržaja i provenance-a, ne iz korisničkog imena fajla.

Iz tog fajla ne smeš zaključiti:

- da jedinjenje ne može stvarati hidrate ili solvate;
- da nema drugi polimorf;
- da je prikazana forma termodinamički najstabilnija;
- da je ista forma prisutna na sobnoj temperaturi;
- koliki joj je melting point;
- da je odsustvo solventa dokazano svim drugim analitičkim metodama.

Jedan SCXRD CIF je posmatranje jedne forme jednog uzorka pod jednim skupom uslova.

## Primer iz white paper-a

CCDC white paper na stranama 3 i 10 koristi melting point da pokaže zašto property mora biti vezan za konkretnu čvrstu formu. Vrednost „150 °C“ vezana samo za molekulski identitet može pomešati:

- polimorf I i polimorf II;
- anhidrat i hidrat;
- neutralnu formu i so;
- različite metode i brzine zagrevanja;
- početak topljenja, opseg ili raspad.

Na stranama 17–18 white paper opisuje polymorph-risk workflow: Mogul za konformacionu geometriju, packing comparison i hydrogen-bond propensity. To su izvori dokaza i prioriteta za eksperimente; nisu dokaz da neotkrivena forma sigurno postoji niti da je poznata forma najstabilnija.

Kako se gradi i tumači referentna geometrijska raspodela, zašto su torzije kružne i kako HBP razlikuje propensity, observed vezu, grouping i coordination score obrađeno je u [lekciji 11A](11a-referentne-raspodele-hbp.md).

[GSK/CCDC analiza](https://pubs.rsc.org/en/content/articlehtml/2021/ce/d1ce00665g) dodatno pokazuje koliko se interni i javni skupovi razlikuju po raspodeli solidnih formi. Autori su morali ručno da pregledaju strukture jer canonical SMILES, stereokemija i bond-order dodele nisu bili dovoljni za pouzdano grupisanje.

## Termodinamički minimum

**Pitanje:** zašto jedna forma može biti povoljnija na niskoj, a druga na višoj temperaturi? Različita pakovanja imaju različite interakcije, ali i različita dostupna mikroskopska stanja i kretanja.

**Entalpija** \(H=U+pV\) sabira unutrašnju energiju \(U\) i pritisno-zapreminski član \(pV\), gde su \(p\) pritisak, a \(V\) zapremina. Razlika entalpija pri stalnom pritisku odgovara razmenjenoj toploti kada je jedini rad pritisno-zapreminski. U kristalu na nju utiču međuatomske i intermolekulske interakcije, konformacija i toplotno kretanje; nije samo broj jakih kontakata.

**Entropija** \(S\) opisuje koliko su brojna i kako su dostupna mikroskopska stanja kompatibilna sa zadatim makroskopskim uslovima. Vibracije rešetke, molekulska kretanja i moguće orijentacije mogu razlikovati dve forme. Uredan kristal ima entropiju; iz vizuelnog utiska „više nereda“ ne možeš pouzdano odrediti njenu vrednost. [OpenStax o entropiji i mikrostanjima](https://openstax.org/books/chemistry-2e/pages/16-2-entropy) daje osnovu ovog tumačenja.

Pri konstantnoj temperaturi, pritisku i ukupnom sastavu, ravnotežno stabilno stanje ima najnižu Gibbsovu slobodnu energiju. Za poređenje polimorfa istog sastava koristi se ista količina supstance, na primer jedan mol iste formula unit:

\[
G = H - TS
\]

\(T\) je apsolutna temperatura u K. U računima po molu i \(G\), \(H\) i \(S\) odnose se na istu molarnu osnovu: \(G,H\) su u J/mol, a \(S\) u J/(mol·K), pa \(TS\) ima jedinicu J/mol. Član \(-TS\) pokazuje kako viša temperatura daje veći značaj entropijskoj razlici. Poređenje sastava sa različitim sadržajem vode obrađeno je [posebno ispod](#ravnoteza-hidrata).

Za dve forme A i B:

\[
\Delta G_{B-A}(T)=\Delta H_{B-A}-T\Delta S_{B-A}
\]

- ako je \(\Delta G_{B-A}>0\), A ima niži \(G\) i termodinamički je stabilnija;
- ako je \(\Delta G_{B-A}<0\), B je stabilnija;
- ako je \(\Delta G_{B-A}=0\), forme su u ravnoteži pri datim uslovima.

### Numerički primer

U nastavnom računu uzimamo dve konstantne razlike:

\[
\Delta H_{B-A}=1.0\ \text{kJ mol}^{-1}
\]

\[
\Delta S_{B-A}=4.0\ \text{J mol}^{-1}\text{K}^{-1}
\]

Tada:

\[
\Delta G_{B-A}=1000-4T\quad \text{J mol}^{-1}
\]

- na 100 K, \(\Delta G=+600\ \text{J mol}^{-1}\): A je stabilnija;
- na 298 K, \(\Delta G=-192\ \text{J mol}^{-1}\): B je stabilnija;
- linearno ekstrapolirani presek je na 250 K.

B ima entalpiju višu za 1000 J/mol, pa je pri niskoj temperaturi ta cena dominantna. Međutim, B ima i entropiju višu za 4 J/(mol·K): na 100 K član \(-T\Delta S=-400\) J/mol ne nadoknađuje cenu, dok na 298 K doprinosi −1192 J/mol i preokreće znak. Presek \(1000/4=250\) K pokazuje mesto izjednačenja u modelu. To ne govori koliko se brzo forma menja. [OpenStax Gibbsov kriterijum](https://openstax.org/books/chemistry-2e/pages/16-4-free-energy) povezuje znak slobodne energije i uslove ravnoteže.

### Stručna provera temperaturnog zaključka

Konstantnim \(\Delta H\) i \(\Delta S\) zanemarili smo razliku toplotnih kapaciteta \(\Delta C_p\), kao i topljenje, raspad i druge fazne prelaze koji bi se mogli javiti pre izračunatog preseka.

U ovom modelu redosled stabilnosti menja se sa temperaturom, što je obrazac
**kompatibilan** sa enantiotropijom. Sam presek dve aproksimirane prave nije
dokaz enantiotropnog odnosa: treba pokazati da obe faze postoje u relevantnom
opsegu i potvrditi fazni odnos eksperimentima, uz \(\Delta C_p\), topljenje,
raspad i druge prelaze. U monotropnom odnosu jedna forma ostaje stabilnija u
čitavom fizički relevantnom opsegu ispod topljenja.

!!! warning "Melting point nije slobodna energija"
    Viši melting point može biti važan trag, ali sam ne određuje stabilnost na svim temperaturama. Potrebni su entalpija/entropija, fazni prelazi, toplotni kapaciteti i eksperimentalni kontekst.

## Kinetika: zašto se prvo pojavi „pogrešna“ forma

Termodinamika kaže koja forma ima najniži \(G\) u ravnoteži. Kinetika određuje koliko brzo faza nukleira, raste ili prelazi u drugu fazu.

Sledeća kvalitativna skica važi pri jednoj fiksnoj temperaturi i istom sastavu, za slučaj kada A ima niži \(G\). Horizontalna osa je put transformacije, a ne vreme ili rastojanje između molekula:

```text
G ↑                         ‡ prelazno područje
  │                        / \
  │                       /   \_____ B: viši lokalni minimum
  │  \                   /
  │   \_____ A _________/             barijera: vrh − polazni minimum
  │          niži minimum
  └────────────────────────────────→ put transformacije
```

Razlika visina **dva minimuma** određuje ravnotežni smer B→A, dok visina prelaznog područja **iznad B** predstavlja barijeru tog prelaza. Zato B može opstati dugo. Skica sažima složen fazni put; stvarna nukleacija i rast zavise i od površina, veličine jezgra i uslova, pa brzinu ne određujemo iz ove skice.

Kristalizacija zavisi od:

- supersaturacije;
- solventa i aktivnosti vode;
- temperature i brzine hlađenja;
- brzine isparavanja;
- mešanja;
- nečistoća i površina;
- seeding-a;
- koncentracije i pH;
- vremena.

Metastabilna forma je lokalni minimum slobodne energije odvojen kinetičkom barijerom. Može nastati brže i opstati dovoljno dugo da bude izolovana, iako druga forma ima niži \(G\). „Metastabilno“ ne znači „trenutno se raspada“ niti „loš podatak“.

Nukleacija i rast takođe stvaraju selection bias baze: u bazi vidimo ono što je pokušano, kristalisalo, bilo merljivo i sačuvano, ne ceo prostor mogućih formi.

## Anhidrat i voda iz okoline u ravnoteži sa hidratom {#ravnoteza-hidrata}

Anhidrat i hidrat nemaju isti sastav. Za hidrat sa \(\nu\) molekula vode po istoj osnovnoj formulskoj jedinki bilans je:

\[
\text{anhidrat}+\nu\,\mathrm{H_2O}_{\mathrm{okolina}}
\rightleftharpoons\text{hidrat}.
\]

**Hemijski potencijal vode** \(\mu_w\) govori kako se Gibbsova energija rezervoara menja kada mu se pri zadatim uslovima doda mala količina vode, po molu dodate vode. On povezuje vodu u okolini sa vodom ugrađenom u čvrstu fazu. Za ovaj bilans po molu osnovne jedinke:

\[
\Delta_rG=G_{\mathrm{hidrat}}-G_{\mathrm{anhidrat}}-\nu\mu_w.
\]

Negativan \(\Delta_rG\) favorizuje hidrataciju, a nula znači ravnotežu tih faza sa zadatom okolinom. **Aktivnost vode** \(a_w>0\) je bezdimenziona mera njene termodinamičke dostupnosti u odnosu na izabrano standardno stanje, sa vezom:

\[
\mu_w=\mu_w^\circ+RT\ln a_w.
\]

\(\mu_w^\circ\) je referentni hemijski potencijal, \(R\) gasna konstanta u J/(mol·K), a \(T\) temperatura u K. Veća aktivnost pri istoj temperaturi povećava \(\mu_w\), pa član \(-\nu\mu_w\) više pogoduje hidrataciji. Aktivnost nije prosto broj molekula vode niti opšta koncentracija; njena definicija zavisi od izabranog standardnog stanja ([IUPAC: aktivnost](https://goldbook.iupac.org/terms/view/A00115)). [Studija hidrata/anhidrata karbamazepina](https://doi.org/10.1021/op7001497) pokazuje uticaj aktivnosti vode pri istoj temperaturi. Sam broj H-veza u hidratu ne odlučuje ovaj bilans.

## Solubilnost i fazna stabilnost

**Rastvorljivost** (*solubility*) počinje od ravnoteže `čvrsta faza ⇌ rastvorena vrsta`. U zasićenom rastvoru, pri zadatoj temperaturi, rastvaraču i hemijskom stanju, nema neto rastvaranja iako se razmena jedinki nastavlja. Hemijski potencijal iste komponente u čvrstoj fazi i rastvoru tada je jednak. Rastvorljivost opisuje sastav takvog rastvora; brzina kojom do njega stižemo je drugo pitanje.

Zatim proveri da li tokom merenja ostaje ista čvrsta faza. Ako početna forma A pređe u B, konačna koncentracija više ne opisuje jednostavno rastvorljivost početne A. Pri istim uslovima metastabilna forma često ima višu **rastvorljivost u odnosu na tu fazu**: njen viši hemijski potencijal dopušta višu zasićenu aktivnost rastvorene komponente. Ako faza ostaje nepromenjena do zasićenja, to je **metastabilna, fazno uslovljena rastvorljivost**, uz kinetički sprečen prelaz u stabilniju fazu.

### Stručna provera merenja

Globalna ravnoteža ne zadržava metastabilnu čvrstu fazu kada je prelaz u stabilnu dostupan; dugotrajnu zasićenu ravnotežu tada određuje stabilna faza. Vrednost se pripisuje metastabilnoj fazi samo uz potvrđen identitet tokom merenja i reproduktivan odnos čvrsta faza–rastvor na vremenskoj skali eksperimenta. Ako se faza transformiše ili zasićenje nije dostignuto, plato može biti kinetički ili prividan. Pored toga:

- dissolution rate nije isto što i equilibrium solubility;
- veličina čestice, površina i habit utiču na brzinu;
- forma se tokom merenja može transformisati;
- pH i jonizacija mogu dominirati;
- hidrat/solvat može menjati aktivnost i sastav;
- rezultat mora biti vezan za fazu koja je stvarno prisutna pre i posle merenja.

Zato property tabela mora imati najmanje: form ID, temperaturu, solvent/pH, metodu, jedinicu, uzorak, vreme, neizvesnost i dokaz faznog identiteta.

## Kako se forme eksperimentalno razlikuju

Nijedna pojedina metoda nije univerzalno dovoljna:

| Metoda | Primarni doprinos |
|---|---|
| SCXRD | atomski i periodični model jednog pogodnog kristala |
| PXRD | fazni fingerprint bulk uzorka i mešavine |
| DSC | endotermni/egzotermni događaji, topljenje i prelazi |
| TGA | gubitak mase, npr. desolvacija/dehidratacija |
| DVS | odgovor na relativnu vlažnost |
| IR/Raman/solid-state NMR | lokalno hemijsko okruženje i komponente |
| hot-stage microscopy | vizuelno praćenje faznih događaja |

„Isti SMILES“ ne razlikuje polimorfe. „Različita ćelija“ je jak trag, ali redetermination, temperatura, druga postavka ćelije ili pogrešna simetrija mogu napraviti prividnu razliku. Potrebno je kombinovati sastav, strukturu, uslove i eksperimentalne obrasce.

## Hijerarhija koja ne meša nivoe

Za teorijsko razumevanje treba razlikovati:

| Entitet | Ključne veze |
|---|---|
| Compound | standardizovani graf, stereokemija, tautomer/protomer politika |
| Component | compound, formalni naboj, uloga |
| Form composition | komponente i stehiometrija |
| Phase/Form | sastav, polymorph label, fazni odnosi |
| Determination | CIF, temperatura, pritisak, metoda, publikacija |
| Sample | batch, priprema, istorija, čistoća |
| Measurement | property, vrednost, jedinica, uslovi, uncertainty |
| Evidence | PXRD/SCXRD/DSC/TGA izvor i quality status |

Status hijerarhije identiteta objašnjen je u [centralnoj napomeni o teorijskom i referentnom sloju](kako-koristiti.md#teorijski-i-referentni-sloj). Naziv „Form I“ nije globalni identifikator: različite organizacije mogu različito numerisati forme, pa etiketa ima značenje samo uz izvor i namespace.

## Moguće ose relevantne za dve aplikacije

### Globalna pretraga

Tri različite moguće namere su:

1. sličan hemijski entitet bez obzira na formu;
2. ista/kompatibilna kompoziciona klasa;
3. slično kristalno pakovanje unutar uporedivih formi.

Mogući filteri, ako ih product scope potvrdi, uključuju:

- neutral/free form, salt, hydrate, solvate, cocrystal;
- broj komponenti i stehiometrija;
- charge state;
- prisustvo vode/solventa;
- ista formula ili isti parent compound;
- temperatura i quality profil određivanja.

Pogodak može biti sličan po molekulu, sastavu ili periodičnom pakovanju; jedan zbirni skor bez te dekompozicije može visoko rangirati hemijski sličnu, ali razvojno nerelevantnu formu. Koje ose budući proizvod prikazuje ostaje stakeholder odluka.

### Poređenje svih parova

Pre izbora metrike potrebno je konceptualno razjasniti odnos:

- isto određivanje/duplikat;
- redetermination iste faze;
- kandidat za polimorf;
- salt/solvate/hydrate/cocrystal odnos;
- drugačiji hemijski entitet.

Tek zatim treba računati odgovarajuće metrike. Packing RMSD između anhidrata i hidrata može biti koristan kao parcijalna analiza zajedničkog API okruženja, ali nije isto pitanje kao dokaz polimorfnosti.

Za stručno tumačenje para relevantni su:

- mapiranje komponenti i atoma;
- razliku sastava i naboja;
- konformacionu razliku;
- packing/interakcioni profil;
- uslove merenja;
- quality/uncertainty;
- klasifikaciju odnosa sa obrazloženjem.

## Tipične zamke

1. Nazvati svaki različit CIF polimorfom.
2. Nazvati hidrat polimorfom anhidrata bez označavanja promene sastava.
3. Tretirati so i neutralni API kao isti graf posle uklanjanja counterion-a.
4. Zaključiti „nema solventa“ samo zato što ga 2D reprezentacija ne prikazuje.
5. Koristiti InChIKey kao identifikator kristalne faze.
6. Zaključiti stabilnost iz jedne neobične torzije.
7. Izjednačiti thermodynamic stability, chemical stability i shelf-life.
8. Izjednačiti equilibrium solubility i dissolution rate.
9. Ignorisati temperaturu SCXRD merenja.
10. Napraviti train/test split u kome redeterminations ili forme istog parent compound-a cure na obe strane.

## Mini-vežbe

### 1. Isto ili različito?

Dva kristala imaju isti neutralni molekul i istu sumarnu formulu, ali različito pakovanje. Kako ih klasifikuješ?

??? success "Odgovor"
    Kao kandidate za polimorfe. Potrebno je isključiti trivijalnu promenu postavke ćelije, temperaturnu ekspanziju, redetermination i grešku modela.

### 2. API, HCl i voda

Jedna forma sadrži protonovani API, hlorid i jednu vodu po API. Koje oznake su relevantne?

??? success "Odgovor"
    To je so i hidrat. Kategorije se kombinuju; nije dovoljno izabrati samo jednu.

### 3. Šta dokazuje lokalni CIF?

Da li <code>cu_n14_a.cif</code> dokazuje da C25H20N3O2P nema polimorfe?

??? success "Odgovor"
    Ne. Dokazuje samo da je za jedan uzorak pod navedenim uslovima modelovana jedna konkretna kristalna struktura.

### 4. Termodinamički prelaz

Za \(\Delta H_{B-A}=1.0\ \text{kJ mol}^{-1}\) i \(\Delta S_{B-A}=4.0\ \text{J mol}^{-1}\text{K}^{-1}\), pri kojoj temperaturi su A i B približno u ravnoteži?

??? success "Odgovor"
    Uz pretpostavku konstantnih \(\Delta H\) i \(\Delta S\), i uz zanemarene
    \(\Delta C_p\), topljenje, raspad i druge fazne prelaze, \(\Delta G=0\)
    daje \(T=\Delta H/\Delta S=1000/4=250\ \text{K}\). To je presek
    idealizovanog modela, ne samostalan dokaz enantiotropije.

### 5. Dizajn split-a

Zašto nasumični split po CIF redovima može dati lažno dobru ML metriku za klasifikaciju formi?

??? success "Odgovor"
    Redeterminations, skoro identične strukture i više formi istog parent compound-a mogu završiti u treningu i testu. Model tada prepoznaje familiju ili eksperimentalni izvor umesto da generalizuje. Split treba grupisati najmanje po parent compound-u i povezanim određivanjima, a po potrebi i po scaffold-u ili vremenu.

## Kriterijum prolaza

Poglavlje si savladao kada za proizvoljan par CIF-ova možeš prvo da postaviš pitanje o sastavu i faznom identitetu, zatim izabereš prikladno strukturno poređenje i objasniš koje dodatne eksperimente treba tražiti pre tvrdnje o polimorfnosti ili stabilnosti.

## Primarni i autoritativni izvori

- [IUPAC Gold Book: polymorph](https://goldbook.iupac.org/terms/view/15225)
- [IUPAC Gold Book: solvate](https://goldbook.iupac.org/terms/view/15234)
- [IUPAC Gold Book: hydrate](https://goldbook.iupac.org/terms/view/15195)
- [IUCr Online Dictionary: co-crystal](https://dictionary.iucr.org/Co-crystal)
- [FDA: Regulatory Classification of Pharmaceutical Co-Crystals](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/regulatory-classification-pharmaceutical-co-crystals)
- [Aitipamula et al. 2012, DOI 10.1021/cg3002948](https://doi.org/10.1021/cg3002948)
- [Kalash et al. 2021, GSK/CCDC solid-form analiza](https://doi.org/10.1039/D1CE00665G)
