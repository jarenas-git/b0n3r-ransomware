from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import os

class KeyLocker():
    def __init__(self):
        self.key=None
        self.key_path = os.environ['USERPROFILE'] + "\\Documents\\b0n3rk3yZ-DONOTDELETE\\"
    def generate_folderkey(self):
        if os.path.exists(self.key_path):
            pass
        else:
            os.mkdir(self.key_path)
    def generate_keys(self):
        self.key = RSA.generate(2048)

        #If you wanna write to file.
        # with open(self.key_path+"privb0n3r.pem","wb") as fpr:
        #     fpr.write(self.key.export_key())
        # # with open(self.key_path+"pubb0n3r.pem","wb") as fpb:
        # #     fpb.write(self.key.publickey().export_key())
    def encrypt(self,data):
        cipher = PKCS1_OAEP.new(self.key)
        return cipher.encrypt(data)
    def decrypt(self,data):
        cipher = PKCS1_OAEP.new(self.key)
        return cipher.decrypt(data)
