from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from getfiles import deleteFile
from Crypto.Util.Padding import pad,unpad
import os


class Decryptor():
    def __init__(self,key,dir):
        self.ckey = key
        self.dir = dir

    def get_files(self):
        file_list = []
        for dir, _, files in os.walk(self.dir):
            for file in files:
                file_ext = os.path.splitext(file)[-1]
                if file_ext==".b0n3r":
                    file_list.append([os.path.join(dir,file)])
                elif file_ext==".b0n3r0":

                    multifile = map(lambda x:os.path.join(dir,x),filter(lambda x:os.path.splitext(x)[0]==os.path.splitext(file)[0],os.listdir(dir)))

                    #Does the same thing, easier to read.
                    # multifile=[]
                    # for item in os.listdir(dir):
                    #     if os.path.splitext(item)[0]==os.path.splitext(file)[0]:
                    #         multifile.append(os.path.join(dir,item))
                    #     else:
                    #         continue
                    file_list.append(sorted(multifile))
        return file_list

    def decrypt(self,file):
        try:
            with open(file,"rb") as fenc:
                content = fenc.read()
        except Exception as e:
            print(e)
            print("An error has occured. Cannot read" + file)
        to_decrypt = content[0:-272]
        iv= content[-272:-256]
        aeskey = content[-256::]
        c = PKCS1_OAEP.new(self.ckey)
        csym = AES.new(c.decrypt(aeskey), AES.MODE_CBC, iv)
        return unpad(csym.decrypt(to_decrypt),16)

    def decrypt_all(self):
        for files in self.get_files():
            for file in files:
                try:
                    with open(os.path.splitext(file)[0],"ab") as f:
                        f.write(self.decrypt(file))
                    print("Decrypted: "+file)
                except Exception as e:
                    print(e)
                    print("An exception has occured. Cannot write decrypted data.")
                else:
                    os.remove(file)

if __name__=="__main__":
    try:
        with open(os.environ['USERPROFILE'] + "\\Documents\\b0n3rk3yZ-DONOTDELETE\\privb0n3r.pem", "rb") as f:
            private_key = RSA.import_key(f.read())
    except Exception as e:
        print(e)
    decryptor = Decryptor(private_key,os.environ['USERPROFILE'])
    decryptor.decrypt_all()

