import urllib.request
# from BeautifulSoup import *
from bs4 import BeautifulSoup
urlname = input('Enter the url: ')
htmldoc = urllib.request.urlopen(urlname).read()
soup = BeautifulSoup(htmldoc, 'html.parser')
# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes
tags = soup('a')
for tag in tags:
    print (tag.get('href', None))
