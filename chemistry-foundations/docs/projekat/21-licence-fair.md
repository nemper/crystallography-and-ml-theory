# 21. Licence, FAIR i poreklo podataka

## Šta treba da umeš posle ovog poglavlja

Posle ovog poglavlja treba da možeš da:

- razdvojiš tehničku mogućnost pristupa od pravne/ugovorne dozvole za upotrebu;
- objasniš zašto raw CSD podaci i CSD-derived skupovi nisu deo ovog repoa;
- pokažeš zašto privatni GitHub repo nije automatsko rešenje licencnog problema;
- primeniš FAIR na podatke koji ostaju poverljivi i kontrolisano dostupni;
- objasniš koje vrste provenance dokaza povezuju izvor, transformaciju, model i rezultat;
- prepoznaš nevidljivi, tematski nepodudarni embedded PDF tekst kao ingest i provenance incident;
- objasniš licence-aware pitanja koja obe 2CDC aplikacije moraju da razjasne.

!!! info "Granica ovog poglavlja"
    Ovo je inženjersko čitanje javno dostupnih uslova i principa, ne pravni savet. Merodavan je konkretan ugovor organizacije sa CCDC-om i pisano tumačenje vlasnika podataka.

## Prvo pravilo: mogu da pročitam nije isto što i smem da koristim

Za svaki dataset postoje najmanje četiri odvojena pitanja:

1. **Pristup:** može li nalog ili proces tehnički da pročita podatak?
2. **Dozvoljena obrada:** sme li da pretražuje, transformiše, indeksira ili trenira model?
3. **Deljenje:** sme li raw ili izvedeni rezultat napustiti licenciranu organizaciju/lokaciju?
4. **Objavljivanje:** smeju li kod, statistika, embedding, model ili primer biti javni?

Dozvola za jedno ne povlači automatski ostala. Download dugme nije licenca za redistribuciju; API token nije dozvola za javni mirror; mogućnost računanja embedding-a nije dokaz da se embedding sme objaviti.

## Šta javni CCDC uslovi zaista kažu

[CCDC Conditions of Use za CSD Python API i CSD Portfolio](https://downloads.ccdc.cam.ac.uk/documentation/API/conditions_of_use.html) navode, između ostalog, da:

- CSD Portfolio, njegovi programi, data files, baza i izvedeni podskupovi predstavljaju vlasničke komponente CCDC-a i njegovih licencora;
- upotreba zavisi od važećeg Licence of Access ili Products Licence and Support Agreement;
- komponente se tretiraju kao poverljive i ne redistribuiraju trećim licima u celini ili delovima;
- distribucija softvera ili podataka izvedenih iz ili razvijenih korišćenjem CSD Portfolio-a zahteva prethodno pisano odobrenje CCDC-a;
- naučni rezultati mogu biti objavljeni uz odgovarajuću citaciju i u granicama ugovora;
- zajednički akademsko-komercijalni projekti mogu zahtevati posebno odobrenje.

Važeći [CCDC Standard Licence Agreement](https://www.ccdc.cam.ac.uk/licence-agreement/) i ugovor konkretne institucije imaju prednost nad ovim sažetkom.

### Zašto CSD izvozi nisu u ovom repou

Originalni CSD izvozi nisu deo ovog obrazovnog repoa zato što dostupnost u licenciranom alatu ne daje automatski pravo kopiranja na drugog hosta ili redistribucije. Nastavni tekst može opisati agregate, metode i sintetičke primere, ali prihvatljivost svakog konkretnog raw ili izvedenog artefakta zavisi od ugovora, porekla i mogućnosti rekonstrukcije zaštićenog sadržaja. Ovo je objašnjenje sadašnjeg dokumentacionog scope-a, ne trajna allow/deny lista za budući razvoj.

Čak i private repo može predstavljati kopiju kod trećeg pružaoca usluge, imati širi krug naloga, backup-e i drugačiju geografsku lokaciju. „Private“ je kontrola pristupa, ne nova licenca.

!!! danger "Derived nije automatski slobodno"
    Embedding, fingerprint indeks, trenirani model, agregirane karakteristike ili eksportovani result set mogu biti izvedeni materijal. Da li se konkretan artefakt sme distribuirati zavisi od ugovora, mogućnosti rekonstrukcije, poslovne namene i pisanog odobrenja. Odsustvo jasne dozvole nije dokaz da je eksport dozvoljen.

## Konceptualne granice odgovornosti

Za licencnu analizu korisno je razlikovati sledeće domene, bez pretpostavke kako će oni tehnički biti realizovani:

| Domen | Sadržaj | Ključno pitanje |
|---|---|---|
| otvoreni kod i znanje | algoritmi, dokumentacija, sintetički primeri | šta se može zakonito deliti i ponoviti bez zaštićenih podataka? |
| licencirani podaci i derivati | CSD podaci, izvedene reprezentacije i licencirani alati | ko, gde i za koju namenu sme da ih koristi? |
| interni projektni podaci | interni CIF-ovi, svojstva i laboratorijski metadata | ko kontroliše poverljivost, obradu i rok čuvanja? |
| publikovani rezultat | odobrene metrike, slike, tabele ili modeli | da li izlaz otkriva ili rekonstruiše zaštićen sadržaj? |

Granice među domenima određuju prava i značenje podataka; same po sebi ne propisuju servis, API, lokaciju skladišta ili deployment arhitekturu.

## FAIR nije isto što i open

Originalni [FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18) znače:

| Slovo | Princip | Konceptualna posledica |
|---|---|---|
| F - Findable | podatak i metadata imaju stabilan identitet i mogu se pronaći | identitet ne treba da zavisi od filename-a ili trenutne lokacije |
| A - Accessible | postoji standardizovan postupak pristupa | pristup može zahtevati autentikaciju i autorizaciju |
| I - Interoperable | koriste se formalni jezici, rečnici i kvalifikovane veze | značenje jedinica, relacija i termina mora biti deljivo |
| R - Reusable | značenje, poreklo, licence i domenski standardi su dovoljno bogati | ponovna upotreba zavisi od konteksta, kvaliteta i dozvole |

Princip A1.2 eksplicitno dozvoljava autentikaciju i autorizaciju kada su potrebne. Zbog toga proprietary ili licencirani podatak može biti FAIR:

- metadata kaže da zapis postoji;
- identifikator je stabilan;
- uslovi pristupa su mašinski i ljudski razumljivi;
- ovlašćeni korisnik koristi standardni protokol;
- licenca i dozvoljene namene su eksplicitne;
- semantika i provenance ostaju dostupni u dozvoljenom obimu.

[GO FAIR objašnjenje FAIR naspram Open](https://www.go-fair.org/resources/faq/ask-question-difference-fair-data-open-data/) sažima princip kao „as open as possible, as closed as necessary“. Obrnuto takođe važi: fajl može biti javno dostupan, ali ne-FAIR ako nema stabilan identifikator, šemu, provenance, mašinski čitljivu licencu ili dosledne jedinice.

!!! warning "FAIR nije quality sertifikat"
    FAIR pomaže da se podatak pronađe, pristupi mu, poveže i ponovo upotrebi. Ne garantuje da je kristalografski model tačan, da je property dobro izmeren ili da ML skup nema bias. Quality i FAIR su povezani, ali različiti kontrolni slojevi.

## Licenca je deo značenja upotrebe, ne fusnota

Procena dozvoljenosti zavisi od više od naziva licence. Potrebno je razumeti ko kontroliše izvor, koji ugovor je merodavan, na koje korisnike, lokacije i namene se odnosi, da li pokriva čitanje, transformaciju, trening, čuvanje, deljenje i publikovanje, kao i šta se dešava pri isteku ili opozivu. Ove dimenzije su pitanja pravnog i podatkovnog scope-a, ne predlog konkretne permission schema-e ili policy engine-a.

Opšti bezbednosni princip je konzervativan: nepoznata dozvola ne može se tumačiti kao pozitivna dozvola.

## Provenance: dokazni lanac za svaki bajt i svaku tvrdnju

Provenance odgovara na pitanja:

- odakle je artefakt došao;
- ko ga je uneo i kada;
- koji ugovor/licenca važi;
- koji alat i verzija su ga parsirali;
- koje transformacije su izvršene;
- koji izlaz je nastao iz kojih ulaza;
- ko je pregledao alert ili izuzetak;
- da li se posledice opoziva ili isteka mogu pratiti kroz izvedene artefakte.

To zahteva identitet izvora, dokaz integriteta bajtova, vreme i poreklo prijema, vlasništvo i dozvolu, klasifikaciju poverljivosti, verzije alata i pravila, transformacioni lineage, status pregleda i veze ka roditeljskim artefaktima. Spisak opisuje kategorije dokaza; ne propisuje manifest, nazive polja ili storage model.

Hash dokazuje da je konkretan niz bajtova isti; ne dokazuje da je sadržaj tačan, vidljiv korisniku ili licencno dozvoljen.

## Lokalni CIF kao provenance primer

<code>cu_n14_a.cif</code> sadrži mnogo korisnih provenance tragova:

- <code>_audit_creation_method SHELXL-2013</code>;
- APEX5 verziju za data collection;
- SAINT verziju za cell refinement i reduction;
- XT/SHELXT za structure solution;
- SHELXL-2013 za refinement;
- ugrađene <code>_shelx_res_file</code> i <code>_shelx_hkl_file</code> blokove.

Istovremeno, systematic/common name, melting point, diffraction source i deo publication metadata polja imaju <code>?</code>. To znači „nepoznato/nije dato“, ne praznu nulu. Fajl zato nije samodovoljan dokaz o vlasništvu, dozvoli upotrebe, identitetu uzorka ili svim eksperimentalnim svojstvima.

Ugrađeni HKL podaci takođe znače da fajl sadrži više od atomskih koordinata. Pravilo eksportovanja „dozvoljen je CIF“ mora precizirati da li uključuje structure factors i refinement source.

## Nevidljivi, tematski nepodudarni embedded PDF tekst: stvarni ingest incident

Vizuelni pregled CCDC white paper-a pokazuje naslov „Maximising the Impact of Proprietary Structural Data“. Međutim, standardna tekstualna ekstrakcija sa strana 1–2 vraća i nevidljivi, tematski nepodudarni embedded tekst:

> Ultra-large docking. How to run ultra-large GOLD docking jobs on cloud resources.

Taj tekst se ne vidi na renderovanim stranama, a njegova tema se ne podudara sa vidljivim sadržajem dokumenta. Da je reč o zaostalom sloju ili šablonu PDF-a jeste **inferencija**, ne utvrđena činjenica; uzrok zahteva dodatnu forenzičku proveru PDF objekata i strukture slojeva.

Ako ingest sačuva samo izvučeni tekst:

- pretraga može pogrešno indeksirati white paper kao docking dokument;
- RAG može citirati tvrdnju koja korisniku nije vidljiva;
- klasifikator teme dobija pogrešan label signal;
- deduplikacija može povezati nepovezane dokumente;
- audit ne može objasniti odakle je rečenica došla.

### Koje dokaze PDF ingest mora da razlikuje

Ovaj incident pokazuje da originalni PDF, njegov hash i metadata, tekst koji vraća određeni parser, vizuelni render, eventualni OCR i odluka o tome koji sadržaj je vidljiv nisu ista vrsta dokaza. Razlika između embedded i vidljivog teksta mora ostati proverljiva, a sadržaj sa nerešenim konfliktom ne može imati isti status kao vizuelno potvrđen tekst. To su provenance i quality principi; konkretan workflow, statusi i način skladištenja zavise od budućeg okruženja.

!!! example "Zašto je ovo FAIR problem"
    Bez provenance-a ne možemo znati da li je rečenica došla iz vidljivog sadržaja, OCR-a, nevidljivog embedded sloja ili naknadne transformacije. Podatak može biti lako pronađen, ali nije pouzdano reusable jer mu poreklo i značenje nisu jasni.

## Konceptualni životni ciklus hemijskih i dokumentnih izvora

Kod hemijskih i dokumentnih izvora korisno je razlikovati registrovani izvor, parsiranu reprezentaciju, validacioni nalaz, stručno protumačen zapis, izvedene rezultate i kasniji status pristupa ili povlačenja. Svaki nivo odgovara na drugo pitanje: integritet bajtova, tehničku čitljivost, naučnu konzistentnost, stručnu odluku, poreklo derivata ili dozvoljenost dalje upotrebe.

Originalni, protumačeni i izvedeni sadržaj ne treba predstavljati kao istu vrstu činjenice. Ovaj životni ciklus je pojmovni model za razmišljanje o provenance-u, ne propisan ingest pipeline.

## Pitanja licence za globalnu pretragu

Globalna pretraga nad velikom licenciranom bazom otvara nekoliko odvojenih pitanja: gde je obrada dozvoljena, ko sme da vidi koji nivo rezultata, da li su indeksiranje i privremeni derivati dopušteni, da li rezultat omogućava bulk rekonstrukciju, šta sme da napusti organizaciju i kako istek ili opoziv utiču na ranije izvedene artefakte. I telemetrija i eksterni servisi mogu postati neželjen kanal podataka. Poglavlje ne bira API, tenant model, cache ili UI; ono pokazuje koje pravne granice takav dizajn mora da razjasni.

## Pitanja licence za poređenje svih parova

Kod korisničkih CIF-ova potrebno je razjasniti pravo na obradu, poverljivost, razdvajanje različitih vlasnika/projekata, eventualnu ponovnu upotrebu za trening, rok čuvanja i dozvoljeni sadržaj bogatog pairwise rezultata. Rezultat izveden iz dva izvora može naslediti ograničenja oba izvora. To su pitanja scope-a i lineage-a, ne predlog upload, retention ili export implementacije.

## Kako restricted podaci mogu biti FAIR

FAIR ne zahteva objavljivanje sadržaja CSD-a. Restricted podatak može imati stabilan identitet i bogate metadata bez otkrivanja koordinata, standardizovan ali kontrolisan pristup, interoperabilne rečnike i jedinice, eksplicitnu licencu i pun provenance. Informacija o postojanju ili povlačenju zapisa može ostati dostupna samo u meri koju ugovor dozvoljava.

Persistent identifier može biti interni i ne mora otkriti sadržaj. „Ne postoji za neovlašćenog korisnika“ i „postoji, ali zahteva dozvolu“ su različite policy odluke, a FAIR sam ne bira između njih.

## Tipične zamke

1. Privatni repo proglasiti licencom.
2. Pretpostaviti da se svaki API rezultat sme trajno keširati.
3. Objaviti embedding jer „nije raw CIF“.
4. Pomešati FAIR sa open, free ili public domain.
5. Pomešati open-source kod sa pravima na podatke koje kod obrađuje.
6. Sačuvati samo canonical record i izgubiti originalni dokaz.
7. Izgubiti verziju parsera, baze, checkCIF ruleset-a ili modela.
8. Tretirati <code>?</code> kao nulu.
9. Indeksirati nevidljivi, tematski nepodudarni embedded PDF tekst bez vizuelnog cross-check-a.
10. Propagirati brisanje na raw fajl, ali ostaviti cache, embedding i model derivative.
11. Slati proprietary sadržaj eksternom validatoru ili LLM-u bez odobrenja.
12. Verovati da citiranje izvora zamenjuje dozvolu za redistribuciju.

## Mini-vežbe

### 1. Privatni GitHub

Imaš CSD eksport i private repo sa dva saradnika. Da li ga smeš commit-ovati zato što repo nije javan?

??? success "Odgovor"
    Ne možeš to zaključiti. Private repo je tehnička kontrola, ali i dalje pravi kopiju kod treće strane i daje pristup drugim nalozima. Proveri konkretni CCDC ugovor i organizacionu politiku; bez dozvole raw eksport ostaje van repoa.

### 2. FAIR, ali zatvoreno

Može li interni proprietary dataset biti FAIR ako pristup zahteva login?

??? success "Odgovor"
    Da. FAIR A1.2 dozvoljava authentication/authorization. Potrebni su stabilni identifikatori, bogati metadata, standardan protokol, jasna licenca/uslovi, interoperabilna semantika i provenance.

### 3. Nevidljivi embedded PDF tekst

Parser nalazi docking tekst na naslovnoj strani, ali render ga ne prikazuje. Šta zaključuješ?

??? success "Odgovor"
    Embedded tekst i vidljivi sadržaj su različiti dokazi. Sporni tekst ne tretiraj kao potvrđen sadržaj dok se konflikt ne proveri renderom/OCR-om; sačuvaj poreklo ekstrakcije, parser i verziju.

### 4. Embedding za objavu

Model je treniran nad CSD-derived fingerprintima. Da li je dovoljno što model weights ne sadrže čitljive CIF redove?

??? success "Odgovor"
    Ne. Model može biti ugovorno izvedeni materijal i može memorisati ili omogućiti inference o podacima. Potrebna je licencna analiza, test rekonstrukcije/memorisanja i, kada uslovi zahtevaju, prethodno pisano odobrenje CCDC-a.

### 5. Istek licence

Licenca za izvor ističe sutra. Koji artefakti moraju biti pronađeni?

??? success "Odgovor"
    Raw kopije, canonical zapisi, cache, indeks, embeddings, trenirani/evaluirani modeli, report-i i backup-i povezani lineage grafom. Za svaki se primenjuje ugovorena retention/deletion ili review odluka.

## Kriterijum prolaza

Poglavlje si savladao kada možeš da objasniš kako se pristup, obrada, deljenje i objavljivanje razlikuju, zašto provenance mora povezati izvor i derivative i zašto FAIR ne ukida licencna ograničenja.

## Primarni i autoritativni izvori

- [CCDC CSD Portfolio Conditions of Use](https://downloads.ccdc.cam.ac.uk/documentation/API/conditions_of_use.html)
- [CCDC Standard Licence Agreement](https://www.ccdc.cam.ac.uk/licence-agreement/)
- [Wilkinson et al. 2016: FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18)
- [GO FAIR: FAIR nije isto što i Open](https://www.go-fair.org/resources/faq/ask-question-difference-fair-data-open-data/)
- [IUCr: Crystallographic Information Framework](https://dictionary.iucr.org/Crystallographic_Information_Framework)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
