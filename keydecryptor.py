from Crypto.PublicKey import RSA
from decryptor import Decryptor

with open("keys\\sprivb0n3r.pem", "rb") as f:
    private_key = RSA.import_key(f.read())
dec_key = Decryptor(private_key,"keys")
dec_key.decrypt_all()




