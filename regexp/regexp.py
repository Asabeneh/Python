# import re
# fname = input("Enter the file name:")
# if(fname == ""):
#     fname = 'mbox-short.txt'
# try:
#     fopen = open(fname)
# except:
#     print("Couldn't open the file",fname)
#     exit()
#
# for line in fopen:
#     # print(line)
#     line = line.strip()
#     if(line.startswith("From")):
#         print(line)
#     #print(line)
#     if re.search('^From:',line):#return first match
#         print(line)

import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
A = "This Is GOI'\S+@\S+',x)NG TO BE GREAT Really"
y = re.findall('[0-9]',x)
z = re.findall('^From:.*?\S+@\S+',x)

print (y)
print (z)
