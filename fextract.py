fileName = open('mbox-short.txt','r')
for line in fileName:
    line = line.rstrip()
    # if not line.startswith("From "):
    #     continue
    if not '@uct.ac.za' in line:
        continue
    print(line)

# emails = []
# counter = 0
# numline = 0
# for line in fileName:
#     numline+=1
#
#
#     if(line.startswith('From ')):
#
#         print (line)
#         print(numline)
#         startPos = line.find(' ')
#         removeFrom = line[startPos:].lstrip()
#         endPos = removeFrom.find(' ')
#         email = removeFrom[0:endPos]
#         counter =counter + 1
#         emails.insert(counter,email)
#
#         #
#         # print(counter)
#         # print(endPos)
#         # print(removeFrom[0:endPos])
#         email = removeFrom[0:endPos]
#
#         # print(email)
# print(emails)
# print("Total number of emails:",len(emails))
# print("Total number of lines:",numline)
