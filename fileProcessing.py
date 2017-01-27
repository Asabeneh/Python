print("Enter mbox.txt or mbox-short.txt!")
fname = input("Enter file name in .txt form: ")
try:
    fopen = open(fname)
except:
    print("File can't be opened: ",fname)
    exit()
emails = []
counter = 0
numline = 0
for line in fopen:
    numline+=1
    line = line.rstrip()
    if(line.startswith('From ')):
        spos = line.find(' ')
        emailline= line[spos:].lstrip()
        epos = emailline.find(' ')
        email = emailline[0:epos]
        counter =counter + 1
        emails.insert(counter,email)
        email = emailline[0:epos]

print("\nE-mails in python list: \n", emails)
print("\nTotal number of emails:",len(emails))
print("Total number of lines:",numline)
