import urllib.request
# from BeautifulSoup import *
from bs4 import BeautifulSoup

urlname = input('Enter file name: ')
if(urlname == ''):
    urlname = 'http://python-data.dr-chuck.net/comments_42.html'
fopen = urllib.request.urlopen(urlname).read()

soup = BeautifulSoup(fopen, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('span')
print(tags)
nums = list()
for tag in tags:
    # Look at the parts of a tag
    print ('TAG:',tag)
    print ('URL:',tag.get('span', None))
    print ('Contents:',tag.contents[0])
    nums.append(int(tag.contents[0]))
    print ('Attrs:',tag.attrs)
print(sum(nums))
#
# import urllib.request
# # from BeautifulSoup import *
# from bs4 import BeautifulSoup
# urlname = input('Enter the url: ')
# htmldoc = urllib.request.urlopen(urlname).read()
# soup = BeautifulSoup(htmldoc, 'html.parser')
# # Retrieve a list of the anchor tags
# # Each tag is like a dictionary of HTML attributes
# tags = soup('a')
# count = 0
# for tag in tags:
#     count+=1
#     print (tag.get('href', None))
# print(count)
