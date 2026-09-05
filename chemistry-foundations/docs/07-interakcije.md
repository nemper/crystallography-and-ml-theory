# 7. Intermolekulske interakcije

**Dva prolaza.** Prvi prolaz traži [veze i slobodne parove](02-veze.md), [dužinu i ugao](03-geometrija.md#32-tri-osnovne-geometrijske-velicine) i [različite donorske uloge](04-organska.md#donorske-uloge). Čitaj do [kapije prvog prolaza](#kapija-prvog-prolaza), zatim savladaj [ćeliju i koordinate](08-celija.md), [simetriju i ASU](09-simetrija.md) i [zauzeće mesta i nered modela](10-difrakcija-kvalitet.md#occupancy-koliko-je-kristalografsko-mesto-zauzeto). Tek posle poglavlja 10 vrati se na [periodične kontakte u drugom prolazu](#drugi-prolaz).

## Šta treba da umeš posle ovog poglavlja

Posle **prvog prolaza** treba da možeš da:

- razlikuješ hemijsku vezu, geometrijski kontakt i fizički podržanu intermolekulsku interakciju;
- objasniš osnovne uloge elektrostatike, disperzije, odbijanja, vodoničnih i halogenih veza;
- izračunaš jednostavnu udaljenost i ugao kandidata za vodoničnu vezu;
- objasniš zašto kraće rastojanje nije nužno povoljnije.

Posle **drugog prolaza**, uz ćeliju, simetriju i zauzeće mesta, treba da možeš da:

- pronađeš susede koji prelaze granicu jedinične ćelije;
- koristiš simetrijske operacije i celobrojne translacije pri traženju kontakata;
- izračunaš udaljenost i ugao kandidata za vodoničnu vezu;
- objasniš zašto jedan distance cutoff nije dovoljan za sve elemente i sva hemijska okruženja;
- predstaviš kristal kao periodični kontaktni graf sa poreklom i neizvesnošću svake ivice;
- prevedeš interakcije u objašnjive feature-e za obe 2CDC aplikacije.

## Prvi prolaz: hemijska i fizička intuicija {#prvi-prolaz}

## Intuicija: molekul se ne završava ivicom nacrtane ćelije

Molekulski graf govori koji su atomi hemijski povezani unutar komponente. Kristal, međutim, nastaje kada se molekuli, joni ili koordinacioni entiteti periodično rasporede i međusobno utiču. Najbliži sused nekog atoma često nije u istoj nacrtanoj ćeliji niti u istoj asimetričnoj jedinici.

Zamisli atom blizu desne strane periodične slike. Njegov najbliži sused može biti tik preko leve strane sledeće slike:

Sledeća šema služi orijentaciji; račun simetrijskih kopija pripada drugom prolazu.

~~~mermaid
flowchart LR
    A["Asimetrična jedinica<br/>jedinstveni atomski položaji"]
    B["Simetrijske kopije<br/>unutar jedinične ćelije"]
    C["Celobrojne translacije<br/>susednih ćelija"]
    D["Periodični susedi"]
    E["Hemijski klasifikovani<br/>kontakti i mreže"]
    A --> B --> C --> D --> E
~~~

Ako algoritam računa samo udaljenosti između redova atomskog loop-a, propustiće intermolekulske kontakte. Ako, suprotno tome, svaki kratak razmak proglasi vezom, napraviće lažnu hemiju.

!!! danger "Kontakt nije automatski interakcija"
    Udaljenost je geometrijska činjenica izvedena iz kristalografskog modela. Naziv „vodonična veza“, „halogena veza“ ili „π-interakcija“ zahteva hemijski kontekst i odgovarajuću geometriju, a tvrdnja o energetskom značaju može zahtevati dodatni proračun ili eksperimentalni dokaz.

## Šta drži molekulski kristal

Intermolekulsko ponašanje je zbir više doprinosa koji se međusobno preklapaju:

| Doprinos | Osnovna ideja | Zašto jednostavan feature može da pogreši |
|---|---|---|
| elektrostatika | privlačenje suprotnih i odbijanje istih raspodela naboja | formalni naboj nije potpuna raspodela elektronske gustine |
| indukcija/polarizacija | električno polje jednog partnera deformiše drugi | zavisi od okruženja i polarizabilnosti |
| disperzija | korelisane trenutne fluktuacije elektrona | prisutna je i između nepolarnih grupa; nije samo „slaba slučajnost“ |
| Pauli odbijanje | elektronske gustine se ne mogu proizvoljno preklopiti | veoma kratko nije automatski veoma povoljno |
| usmerene interakcije | H-veze, halogene veze i srodni obrasci | traže donor/akceptor identitet i uglove, ne samo udaljenost |

Za dve tačkaste naelektrisane čestice najjednostavniji elektrostatički model je:

\[
U_{\mathrm{el}}(r)=
\frac{1}{4\pi\varepsilon_0\varepsilon_r}
\frac{q_iq_j}{r}.
\]

On dobro pokazuje znak i zavisnost od udaljenosti, ali molekuli nisu zbir fiksnih tačkastih formalnih naboja, a efektivna permitivnost kristala nije univerzalna konstanta.

| Simbol | Značenje i SI jedinica |
|---|---|
| \(U_{\mathrm{el}}\) | potencijalna energija jednog para, J |
| \(r>0\) | razmak dve tačkaste čestice, m |
| \(q_i,q_j\) | njihovi naboji sa znakom, C (kulon) |
| \(\varepsilon_0\) | permitivnost vakuuma, F/m odnosno C²/(J·m) |
| \(\varepsilon_r\) | relativna permitivnost homogenog medijuma u ovom modelu, bezdimenziona |
| \(\pi\) | matematička konstanta, približno 3,14159 |

Nula energije izabrana je za beskonačno razdvojene čestice, \(U_{\mathrm{el}}(\infty)=0\). Suprotni znaci naboja daju negativnu energiju, isti znaci pozitivnu. Ako su naboji zapisani u jedinicama elementarnog naboja, a razmak u Å, pre SI računa moraju se pretvoriti u C i m. Molarna energija dobija se množenjem energije jednog para Avogadrovim brojem; jedinice ne treba mešati.

Kombinacija kratkodometnog odbijanja i disperzione privlačnosti često se ilustruje Lennard-Jones izrazom:

\[
U_{\mathrm{LJ}}(r)=4\varepsilon
\left[
\left(\frac{\sigma}{r}\right)^{12}
-
\left(\frac{\sigma}{r}\right)^6
\right].
\]

Ova jednačina je dobra intuicija za postojanje optimalnog razmaka. Nije dokaz da stvarni kristalni kontakt prati baš tu parametrizaciju, niti opisuje usmerenost, polarizaciju, transfer naboja ili višestruke kolektivne efekte.

Ovde je \(\sigma\) parametar dužine u istim jedinicama kao \(r\), a \(\varepsilon>0\) parametar energije u istim jedinicama kao \(U_{\mathrm{LJ}}\): J po paru ili dosledno kJ/mol u molarnom zapisu. **LJ \(\varepsilon\) je dubina energetskog minimuma; nije permitivnost \(\varepsilon_0\) ni relativna permitivnost \(\varepsilon_r\).** Izraz takođe bira \(U_{\mathrm{LJ}}(\infty)=0\).

### Zašto kraći kontakt nije nužno povoljniji

Član \(+4\varepsilon(\sigma/r)^{12}\) je odbojni doprinos, a \(-4\varepsilon(\sigma/r)^6\) privlačni. Pri smanjivanju razmaka prvi raste brže. Nastavni prikaz ukupne krive označava nulu, minimum i obe strane minimuma; horizontalni razmaci u skici nisu u razmeri:

```text
U/ε
 ↑    ╲  odbojna sila: r < r_min
 │     ╲
0├──────●────────────────────────────────────→ r/σ
 │       ╲  σ: U=0                  _________  U → 0⁻
 │        ╲                    ____/
 │         ╲              ____/    privlačna sila: r > r_min
−1          ╰────●───────╯
                 minimum: r_min/σ = 2^(1/6) ≈ 1,122
```

\(U=0\) je na \(r=\sigma\), dok je minimum na \(r_\min=2^{1/6}\sigma\), sa \(U(r_\min)=-\varepsilon\). Na minimumu se odbojni i privlačni **doprinosi sili** poništavaju; doprinosi energiji tada su \(+\varepsilon\) i \(-2\varepsilon\). Negativna ukupna energija zato nije sinonim za privlačnu silu: između \(\sigma\) i \(r_\min\) energija jeste negativna, ali približavanje povećava energiju i sila je odbojna.

| \(r/\sigma\) | \(U/\varepsilon\) | Tumačenje |
|---:|---:|---|
| 0,9 | +6,636 | veliko kratkodometno odbijanje |
| 1 | 0 | nula energije na konačnom razmaku |
| \(2^{1/6}\approx1,122\) | −1 | minimum |
| 2 | −0,06152 | slaba preostala privlačnost |
| \(\infty\) | 0 | razdvojeni partneri, referentna nula |

Na minimumu je \((\sigma/r)^6=1/2\), pa formula daje \(4\varepsilon(1/4-1/2)=-\varepsilon\). [LAMMPS dokumentacija LJ izraza](https://docs.lammps.org/pair_lj.html) izričito razlikuje \(\sigma\) od položaja minimuma. Nijedna od ove dve parne formule nije potpun model kristalne energije; broj kratkih kontakata ne određuje termodinamičku stabilnost.

## Vodonična veza: donor, vodonik, akceptor i geometrija

Kandidat se zapisuje:

\[
\mathrm{D-H\cdots A},
\]

gde je D donor atom, H vodonik vezan za donor, a A akceptor. Za procenu se obično gledaju najmanje:

- hemijski identitet i stanje donora;
- hemijski identitet, protonacija i koordinaciono stanje akceptora;
- udaljenost \(d(\mathrm{H,A})\);
- udaljenost \(d(\mathrm{D,A})\);
- ugao \(\angle\mathrm{D-H-A}\).

Pravolinijskiji raspored je često geometrijski ubedljiviji, ali ne postoji jedan univerzalni prag koji bez izuzetka važi za sve donore, akceptore, temperature i kvalitet strukture. IUPAC definicija naglašava privlačnu interakciju i dokaz koji prevazilazi samo proizvoljan cutoff.

Tipični kandidati uključuju O-H i N-H donore. O i N mogu biti akceptori, ali ne u svakom stanju: protonacija, rezonanca, pozitivni naboj ili koordinacija metalu mogu promeniti njihovu sposobnost prihvatanja H-veze. Zbog toga feature <code>element == O</code> nije dovoljan.

### Prvi mali geometrijski račun

Uzmi nastavne kartezijanske položaje u Å: D=(0,0,0), H=(1,0,0), A=(3,0,0), sa hemijski smislenim D–H i akceptorom A. Tada je \(d(\mathrm{D,H})=1\) Å, \(d(\mathrm{H,A})=2\) Å i \(d(\mathrm{D,A})=3\) Å. Vektori iz vrha H su \((-1,0,0)\) i \((2,0,0)\); njihov skalarni proizvod je −2, a proizvod normi 2. Zato je \(\cos\theta=-1\) i \(\angle\mathrm{D-H-A}=180^\circ\). Geometrija je pravolinijska; još nije izračunata energija interakcije. Ovde nema ćelije ni simetrijskih operacija: sledeće lekcije omogućavaju isti račun kada je A periodična slika. [Donorstvo H-veze i protonski transfer](04-organska.md#donorske-uloge) ostaju različiti pojmovi.

### Položaj vodonika je deo neizvesnosti

U rendgenskim strukturama mnogi H atomi su postavljeni geometrijski i refinirani riding modelom. U drugim slučajevima položaj H može biti nezavisnije refiniran. U <code>cu_n14_a.cif</code> H2N ima refinirani položaj i prijavljenu vezu:

\[
d(\mathrm{N2-H2N})=0.876(19)\ \text{Å}.
\]

To je korisnije od potpuno implicitnog H, ali ni tada ne treba zanemariti standardnu neizvesnost i kvalitet ostatka modela.

### Rendgenski i normalizovani H nisu iste koordinate

Rendgensko zračenje rasipa se na elektronskoj gustini, dok neutroni daju informacije o položajima jezgara. Kod konvencionalnog rendgenskog refiniranja sa sfernim atomskim modelom elektronska gustina vezanog H pomerena je ka vezi, pa su dobijene X–H dužine tipično kraće od internuklearnih. To važi i kada je položaj H slobodno refiniran; napredniji asferni modeli mogu znatno smanjiti ovu razliku. [IUCr istraživanje IAM/TAAM modela](https://journals.iucr.org/b/issues/2020/03/00/px5019/) objašnjava zašto „refiniran H“ nije automatski precizan položaj jezgra.

Pri **neutronskoj normalizaciji** H se pomera duž postojeće X–H veze do izabrane referentne internuklearne dužine. To menja H···A udaljenost i D–H···A ugao, dok D···A ostaje isti. Referentne dužine zavise od pravila i hemijskog okruženja; normalizacija nije novo merenje niti opravdanje da se prepišu izvorne koordinate. [CCDC opis normalizacije](https://downloads.ccdc.cam.ac.uk/documentation/API/modules/molecule_api.html#ccdc.molecule.Molecule.normalise_hydrogens) i [Allen–Bruno studija referentnih X–H dužina](https://doi.org/10.1107/S0108768110012048) daju osnovu ovog postupka. Sačuvaj raw geometriju i zasebno izvedenu geometriju sa metodom i ciljnom X–H dužinom. Svi N14 brojevi u nastavku računati su iz originalnih, nenormalizovanih CIF koordinata.

## Ostale projektno relevantne interakcije

### Jonske i charge-assisted interakcije

Suprotno naelektrisane komponente mogu dati dugodometan elektrostatički doprinos. Kod soli nije dovoljno analizirati samo najbliži atom; periodična raspodela naboja i counterion-i su deo sistema. Uklanjanje counterion-a pre izrade crystal feature-a menja fizički problem.

### Halogene veze

Halogena veza uključuje elektrofilni region vezanog halogenog atoma i nukleofilni partner. Često je usmerena duž produžetka kovalentne veze R-X. Sama kratka X···A udaljenost nije potpuna definicija; potreban je i ugaoni/elektronski kontekst. IUPAC preporuka daje precizniji okvir.

### π-sistemi

Za moguće π···π ili C-H···π kontakte mogu se koristiti centroidi prstenova, normale ravni, međuravanski ugao i lateralni pomak. Sam centroid-centroid razmak ne razlikuje povoljno preklapanje od geometrije u kojoj su prstenovi samo slučajno blizu.

### Metal-involving kontakti

Kod koordinacionih jedinjenja granica između koordinacione veze i nekovalentnog kontakta može zavisiti od oksidacionog stanja, donor-atoma, koordinacionog broja i geometrije. Jedinstveni globalni cutoff po paru elemenata posebno je rizičan za lantanoide, haptovezivanje i mostne ligande.

## Van der Waals radijusi: koristan ekran, ne prirodni zakon

Jedan jednostavan deskriptor kontakta je:

\[
\Delta_{\mathrm{vdW}} =
d_{ij}-
\left(r_i^{\mathrm{vdW}}+r_j^{\mathrm{vdW}}\right),
\]

ili normalizovan oblik:

\[
R_{\mathrm{norm}}=
\frac{d_{ij}}
{r_i^{\mathrm{vdW}}+r_j^{\mathrm{vdW}}}.
\]

Negativan \(\Delta_{\mathrm{vdW}}\), odnosno \(R_{\mathrm{norm}}<1\), označava razmak kraći od zbira izabrane tabele radijusa. To je screening signal. Rezultat zavisi od tabele radijusa, protonacije, kvaliteta koordinata i hemijskog tipa atoma. Aplikacija mora čuvati naziv i verziju korišćenog skupa radijusa.

## Kapija prvog prolaza {#kapija-prvog-prolaza}

Pre odlaska u [poglavlje 8](08-celija.md) objasni razliku kontakta i interakcije, izračunaj tri dužine i ugao gornjeg D–H···A primera i pokaži na LJ krivoj zašto \(r=0,9\sigma\) nije povoljniji od minimuma. Periodične primere i završnu kapiju radi tek po povratku posle poglavlja [8](08-celija.md), [9](09-simetrija.md) i [10](10-difrakcija-kvalitet.md).

## Drugi prolaz: periodični kontakti {#drugi-prolaz}

**Preduslovi:** znaš \(\mathbf r=\mathbf A\mathbf f\), fizičko rastojanje u kosoj ćeliji, simetrijsku operaciju i razliku ASU–ćelija–periodični nastavak iz [8](08-celija.md) i [9](09-simetrija.md), kao i occupancy/disorder iz [10](10-difrakcija-kvalitet.md#occupancy-koliko-je-kristalografsko-mesto-zauzeto). Sledeći kratki podsetnik povezuje kvalitet modela sa kontaktima; formule punog kontaktnog računa imaju glavno mesto u narednom odeljku.

### Pre računa: zauzeće mesta i nered modela

**Zauzeće mesta** (*occupancy*) govori koji udeo ekvivalentnih kristalografskih mesta zauzima navedena vrsta ili modelovana alternativa; nije verovatnoća da je atom „tačan“. **Nered** (*disorder*) znači da jedinstven uredan položaj/raspored ne opisuje sve ćelije ili celo vreme merenja. Model zato može sadržati međusobno isključive atomske alternative. Ako su dve orijentacije molekula zastupljene sa 0,6 i 0,4, ne smemo sve njihove atome proglasiti istovremeno prisutnim i izbrojati lažne kontakte među alternativama. Proizvod occupancy vrednosti sam ne daje zajedničku verovatnoću kontakta bez pretpostavke o zavisnosti alternativa.

Broj simetrijskih kopija mesta (*multiplicity*) odvojen je od occupancy; specijalno mesto može imati manje različitih kopija uz puno zauzeće. Pre geometrije odaberi hemijski konzistentnu alternativu ili odvojeno prikaži moguće kontakte. [Detalji zauzeća](10-difrakcija-kvalitet.md#occupancy-koliko-je-kristalografsko-mesto-zauzeto) i [nereda i pomeranja](10-difrakcija-kvalitet.md#disorder-i-displacement-parametri) pripadaju kasnijoj stručnoj proveri kvaliteta.

## Kako se stvarno nalaze periodični susedi

Neka matrica ćelije \(\mathbf A\) ima vektore \(\mathbf a,\mathbf b,\mathbf c\) kao kolone. Frakcionu koordinatu atoma \(j\), \(\mathbf f_j\), simetrijska operacija \(s\) pretvara u:

\[
\mathbf f_{j,s}=\mathbf R_s\mathbf f_j+\mathbf t_s.
\]

Sve periodične slike dobijaju se dodavanjem celobrojnog vektora:

\[
\mathbf f_{j,s,\mathbf n}=
\mathbf R_s\mathbf f_j+\mathbf t_s+\mathbf n,
\qquad
\mathbf n\in\mathbb Z^3.
\]

Udaljenost od atoma \(i\) je:

\[
d_{ij}^{(s,\mathbf n)}
=
\left\|
\mathbf A
\left(
\mathbf f_{j,s,\mathbf n}-\mathbf f_i
\right)
\right\|_2.
\]

Pouzdan tok je:

1. pročitaj ćeliju i symmetry operations iz CIF-a;
2. generiši simetrijske slike;
3. odredi dovoljan opseg celobrojnih translacija za zadati radijus pretrage;
4. računaj udaljenosti u Cartesian prostoru ili pomoću metric tensor-a;
5. ukloni duplikate nastale na specijalnim pozicijama;
6. tek zatim primeni hemijsko tipiziranje i geometrijske kriterijume;
7. uz svaku ivicu sačuvaj operaciju, translaciju, udaljenost, uglove i confidence.

### Referentni sloj: simetrijske kopije i deduplikacija

Kod centrirane konvencionalne ćelije centrirajući pomaci moraju biti uključeni u puni skup simetrijskih translacija \(\mathbf t_s\). Susedi se ne traže samo među redovima ASU: iz nje se generišu simetrijske slike, zatim njihove celobrojno translirane kopije. Kopije se deduplikuju samo kada predstavljaju isto kristalografsko mesto unutar tolerancije i slažu se vrsta atoma, occupancy i disorder identitet; sama blizina nije dovoljna. Ishod kontakta za isto fizičko atomsko mapiranje treba da ostane isti pod ekvivalentnim \((\mathbf R_s,\mathbf t_s,\mathbf n)\) zapisima, dok se konkretni zapis čuva kao trag porekla (*provenance*) kontakta.

!!! warning "Frakcioni prostor nije euklidski ekran"
    Razlika frakcionih koordinata nema jedinicu Å i njena obična Euklidska norma nije fizička udaljenost. Kod kose ćelije ni zaokruživanje svake komponente razlike na najbliži ceo broj nije uvek dovoljno za nalaženje najkraće slike. Koristi metric tensor ili proverenu periodičnu neighbor-search implementaciju.

## Lokalni N14 primer: kontakt koji nije u atomskom loop-u

Lokalni CIF navodi simetrijsku operaciju:

\[
(x,y,z)\longmapsto(-x,\ y+\tfrac12,\ -z+\tfrac12).
\]

Za O2 sa frakcionim koordinatama:

\[
(0.50686,\ 0.40197,\ 0.21973)
\]

primena operacije, a zatim translacija za jednu ćeliju duž \(\mathbf a\), daje:

\[
\mathrm{O2}^{(ii)}=
(0.49314,\ 0.90197,\ 0.28027).
\]

H2N i donor N2 iz originalne asimetrične jedinice imaju:

\[
\begin{aligned}
\mathrm{H2N}&=(0.4235,\ 0.7644,\ 0.3418),\\
\mathrm{N2}&=(0.42369,\ 0.70769,\ 0.33548).
\end{aligned}
\]

Kada se sve koordinate pretvore pomoću stvarne monoklinične ćelije, dobija se geometrijski kandidat:

| Veličina | Vrednost |
|---|---:|
| \(d(\mathrm{H2N,O2}^{(ii)})\) | približno 2,400 Å |
| \(d(\mathrm{N2,O2}^{(ii)})\) | približno 3,182 Å |
| \(\angle\mathrm{N2-H2N-O2}^{(ii)}\) | približno 148,9° |

Ista symmetry-related molekulska kopija daje i O1 kandidat:

| Veličina | Vrednost |
|---|---:|
| \(d(\mathrm{H2N,O1}^{(ii)})\) | približno 2,501 Å |
| \(d(\mathrm{N2,O1}^{(ii)})\) | približno 3,332 Å |
| \(\angle\mathrm{N2-H2N-O1}^{(ii)}\) | približno 158,9° |

Ovi brojevi opravdavaju oznaku **geometrijski kandidati za N-H···O kontakte**. Sami ne dokazuju pojedinačnu energiju, niti opravdavaju automatsko biranje samo jednog od dva O atoma. Zato je naučno potreban geometrijski trag i poznata definicija klasifikacije; sam boolean <code>is_hbond=true</code> nije dovoljan dokaz.

## Od liste kontakata do periodičnog grafa

Za aplikacije je korisno razlikovati dva grafa:

- **atomski kontaktni graf**: čvorovi su atomi, a ivice su tipizirani periodični kontakti;
- **molekulski packing graf**: čvorovi su molekulske/komponentne kopije, a ivice sabiraju njihove kontakte.

Da bi periodični kontakt mogao da se protumači i reprodukuje, evidence mora da odgovori na:

| Kategorija | Zašto je potrebna |
|---|---|
| atom/component mapping | da se zna ko sa kim interaguje |
| symmetry operation ID | da se kontakt reprodukuje |
| translation \((n_a,n_b,n_c)\) | da se pronađe konkretna periodična slika |
| \(d_{\mathrm{H,A}}\), \(d_{\mathrm{D,A}}\), ugao | objašnjenje geometrije |
| interaction candidate type | H-bond, halogen, π, generic contact... |
| rule set i verzija | pragovi i atom typing se menjaju |
| quality/uncertainty | disorder, occupancy, H treatment, s.u. |

Status dokazne tabele objašnjen je u [centralnoj napomeni o teorijskom i referentnom sloju](kako-koristiti.md#teorijski-i-referentni-sloj). Graf treba da bude invarijantan na izbor origina, ekvivalentne jedinične ćelije i redosleda atoma. Sirovi symmetry-operation indeks nije stabilan između dva ekvivalentna CIF zapisa, pa služi za provenance unutar konkretnog zapisa, ne kao globalni feature ID.

## Zašto je ovo relevantno za dve aplikacije

### Globalna pretraga

- Hemijski graf služi za brz molekulski dohvat; periodični kontaktni deskriptori daju packing/interakcioni re-ranking.
- Donor/akceptor motiv može biti filter samo uz jasno poznatu definiciju pravila.
- Kontaktne mreže moraju uključiti symmetry-related i cross-boundary susede.
- Nedostajući H, disorder ili nepouzdan bond typing treba da smanje confidence, ne da postanu lažno odsustvo interakcije.
- Learned embedding kontakata ne objašnjava sam po sebi komponentne skorove ili geometrijski trag.

### Poređenje svih parova

- Poredi se obrazac interakcija posle mapiranja hemijski odgovarajućih atoma i komponenti.
- Odvojeno vrati pokrivenost donora/akceptora, podudaranje tipa, geometrijsku razliku i topologiju mreže.
- Isti kontakt opisan drugom symmetry operation numeracijom ili ćelijskom translacijom mora ostati isti fizički kontakt.
- Razlika jedne slabe ivice ne treba automatski da nadvlada podudaranje cele mreže.
- Izveštaj mora razlikovati „kontakt nije pronađen“ od „nije bilo dovoljno pouzdanih podataka da se testira“.

## Tipične zamke

1. Tražiti kontakte samo među atomima iz asimetrične jedinice.
2. Meriti Euklidsku udaljenost direktno u frakcionim koordinatama.
3. Ograničiti periodičnu pretragu na jednu unapred fiksiranu susednu ćeliju za svaki cutoff i oblik ćelije.
4. Proglasiti svaki O ili N za akceptor.
5. Proglasiti svaku udaljenost kraću od zbira van der Waals radijusa za stabilizujuću interakciju.
6. Ignorisati uglove kod usmerenih interakcija.
7. Ukloniti solvent ili counterion pre packing analize.
8. Tretirati symmetry-generated intermolekulski kontakt kao kovalentnu vezu.
9. Porediti symmetry-operation indekse između dva CIF-a kao stabilne kategorije.
10. Izjednačiti broj kontakata sa stabilnošću ili kristalnom energijom.
11. Zaključiti da interakcija ne postoji zato što H atom nije eksplicitno naveden.
12. Koristiti jedan skup geometrijskih pragova bez verzije i validacije na koordinacionim kompleksima.

## Mini-vežbe

### 1. Granica ćelije

Atom A ima frakcionu koordinatu \(x=0.98\), a atom B \(x=0.03\), u ortogonalnoj ćeliji sa \(a=10\ \text{Å}\). Kolika je njihova najkraća razlika duž \(\mathbf a\)?

??? success "Odgovor"
    Ne koristi se \(0.95a=9.5\ \text{Å}\), već periodična slika B sa \(x=1.03\). Razlika je \(0.05a=0.5\ \text{Å}\).

### 2. N14 O2 slika

Primeni operaciju \((-x,y+\tfrac12,-z+\tfrac12)\) na O2 i izaberi translaciju koja koordinatu smešta blizu H2N.

??? success "Odgovor"
    Posle operacije dobija se \((-0.50686,0.90197,0.28027)\). Dodavanje \((1,0,0)\) daje \((0.49314,0.90197,0.28027)\), periodičnu sliku korišćenu u lokalnom primeru.

### 3. Da li je to dokazana H-veza?

Da li \(d(\mathrm{H,A})=2.40\ \text{Å}\) sam po sebi dokazuje vodoničnu vezu?

??? success "Odgovor"
    Ne. Potrebni su hemijski validan donor i akceptor, D-H···A geometrija i kontekst. Za snažniju energetsku ili funkcionalnu tvrdnju mogu biti potrebni dodatni proračuni ili eksperimenti.

### 4. Nedostajući vodonik

CIF nema eksplicitne H atome. Kako aplikacija treba da prijavi odsustvo H-veza?

??? success "Odgovor"
    Ne kao dokazano odsustvo. Može pokušati kontrolisano dodavanje H na osnovu pouzdane hemijske strukture, ali mora čuvati da su položaji izvedeni i vratiti niži confidence ili status „nije procenjeno“ kada protonacija/bond typing nisu sigurni.

### 5. Stabilnost

Struktura A ima 12 geometrijskih H-bond kandidata, a B osam. Da li je A stabilnija?

??? success "Odgovor"
    To se ne može zaključiti iz broja. Kontakti se razlikuju po geometriji, partnerima, kooperativnosti i energetskim doprinosima, a stabilnost uključuje celokupnu rešetku, entropiju, temperaturu i druge forme.

### 6. Feature invarijantnost

Isti kontakt je u drugom CIF-u generisan operacijom broj 4 umesto broj 2. Da li feature treba da se promeni?

??? success "Odgovor"
    Ne ako je fizičko mapiranje isto. Indeks operacije je lokalni provenance podatak. Kanonski kontaktni deskriptor treba da zavisi od hemijskih partnera, geometrije i periodične topologije, a ne od redosleda operacija u fajlu.

## Kriterijum prolaza: drugi prolaz {#kriterijum-prolaza}

Poglavlje si savladao kada iz <code>cu_n14_a.cif</code> možeš da reprodukuješ N2-H2N···O2 geometrijski kandidat, navedeš tačnu simetrijsku operaciju i translaciju, objasniš zašto je to kandidat a ne automatski energetski dokaz i predložiš invarijantan zapis ivice za obe aplikacije.

## Primarni i autoritativni izvori

- [IUPAC preporuka: definicija vodonične veze](https://publications.iupac.org/pac/83/8/1637/index.html)
- [IUPAC preporuka: definicija halogene veze](https://publications.iupac.org/pac/85/8/1711/index.html)
- [IUCr Online Dictionary: crystal structure](https://dictionary.iucr.org/Crystal_structure)
- [IUCr teaching pamphlet 21: crystal packing](https://www.iucr.org/education/pamphlets/21)
- [CCDC Python API: crystals, packing i contacts](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/crystal.html)
- [CCDC Python API: packing similarity](https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/packing_similarity.html)
- [Etter, MacDonald i Bernstein: graph-set opis H-veza](https://doi.org/10.1107/S0108768189012929)
- [Bernstein i saradnici: graph-set analiza H-bond obrazaca](https://doi.org/10.1002/anie.199515551)
