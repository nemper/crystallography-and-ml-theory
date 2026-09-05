# Spoljni LLM API-ji, granica podataka i bezbednost

## Svrha modula

Spoljni LLM API može biti predmet obrazovne ili komparativne analize za jezičke zadatke. Sam naziv providera, plaćeni nalog, privatni repozitorijum ili opcija „zero data retention“ ne daju pravo da se projektni, fakultetski ili CSD sadržaj pošalje trećoj strani.

Ovo poglavlje opisuje principe klasifikacije podataka, minimizacije, retention-a, prompt-injection odbrane i vendor-neutral evaluacije. Ne određuje konkretan provider, model, tehnički interfejs niti način uvođenja.

## API nije deo naučnog jezgra

Spoljni model može da se razmatra za:

- terminološko razjašnjenje i parafraziranje odobrenog teksta;
- predlog kontrolisanog upita koji se lokalno validira;
- sažimanje minimalnog evidence-a bez menjanja vrednosti;
- odgovor nad dokumentima koje je dozvoljeno poslati konkretnom processor-u;
- pomoć u pisanju objašnjenja, uz vidljive izvore i uzdržavanje.

Ne dobija autoritet da:

- parsira raw CIF/CQS ili bira koji je format source of truth;
- određuje hemijske veze, stereo, koordinaciju, simetriju, mapping ili packing;
- računa ili menja candidate set, parove, score, status ili denominator;
- odlučuje o pravima, svrsi, tenant-u ili izvozu;
- izvršava proizvoljne alate, URL-ove, kod ili pretrage;
- koristi sopstveno sećanje kao dokaz za lokalnu naučnu tvrdnju.

Naučni rezultat zato mora ostati dostupan bez spoljnog API-ja. Strukturisan output smanjuje formatne greške, ali nije dokaz semantičke, naučne ili policy ispravnosti.

## Klasifikacija podataka pre egress-a

Jedna oznaka „poverljivo“ nije dovoljna. Za svaki potencijalni izlazak podataka treba razmotriti najmanje sledeće dimenzije:

| Dimenzija | Pitanje |
|---|---|
| vlasništvo i licenca | ko je vlasnik i da li je obrada kod treće strane dozvoljena |
| identifikabilnost | sadrži li osoba, institucija, projekat, tenant ili poslovni identitet |
| naučna/poslovna osetljivost | da li otkriva neobjavljen rezultat, strukturu, query ili odluku |
| oblik sadržaja | raw dokument, koordinate, izvedena činjenica, embedding ili agregat |
| svrha | inference, evaluacija, trening, podrška, debug, logging ili publikacija |
| processor i podprocessor | ko prima sadržaj i pod kojim ugovorom |
| region | gde se sadržaj obrađuje i čuva |
| stanje i retention | koji endpoint, feature, cache, log ili sesija zadržava podatak |
| dalja upotreba | trening, abuse monitoring, feedback ili dataset sharing |

Nepoznata vrednost nije prećutna dozvola. Prava se procenjuju za konkretnu operaciju: čitanje, slanje, privremenu obradu, čuvanje, embedding, trening, prikaz i distribucija nisu ista prava.

### CCDC prava su zasebna granica

CCDC uslovi i pravo redistribucije moraju se proveriti nezavisno od tehničkih privacy kontrola providera. ZDR ne menja CCDC licencu; ugovor sa providerom ne pretvara licencirani CSD sadržaj u javni podatak. Isto važi za fakultetske fajlove i neobjavljene rezultate.

Derived činjenica takođe može zadržati ograničenja izvora. Hash, embedding, sažetak ili uklonjen filename nisu automatski slobodni za egress ili redistribuciju.

## Minimizacija i sanitizacija

Minimizacija znači slanje samo informacije neophodne za imenovani jezički zadatak. To nije isto što i ručno brisanje nekoliko očiglednih identifikatora.

Moguća curenja obuhvataju:

- retku kombinaciju elemenata, koordinata ili vrednosti po kojoj se struktura može ponovo identifikovati;
- refcode, DOI, interne nazive, putanje, tenant i projekat;
- property/enum nazive u structured-output opisu;
- prompt primere, stack trace, warning ili tool rezultat;
- reversible pseudonim koji druga tabela može da razreši;
- tekst izveden iz licenciranog dokumenta, iako raw fajl nije poslat.

Sanitizacija zato zahteva eksplicitnu procenu potrebnosti, prava, mogućnosti ponovne identifikacije i toga da li se značenje zadatka promenilo posle transformacije. Ako transformacija uništi informaciju potrebnu za korektan odgovor, API više nije odgovarajući alat za taj zadatak.

## Referentni bezbednosni principi

Konkretna arhitektura zavisi od organizacije, ali sledeći principi su opšti:

1. **Kontrolisana egress granica.** Pozivi prolaze kroz mesto na kojem se proveravaju prava, svrha, feature-i i budžet.
2. **Least privilege.** Model vidi samo minimum činjenica i samo zatvoren skup mogućih akcija.
3. **Razdvajanje predloga i odluke.** Model može predložiti; lokalna politika odobrava ili odbija.
4. **Tenant i kontekst izolacija.** State, cache, log i prethodne poruke ne smeju mešati projekte.
5. **Fail-closed nepoznanice.** Neproveren ugovor, region, feature ili pravo zaustavlja egress.
6. **Lokalni fallback.** Nedostupnost providera ne menja naučni rezultat niti prava.
7. **Minimalno beleženje.** Za accountability se čuvaju potrebni metapodaci, ne prompt/output po navici.

Ovo su security obrasci, ne specifikacija konkretnog servisa ili topologije.

## Retention je svojstvo celog poziva

„Provider ne trenira na API podacima“ ne znači isto što i:

- nema abuse-monitoring logova;
- nema application state-a;
- nema prompt cache-a;
- nema Files, Batch, search ili agent state-a;
- nema podprocessora;
- aktivan je ZDR za baš tu organizaciju/projekat;
- sadržaj sme da se pošalje po izvornoj licenci.

Retention se zato posmatra kao funkcija tačnog ugovora, organizacije ili projekta, endpoint-a, modela, regiona, API verzije, uključenih feature-a, cache-a, logging/feedback podešavanja i pravnih/safety izuzetaka. Promena bilo koje od ovih stavki može promeniti data-control zaključak.

Model katalog je promenljiv. Datirani presek ili tačan model identitet pomaže reproduktivnosti, ali ne zamenjuje proveru prava, processor-a i feature retention-a.

## Prompt cache i state

Prompt cache može čuvati izvedenu reprezentaciju sadržaja čak i kada odgovor nije trajno sačuvan. Provider-hosted razgovori, Files, vector stores, batch jobs, search, agenti, background izvršenje i feedback takođe mogu imati različita pravila.

Zato se bezbednosno pitanje ne svodi na „da li je prompt sačuvan“. Treba utvrditi:

- koji sadržaj ili izvedeni artefakt ulazi u state;
- koliko traje i gde se nalazi;
- da li je izolovan po organizaciji/projektu/tenant-u;
- ko ga može ponovo koristiti ili videti;
- kako se briše i koji izuzeci važe;
- da li je taj oblik obrade dozvoljen izvornim pravima.

Cache key nije authorization granica, a kratak TTL nije dozvola za sadržaj koji uopšte ne sme da napusti lokalni data-plane.

## Prompt injection i confused deputy

U ovom domenu nepoverljiv sadržaj nije samo korisnička poruka. Instrukciju nalik sistemskoj može sadržati:

- CIF komentar ili semicolon text field;
- chemical name, autor, naslov, filename ili refcode;
- MOL/MOL2 komentar;
- PDF, RAG chunk ili web sadržaj;
- parser warning, exception ili output spoljnog alata;
- prethodni model odgovor.

Takav tekst ostaje **podatak**, čak i kada sadrži imperativ, JSON, XML, URL ili pseudo-tool poziv.

| Pretnja | Princip odbrane |
|---|---|
| indirektna prompt injection | razdvajanje instruction i data kanala; retrieved tekst nema viši autoritet |
| confused deputy | model ne poseduje prava korisnika niti sam odobrava alat |
| data exfiltration kroz output | izlaz prolazi istu klasifikaciju i ACL kao ulaz |
| RAG poisoning | provenance, eligibility i kvalitet korpusa pre retrieval-a |
| arbitrary tool/URL | zatvoren capability skup i lokalna semantička/policy provera |
| cross-tenant memory/cache | izolacija stanja i zabrana implicitnog deljenja konteksta |
| denial of wallet/service | limiti ulaza/izlaza, vremena i troška, bez uticaja na naučno jezgro |
| schema smuggling | opisi, enum-i i primeri se takođe klasifikuju kao sadržaj |

Structured output ili strict tool use može ograničiti oblik predloga. Ne čini tool result pouzdanim i ne rešava prompt injection samostalno.

## Audit bez nepotrebnog sadržaja

Cilj audit-a je da se rekonstruiše odluka o egress-u i ponašanje sistema, ne da se napravi druga kopija osetljivog prompta. U zavisnosti od rizika, korisni su:

- identitet politike i važeća odluka o pravima;
- tačan provider/model/feature kontekst i vreme provere;
- kategorije poslatih podataka i svrha;
- hash ili drugi nereverzibilni locator kada je opravdan;
- status poziva, refusal/truncation i bezbednosna odluka;
- agregatna latencija, tokeni i trošak;
- reference na lokalno zaštićen evidence, umesto samog sadržaja.

Hash može i dalje biti lični ili licencno osetljiv podatak i ne treba ga smatrati anonimnim po automatizmu. Log pristup, retention i redaction moraju biti najmanje strogi kao za događaj koji opisuju.

## Vendor-neutral evaluacija

Providerova hosted evaluacija ili javni benchmark ne meri lokalnu kombinaciju jezika, stručne terminologije, prava, evidence vernosti i napada. Poređenje je smisleno samo kada kandidati dobiju isti dozvoljeni sadržaj i kada su gold i scoring nezavisni od jednog providera.

Relevantne grupe mera su:

- tačnost namere i kontrolisanog strukturisanog predloga;
- vernost numeričkim i tekstualnim činjenicama;
- citation/evidence entailment i pravilno uzdržavanje;
- prompt-injection, cross-tenant i rights-bypass stopa;
- refusal, truncation i neuspeh feature-a;
- latency, trošak i operativna zavisnost;
- rezultati po jeziku, pismu, source i risk slice-u.

Isti model ne treba istovremeno da generiše gold, odgovara i bude jedini sudija. Parafraze istog intent-a i chunk-ovi istog dokumenta nisu nezavisne statističke jedinice.

### Rule of three

Ako se u \(n\) nezavisnih Bernoulli testova sa zajedničkom verovatnoćom kritičnog događaja ne vidi nijedan takav događaj, jednostrana 95% binomna gornja granica i njena aproksimacija su:

\[
p_{upper}=1-0.05^{1/n}\approx\frac{3}{n}.
\]

Zato „0 od 100“ ne dokazuje nulti rizik; približna gornja granica je oko 3%. Ovo je screening argument, ne security proof. Granica se odnosi na populaciju i postupak uzorkovanja koje testovi predstavljaju, ne na svaki budući adaptivni napad. Parafraze istog napada i namerno odabran challenge skup nisu automatski nezavisan reprezentativan uzorak ([Hanley i Lippman-Hand](https://doi.org/10.1001/jama.1983.03330370053031)).

## Česte greške

1. Slati raw CIF, CSD ili CQS sadržaj zato što je nalog poslovni ili repo privatan.
2. Mešati „ne trenira“, ZDR, retention, DPA i izvornu licencu.
3. Pretpostaviti da je uklonjen filename dovoljna anonimizacija.
4. Verovati schema-valid izlazu bez lokalne semantic/evidence/policy provere.
5. Davati modelu proizvoljan URL, shell, code, Files, search ili remote-tool capability.
6. Stavljati poverljive vrednosti u opise, enum-e ili primere output formata.
7. Koristiti moving alias ili preview model kao da je reproducibilan snapshot.
8. Logovati prompt/output radi debug-a bez potrebe, prava i retention politike.
9. Fail-open preusmeriti osetljiv sadržaj drugom provideru pri incidentu.
10. Dozvoliti da lep narativ promeni naučni score, status ili denominator.

## Primarni i zvanični izvori

### CCDC i upravljanje podacima

- [CCDC: Can I redistribute data from the CSD?](https://support.ccdc.cam.ac.uk/support/solutions/articles/103000339607-can-i-redistribute-data-from-the-csd-)
- [CSD Python API / CSD Portfolio Conditions of Use](https://downloads.ccdc.cam.ac.uk/documentation/API/conditions_of_use.html)

### Bezbednost i evaluacija

- [NIST AI 600-1 — Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1)
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [NIST SP 800-207 — Zero Trust Architecture](https://doi.org/10.6028/NIST.SP.800-207)
- [NIST SP 800-92 — Log Management](https://doi.org/10.6028/NIST.SP.800-92)
- [OWASP LLM01: Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [OWASP LLM08: Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/)
- [IUCr CIF 1.1 syntax](https://www.iucr.org/resources/cif/spec/version1.1/cifsyntax)
- [Greshake et al. — Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)
- [PoisonedRAG — USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag)
- [StruQ — USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/chen-sizhe)
- [CaMeL — Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813)
