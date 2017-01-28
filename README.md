#Python
##Python CheatSheet
This python repository is prepared to be an online reference material. Therefore, the repository has python scripting codes from beginner to advanced levels. To make convient for learns, I organized the repository in different folder structure:Variable,Expressions, Conditionals, Functions, Loops, Lists, Dictionaries and Tuples. In different folder of the repository there many python scripting codes. Codes in the Variable, Expressions, Conditionals, Functions and Loops are beginner level. The codes in the Lists, Dictionaries, Tuples and other are advanced levels. Scripting codes in the list, dictionary, tuples folder can extract large text files.It loops through each line of the file and filter the line containing emails. Then email is extracted from each lines containing email by finding and slicing method. Then email is inserted in a python list. The total emails in the file and  total number of lines are counted.

##Variable
Variable are a means to store data. The data type which could be stored may be a number(int, float) or string.
```python
#Variables containing string
name = "Python Monthy"
quest = "Scripting"
activity = "Scraping"
#To check the type of the Variables
print("name is a string",type(name))
print("quest is a string",type(quest))
print("activity is a string",type(activity))
#Variables containing numbers, integer
age = 100
year = 2017
print(age)
print(year)
#To check the type of the Variables
print("age is an int",type(age))
print("year is an int",type(year))

#variable contiaing number, float
pi = 3.14
temp = 98.6
print(pi)
print(temp)
#To check the type of the Variables
print("pi is a float",type(pi))
print("temp is a float",type(temp))

satisfied = False
hungery = False
single = True
print(satisfied)
print(single)
#To check the type of the Variables
print("satisfied is a boolean",type(satisfied))
print("single is a boolean",type(single))

#Declaring list variable in python
items = list() # this is a list
items = [] # this is also a list
print(type(items))
#Declaring list variable in python
dic = dict()
print(type(dic))
```
## Data type
###Numbers
Numbers are integer(int) and decimals(float).
####Integers(Int)
```python
...-5,-4,-3,-2,-1,0,1,2,3,4,5...
```
####Decimals(float)
```python
...-5, -5.5,0.25,0,1,3...
```
###Booleans
Boolean values are always true or false. It is affrimation or negation of a statement. 
```python
islighton = True
islightof = False

hunger = False
statisfied = false
married = False
student = True

True, False
```
## Strings
```python
lang ="Python"
task ="scraping"
greeting = "Hello Python ninjas"
```

## Funcition
```python 
def saySomething():
        print("Good Morning")
  ```
## Conditions

### One - way decision
```python
if
```
### Two -way decision
```python
if 
else
```
### Multi -way decision
```python
if
elif 
elif
elif
else
```
## Loop
```python
web = ['HTML', 'CSS', 'JavaScript','Bootstrap', 'EJS','Blaze','Mustache','handlebarjs','ReactJs', 'AngularJS', 'Python', 'PHP','NodeJS','MongoDB','SQL']
for wblang in web:
        print (wblang)
      
Print Result:
['HTML', 'CSS', 'JavaScript','Bootstrap', 'EJS','Blaze','Mustache','handlebarjs','ReactJs', 'AngularJS', 'Python', 'PHP','NodeJS','MongoDB','SQL']

 #Another method to looping
 for i in range(len(web)):
        print(web[i])
Print Result:
['HTML', 'CSS', 'JavaScript','Bootstrap', 'EJS','Blaze','Mustache','handlebarjs','ReactJs', 'AngularJS', 'Python', 'PHP','NodeJS','MongoDB','SQL']
```  
while True:
## List
A linear collection of values which maintain order.A list is an ordered sequence. Each value in a sequence has its own index order.

```python
socialmedia = ['facebook','twitter','instagram', 'linkedin','pintrest','myspace'] #Fixed amount of values
lists = list() or lists = [] #Method of decalaring list variable

lists[0] = 'book'
lists[1] = 'laptop'
list[2] = 50
lists[3] = 1.5
lists[4] = 'Mango'
lists[5] = False
lists[6] = "Venomous Snake"

 print(lists)
 
 Print Result:
['book', 'laptop',50, 1.5,'Mango', False, "Venomous Snake"]
 
```
### List Methods

## Dictionary
A data collection in which each values has its own label or key. Dictionary in python is analogous to objects in JavaScript. Dictionary doesn't maintain order.Dictionary values is looked up by their keys or labels. Dictionaries are mutable or modifiable similar to lists. However, strings are immutable.
The most common use of dictionary is to count how often something can occur. Refering a key which is not in a dictionary results error.

```python
shoppingbag = dict()

shoppingbag['milk'] = 2
shoppingbag['egg'] = 1
shoppingbag['coffee'] = 2
shoppingbag['sugar'] = 1.5

print(shoppingbag)

Print result:
{'milk':2,'egg':1, 'coffee':2,'sugar':1.5}
```
## Tuples

