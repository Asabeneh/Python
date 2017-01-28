dic = dict()
fname = input("Enter file:")
if(fname == ""):
    fname = 'mbox-short.txt'
try:
    fopen = open(fname,'r')
except:
    print("Couldn't open the file, ", fname)
numlines = 0
words = list()
for line in fopen:
    numlines+=1
    if(line.startswith("From ")):
        line = line.strip()
        line = line.split()
        word= line[1]
        words.append(word)
        # print(words)
        # print(line)
        # print(words)

wordcount = dict()
for value in words:
    wordcount[value] = wordcount.get(value,0) + 1

print(wordcount)
print(len(wordcount))

value = list()
for key in wordcount:
    print(key)
    value.append(wordcount[key])
    print(wordcount[key])
print(max(value))
print(list(wordcount))
print(wordcount.keys())
print(wordcount.values())
print(wordcount.items())
freqword = None
freqwordvalue = None
for key, value in wordcount.items():
    if freqword is None or value > freqwordvalue:
        freqword = key
        freqwordvalue = value

print(freqword,freqwordvalue)
