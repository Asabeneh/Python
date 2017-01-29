#To get file from user, user doesn't put a file
fname = input("Enter file: ")
if(fname == ""):
    fname = 'romeo.txt'
# To handle errors gracefully
try:
    fopen = open(fname, 'r')
except:
    print("Couldn't find ",fname)
    exit()

fopen = open(fname, 'r')
dic = dict()
prepos = ['a','the',
'this','these','that','those',
'be','been','being',
'is','was','are','were',
'and','or','nor','yet','but',
'with','without',
'on','at','in','for','to','of',
'will','would','can','could',
'may','might','ought to','has',
'have','had','must','already',
'so','because','it','its'
'i','me','mine','we','us','our','ours',
'he','his','she','her','hers',
'you','your','yours',
'they','them','their','by','no','not','who','when','where','what','why','which','from',',','/','-']

# This function changes the fill in to dictionary
def changetodic():
    for line in fopen:
        line = line.strip().lower()
        # print(line)
        words = line.split()
        # print(words)
        for word in words:
            if not word in prepos:
                dic[word] = dic.get(word,0) + 1
changetodic()# Function call to execute the above function
# print(dic)
lists = list()
#Function changes the dictionary to a list of tuples
def changetolist():
    for key, val in dic.items():
        lists.append((val, key))
    lists.sort(reverse=True)

changetolist() # Function call to execute the above function
def filtertopten():
    for val,key in lists[0:10]:
        print('The word',key.title(),'repeated',val,'times')
filtertopten()# Function call to execute the above function
