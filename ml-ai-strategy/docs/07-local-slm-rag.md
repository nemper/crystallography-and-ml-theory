# Lokalni SLM, kontrolisana interpretacija i RAG

## Svrha modula

Lokalni mali jezički model (SLM) može da olakša unos namere, terminološko razjašnjenje i objašnjenje već izračunatih rezultata. Ne predstavlja kristalnu strukturu, ne određuje hemijsku istinu i ne zamenjuje parser, prava pristupa ili determinističke algoritme.

Ovo poglavlje je teorijska mapa mogućih uloga. Ne propisuje konkretan model, format razmene, izvršni servis niti način uvođenja.

## Granica naučnog autoriteta

Jezički sloj može da:

- prepozna korisničku nameru i mapira sinonime na kontrolisane pojmove;
- uoči da je zahtev dvosmislen i postavi pitanje za razjašnjenje;
- predloži strukturisan plan upita koji se zatim nezavisno proverava;
- pronađe odlomke u odobrenoj dokumentaciji;
- verbalizuje deterministički izračunate činjenice uz precizne izvore;
- sažme upozorenja i objasni zašto je neka grana neprimenljiva ili neodređena.

Jezički sloj ne treba da:

- tumači raw CIF, CQS, MOL ili MOL2 kao autoritativni parser;
- određuje bond order, stereohemiju, koordinaciju, simetriju, periodične susede ili atom mapping;
- računa fingerprint, MCS, RMSD, packing, PXRD, similarity ili property vrednost;
- menja skup kandidata, parova, denominatore ili naučne statuse;
- odlučuje o licenci, tenant-u, svrsi upotrebe, izvozu ili pristupu alatu;
- izvršava slobodno generisan SQL, Cypher, shell ili mrežni poziv.

Osnovni princip je jednostavan: naučni rezultat mora imati isto značenje i bez jezičkog modela. Model može da predloži ili objasni; deterministički parseri, validatori i algoritmi utvrđuju šta je dozvoljeno i šta je izračunato.

## Kontrolisani jezik između korisnika i izvršenja

Prirodni jezik je otvoren i dvosmislen, dok hemijski upit mora imati zatvoren skup operacija i eksplicitnu semantiku. Između njih zato može postojati kontrolisana međureprezentacija. Njena konkretna sintaksa nije tema ovog modula; teorijski je važno da razdvaja:

1. **sintaksu** — da li je predlog u dozvoljenom obliku;
2. **semantiku** — da li pojmovi znače ono što korisnik namerava;
3. **primenljivost** — da li potrebna reprezentacija i podaci postoje;
4. **autorizaciju** — da li je operacija dozvoljena za izvor i svrhu;
5. **izvršenje** — determinističko računanje i potpuno accounting izveštavanje.

Grammar-constrained decoding ili schema-constrained output može da smanji broj formalno nevalidnih izlaza. Ne dokazuje da je upit hemijski ispravan, dozvoljen ili veran nameri. Validan strukturisan izlaz može i dalje da pomeša, na primer, „metal postoji u zapisu“ sa „metal je direktno koordinisan mapiranom ligandu“.

Kada više dozvoljenih tumačenja vodi različitim skupovima rezultata, bezbedan ishod je razjašnjenje ili uzdržavanje, a ne pogađanje najverovatnijeg značenja.

## Šta lokalni materijali pokazuju o jezičkoj semantici

Lokalni CQS i export primeri korisni su kao dokaz da naziv pretrage i članstvo u staroj grupi nisu nezavisan gold standard. Različite search grupe mogu kodirati različite stručne pretpostavke, a njihov naziv ne dokazuje razlog zbog kojeg je entry ušao u rezultat.

N14 CIF/MOL/MOL2 primer pokazuje drugu granicu: filename, format i tekstualni komentar ne dokazuju sastav ili povezanost. Bogat CIF može sadržati velike RES/HKL ili druge tekstualne blokove koji su podatak za namenski parser, ne instrukcija jezičkom modelu.

PDF ekstrakcija takođe može dati skriven, ponovljen ili pogrešno raspoređen tekst. Dokumentacioni retrieval zato zahteva proveru prikaza i lokatora; činjenica da je string izvučen iz PDF-a nije sama po sebi dokaz da ga čitalac vidi na toj strani.

Ovi primeri nisu specifikacija budućih testova. Oni su obrazloženje zašto kontrolisana semantika, provenance i stručna provera moraju biti odvojeni od verovatnoće teksta.

## Nivoi jezičke pomoći

Moguće porodice rešenja imaju različite osobine:

| Porodica | Šta dobro radi | Glavno ograničenje |
|---|---|---|
| formulari, rečnici i pravila | predvidljiv unos, zatvoren vocabulary, jasne greške | slabija fleksibilnost jezika |
| grammar-constrained SLM | parafraze i kontrolisan strukturisan predlog | formalna validnost nije semantička istinitost |
| instruction SLM | razjašnjenje i objašnjenje šireg spektra pitanja | veći rizik halucinacije i veći resursi |
| retrieval-grounded SLM | odgovor nad pronađenim odlomcima | zavisi od eligibility-ja, retrieval recall-a i kvaliteta izvora |
| adapter ili fine-tuned SLM | stabilnija terminologija u dobro definisanom zadatku | zahteva prava, čist gold i zaštitu od memorisanja |

Ovo nisu stepenice koje se moraju proći navedenim redom. Izbor zavisi od jezika korisnika, troška greške, dostupnih labela, hardvera, licence i toga da li problem uopšte zahteva generativni model.

Model-card opisuje opštu namenu; ne dokazuje kvalitet na lokalnom stručnom jeziku, hemijskim razgraničenjima ili bezbednosnim slučajevima.

## Memorija, kvantizacija i supply chain

Donja granica memorije samo za težine približno je:

\[
M_{weights}\approx \frac{P\cdot b}{8},
\]

gde je \(P\) broj parametara, a \(b\) broj bitova po težini. Stvarni zahtev uključuje runtime overhead, KV cache, aktivacije, privremene buffere, tokenizer, kontekst i eventualne adaptere. Zbog toga račun `parametri × bitovi` nije obećanje da će model stati na uređaj.

Kvantizacija menja sistem koji se evaluira. Ista bazna težina u različitim formatima ili backend-ovima može promeniti tačnost strukturisanog izlaza, jezičke slice-ove, brzinu i kalibraciju. Revizija modela, tokenizer, chat template, format težina, runtime i licenca pripadaju provenance-u čak i kada ovaj modul ne određuje njihovu konkretnu šemu.

Open-weight ne znači automatski da su poreklo, licenca i integritet bez rizika. Težine, tokenizer, adapter i izvršni runtime treba posmatrati kao odvojene supply-chain artefakte.

## RAG nije crystal embedding

RAG ovde znači pronalaženje **dokumenata**: uputstava, odobrenih lokalnih beležaka, metodoloških objašnjenja i drugih tekstualnih izvora. Chemical/crystal similarity koristi druge objekte, reprezentacije, metrike i gold podatke.

Raw CIF tekst ili njegova prozna parafraza nije valjana zamena za 2D graf, periodični graf, packing deskriptor ili kristalni encoder. Isto tako, dokumentni embedding ne sme postati naučni similarity score samo zato što je generisan neuronskim modelom.

### Eligibility korpusa

Pre indeksiranja treba znati:

- ko je vlasnik izvora i koja upotreba je dozvoljena;
- da li dokument sme da se lokalno čuva, indeksira, ugrađuje u embedding i citira;
- koja verzija i datum važe;
- da li je sadržaj odobren, povučen, quarantined ili superseded;
- koje stranice, sekcije i druge lokatore odgovor može da pokaže korisniku.

Eligibility i ACL filtriranje moraju prethoditi retrieval-u. Post-filter posle pretrage ne uklanja činjenicu da je nedozvoljeni dokument već mogao uticati na rang, cache ili model kontekst.

## Porodice dokumentnog retrieval-a

### Leksički retrieval i BM25

BM25 je jaka referenca kada upiti sadrže tačne oznake, refcode, DOI, CIF tag, naziv alata ili retku terminologiju. Uobičajena forma je:

\[
\operatorname{BM25}(q,d)=\sum_{t\in q}\operatorname{IDF}(t)
\frac{f(t,d)(k_1+1)}
{f(t,d)+k_1\left(1-b+b\frac{|d|}{\operatorname{avgdl}}\right)}.
\]

Field-aware indeks može različito tretirati naslov, tag, refcode i telo, ali parametri i tokenizer moraju odgovarati jeziku i korpusu.

U formuli je \(q\) upit, \(d\) dokument/odlomak, \(t\) termin, \(f(t,d)\) broj njegovih pojavljivanja, \(|d|\) dužina dokumenta, a `avgdl` prosečna dužina. `IDF` daje veću težinu terminima koji su ređi u korpusu; njena tačna varijanta se navodi. Parametar \(k_1\) kontroliše zasićenje doprinosa ponovljenog termina, a \(b\) jačinu korekcije za dužinu. BM25 score nije verovatnoća da je odgovor tačan.

### Dense bi-encoder

Dense retrieval mapira upit i dokument u zajednički vektorski prostor. Može pomoći kod sinonima, parafraza i višejezičnih upita, ali može propustiti retke identifikatore i tačne stringove. Njegov embedding prostor je model- i revizija-specifičan.

### Fuzija rang-lista i RRF

Reciprocal Rank Fusion kombinuje rang-liste bez pretpostavke da su njihovi skorovi direktno uporedivi:

\[
\operatorname{RRF}(d)=\sum_{r\in R}\frac{1}{k+\operatorname{rank}_r(d)}.
\]

RRF je koristan kada leksički i semantički kanal nalaze komplementarne dokumente. Ne popravlja dokument koji nijedan kanal nije kandidovao.

Ovde je \(R\) skup rang-lista, rang počinje od 1, a \(k\) je pozitivna konstanta koja ublažava dominaciju prvog mesta; nije broj vraćenih rezultata. Dokument odsutan iz neke liste iz te liste dobija doprinos nula. Mora se navesti dubina svake liste jer ona menja fuziju.

### Cross-encoder, late interaction i reranking

Cross-encoder zajednički obrađuje upit i kandidat i može preciznije proceniti relevantnost, uz veći trošak po paru. ColBERT-like late interaction čuva token-level signale i nalazi se između bi-encoder efikasnosti i pune cross-encoder interakcije.

Reranker ne može da vrati relevantan dokument koji nije u candidate skupu. Zbog toga se candidate recall i finalno rangiranje mere odvojeno.

## Grounded generisanje

Generator dobija samo minimalan, odobren evidence skup. Za svaku bitnu tvrdnju treba da bude moguće utvrditi:

- iz kojeg dokumenta i verzije potiče;
- na kojoj stranici, sekciji ili drugom lokatoru se nalazi;
- da li je tvrdnja direktno podržana ili je označena kao zaključivanje;
- da li postoje konfliktni ili zastareli izvori;
- šta ostaje nepoznato.

Citiranje dokumenta nije dovoljno ako odlomak ne podržava tvrdnju. Numeričke vrednosti, prava, statusi i naučni rezultati treba da dolaze iz strukturisanog evidence-a, a ne iz memorije modela. Ako evidence nije dovoljan, odgovor treba da ostane uzdržan.

## Prilagođavanje modela

| Metoda | Šta menja | Kada je obrazovno relevantna | Glavni rizik |
|---|---|---|---|
| prompt i kontrolisani primeri | kontekst, ne težine | mali broj jasnih namera | krhkost prema parafrazama i template-u |
| constrained decoding | prostor dozvoljenih izlaza | zatvorena sintaksa | ne rešava semantičku grešku |
| supervised fine-tuning | ponašanje težina | dovoljno čistih, dozvoljenih primera | leakage, overfit i memorisanje |
| LoRA | trenira niskorangirane adaptere uz zamrznutu bazu | ograničeni resursi i modularno prilagođavanje | adapter i baza zajedno čine evaluacionu jedinicu |
| QLoRA | LoRA nad kvantizovanom bazom | dodatna ušteda memorije | kvantizaciona greška i veća runtime zavisnost |

LoRA aproksimira promenu težina niskorangiranom matricom, često zapisano kao \(\Delta W=BA\), gde je rang mnogo manji od dimenzija pune matrice. Manji broj treniranih parametara ne uklanja potrebu za pravima nad podacima, nezavisnim testom i proverom memorisanja.

## Podaci, split i leakage

Jedinica nezavisnosti za interpretaciju namere nije svaka parafraza. Varijante iste intent/template familije treba grupisati. Za dokumentni RAG, chunk-ovi istog dokumenta ili izdanja nisu nezavisni primeri; evaluacija mora uzeti u obzir source/topic familije.

Posebno treba odvojiti podatke korišćene za prompt primere ili prilagođavanje, izbor modela i pragova, kalibraciju i netaknuti finalni test. Restricted ili neodobren sadržaj ne sme postati trening primer.

Synthetic primeri su korisni za rubne forme i bezbednosne napade, ali nisu jedini dokaz stručnog kvaliteta. LLM judge može biti pomoćni signal; ne treba da bude jedini autoritet za gold koji ocenjuje isti tip modela.

## Evaluacija

### Interpretacija namere

Relevantne metrike uključuju tačnost namere i kontrolisanih pojmova, execution equivalence, stopu pravilnog razjašnjenja/odbijanja/uzdržavanja, stopu semantički pogrešnih ali formalno validnih predloga i rezultate po jeziku, pismu, terminološkoj i bezbednosnoj grupi.

### Retrieval

Odvojeno se mere candidate recall, Recall@k, MRR ili nDCG, judgment coverage, tačni identifikatori i rezultati po jeziku/source familiji. Dense ili reranking doprinos ima smisla samo nad istim eligible korpusom i istim qrels-ima.

### Grounded odgovor

Proveravaju se vernost evidence-u, potpunost lokatora, numerička tačnost, označavanje zaključivanja, konfliktnih izvora i nepoznatog. Stil odgovora ne sme da prikrije unsupported claim.

### Statističko izveštavanje i abstention

Poređenje se radi na istim primerima, sa intervalima koji resampluju nezavisne intent ili source familije. Seed varijacija se prijavljuje odvojeno od broja nezavisnih upita. Pored proseka treba prikazati unapred definisane kritične slice-ove.

Samoprijavljeni confidence modela nije kalibrisana verovatnoća. Korisniji su empirijski risk–coverage odnosi zasnovani na validator signalima, neslaganju metoda i posebnom calibration skupu. Prag i kalibracija važe za konkretnu kombinaciju modela, revizije, template-a, runtime-a i kvantizacije.

## Threat model lokalnog sloja

„Lokalno“ smanjuje egress, ali ne pretvara sadržaj u pouzdanu instrukciju.

| Napad ili failure | Teorijska kontrola |
|---|---|
| CIF/PDF komentar kaže da se ignorišu pravila | strogo razdvojiti instrukcije od nepoverljivih podataka |
| model predlaže nepoznat alat ili operaciju | zatvoren skup operacija i nezavisna policy provera |
| korisnik traži bulk izvoz | prava i svrha proveravaju se izvan modela |
| dugačak tekst potiskuje pravila | ograničenje konteksta i eksplicitna truncation politika |
| retrieval vraća povučen ili zabranjen dokument | eligibility i ACL pre retrieval-a, uz proveru rezultata |
| odgovor izmišlja naučnu tvrdnju | claim–evidence provera i uzdržavanje |
| adapter pamti poverljiv primer | prava za trening, memorization testovi i kontrola distribucije |
| prethodni razgovor meša projekte | izolacija konteksta i jasno upravljanje stanjem |

## Česte greške

1. Slati raw CIF modelu i tražiti da „razume kristal“.
2. Koristiti text embedding CIF-a kao crystal embedding.
3. Verovati formalno validnom izlazu bez semantičke i policy provere.
4. Tretirati CQS naziv ili članstvo u search grupi kao gold.
5. Mešati dokumentni retrieval sa chemical/crystal similarity pretragom.
6. Indeksirati svaki parser-extracted PDF string bez vizuelne ili OCR provere.
7. Deliti parafraze iste namere između treninga i testa.
8. Birati model samo po broju parametara ili javnom leaderboard-u.
9. Pretpostaviti da kvantizovana težina garantovano staje u raspoloživu memoriju.
10. Dozvoliti modelu da sam odobri alat, pravo ili nivo rizika.

## Primarni i zvanični izvori

### Retrieval i prilagođavanje

- [Lewis et al. 2020: Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401)
- [Scholak et al. 2021: PICARD constrained decoding](https://arxiv.org/abs/2109.05093)
- [Geng et al. 2023: Grammar-Constrained Decoding](https://aclanthology.org/2023.emnlp-main.674/)
- [Dong et al. 2024: XGrammar](https://arxiv.org/abs/2411.15100)
- [llama.cpp: GBNF and JSON Schema grammars](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md)
- [Robertson i Zaragoza 2009: Probabilistic Relevance Framework/BM25](https://doi.org/10.1561/1500000019)
- [Cormack et al. 2009: Reciprocal Rank Fusion](https://doi.org/10.1145/1571941.1572114)
- [Khattab i Zaharia 2020: ColBERT late interaction](https://arxiv.org/abs/2004.12832)
- [Hu et al. 2021: LoRA](https://arxiv.org/abs/2106.09685)
- [Dettmers et al. 2023: QLoRA](https://arxiv.org/abs/2305.14314)
