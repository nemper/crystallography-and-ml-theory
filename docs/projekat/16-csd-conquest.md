# 16. CSD i ConQuest tok podataka

**Prioritet: MORAŠ.** Ova strana objašnjava šta lokalni izvozi jesu, šta nisu i kako će aplikacije jednog dana bezbedno raditi sa licenciranim CSD pristupom.

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

`.cqs` je binarni ConQuest query/session objekat. U dostavljenim lokalnim fajlovima sadrži i sačuvano stanje/rezultate, ali nije obična prenosiva result-lista niti univerzalni javni standard za razmenu. Pre produkcione reprodukcije treba ga otvoriti u kompatibilnoj ConQuest verziji, pregledati vizuelno i izvesti mašinski čitljiv manifest svih constraints/filtera.

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

## 16.6 Budući licencirani tok

```mermaid
flowchart LR
    Q[Verzionisani query manifest] --> S[CSD/ConQuest/API search]
    S --> E[Entry IDs + dozvoljeni fields]
    E --> R[Raw licensed cache]
    R --> V[Validation + provenance]
    V --> IDX[Task-specific indeksi]
    IDX --> API[Naše dve aplikacije]
    API --> AUD[Audit + usage controls]
```

Za svaki dataset snapshot sačuvati:

- CSD release i licensed product/API verziju;
- query definiciju, screenshot/export i hash;
- sve filtere i njihova default stanja;
- datum, broj pogodaka i refcode manifest;
- dozvolu/pravni osnov za storage, processing, rezultat i download;
- parser/toolkit verzije i transformacije;
- neuspele ili delimične zapise, ne samo uspešne.

## 16.7 API funkcionalnosti i granica licence

CCDC Python API dokumentuje [IO](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/io.html), [descriptors](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/descriptors.html), [molecular geometry analysis](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/molecular_geometry_analysis.html) i [packing similarity](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/packing_similarity.html). Dostupnost pojedinih funkcija zavisi od licence/proizvoda.

Do dobijanja institucijskog pristupa nije moguće pošteno tvrditi da globalna pretraga radi nad celim CSD-om. Sada se mogu projektovati schema, pipeline, evaluation fixtures i adapter interfejsi, ali coverage i performanse moraju biti potvrđeni nad odobrenim snapshot-om.

## 16.8 Minimalni query manifest

```yaml
query_id: dap-bis-imine-plus-any-metal-v1
source_file_sha256: "065c31c2669bca2fb087a58650e1a9b8c71ea6bb8f87050b8cab6bd79416aaa5"
source_tool: ConQuest
source_version: "2022.2.0"
searched_database: "CSD 5.43 with March/June 2022 updates"
artifact_temp_path_timestamp: "2026-06-06T18:53:01 (timezone not established)"
timestamp_semantics: "search-or-save trace; not an authoritative run date"
atoms: 19
connected_components: 2
structural_motif: dap-bis-imine-18-atoms
extra_atom_type: 4M
metal_to_motif_constraint: none
entry_filters:
  require_3d: false
  max_r_factor: null
human_intent: "candidate complexes; requires post-validation"
review_status: query-decoded_intent-pending-faculty-confirmation
```

## 16.9 Pitanja za naučni tim

Pre definisanja ground truth-a treba dobiti odgovore:

1. Da li „DAP“ ovde tačno znači 2,6-diacetylpyridine-derived bis(imine) scaffold?
2. Da li metal treba da bude direktno koordinisan i kojim donor set-om?
3. Da li su monodentate/bidentate, bridging, protonated ili decomposed varijante pozitivne?
4. Da li entry sa metalom samo u counterion-u treba isključiti?
5. Da li se polymers, disorder i records bez 3D zadržavaju za retrieval, a izuzimaju iz 3D poređenja?
6. Koja CSD licenca i deployment boundary važe za oba proizvoda?

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
