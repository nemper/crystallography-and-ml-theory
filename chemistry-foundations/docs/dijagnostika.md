# Dijagnostika i kriterijumi prolaza

Ovo nije test inteligencije nego usmerivač. Odgovori bez pretrage. Ako ne znaš, napiši "ne znam"; upravo tome kurs služi.

## Ulazna provera

1. Koja je razlika između atoma N, molekula N₂ i jona N³⁻?
2. Da li ista sumarna formula garantuje isti molekulski graf?
3. Šta linija između dva atoma u hemijskom crtežu predstavlja, a šta ne predstavlja?
4. Zašto su ugao C-A-B i torzija A-B-C-D različiti objekti?
5. Može li isti molekul imati više stabilnih 3D konformacija?
6. Šta je ligand i da li koordinacioni broj mora biti jednak broju liganada?
7. Da li "Cu" u nazivu fajla dokazuje da struktura sadrži bakar?
8. Šta se periodično ponavlja u kristalu?
9. Zašto atom sa frakcionom koordinatom 1.02 nije nužno van kristala?
10. Da li dva CIF-a sa različitim parametrima ćelije moraju opisivati različito pakovanje?
11. Šta vrednost `12.7138(3)` govori o neizvesnosti?
12. Da li niz SMILES pouzdano čuva kristalno pakovanje?
13. Zašto se aromatična veza može drugačije zapisati u dva validna formata?
14. Šta Tanimoto sličnost meri ako je ulaz Morgan/ECFP bit-vektor?
15. Zašto nizak R faktor nije dokaz da je hemijski model potpuno tačan?
16. Kako sprečiti da bliski redeterminations iste strukture procure u trening i test?

Početni rezultat od 0 je očekivan. Rezultat se ne koristi za preskakanje kristalografije; koristi se samo da skrati osnovne hemijske vežbe koje već pouzdano radiš.

## Kontrolne kapije

### Kapija A - hemijski graf

**Preduslovi:** poglavlja1–4; ulazna provera je samo orijentacija.

Prolaz kada možeš da:

- iz formule razlikuješ sastav od povezanosti;
- odrediš uobičajenu valencu i formalno naelektrisanje u jednostavnim primerima;
- objasniš rezonancu bez tvrdnje da molekul "skače" između crteža;
- označiš funkcionalne grupe i potencijalne donor/acceptor atome u N14.

### Kapija B - 3D i koordinacija

**Preduslovi:** poglavlja3–6 i11 za pojam polimorfa; polaže se iza11. Pre11 proveravaj samo geometriju i koordinacionu hemiju.

Prolaz kada možeš da:

- izračunaš dužinu, ugao i torziju iz koordinata;
- razlikuješ konformer, konfiguracioni izomer i polimorf;
- za kompleks odrediš donorne atome, denticitet, koordinacioni broj i približnu geometriju;
- objasniš zašto metal-ligand "bond order" nije uvek jednostavan ceo broj.

### Kapija C - kristalni model

**Preduslovi:** poglavlja8–10, zatim drugi prolaz7 i11. Prvi prolaz7 ne zahteva ovu kapiju.

Prolaz kada možeš da:

- iz \(a,b,c,\alpha,\beta,\gamma\) formiraš matricu ćelije;
- pretvoriš frakcione koordinate u kartezijanske i primeniš periodic boundary conditions;
- objasniš asymmetric unit, space group, Z i Z';
- protumačiš occupancy, disorder, s.u., R, wR i goodness-of-fit bez rigidnih univerzalnih pragova.

### Kapija D - projektovanje sličnosti

**Preduslovi:** poglavlja12–20, uključujući mapiranje, kandidatski dohvat i osnovnu evaluaciju; neuralni modeli nisu preduslov.

Prolaz kada možeš da:

- napišeš najmanje tri različite definicije relevantnosti za isti par CIF-ova;
- navedeš informaciju koju svaki format gubi;
- projektuješ dvofazni retrieval/reranking tok;
- napraviš evaluacione splitove po hemijskim i kristalnim familijama;
- prikažeš korisniku komponente skora i neizvesnost.

## Završni usmeni test

Uzmi dva lokalna CIF zapisa i objasni:

1. šta je sigurno zapisano;
2. šta je hemijski dodeljeno;
3. šta treba standardizovati;
4. u kojim su slojevima slični;
5. koje razlike mogu biti artefakti eksperimenta;
6. koja bi mera bila prikladna za globalni dohvat, a koja za precizno poređenje.

Ako odgovor može da prati i hemičar i ML inženjer, cilj kursa je postignut.
