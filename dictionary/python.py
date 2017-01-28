#Getting file in .txt format
filename = input("Enter file:")
handlefile = open(filename, 'r') # Opening file
text = handlefile.read().lower().strip() # Reading the file, change to lower case, remove white space
print (text)
words = text.split() # Changing the text to strings and putting in a list
print(len(words))
print (words)
counts = dict() # Assigning empty dictionary
for word in words:
    counts[word] = counts.get(word,0) + 1 # key and value pair counted
count = None;
frequentword = None;
print (counts.items)
for frequentword, count in counts.items():
    if frequentword is None or count > count:
        frequentword = frequentword
        count = count
print(frequentword,count)
print(counts);
print(counts.get('the'));
