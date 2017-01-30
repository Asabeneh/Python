import re
fname = input("Enter file name:")
if(fname ==""):
    fname = "regex_sum_42.txt"
fopen = open(fname,'r')
nums = list()
for line in fopen:
    line = line.strip()
    # print(line)
    num = re.findall('[0-9]+',line)
    if (num):
        nums.append(num)
numbers = list()
for n in nums:
        for m in n:
            value = int(m)
            numbers.append(value)

print(numbers)
print(len(numbers))
print(sum(numbers))
