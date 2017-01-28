fname = input("Enter file: ")
fopen = open(fname, 'r')
dic = dict()
for line in fopen:
    line = line.strip()
    words = line.split()
    for word in words:
        dic[word] = dic.get(word,0) + 1

lists = list()
for key, val in dic.items():
    lists.append((val, key))
lists.sort(reverse=True)
def filter():
    for val,key in lists[0:10]:
        print(key.title(),val)
filter()
