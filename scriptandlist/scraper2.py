# import libraries
import urllib2, urllib, os, sys
from bs4 import BeautifulSoup


def getlist(filename):
    with open(filename, 'r') as inputfile:
        return inputfile.readlines()


data_root_directory = "/home/birdbook/data/birdimages/"

birdlist = getlist("birdlist2.txt")
for bird in birdlist:
    if len(bird) > 3:
        pass
    bird = bird.rstrip()
    bird = bird.replace("'","")
    bird = bird.replace("-"," ")
    print "Trying bird :" + bird 
    
    # bird = bird[0:bird.index("(")]
    # bird = bird.rstrip()
    # check if directory exists for the bird and create one if it doesn't exist

    # cont_response = raw_input("Enter Y to continue for bird : " + bird + " and Q to quit\n")

    # if cont_response == "Q":
    #    sys.exit(3)

    if not os.path.isdir(data_root_directory + bird):
        os.makedirs(data_root_directory + bird)

    count = 0

    try:
        birdforlink = bird.replace(" ", "%20")

        for i in range(1, 7):
            url = "http://www.indianaturewatch.net/view_cat.php?tag=" + birdforlink + "&page=" + str(i)

            # query the website and return the html to the variable 'page'
            page = urllib2.urlopen(url)

            # parse the html using beautiful soup and store in variable `soup`
            soup = BeautifulSoup(page, 'html.parser')

            for link in soup.find_all('img'):
                pagelink = link.get('src')

                if "images/album" in str(pagelink):
                    count += 1
                    imgurl = ("http://indianaturewatch.net/" + str(pagelink).replace("thumb", "photo"))

                    urllib.urlretrieve(imgurl, data_root_directory + bird + "/" + str(count) + ".jpg")

                    print "Downloaded : " + bird + " : " + str(count) + " : " + imgurl
    except:
        pass
