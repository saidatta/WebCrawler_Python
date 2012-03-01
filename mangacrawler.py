from BeautifulSoup import BeautifulSoup # need to change to bs4. check it again.
import urllib2, urllib
from urllib import urlretrieve
from urllib2 import urlopen 
import os
import sys
#import uti

# Global Variables. 
target_url = 'http://mangareader.net'
target_info = 'gantz' #target - case sensitive, Tried Gantz but throwed an error.
user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.02011-10-16 20:21:42'
headers = { 'User_Agent' : user_agent } # a dict. for the user agent.
directory = 'C:/Users/Venkata/Desktop/Crawler_Manga' # where I am going to download my info.
startPt = 1 #which chapter you want to start from.
last = 0

#lists for mangas.
urlChapters = [] # list of urls.
urlChapter = [] # url of current chapter.
urlImage = [] # list of images.

request = urllib2.Request(target_url+'/'+ target_info, headers = headers)
response = urllib2.urlopen(request)
doc = response.read()
#print doc ### prints the source of the page.
soupDoc = BeautifulSoup(doc) # soup to parse the html.
#soup = soup.prettify()

# resource from http://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautiful-soup
#'a' for all the items, then href for the links.
links = soupDoc.findAll('a') #making a list of all Links on manga.

#print links

for link in links:
	#print link
	urlChapters.append(target_url+link['href']) #href - relates the links (look at page source)
	
def getChapter(url):
	'''
	A method to get all the usable links to later parse only the images.
	'''
	print url
	chapterurl = url #the url of the chapter.
	reqChapter = urllib2.Request(chapterurl,headers = headers)#requesting.
	responseChapter = urllib2.urlopen(reqChapter) #returns the request. 
	# Format: <addinfourl at 44207160 whose fp = <socket._fileobject object at 0x02A23D30>>  
	chapter = responseChapter.read() # the whole webpage source code
	#Format: <!DOCTYPE ...... 
	soup = BeautifulSoup(chapter)
	
	soupLinks = soup.findAll('option')# making a list of all links on the given type.
	#Format: <option value="/air-gear/339/2">2</option> - get all the option values.
	for link in soupLinks:
		urlChapter.append(link['value'])

def getChapterImage(url):
	'''
    Creates the list of all the URIs from the images, so we can later download them.
    '''
	urlImg = url
	requestImg = urllib2.Request(urlImg, headers = headers)
	responseImg = urllib2.urlopen(requestImg)
	documentImg = responseImg.read()
	soupImg = BeautifulSoup(documentImg)
	linksImg = soupImg.findAll('img')# print linksImg
	for link in linksImg:
		urlImage.append(link['src'])
	#responseChapter = urllib2.urlopen(reqChapter) #returns the request
'''
    We need to check if the directory exists before trying to create them.
'''
def save(path):
    name = path
    name2 = name.split('/')#the pathname after the split.
    dir = directory+target_info+'/'#adding the target manga with the / at the end.
    dirChapter = dir+name2[-1]+'/'
    if not os.path.exists(dir):
        os.mkdir(dir)
    if not os.path.exists(dirChapter):
        os.mkdir(dirChapter)
    return dirChapter

startPt += 20
temp = urlChapters[startPt:] # a new list by removing all the inital header junk.
finalLinks = temp[:(len(temp)-8)]

for link in finalLinks:
	#print link,'\n'
	targetfolder = save(link) #dirtarget
	#getChapter(link)
	#getChapterImage(link)
	urlChapter = []
    # We now get the list of urls from the Chapter and loop again inside them.
	getChapter(link)
	for urls in urlChapter:
		# Here we grab the image URL and create a complete URL
		getChapterImage(target_url+urls)
        # Defines where it will be stored
        saveDir = os.path.join(targetfolder, urlImage[-1].split('/')[-1])
        if not os.path.exists(saveDir):
            # And so we download it!
            urlretrieve(urlImage[-1], saveDir)
            print urlImage[-1], "saved in:", saveDir
        else:
            # Check if the download it's a Zero-Sized / Broken file.
            if int(urllib.urlopen(urlImage[-1]).info()['Content-Length']) == os.stat(saveDir).st_size:
                # redundant download.
                print urlImage[-1], " - Redundant (Already done)."
            else:
				#Size the arrays.
                print "Global Length: ", int(urllib.urlopen(urlImage[-1]).info()['Content-Length']) 
                print "Local Length:", os.stat(saveDir).st_size
                urlretrieve(urlImage[-1], saveDir)
                print urlImage[-1], "downloading again."
	



	
