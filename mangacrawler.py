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

#lists for mangas.
urlChapters = [] # list of urls.
urlChapter = [] # url of current chapter.
urlImage = [] # list of images.

request = urllib2.Request(target_url+'/'+ target_info, headers = headers)
response = urllib2.urlopen(request)
doc = response.read()
#print doc ### prints the source of the page.
soup = BeautifulSoup(doc) # soup to parse the html.
#soup = soup.prettify()

# resource from http://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautiful-soup
#'a' for all the items, then href for the links.
links = soup.findAll('a') #making a list with all Links on manga.

print links

for link in links:
	urlChapters.append(target_url+link['href']) #href - relates the links (look at page source)
	
	

