PASSWORD MANAGER

Ovaj alat za pohranu i upravljanje lozinkama koristi AES enkripciju za kriptiranje lozinki i SHA-256 kao funkciju sažetka (hash) za pohranjivanje adresa. Za stvaranje tajnog kluča potrebnog za enkripciju lozinki korištena je funkcija derivacije ključa 'scrypt'.

Ostvareni sigurnosi zahtjevi:
1. Povjerljivost zaporki
AES Enkripcija: Korištenje AES enkripcije u EAX modu za kriptiranje lozinki osigurava visoku razinu povjerljivosti. EAX mod pruža autentificiranu enkripciju koja osigurava povjerljivost, integritet podataka, i zaštitu od ponovnih napada. Budući da je ključ za AES enkripciju izveden iz glavne lozinke pomoću scrypt, napadač ne može dekriptirati lozinke bez poznavanja glavne lozinke.
 
2. Povjerljivost adresa
SHA-256 Hashiranje: Za adrese se koristi hashiranje pomoću SHA-256 funkcije sažetka. Ovo osigurava da se u bazi podataka ne pohranjuju originalne adrese, već samo njihovi hash-evi.

3. Integritet adresa i zaporki
Autentifikacija Enkripcijom: Korištenje autentificirane enkripcije (AES u EAX modu) znači da se uz svaku enkriptiranu lozinku generira i autentifikacijska oznaka (tag), koja se koristi za verifikaciju integriteta lozinke pri dekriptiranju. To osigurava da se zaporka ne može promijeniti bez detekcije, također se time sprječava "napad zamijene", gdje bi napadač mogao zamijeniti lozinku određene adrese s lozinkom druge adrese.


Potrebno instalirati prije korištenja pakete:
pip install pycryptodome typer

Korištenje:

Za inicijalizaciju alata s glavnom zaporkom:
python3 password_manager.py init "vaša_glavna_zaporka"

Za pohranu lozinke za specifičnu adresu:
python3 password_manager.py put "vaša_glavna_zaporka" "adresa" "lozinka"

Za dohvaćanje pohranjene lozinke za adresu:
python3 password_manager.py get "vaša_glavna_zaporka" "adresa"

Za ažuriranje glavne zaporke:
python3 password_manager.py reinit "stara_glavna_zaporka" "nova_glavna_zaporka"

Za resetiranje alata:
python3 password_manager.py reset "vaša_glavna_zaporka"

Za pomoć:
python3 password_manager.py --help