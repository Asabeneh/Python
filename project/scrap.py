import urllib.request
# fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for line in fhand:
    print(line.strip())
