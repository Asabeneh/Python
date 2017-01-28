fname = input("Enter file name: ")
if(fname == ""):
    fname = 'mbox-short.txt'
fopen = open(fname)
emails = list()
senders = list()
domains = list()
numlines = 0
for line in fopen:
    numlines+=1
    if line.startswith('From '):
        words = line.split()
        # print(words)
        email = words[1]
        senderdomain = email.split('@')
        senders.append(senderdomain[0])
        domains.append(senderdomain[1])
        # print(email)
        emails.append(email)
senderscount = dict()
emailscount = dict()
for sender in senders:
    print(senderscount.get(sender,0)+1)
    senderscount[sender] =senderscount.get(sender,0)+1
for em in emails:
    emailscount[em] =emailscount.get(em,0)+1

print("Senders count:\n", senderscount)
print("Emails count: \n", emailscount)

print("The number of emails: ", len(emails))
print("The total emails communication: \n",emails,"\n")
print("The list fo senders: \n", senders,"\n")
print("The domains: \n",domains,"\n")
print("The number of lines in the file:",numlines)
