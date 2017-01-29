import re

fname = input("Enter file name: ")
if(fname == ""):
    fname = 'mbox-short.txt'
try:
    fopen = open(fname,'r')
except:
    print('couldn\'t find the file',fname)
    exit()
numlist =list()
for line in fopen:
    line = line.strip()
    extract = re.findall('X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(extract)!=1:continue
    num = float(extract[0])
    numlist.append(num)
print ('Minimum',max(numlist))
