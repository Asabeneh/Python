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
# This function changes the fill in to dictionary
def changetodic():
    for line in fopen:
        line = line.strip().lower()
        # print(line)
        words = line.split()
        # print(words)
        for word in words:
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
    for val,key in lists[0:20]:
        print('The word',key.title(),'repeated',val,'times')
filtertopten()# Function call to execute the above function
