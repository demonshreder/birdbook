import os


def countfilesinsbubdir(rootdirpath):
    count = 0
    for root, dirs, files in os.walk(rootdirpath):
        for dir in dirs:
            dirpath = os.path.join(rootdirpath, dir)
            filesindir = os.listdir(dirpath)
            if len(filesindir)<25:
                count += 1
                print str(dir) + " : " + str(len(filesindir))

    return count


rootdirpath = "/home/birdbook/data/birdimages/"
count = countfilesinsbubdir(rootdirpath)

print "\n"
print "Total number of directories : " + str(count)


