# Flight Tracker 

## Opis projekta 
 
Flight Tracker je web aplikacija koja prati prolazne letove i njihove završne destinacije sa jednog aerodroma. U aplikaciji se može dodavati više destinacija, nebitno u kojoj državi i u kojem gradu. 
U aplikaciji koristimo CRUD operacije za dodavanje,brisanje,izmjenu i pregled letova i njihovih odredišta.

## Prikaz funkcionalnosti
  * Prikaz svih letova i destinacija
  * Sortiranje letova i destinacija po različitim kriterijima (ID, datum polaska, trajanje, dužina, destinacija, naziv, grad, država)
  * Forme za uređivanje i brisanje letova i destinacija
  * Forma za unos novih destinacija sa poljima za naziv i državu
  * Forma za unos novog leta sa 
  * Navigation bar -> za vraćanje na početnu stranicu (Home page), dodavanje novih letova i destinacija
  * Brisanje letova i destinacija

## Pokretanje aplikacije 
Preuzimanje sa Github-a:

```bash
cd ~/Downloads
git clone https://github.com/budicmarin/projektInf
cd projektInf
```
Docker:
```bash
docker build -t flight .
docker run -p 5000:5000 flight
```

### Pristup aplikaciji
U pregledniku upišite http://localhost:5000 ili preko terminala možete taj isti link otvoriti.
