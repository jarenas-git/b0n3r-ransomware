#FIRST
from Crypto.PublicKey import RSA
import os
def generate_keys(key_path):
    #Create keys directory
    if os.path.exists("keys"):
        pass
    else:
        os.mkdir("keys")

    #Generate Server RSA keys. (Server side)
    key = RSA.generate(2048)
    with open(key_path + "sprivb0n3r.pem", "wb") as fpr:
        fpr.write(key.export_key())
        print("Finish writing your privkey")
    with open(key_path + "spubb0n3r.pem", "wb") as fpb:
        fpb.write(key.publickey().export_key())
        print("Finish writing your pubkey")
        print(key.publickey().export_key())



generate_keys("keys\\")

