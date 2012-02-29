import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("http://projecteuler.net/problem=373")
soup = BeautifulSoup(page)
#print soup.html.head

#print soup.findAll(['triangle', 'p'])
print soup.findAll(align="center")

#print soup.td.extract()
#print soup.prettify()

'''
Get the user's input: the starting URL and the desired 
file type. Add the URL to the currently empty list of 
 URLs to search. While the list of URLs to search is 
 not empty,
  {
    Get the first URL in the list.
    Move the URL to the list of URLs already searched.
    Check the URL to make sure its protocol is HTTP 
       (if not, break out of the loop, back to "While").
    See whether there's a robots.txt file at this site 
      that includes a "Disallow" statement.
      (If so, break out of the loop, back to "While".)
    Try to "open" the URL (that is, retrieve
     that document From the Web).
    If it's not an HTML file, break out of the loop,
     back to "While."
    Step through the HTML file. While the HTML text 
       contains another link,
    { 
       Validate the link's URL and make sure robots are 
    allowed (just as in the outer loop).
     If it's an HTML file,
       If the URL isn't present in either the to-search 
       list or the already-searched list, add it to 
       the to-search list.
         Else if it's the type of the file the user 
         requested,
            Add it to the list of files found.
    }
  }
'''