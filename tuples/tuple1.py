fname = input("Enter file: ")
fopen = open(fname, 'r')
dic = dict()
def changetodic():
    for line in fopen:
        line = line.strip()
        words = line.split()
        for word in words:
            dic[word] = dic.get(word,0) + 1
changetodic()
lists = list()
def changetolist():
    for key, val in dic.items():
        lists.append((val, key))
    lists.sort(reverse=True)

changetolist()
def filtertopten():
    for val,key in lists[0:10]:
        print(key.title(),val)
filtertopten()
