pip install pycryptodome typer
echo
echo "> Inicjalizacija alata Glavnom Zaporkom: '1234'"
echo NAREDBA: python3 password_manager.py init 1234
python3 password_manager.py init 1234
echo
echo "> Ponovna inicijalizacija alata"
echo NAREDBA: python3 password_manager.py init 1234
python3 password_manager.py init 1234
echo
echo "> Spremanje lozinke: '3333' za adresu: 'fer.hr'"
echo NAREDBA: python3 password_manager.py put 1234 fer.hr 3333
python3 password_manager.py put 1234 fer.hr 3333
echo
echo "> Spremanje lozinke: '2222' za adresu: 'google.com'"
echo NAREDBA: python3 password_manager.py put 1234 google.com 2222
python3 password_manager.py put 1234 google.com 2222
echo
echo "> Spremanje lozinke: '5555' za adresu: 'yahoo.com'"
echo NAREDBA: python3 password_manager.py put 1234 yahoo.com 5555
python3 password_manager.py put 1234 yahoo.com 5555
echo
echo "> Dohvacanje lozinke za adresu: 'fer.hr'"
echo NAREDBA: python3 password_manager.py get 1234 fer.hr
python3 password_manager.py get 1234 fer.hr
echo
echo "> Dohvacanje lozinke za adresu: 'ffzg.hr' (nije spremljena lozinka)"
echo NAREDBA: python3 password_manager.py get 1234 ffzg.hr
python3 password_manager.py get 1234 ffzg.hr
echo
echo "> Dohvacanje lozinke za adresu: 'fer.hr' neispravnom glavnom zaporkom"
echo NAREDBA: python3 password_manager.py get 1111 fer.hr
python3 password_manager.py get 1111 fer.hr
echo
echo "> Spremanje lozinke: '2222' za adresu: 'fer.hr' neispravnom glavnom zaporkom"
echo NAREDBA: python3 password_manager.py put 1111 fer.hr 2222
python3 password_manager.py put 1111 fer.hr 2222
echo
echo "> Spremanje lozinke: '2222' za adresu: 'fer.hr' ispravnom glavnom zaporkom"
echo NAREDBA: python3 password_manager.py put 1234 fer.hr 2222
python3 password_manager.py put 1234 fer.hr 2222
echo
echo "> Dohvacanje lozinke za adresu: 'fer.hr' (promijenjena stara lozinka novom)"
echo NAREDBA: python3 password_manager.py get 1234 fer.hr
python3 password_manager.py get 1234 fer.hr
echo
echo "> Ponovna inicjalizacija lozinkom: '0000'"
echo NAREDBA: python3 password_manager.py reinit 1234 0000
python3 password_manager.py reinit 1234 0000
echo
echo "> Resetiranje'"
echo NAREDBA: python3 password_manager.py reset 0000
python3 password_manager.py reset 0000

