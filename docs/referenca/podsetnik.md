# Brzi pojmovni podsetnik

Ova strana sažima teorijske razlike koje treba razumeti. Nije operativna kontrolna tabla, runbook, release checklist ili redosled realizacije projekta.

!!! danger "Prvo pitanje nije: koji model?"
    Prvo odredi **koji objekat** porediš i **po kom svojstvu**. Sastav, molekulski graf, koordinaciono okruženje, 3D konformacija, kristalno pakovanje i mreža interakcija nisu ista stvar. Jedan broj bez tih specifikacija nema stabilno naučno značenje.

## Dve aplikacije na nivou problema

| | Aplikacija 1 — globalna CSD pretraga | Aplikacija 2 — precizno poređenje svih parova |
|---|---|---|
| ulaz | jedan korisnički CIF i potvrđeni filter/search intent | skup korisničkih CIF-ova i potvrđeni comparison intent |
| pitanje | koji zapisi iz dozvoljenog korpusa su relevantni za imenovanu vrstu sličnosti? | kako se svaki potreban par slaže i razlikuje po imenovanim osama? |
| tipičan algoritamski obrazac | širok candidate retrieval i skuplja provera/rangiranje | component/atom mapping i više odvojenih poređenja |
| ključni rizik | brz metod tiho propušta relevantne strukture | prividno precizan score spaja neuporedive pojmove |
| naučni dokaz | ekspertna relevantnost, coverage, recall/ranking i jasno ograničenje populacije | evidence po osi, coverage/status i invariance provere |
| otvorene odluke | search modes, filteri, korpus, izlaz, prava i metrike | comparison profile, grane, agregacija, limiti, prava i metrike |

Detaljna pitanja koja dostupni fajlovi ne rešavaju nalaze se u [Pitanjima i odlukama za kolege sa fakulteta](pitanja-za-fakultet.md).

## Šta tačno znači „slično“?

Svaki claim može se dopuniti ovako:

> Za objekat **____**, u svrhu odluke **____**, relevantnost znači **____**; obavezno razlikujemo **____**, a rezultat važi samo kada su dostupni **____**.

| Sloj | Pitanje | Potreban evidence | Šta ne dokazuje |
|---|---|---|---|
| sastav | isti elementi, broj atoma, naboj i komponente? | formula/component kontekst | isti graf ili ista supstanca |
| 2D graf | isti scaffold, podstruktura ili povezanost? | graph policy i atom mapping | ista konformacija ili packing |
| koordinacija | isti metal, donor set, CN i geometrija? | metal–donor mapping, geometrija i neizvesnost | samo prisustvo metala u entry-ju |
| 3D konformacija | mapirani atomi imaju sličan raspored? | mapping, alignment, coverage i RMSD | isti periodični kristal |
| ćelija/rešetka | metrike rešetke su kompatibilne? | kompatibilna/redukovana ćelija i tolerancije | isti packing |
| packing | isto periodično okruženje molekula? | periodični cluster, coverage, RMSD i parametri | isto svojstvo ili stabilnost |
| interakcije | isti definisani kontaktni motivi/mreže? | definicije, geometrija, periodična topologija i uncertainty | energiju bez dodatnog modela |
| svojstvo | slično ponašanje za tačno određeni target? | vrednost, jedinica, uslovi, forma i provenance | strukturnu identičnost |

## Pet nivoa identiteta

```text
hemijski scaffold
└── molekulska/protonaciona vrsta
    └── sastav čvrste forme
        └── polymorph/phase
            └── pojedinačno kristalografsko određivanje
```

„Isto“ na višem nivou ne garantuje isto na nižem. Dva polymorph-a mogu imati isti molekulski graf; dva redetermination zapisa mogu predstavljati istu fazu; salt i neutralna forma ne postaju isti materijal samo uklanjanjem counterion-a.

## Formati i gubitak značenja

| Format | Tipično čuva | Tipično ne čuva ili ostavlja zavisnim od alata |
|---|---|---|
| CIF | ćeliju, simetriju, atom sites, occupancy i eksperimentalne metadata | kompletan i nedvosmislen molekulski bond graph |
| MOL/SDF | molekulski graf i opcione koordinate/properties | periodičnost, packing i većinu eksperimentalnog konteksta |
| MOL2 | atom/bond tipove, substructure i opcione charge-e | univerzalno tačnu metalnu povezanost ili pun crystal provenance |
| SMILES | kompaktan molekulski graf | ćeliju, packing, eksperimentalnu konformaciju i često potpunu stereo/metal semantiku |

Uspešna konverzija je sintaktički događaj, ne dokaz semantičke bezgubitnosti.

## DAP/CQS činjenice

- oba sačuvana upita sadrže isti povezani 18-atomski DAP-bis(iminski) motiv;
- drugi dodaje nepovezani `4M` atom;
- `4M` dokazuje metal negde u istom entry-ju, ne DAP–metal koordinaciju;
- `search2` je strogi podskup `search1`, ali membership nije coordination gold;
- potencijalna tri donorska N atoma nisu isto što i opažena tridentatna koordinacija;
- naziv query fajla izražava ljudsku nameru, dok constraints određuju šta je stvarno pretraženo.

Nameravani DAP i coordination scope ostaje fakultetska odluka Q28–Q32.

## Kristalografske invarijanse

Ekvivalentan zapis može promeniti:

- redosled atoma ili komponenti;
- izbor origina i periodične slike;
- cell setting ili kompatibilnu basis predstavu;
- ASU prikaz i symmetry-operation redosled;
- translaciju/rotaciju molekulske geometrije.

Promena zapisa ne sme automatski postati promena fizičkog kristala. Nasuprot tome, ista formula, space-group etiketa ili reduced cell ne dokazuju isti packing.

## Mapping pre metrike

Component mapping prethodi atom mapping-u, a hemijski validan atom mapping prethodi RMSD-u. RMSD bez common core-a, coverage-a, alignment/symmetry/stereo pravila i porekla koordinata nema stabilno značenje.

Za neuređene parove važi:

\[
N_{pairs}=\frac{n(n-1)}{2}.
\]

Kvadratna složenost je matematička činjenica; scheduler, cache, storage i produkcioni limiti nisu deo ovog podsetnika.

## Quality, missing i uncertainty

- R faktor nije accuracy procenat.
- `parse success` nije dokaz hemijske ni kristalografske validnosti.
- disorder, partial occupancy i missing H menjaju primenljivost pojedinih analiza.
- `not comparable`, `missing`, `ambiguous` i validni score 0 nisu sinonimi.
- simulated PXRD iz CIF-a nije nezavisna potvrda istog CIF modela.
- Mogul/HBP outlier ili propensity nije energija, stabilnost ili dokaz polimorfa.

## ML/AI razlike

- exact oracle proverava aproksimativni ANN indeks; ekspertni gold proverava semantičku relevantnost;
- candidate recall i finalni ranking nisu ista metrika;
- random split bliskih structure families može dati leakage;
- property target mora biti vezan za formu, jedinicu, uslove, metod i vreme;
- model ili embedding ne zamenjuje parser, PBC, atom mapping, licencu ili stručni dokaz;
- složeniji model je opravdan samo ako pod istim uslovima rešava imenovanu grešku.

## Licence i FAIR

- „mogu da pročitam“ nije „smem da obrađujem ili delim“;
- private GitHub nije dozvola za CSD redistribuciju;
- FAIR nije isto što i open, bez greške ili licencno slobodno;
- raw podatak, izvedeni feature, embedding, model i report mogu imati različita prava;
- vendor opis funkcije nije dokaz institucijskog product tier-a ili entitlement-a;
- FL ne daje automatski confidentiality, privacy, security ili licencnu usklađenost.

## Jednominutna provera znanja

1. Isti molekulski graf i drugačiji packing — koji slojevi se slažu, a koji ne moraju?
2. Zašto reduced-cell pogodak nije dokaz istog polimorfa?
3. Koje informacije uz RMSD sprečavaju najčešću pogrešnu interpretaciju?
4. Šta je ispravan zaključak packing grane kada CIF nema ćeliju?
5. Da li CSD-derived embedding automatski sme u javni repo?
6. Zašto `4M` nije koordinaciona etiketa?

??? success "Odgovori"
    1. Slaže se 2D identitet/graf; konformacija može, ali ne mora; packing i interaction mreža mogu biti različiti.  
    2. Različiti kristali mogu imati sličnu metriku ćelije; potrebno je periodično poređenje mapiranih molekula i eksplicitni parametri.  
    3. Common core/atom mapping, broj i coverage mapiranih atoma, alignment/symmetry/H/stereo pravilo i poreklo koordinata.
    4. Analiza nije podržana zbog missing input-a; to nije score 0.
    5. Ne. Potrebno je proveriti ugovor, derivative prava, rekonstruktivnost i pisano odobrenje.
    6. Zato što query zahteva samo metal negde u entry-ju, bez veze ili geometrijskog constraint-a ka DAP motivu.
