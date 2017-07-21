import os, hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def removedups(dirpath):
    allfiles = os.listdir(dirpath)
    hashset = set()
    dupscount = 0
    for filename in allfiles:
        filepath = os.path.join(dirpath,filename)
        checksum = md5(filepath)
        if not checksum in hashset:
            hashset.add(checksum)
        else:
            print "Removing file : " + filepath
            dupscount += 1
            os.remove(filepath)
    print str(dupscount) + " duplicates found in " + dirpath

path = "/home/birdbook/data/birdimages/"

allbirdfolders = os.listdir(path)

for folder in allbirdfolders:
    print "Folder : " + folder
    folderpath = os.path.join(path,folder)
    removedups(folderpath)
