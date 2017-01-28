fname = input("Enter file name: ") #Getting file from user
if(fname == ""):                    #If user doesn't put file take the given default text
    fname = 'mbox-short.txt'
try:
    fopen = open(fname,'r') # opening file
except:
    print("Couldn't find the file ",fname)
emails = list() # Declaring empty list variable to put all emails in list
senders = list() # Declaring empty list variable for the senders
domains = list() # Declaring empty list variable for collecting the domain part of the emails
numlines = 0
for line in fopen: #for loop which iterates through every line of the file
    # line = line.rstrip() #Removing white space from the write
    numlines +=1
    if line.startswith('From '):
        words = line.split() # Removing
        # print(words)
        email = words[1]
        senderdomain = email.split('@')
        senders.append(senderdomain[0])
        domains.append(senderdomain[1])
        print(email)
        emails.append(email)

print("The emails: \n",emails,"\n")
print("The senders name: \n", senders,"\n")
print("The domains name: \n",domains,"\n")
print("\nThe number of emails: ", len(emails))
print("The number of senders: ", len(senders))
print("Total number of lines:",numlines)
