import  urllib.request

furl = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
# furl = urllib.request.urlopen('http://stackoverflow.com/questions/27815281/cant-import-socket-module')

dic = dict()
for line in furl:
    line = line.rstrip()
    print(line)
    words = line.split()
    for word in words:
        dic[word] = dic.get(word,0) + 1
print (dic)
