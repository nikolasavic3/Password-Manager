import typer
import os
from Crypto.Cipher import  AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

app = typer.Typer()

@app.command(help="initialise the password manager with a Master Password")
def init(master_password: str):
    path_to_master_password_flie = pm.master_password_file
    if not pm.checkIfFileEmpty(path_to_master_password_flie):
        print("The Master Password is already initilaised!")
    else:
        pm.initialise(master_password)
@app.command(help="look up the stored password for an adress")
def get(master_password: str, adress: str):
    pm.getPassword(master_password, adress)
@app.command(help="store a password for an adress")
def put(master_password: str, adress: str, password: str):
    pm.storePassword(master_password, adress, password)
@app.command()
def reinit(old_master_password: str, new_master_password: str):
    if pm.verifyMasterPassword(old_master_password):
        pm.initialise(new_master_password)
    else:
        print("You have enterd the incorrect Master Password")
@app.command()
def reset(master_password: str):
    if pm.verifyMasterPassword(master_password):
        pm.reset()
    else:
        print("You have enterd the incorrect Master Password")


class PasswordManager:
    def __init__(self) -> None:
        self.master_password_file = "tag.key"
        self.stored_passwords_file = "stored_passwords_file.key"

    def reset(self):
        with open(self.master_password_file, "wb") as f_master:
            f_master.write(b"")
            with open(self.stored_passwords_file, "wb") as f:
                f.write(b"")
                print("reseted")
        return

    def initialise(self, master_password) -> None:
        #key derivation
        salt = get_random_bytes(16)
        derived_key = scrypt(master_password, salt,16, N=2**14, r=8, p=1)
        #tag
        cipher = AES.new(derived_key, AES.MODE_EAX)
        cipherd_password, tag = cipher.encrypt_and_digest(str.encode(master_password))
        tag_nonce_salt = tag + b" | " + cipher.nonce + b" | " + salt
        with open(self.master_password_file, "wb") as f_master:
            f_master.write(tag_nonce_salt)
            with open(self.stored_passwords_file, "wb") as f:
                f.write(b"")
                print("Password  Manager Initialised!")
        return

    def verifyMasterPassword(self, master_password_to_check : str) -> bool:
        with open(self.master_password_file, "rb") as f_in:
            tag, nonce, salt = f_in.read().split(b" | ")
            secret_key = scrypt(master_password_to_check, salt, 16, N=2**14, r=8, p=1)
            cipher = AES.new(secret_key, AES.MODE_EAX, nonce)
            cipherd_password, tag2 = cipher.encrypt_and_digest(str.encode(master_password_to_check))
            if tag == tag2:
                return True
            else:
                print("You have enterd the incorrect Master Password or the integrity check failed.")
                return False
    
    def deleteWithVerification(self, master_password,adress) -> None:
        passwordVerificationValue = self.verifyMasterPassword(master_password)
        if not passwordVerificationValue:
            print("Password was was not deleted")
        else:
            self.deletePassword(adress)
        

    def deletePassword(self, adress_to_delete) -> None:
        with open(self.stored_passwords_file, "rb") as f_in:
            file_text = f_in.read()
            file_lines = file_text.split(b" ||| ")
            d = False
            if len(file_lines[-1]) == 0:
               file_lines.pop() 
            #hash adress to check
            adress_hash_to_delete = SHA256.new(str.encode(adress_to_delete))
            adress_hash_to_delete_string = str.encode(adress_hash_to_delete.hexdigest())
            with open(self.stored_passwords_file, "wb") as f_out:    
                for line in file_lines:
                    adress , _, _ , _ , _ = line.split(b" | ")
                    if adress_hash_to_delete_string != adress:
                        f_out.write(line + b" ||| ")
                    else:
                        d = True
                        print(f"Adress {adress_to_delete} has been deleted.")
            if d == False:
                print(f"Adress {adress_to_delete} is not stored.")

            


    def storePassword(self, master_password : str, adress : str, password : str) -> bool:
        passwordVerificationValue = self.verifyMasterPassword(master_password)
        if not passwordVerificationValue:
            print("Password was not stored")
            return False
        #check if password is for site exists if yes sotre new
        if self.checkIfPasswordForAdressExists(adress):
            self.deletePassword(adress)
        #hash adress
        adress_hash = SHA256.new(str.encode(adress))
        adress_hash_string = adress_hash.hexdigest()
        adress_hash_string_bytes = str.encode(adress_hash_string)
        #encrypt password
        salt = get_random_bytes(16)
        secret_key = scrypt(master_password, salt, 16, N=2**14, r=8, p=1)
        cipher = AES.new(secret_key, AES.MODE_EAX)
        cipherd_password, tag = cipher.encrypt_and_digest(str.encode(password))
        #store adress, cipherd password, salt, and nonce
        with open(self.stored_passwords_file, "ab") as f_in:
            adress_and_cipherdpassword_and_and_salt_and_nonce = adress_hash_string_bytes + b" | " + cipherd_password + b" | "+ tag +  b" | " + salt + b" | " + cipher.nonce + b" ||| "
            f_in.write(adress_and_cipherdpassword_and_and_salt_and_nonce)
            print(f"Stored password {password} for adress {adress}.")
            return True

    def fetch_password(self, master_password, cipher_password, tag, salt, nonce) -> str:
        #decrypt password
        secret_key = scrypt(master_password, salt, 16, N=2**14, r=8, p=1)
        cipher = AES.new(secret_key, AES.MODE_EAX, nonce)
        password =  cipher.decrypt(cipher_password)
        #check validity
        try:
            cipher.verify(tag)
            return password.decode()
        except ValueError:

            print(f"Verification of stored data integrity unsuccessful")
            return ""

    def checkIfPasswordForAdressExists(self, adress):
        #search inside file if passwords match
        with open(self.stored_passwords_file, "rb") as f_in:
            file_text = f_in.read()
            file_lines = file_text.split(b" ||| ")
            if len(file_lines[-1]) == 0:
               file_lines.pop() 
            #hash adress to check
            adress_hash_to_check = SHA256.new(str.encode(adress))
            adress_hash_to_check_string = str.encode(adress_hash_to_check.hexdigest())

            for line in file_lines:
                adress , cipher_password, tag , salt , nonce = line.split(b" | ")
                if adress_hash_to_check_string == adress:
                    return True
        return False

    def tryToGetPassword(self, master_password: str, adress_to_check: str) -> str:
        #search inside file if passwords match
        with open(self.stored_passwords_file, "rb") as f_in:
            file_text = f_in.read()
            file_lines = file_text.split(b" ||| ")
            if len(file_lines[-1]) == 0:
               file_lines.pop() 
            #hash adress to check
            adress_hash_to_check = SHA256.new(str.encode(adress_to_check))
            adress_hash_to_check_string = str.encode(adress_hash_to_check.hexdigest())

            for line in file_lines:
                adress , cipher_password, tag , salt , nonce = line.split(b" | ")
                if adress_hash_to_check_string == adress:
                    return self.fetch_password(master_password, cipher_password, tag, salt, nonce)
        print(f"The password for: {adress_to_check} is not stored.")
        return ""


    def getPassword(self, master_password: str, adress: str) -> None:
        passwordVerificationValue = self.verifyMasterPassword(master_password)
        if not passwordVerificationValue:
            print("Password was was not retrived.")
            return False
        password = self.tryToGetPassword(master_password, adress)
        if len(password) > 0:
            print(f"The password for adress {adress} is {password}.")
    
    def checkIfFileExists(self, path):
        return os.path.isfile(path)
    
    def checkIfFileEmpty(self, path):
        return os.path.getsize(path) == 0
    
# if __name__ == "__main__":
#     pm = PasswordManager()
#     app()