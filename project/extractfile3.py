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
    if sender not in senderscount:
        senderscount[sender] = 1
    else:
        senderscount[sender]+=1
for em in emails:
    if em not in emailscount:
        emailscount[em] = 1
    else:
        emailscount[em]+=1
print("Senders count:\n", senderscount)
print("Emails count: \n", emailscount)

print("The number of emails: ", len(emails))
print("The total emails communication: \n",emails,"\n")
print("The list fo senders: \n", senders,"\n")
print("The domains: \n",domains,"\n")
print("The number of lines in the file:",numlines)
