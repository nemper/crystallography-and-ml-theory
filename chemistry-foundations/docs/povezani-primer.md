# Jedan primer: od hemijskog objekta do evaluacije

**Kako čitati:** ovo je matična strana nastavljenog primera. Prvi put pročitaj samo pitanje i objekte; ostalim koracima se vrati iz lekcija o reprezentacijama, parovima, pretrazi i evaluaciji. Preduslovi za račun su [geometrija](03-geometrija.md), [reprezentacije](14-reprezentacije.md) i [sličnost](15-slicnost.md).

!!! info "Isključivo nastavni podaci"
    Svi nazivi, grafovi, koordinate, ocene i rezultati na ovoj strani su izmišljeni za ručni račun. Ne opisuju N14, CSD zapis niti sadržaj bilo kog spoljnog fajla. Grafovi su pojednostavljeni fragmenti sa izostavljenim vodonicima; nisu potpune specifikacije stvarnih jedinjenja. Mali skup služi proveri postupka, a ne proceni statističke pouzdanosti.

## Pitanje i imenovani objekti {#objekti}

Tražimo kandidate koji dele označeno molekulsko jezgro sa upitom **Q**, uz slično prostorno uređenje tog jezgra. Posebno pitamo da li je slično i okruženje susednih molekula. To su dve odvojene tvrdnje.

| Objekat | Glavna komponenta | Dodatna komponenta | Značenje |
|---|---|---|---|
| Q | 4 teška atoma: C₁, N₂, O₃, C₄ | jedan predstavnik O dodatne komponente W | upit |
| Q* | isti atomi, veze i komponente kao Q, promenjen redosled i koordinatni okvir | ista W | drugi zapis istog fizičkog objekta |
| B | 5 teških atoma: odgovarajuće jezgro C₁, N₂, O₃ i dva dodatna C | odgovarajuća W | analog, sa stvarno promenjenim fragmentom i geometrijom |
| C | označeno jezgro dostupno u 2D pogledu | nema podataka potrebnih za periodično poređenje | relevantan kandidat za molekulsko pitanje |
| D | nema traženog označenog jezgra | nije bitno za ovaj upit | nerelevantan kandidat |

U Q su ivice glavne komponente C₁–N₂, C₁–O₃ i C₁–C₄. U B se tim ivicama dodaje C₄–C₅. Vrsta atoma i veza mora da se očuva u ovom profilu; prostorna blizina sama ne uspostavlja atomsku mapu. Dodatni O pripada drugoj komponenti i zato nije zamena za O₃ glavnog jezgra.

### Izvorni i namenski pogled

Izvorni nastavni opis Q čuva sve komponente, njihove veze, koordinate i oznaku porekla. **Namenski pogled** za poređenje jezgra bira C₁, N₂ i O₃, ali beleži da je iz glavne komponente izostavljen C₄, a iz celog objekta i W. Izostavljanje iz pogleda nije brisanje iz izvornog opisa.

| Pogled | Šta je dostupno | Dopušten zaključak |
|---|---|---|
| označeni 2D graf | Q, Q*, B, C i D | podudaranje motiva i grafovska pokrivenost |
| koordinate mapiranog jezgra | Q, Q* i B | RMSD tog jezgra nakon poravnanja |
| nastavna skica susednih centara | Q, Q* i B | razlika u navedenim položajima suseda |
| pun periodični eksperimentalni model | nijedan objekat ovog primera | nema stvarnog packing/COMPACK rezultata |

Za C je molekulsko pitanje ocenjivo, dok periodično ostaje **nije ocenjeno: nedostaje ulaz**. Taj status nije dokaz različitog pakovanja niti numerička nula. Nastavak: [izbor reprezentacije](14-reprezentacije.md#147-multimodalni-zapis-ne-jedna-magicna-reprezentacija).

## Najpre komponentna, zatim atomska mapa {#komponente}

Hemijska dozvoljenost se zadaje pre minimizacije troška:

| Q komponenta → B komponenta | Glavna B | Dodatna W u B |
|---|---|---|
| glavna Q | dozvoljeno poređenje zajedničkog jezgra | zabranjeno u ovom profilu |
| dodatna W u Q | zabranjeno u ovom profilu | dozvoljeno zasebno poređenje |

Zato je mapa glavna Q → glavna B i W → W. U glavnom paru biramo atomsku mapu C₁→C₁, N₂→N₂, O₃→O₃. Za ovaj namenski pogled C₄ u Q i C₄/C₅ u B ostaju van geometrijskog računa. Ovo nije tvrdnja da je pronađeno najveće moguće zajedničko jezgro: graf dopušta i četvrti atom, ali smo za ručnu geometriju unapred izabrali tri nekolinearna atoma.

Zašto se komponentna mapa traži globalno prikazuje [mala matrica dodele](19-parovi.md#globalna-dodela); izbor dopuštenog jezgra dodatno zavisi od [MCS varijante](19-parovi.md#mcs-varijante).

## Centriranje, poznata rotacija i ručni RMSD {#poravnanje}

Sva rastojanja su u Å. Koordinate jezgra Q su:

| Mapirani atom | Q | Q* | B |
|---|---|---|---|
| C₁ | (0; 0; 0) | (5; −1; 0) | (5; −1; 0) |
| N₂ | (2; 0; 0) | (5; 1; 0) | (5; 1,2; 0) |
| O₃ | (0; 2; 0) | (3; −1; 0) | (2,8; −1; 0) |

Poznata rotacija za kolona-vektore je

\[
R=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix},\qquad
t=(5,-1,0)^T,\qquad q_i^*=Rq_i+t.
\]

To je rotacija od 90° oko z-ose, sa determinantom +1, pa ne uključuje refleksiju. Za Q* se istim pravilom transformiše **ceo** fizički model, uključujući dodatnu komponentu i susede. Menjanje samo glavnog molekula unutar nepomerene okoline ne bi bilo isto prekodiranje kristala.

Težište mapiranog jezgra Q je \(\bar q=(2/3,2/3,0)\). Njegove centrirane koordinate su:

\[
p_1=(-2/3,-2/3,0),\quad p_2=(4/3,-2/3,0),\quad
p_3=(-2/3,4/3,0).
\]

Težište Q* je \((13/3,-1/3,0)\). Posle oduzimanja tog težišta i primene \(R^T\), Q* daje upravo \(p_i\). Zato je **RMSD(Q,Q*) = 0 Å**, uz poznatu mapu svih izabranih atoma. To proverava ekvivalentnost zapisa.

U B je jezgro uvećano za faktor 1,1 pre iste rotacije i translacije: \(b_i=R(1,1q_i)+t\). Njegovo težište je \((64/15,-4/15,0)\). Posle centriranja i povratne rotacije dobijamo \(1,1p_i\); preostala odstupanja su \(0,1p_i\). U poravnanju ne dopuštamo skaliranje, jer bi ono sakrilo stvarnu geometrijsku razliku.

\[
\sum_i\|p_i\|^2=8/9+20/9+20/9=16/3,
\]
\[
\mathrm{RMSD}(Q,B)=\sqrt{\frac{1}{3}\sum_i\|0,1p_i\|^2}
=\sqrt{\frac{1}{100}\frac{16}{9}}=\frac{2}{15}\approx0,1333\ \text{Å}.
\]

Ovde je poznata povratna rotacija i optimalna rigidna rotacija za ovaj uniformno uvećani, centrirani trougao. Najveće pojedinačno odstupanje je \(\sqrt{20}/30\approx0,1491\) Å. Nizak RMSD govori samo o ovim mapiranim atomima.

### Pokrivenost ima dve strane i imenovan obuhvat

| Mera za Q–B | Q strana | B strana |
|---|---:|---:|
| geometrijski mapirano jezgro / teški atomi glavne komponente | 3/4 = 75% | 3/5 = 60% |
| isto jezgro / teški atomi celog opisa sa W | 3/5 = 60% | 3/6 = 50% |
| komponentno dodeljene komponente / sve komponente | 2/2 | 2/2 |

Komponentna dodela W→W ne dodaje automatski W u RMSD jezgra. Potpuno poklapanje Q–Q* može se proveriti nad svim atomima; račun iz tabele koordinata pokazuje samo tri izabrana. Nastavak: [tumačenje RMSD-a](15-slicnost.md#154-rmsd-i-geometrijska-slicnost) i [poređenje parova](19-parovi.md#geometrijsko-poredenje).

## Molekul i njegovo okruženje

Zamisli susedne molekulske centre u okviru poravnatog jezgra Q na pomerajima (4;0;0) i (0;4;0), a u B na (4;0;0) i (0;5;0) Å. Jedan pomeraj je isti, drugi se razlikuje za 1 Å. U Q* se oba suseda rotiraju i transliraju zajedno sa Q i posle povratne transformacije ostaju ista.

Ovo pokazuje zašto slična molekulska geometrija ne određuje raspored suseda. **Dva centra nisu periodični kristalni klaster, a ova skica nije COMPACK proračun.** Za jači zaključak nedostaju kompletne molekulske orijentacije, ćelija, simetrija, politika klastera i validirano poređenje. Jedan izmereni pomeraj ne dokazuje polimorfizam.

## Jedan uspešan par i jedan propušten kandidat {#kandidati}

Za nastavno molekulsko pitanje stručna rubrika dodeljuje B ocenu **2** (najrelevantniji), C ocenu **1** (relevantan) i D ocenu **0**. Ocene su zadate za vežbu, nisu rezultat stvarne ekspertize. Sva tri kandidata su ocenjena; pozitivna relevantnost znači ocena > 0. Q* se ne broji kao nezavisna struktura u evaluacionom korpusu.

Pretpostavimo da iscrpna pretraga izabranog deskriptora daje top-2 **[B,C]**, a kandidatski indeks vraća **[B,D]**. Naknadno rangiranje uspešno stavlja B na prvo mesto, a poređenje Q–B iz prethodnog koraka daje RMSD 0,1333 Å sa navedenom pokrivenošću. C se nije našao među kandidatima; rangiranje ne može da vrati kandidata koji mu nije dostavljen.

| Mera | Ručni račun | Imenilac |
|---|---|---|
| infrastrukturni Recall@2 | \(\lvert\{B,D\}\cap\{B,C\}\rvert/2=1/2\) | exact top-2 iste reprezentacije i metrike |
| ekspertski candidate Recall@2 | \(\lvert\{B,D\}\cap\{B,C\}\rvert/2=1/2\) | svi relevantni kandidati u ovom ocenjenom korpusu |
| end-to-end Recall@1 | \(\lvert\{B\}\cap\{B,C\}\rvert/2=1/2\) | svi relevantni kandidati |
| Precision@2 konačne liste [B,D] | 1/2 | dva prikazana mesta |

Brojevi prva dva reda su slučajno jednaki: exact lista potiče iz deskriptora, a ekspertski relevantan skup iz rubrike. U drugom upitu ti skupovi mogu biti različiti. Atomska pokrivenost 3/4 ili 3/5 iz geometrije nema isti imenilac ni značenje kao candidate recall. Nastavak: [globalna pretraga](18-globalna-pretraga.md) i [učenje rangiranja](https://github.com/nemper/crystallography-and-ml-theory/blob/main/ml-ai-strategy/docs/03-global-retrieval-ann-ranking.md).

## Šta bi evaluacija morala da proveri {#evaluacija}

Za ovaj upit razlikujemo uspešno ocenjen par Q–B od propuštenog relevantnog C i neocenjenog periodičnog nivoa. Za generalizaciju su potrebni dodatni nezavisni upiti/familije; Q i Q* uvek ostaju u istoj grupi. Model, njegov kalibrator i pragovi biraju se pre završnog testa.

Vežba proverava da li su brojioci, imenioci, mapa i naučno pitanje dosledni. **Jedan upit i jedan geometrijski par ne određuju interval pouzdanosti niti dokazuju superiornost metode.** Za sledeći korak pročitaj [grupno resamplovanje](20-evaluacija.md#grupno-resamplovanje), a zatim [ML evaluaciju](https://github.com/nemper/crystallography-and-ml-theory/blob/main/ml-ai-strategy/docs/06-metric-learning-and-evaluation.md).
