import os,shutil

def removeemptydirs(dirpath):
    allfiles = os.listdir(dirpath)
    emptydirscount = 0
    for filename in allfiles:
        filepath = os.path.join(dirpath,filename)
        if os.path.isdir(filepath):
            if len(os.listdir(filepath)) < 20:
                print "Removing : " + filename
                shutil.rmtree(filepath)
                emptydirscount += 1

    print str(emptydirscount) + " empty folders found in and deleted from " + dirpath

path = "/home/birdbook/data/birdimages/"

removeemptydirs(path)

