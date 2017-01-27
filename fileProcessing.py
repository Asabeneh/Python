# Instruction for the user to put the proper file format
print("Enter mbox.txt or mbox-short.txt!")
#Geting the file, the file is in the directory
fname = input("Enter file name in .txt form: ")
#To handle  errors gracefully
try:
    fopen = open(fname) # opening file
except:
    print("File can't be opened: ",fname)
    exit()
#Creating a python list or arrays in other programming language for instace in C and JavaScript
emails = []
counter = 0 #Counts the number of lines which contain email
numline = 0 #Counts the totla number of lines in the file
#Looping through the file line by line
for line in fopen:
    numline+=1
    line = line.rstrip() # removing white space in both sides of the line
    if(line.startswith('From ')):#Filtering the lines having email
        spos = line.find(' ') #The beginning of the email string positon after removing from
        emailline= line[spos:].lstrip()
        epos = emailline.find(' ') # space after email, end position
        email = emailline[0:epos] #slicing out the email
        counter =counter + 1
        emails.insert(counter,email) #inserting each emails in the list
        email = emailline[0:epos]

print("\nE-mails in python list: \n", emails)
print("\nTotal number of emails:",len(emails))
print("Total number of lines:",numline)
