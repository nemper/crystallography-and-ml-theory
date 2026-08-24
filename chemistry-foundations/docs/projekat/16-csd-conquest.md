# 16. CSD i ConQuest tok podataka

**Prioritet: MORAŠ.** Ova strana objašnjava šta lokalni izvozi jesu, šta nisu i koje semantičke, licencne i provenance obaveze postoje kada se radi sa CSD podacima. Ne propisuje buduću implementaciju.

## 16.1 CSD, CSD entry i refcode

Cambridge Structural Database (CSD) je kurirana, licencirana baza kristalnih struktura malih organskih i metal-organskih jedinjenja. CCDC-ov pregled razvoja baze je [The Cambridge Structural Database: a quarter of a century after the millionth structure](https://pubs.acs.org/doi/full/10.1021/acs.chemrev.9b00155). Zvanični CCDC snapshot za 2026 navodi 1.431.347 entries; broj je vremenski promenljiv i ne treba ga hardkodovati kao trajnu činjenicu ([CSD Entry Summary Statistics 2026](https://www.ccdc.cam.ac.uk/media/CSD-Entries-Summary-Statistics-2026.pdf)).

**CSD entry** nije nužno jedna jedinstvena hemijska supstanca. Može predstavljati konkretno kristalografsko određivanje pri određenim uslovima, sa sastavom, 3D modelom, bibliografijom i kuriranim anotacijama. Bliski refcode-ovi mogu biti povezane redeterminations ili forme; identitet se ne određuje samo string poređenjem.

Tri nivoa se moraju držati odvojeno:

```text
CSD entry / eksperimentalno određivanje
└── kristal: ćelija + simetrija + sastav + packing
    └── jedna ili više hemijskih komponenti/molekula
```

## 16.2 ConQuest nije samo text search

ConQuest je CCDC alat za crtanje i kombinovanje 2D/3D strukturnih i tekstualno-numeričkih upita. Podstrukturni query definiše atom/bond constraints; opciono se dodaju geometric constraints i entry filters. CCDC dokumentacija objašnjava [search philosophy](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/search_philosophy.html) i [substructure searching](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/substructure_searching.html).

`.cqs` je binarni ConQuest query/session objekat. U dostavljenim lokalnim fajlovima sadrži i sačuvano stanje/rezultate, ali nije obična prenosiva result-lista niti univerzalni javni standard za razmenu. Statička forenzika zato nije zamena za vizuelnu i runtime potvrdu u kompatibilnoj ConQuest verziji, sa eksplicitno zabeleženim constraints/filterima.

## 16.3 Šta smo utvrdili za dva lokalna upita

Forenzički pregled čitljivog serializovanog sadržaja dva `.cqs` fajla pokazuje:

| Upit | Strukturni deo | Dodatni uslov | Lokalni rezultati |
|---|---|---|---:|
| `1 - Sifove baze DAP.cqs` | 18-atomski DAP bis-iminski motiv | nema dodatnog metalnog uslova; metal nije ni zahtevan ni zabranjen | 2.110 |
| `2 - Kompleksi sa DAP SB.cqs` | isti 18-atomski motiv | odvojeni atom tipa `4M` | 2.038 |

CCDC ConQuest vodič definiše `4M` kao grupu svih metalnih elemenata ([ConQuest User Guide](https://www.ccdc.cam.ac.uk/media/Documentation/2F0D7443-9739-46EB-BE9F-69E62E531FB7/2f0d7443973946ebbe9f69e62e531fb7.pdf)). U query objektu atom 19 je **nepovezan** sa DAP motivom: nema metal–N bond/contact/geometric constraint.

Zato je dokazano samo:

> entry sadrži DAP motiv i neki metal negde u istom entry-ju.

Nije dokazano:

> taj DAP ligand koordinira taj metal preko očekivana tri N donor-atoma.

`search2` je tačan podskup `search1`; razlika je 72 entry-ja. Semantika „kompleks sa DAP“ zahteva drugi korak: component assignment, metal-neighbor perception, donor mapping i geometric/chemical validation.

!!! warning "Naziv upita nije ground truth"
    Naziv „Kompleksi sa DAP SB“ izražava nameru autora, ali mašinska etiketa mora da prati stvarne constraints. Konačnu nameru i dozvoljene edge cases treba potvrditi sa naučnim timom.

## 16.4 Filteri i selection bias

Serializovani query pokazuje da standardni filteri za 3D coordinates, R factor, errors, disorder, polymers, ions, powder i organic/organometallic classification nisu uključeni. Lokalni rezultati zato sadrže heterogeni kvalitet i zapise bez pune 3D reprezentacije.

To je legitimno za širok recall, ali ima dve posledice:

1. svaki downstream korak mora eksplicitno da prijavi da li je određena analiza moguća;
2. skup nije slučajan uzorak celog CSD-a, već query-conditioned subset.

Ne sme se iz lokalne učestalosti metala, space groups ili missing SMILES zaključivati globalna CSD distribucija.

## 16.5 Entry filters nisu isto što i hemijski uslov

Primeri različitih slojeva:

- **query graph constraint**: ciljni pyridine-bis(imine) podgraf;
- **entry composition constraint**: prisutan neki metal;
- **geometric constraint**: određeni M···N distance/angle;
- **curation/metadata filter**: 3D coordinates present, bez disorder-a, maksimalni R;
- **post-processing classification**: donor atoms zaista pripadaju DAP komponenti i grade metal coordination environment.

Jedan sloj ne može neopaženo zameniti drugi.

## 16.6 Odvojene odgovornosti u licenciranom okruženju

Bez obzira na izabranu tehnologiju, nekoliko vrsta odgovornosti ne sme da se pomeša:

| Odgovornost | Pitanje koje mora imati odgovor |
|---|---|
| izvor i verzija | Koji CSD release, proizvod i snapshot predstavljaju populaciju? |
| značenje upita | Koji graph/geometric/entry constraints i filteri određuju skup? |
| prava | Ko sme da čita, obrađuje, čuva, prikazuje ili preuzima raw i izvedene podatke? |
| transformacija | Koji alat, verzija i pravilo su proizveli svaki izvedeni prikaz? |
| coverage | Koji zapisi su uspeli, delimični, nepodržani ili neuspešni? |
| dokaz rezultata | Sa kojom verzijom upita, korpusa i reprezentacije je rezultat dobijen? |

Ovo su kategorije provenance-a i odgovornosti, ne propisana baza, API, cache, indeks ili redosled realizacije.

## 16.7 API funkcionalnosti i granica licence

CCDC Python API dokumentuje [IO](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/io.html), [descriptors](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/descriptors.html), [molecular geometry analysis](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/molecular_geometry_analysis.html) i [packing similarity](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/packing_similarity.html). Dostupnost pojedinih funkcija zavisi od licence/proizvoda.

Bez institucijskog pristupa nije moguće pošteno tvrditi da globalna pretraga radi nad celim CSD-om. Coverage, dostupnost funkcija i performanse mogu se potvrditi samo nad odobrenim snapshot-om u stvarnom licencnom okruženju.

## 16.8 Reproduktivni opis upita

Reproduktivnost ne zavisi od jedne konkretne YAML šeme, već od toga da opis razdvoji sledeće činjenice:

| Kategorija | Nalaz za drugi lokalni CQS |
|---|---|
| identitet izvora | SHA-256 `065c31c2669bca2fb087a58650e1a9b8c71ea6bb8f87050b8cab6bd79416aaa5` |
| alat i baza | ConQuest 2022.2.0; CSD 5.43 sa March/June 2022 segmentima |
| izvršivi strukturni uslov | 18-atomski DAP-bis(iminski) motiv plus odvojeni `4M` atom |
| broj povezanih komponenti query grafa | dve; ne postoji metal–motiv constraint |
| sačuvani entry filteri | `require_3d=false`; maksimalni R nije zadat |
| trag vremena | 2026 temp/save trag ne dokazuje da je baza ili run iz 2026. |
| ljudska namera | naziv sugeriše „komplekse“, ali tačan scope čeka potvrdu fakulteta |

Druga serializacija ili terminologija je prihvatljiva ako čuva iste razlike i ne predstavlja ljudski naziv kao izvršivi constraint.

## 16.9 Pitanja za naučni tim

Šest ranijih pitanja nije dovoljno da zaključa scope, prava, dve aplikacije i evaluaciju. Jedina autoritativna lista sada je [Pitanja i odluke za kolege sa fakulteta](../referenca/pitanja-za-fakultet.md).

Za ovo poglavlje posebno su relevantni paketi Q28–Q32: nameravani DAP scope, značenje koordinacije, status oba CQS-a, runtime reprodukcija i eligibility lokalnih izvoza. Već dokazane činjenice — broj rezultata, odnos podskupa i odsustvo metal–motiv constraint-a — ne postavljaju se ponovo kao otvorena pitanja.

## 16.10 Provera znanja

1. Šta dokazuje prisustvo nepovezanog `4M` query atoma?
2. Zašto CSD entry nije sinonim za molekul?
3. Da li 2.038 rezultata čine unbiased globalni trening skup?
4. Koja četiri artefakta su potrebna da se upit reprodukuje?

??? success "Odgovori"
    1. Samo da isti entry sadrži neki metal, ne metal–DAP koordinaciju.  
    2. Entry opisuje određivanje kristala i može imati više komponenti, formi i metapodataka.  
    3. Ne; izabrani su jednim query-jem, filteri su specifični, a pun CSD nije dostupan.  
    4. Verzija alata/baze, potpuna query+filter definicija, snapshot/refcode manifest i provenance/hash.

**Kriterijum prolaza:** možeš da prevedeš ConQuest nameru u eksplicitne mašinske constraints i odvojiš candidate retrieval od hemijski validirane etikete.
