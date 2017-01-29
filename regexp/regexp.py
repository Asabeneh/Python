import re
fname = input("Enter the file name:")
if(fname == ""):
    fname = 'mbox-short.txt'
try:
    fopen = open(fname)
except:
    print("Couldn't open the file",fname)
    exit()

for line in fopen:
    # print(line)
    line = line.strip()
    print(line)
    if re.search('From:',line):
        print(line)

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
# if line.find('From:') >= 0:
#     print (line)
