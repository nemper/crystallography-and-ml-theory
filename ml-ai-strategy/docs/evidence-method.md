# Metod dokaza i validacije

## Lokalni scope i opšta teorija imaju različite izvore

Za pitanje **šta ovaj projekat traži i šta njegovi primeri sadrže**, polazni dokaz su `2CDC/dve funkcionalnosti.txt`, dostavljeni white paper i konkretni lokalni fajlovi. Online rad ne može dokazati sadržaj nepročitanog lokalnog CIF-a, razlog članstva u search grupi ili prava konkretnog korisnika. Za pitanje **kako algoritam radi i pod kojim uslovima tvrdnja važi**, koriste se primarni i zvanični izvori ispod.

Provera dokumentacije nije isto što i reprodukcija algoritma ili benchmark nad punim CSD-om. Pregled citiranih radova ograničava tvrdnje na njihov target, korpus i protokol; neuspešan pristup stranici ne dokazuje da je citat netačan, ali ni da je njegov sadržaj nezavisno potvrđen.

## Hijerarhija izvora

Tvrdnje se proveravaju sledećim redom:

1. standard, normativna dokumentacija ili zvanična specifikacija;
2. originalni rad koji uvodi algoritam;
3. nezavisan benchmark ili reprodukciona studija;
4. zvanična implementaciona dokumentacija;
5. pregledni rad za mapu oblasti, ne kao jedini dokaz superiornosti.

Blogovi, vendor benchmark bez punog protokola i leaderboard broj bez kompatibilnog split-a služe samo kao trag za dalju proveru.

## Oznake tvrdnji

Za svaku važnu preporuku treba moći odrediti jednu od sledećih vrsta; oznake su auditni rečnik za pisanje i proveru, ne obavezni prefiksi u svakom modulu:

- **EVIDENCE** — direktno podržana citiranim izvorom pod navedenim uslovima;
- **INFERENCE** — razumna sinteza više izvora, uz jasno navedene pretpostavke;
- **PROPOSAL** — lokalna arhitektonska ili eksperimentalna odluka koju tek treba testirati;
- **UNKNOWN** — nema dovoljno podataka ili licence/runtime-a da se tvrdnja proveri.

## Pravilo poređenja

„Model X je najbolji“ nije prihvatljiva rečenica bez:

- zadatka i target definicije;
- korpusa, vremenskog snapshot-a i dozvola;
- split jedinice i leakage kontrole;
- baseline-a i jednakog budžeta za tuning;
- metrike, intervala poverenja i kritičnih slice-ova;
- latencije/hardvera i neuspešnih ulaza;
- verzije reprezentacije i softvera.

Ova dokumentacija zato daje **shortlist i decision gates**, a ne marketinški rang modela.
