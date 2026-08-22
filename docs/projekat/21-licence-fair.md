# 21. Licence, FAIR i poreklo podataka

## Šta treba da umeš posle ovog poglavlja

Posle ovog poglavlja treba da možeš da:

- razdvojiš tehničku mogućnost pristupa od pravne/ugovorne dozvole za upotrebu;
- objasniš zašto raw CSD podaci i CSD-derived skupovi nisu deo ovog repoa;
- pokažeš zašto privatni GitHub repo nije automatsko rešenje licencnog problema;
- primeniš FAIR na podatke koji ostaju poverljivi i kontrolisano dostupni;
- dizajniraš provenance zapis za izvor, transformaciju, model i rezultat;
- prepoznaš nevidljivi, tematski nepodudarni embedded PDF tekst kao ingest i provenance incident;
- definišeš licence-aware granice za obe 2CDC aplikacije.

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

Repo treba da sadrži:

- edukativni tekst i naš izvorni kod;
- male sintetičke testove koje smo sami napravili;
- javne podatke sa kompatibilnom, dokumentovanom licencom;
- eventualno reference/manifest zapise o licenciranim artefaktima, bez njihovog sadržaja.

Repo ne treba da sadrži:

- raw CSD bazu;
- masovne CSD izvoze iz ConQuest-a ili API-ja;
- kopirane CSD CIF/MOL/MOL2/SDF redove;
- derived subset koji omogućava rekonstrukciju zaštićenog sadržaja;
- model, embedding ili indeks za koji nije provereno pravo distribucije.

Čak i private repo može predstavljati kopiju kod trećeg pružaoca usluge, imati širi krug naloga, backup-e i drugačiju geografsku lokaciju. „Private“ je kontrola pristupa, ne nova licenca.

!!! danger "Derived nije automatski slobodno"
    Embedding, fingerprint indeks, trenirani model, agregirane karakteristike ili eksportovani result set mogu biti izvedeni materijal. Da li se konkretan artefakt sme distribuirati zavisi od ugovora, mogućnosti rekonstrukcije, poslovne namene i pisanog odobrenja. Kada nije jasno, sistem mora da blokira eksport i traži odluku vlasnika licence/CCDC-a.

## Predlog arhitektonske granice

Najbezbedniji početni dizajn razdvaja:

| Sloj | Sadržaj | Tipična lokacija |
|---|---|---|
| open code plane | parser interfejsi, algoritmi, dokumentacija, sintetički testovi | GitHub repo |
| licensed data plane | CSD podaci, CSD-derived cache/index, licencirani alati | odobrena organizacija/lokacija |
| proprietary project plane | interni CIF-ovi, svojstva, laboratorijski metadata | kontrolisano interno skladište |
| publication plane | odobrene metrike, slike, tabele, dokumenti | javni ili partnerski kanal |

Kod komunicira sa licenciranim data-plane-om kroz kontrolisan servis. Servis vraća samo polja i rezultate koje konkretna licenca i uloga dozvoljavaju. Nije prihvatljivo da web API slučajno postane bulk-export interfejs.

## FAIR nije isto što i open

Originalni [FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18) znače:

| Slovo | Princip | Projektna realizacija |
|---|---|---|
| F - Findable | podatak i metadata imaju stabilan identitet i mogu se pronaći | internal URI, source ID, indeks metapodataka |
| A - Accessible | postoji standardizovan postupak pristupa | API/protokol sa autentikacijom i autorizacijom |
| I - Interoperable | koriste se formalni jezici, rečnici i kvalifikovane veze | CIF dictionaries, kontrolisane jedinice, ontology/role polja |
| R - Reusable | značenje, poreklo, licence i domenski standardi su dovoljno bogati | provenance, quality, usage policy, verzije i citiranje |

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

## Licence kao izvršiva politika, ne fusnota

Za svaki izvor napravi matricu dozvola:

| Polje | Primer pitanja |
|---|---|
| owner/controller | ko odlučuje o upotrebi? |
| licence/contract ID | koji dokument je merodavan? |
| scope | organizacija, lokacija, projekat, korisnici |
| expiry/review date | kada dozvolu ponovo proveravamo? |
| read/search | ko sme da čita i pretražuje? |
| transform/index | smeju li normalizacija, fingerprint i embedding? |
| train/evaluate | sme li ML trening i koje vrste modela? |
| cache/backup | gde i koliko dugo? |
| export/share | koja polja i kojim primaocima? |
| publish | statistike, slike, kod, model weights? |
| citation | obavezna referenca i tekst zahvalnice |
| deletion | kako se opoziv/istek propagira na derivative? |

Policy engine treba da radi fail closed: odsustvo dozvole znači „ne izvršavaj“, ne „pretpostavi da je dozvoljeno“.

## Provenance: dokazni lanac za svaki bajt i svaku tvrdnju

Provenance odgovara na pitanja:

- odakle je artefakt došao;
- ko ga je uneo i kada;
- koji ugovor/licenca važi;
- koji alat i verzija su ga parsirali;
- koje transformacije su izvršene;
- koji izlaz je nastao iz kojih ulaza;
- ko je pregledao alert ili izuzetak;
- da li je derivative opoziv nakon isteka licence.

Minimalni manifest može izgledati ovako:

    source_id: urn:2cdc:source:cu-n14-a
    original_name: cu_n14_a.cif
    sha256: "<unesi-provereni-64-heksadecimalni-hash>"
    received_at: "<uneti-stvarni-ISO-8601-trenutak-prijema-ili-unknown>"
    source_owner: "<utvrditi-pre-upotrebe>"
    licence_id: unresolved_block_use
    confidentiality: internal
    allowed_operations:
      - local_parse
      - local_quality_check
    redistribution: denied_until_confirmed
    parser:
      name: parser_name
      version: parser_version
    validation:
      method: local_validator
      ruleset_version: ruleset_version
      reviewed_by: reviewer_or_service_account
    parent_artifacts: []

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

### Ispravan PDF ingest

Za svaki PDF sačuvaj najmanje:

1. originalni fajl i hash;
2. PDF metadata i broj strana;
3. tekst po strani, sa identitetom parsera;
4. render svake relevantne strane ili reproducibilan render hash;
5. OCR/visible-text rezultat kada je potreban;
6. odstupanje embedded text naspram vizuelnog/OCR sloja;
7. ručnu ili automatsku QA odluku;
8. status: raw, quarantined, reviewed, approved ili rejected.

Praktična pravila:

- nevidljivi embedded tekst ne briši iz raw evidence-a;
- ne puštaj ga u korisnički indeks dok se konflikt ne razreši;
- zapiši koje stranice i stringovi su označeni;
- derived „approved text“ veži na tačnu verziju izvornog PDF-a i QA odluku;
- pri promeni parsera ponovi ekstrakciju i uporedi rezultate.

!!! example "Zašto je ovo FAIR problem"
    Bez provenance-a ne možemo znati da li je rečenica došla iz vidljivog sadržaja, OCR-a, nevidljivog embedded sloja ili naknadne transformacije. Podatak može biti lako pronađen, ali nije pouzdano reusable jer mu poreklo i značenje nisu jasni.

## Ingest tok za hemijske i dokumentne izvore

| Faza | Obavezna kontrola | Izlaz |
|---|---|---|
| register | vlasnik, licenca, hash, klasifikacija | immutable source record |
| parse | alat/verzija, format, greške | raw parsed representation |
| cross-check | CIF schema/checkCIF ili PDF text/render poređenje | validation report |
| curate | jedinice, identitet, forma, vidljivost, alerts | reviewed canonical record |
| derive | fingerprint, embedding, property join, tekst segmenti | lineage-linked derivative |
| serve/export | role, purpose, licence policy, redaction | audit event |
| retire | expiry, revocation, deletion propagation | tombstone i derivative review |

Raw, canonical i derived sloj ne treba prepisivati jedan preko drugog. Nova kuracija stvara novu verziju sa vezom ka prethodnoj.

## Posledice za globalnu pretragu

Globalna aplikacija verovatno ima najveći licencni rizik jer radi nad veoma velikom bazom:

- CSD pretraga i indeksiranje treba da se izvršavaju unutar odobrenog licensed data-plane-a.
- API mora primeniti autentikaciju, autorizaciju, tenant i purpose ograničenje.
- Bulk enumeration i neograničen eksport moraju biti odvojeni od normalnog search endpoint-a.
- Svaki rezultat mora nositi source ID, verziju baze, datum pretrage i dozvoljeni nivo prikaza.
- Cache i embedding moraju imati licence ID, expiry i deletion lineage.
- Slanje CSD podataka ili derivata eksternom SaaS/LLM servisu zahteva prethodnu proveru ugovora.
- Telemetrija ne sme slučajno zapisivati strukture, query fajlove ili pune rezultate.
- UI treba jasno da razlikuje javni/open pogodak, interni proprietary pogodak i licencirani CSD pogodak.

Ako licenca istekne ili se korisnik povuče iz projekta, sistem mora znati koji indeks, model i cache zahtevaju blokadu ili ponovnu procenu. Bez lineage grafa to je praktično nemoguće.

## Posledice za poređenje svih parova

Druga aplikacija prima korisničke fajlove i pravi bogate pairwise rezultate:

- pri upload-u traži potvrdu prava na obradu i klasifikaciju poverljivosti;
- izoluj tenant-e i projekte;
- ne koristi input za budući trening bez posebne dozvole;
- čuvaj original, canonical i derived reprezentacije odvojeno;
- report može sadržati dovoljno geometrije da predstavlja izvedeni strukturni podatak - primeni export policy;
- definiši retention i bezbedno brisanje inputa, rendera, cache-a i privremenih fajlova;
- svaki par mora pokazati source verzije i algoritam/verziju;
- ako jedan član para ima restriktivniju licencu, rezultat nasleđuje najmanje taj nivo restrikcije dok pravilo ne kaže drugačije.

## FAIR implementacija za restricted podatke

Praktičan cilj nije da objavimo sadržaj CSD-a, nego da ovlašćeni agent može pouzdano da ga koristi:

- **F1/F3:** interni stabilni URI za source, form, determination i measurement; metadata nosi njihove veze.
- **F2/F4:** bogati metadata indeks bez otkrivanja zaštićenih koordinata neovlašćenom korisniku.
- **A1/A1.2:** dokumentovan API uz authentication/authorization.
- **A2:** metadata i tombstone ostaju kada je sadržaj povučen, u meri dozvoljenoj ugovorom.
- **I1–I3:** CIF rečnici, kontrolisane jedinice, kvalifikovane relacije i verzionisane ontologije.
- **R1/R1.1:** dovoljni naučni metadata i eksplicitna licenca/policy.
- **R1.2:** pun provenance i transformation lineage.
- **R1.3:** kristalografski i hemijski standardi zajednice.

Persistent identifier može biti interni i ne mora otkriti sadržaj. „Ne postoji za neovlašćenog korisnika“ i „postoji, ali zahteva dozvolu“ su različite policy odluke koje treba svesno doneti.

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

Parser nalazi docking tekst na naslovnoj strani, ali render ga ne prikazuje. Šta radiš?

??? success "Odgovor"
    Sačuvaj raw ekstrakciju kao evidence, označi stranicu konfliktom, ne indeksiraj sporni tekst u approved sloj, vizuelno/OCR proveri dokument i zapiši QA odluku sa parserom i verzijom.

### 4. Embedding za objavu

Model je treniran nad CSD-derived fingerprintima. Da li je dovoljno što model weights ne sadrže čitljive CIF redove?

??? success "Odgovor"
    Ne. Model može biti ugovorno izvedeni materijal i može memorisati ili omogućiti inference o podacima. Potrebna je licencna analiza, test rekonstrukcije/memorisanja i, kada uslovi zahtevaju, prethodno pisano odobrenje CCDC-a.

### 5. Istek licence

Licenca za izvor ističe sutra. Koji artefakti moraju biti pronađeni?

??? success "Odgovor"
    Raw kopije, canonical zapisi, cache, indeks, embeddings, trenirani/evaluirani modeli, report-i i backup-i povezani lineage grafom. Za svaki se primenjuje ugovorena retention/deletion ili review odluka.

## Kriterijum prolaza

Poglavlje si savladao kada možeš da nacrtaš data-flow obe aplikacije, za svaku ivicu navedeš licencu i dozvoljenu operaciju, a zatim pokažeš kako se od jednog source hash-a nalaze svi derivative artefakti i zaustavlja neodobren eksport.

## Primarni i autoritativni izvori

- [CCDC CSD Portfolio Conditions of Use](https://downloads.ccdc.cam.ac.uk/documentation/API/conditions_of_use.html)
- [CCDC Standard Licence Agreement](https://www.ccdc.cam.ac.uk/licence-agreement/)
- [Wilkinson et al. 2016: FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18)
- [GO FAIR: FAIR nije isto što i Open](https://www.go-fair.org/resources/faq/ask-question-difference-fair-data-open-data/)
- [IUCr: Crystallographic Information Framework](https://dictionary.iucr.org/Crystallographic_Information_Framework)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
