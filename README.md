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
age = 25
fnumber= 4
start = 0
penality = -5
```
#### Decimals(float)
```python
...-5, -5.5,0.25,0,1,3...
pi = 3.14
temp = 98.6

```
### Strings
"Hello World!"

###Booleans
Boolean values are always true or false. It is affrimation or negation of a statement. 
```python
islighton = True
islightof = False

hungery = False
statisfied = False
married = False
student = True

print(islighton)
print(islightoff)

print(hungery)
print(married)
print(student)

Print Result:
True
False

False
False
True

```
## Strings

```python
lang ="Python"
task ="scraping"
greeting = "Hello Python ninjas"

print(lang)
print(task)
print(greeting)

Print Result:
python
scraping
Hello Python ninjas
```
### String Methods
```python
greeting = "Hello Donald J. Trump"
greeting.lower()
greeting.upper()
greeting.tittle()
greeting.endswith('g')
greeting.startswith('g')
greeting.isnumeric()

```

methods can be found by dir(greeting) from the console


## Funcition
### Void Function(Functions without parameter)
```python 
def saySomething():
        print("Good Morning")
  ```
### Function with parameters
```python
name =input("What is your name: ").lower()
lang = input("What language do you speak: ").lower()
def greet(lang,name):
    if(lang == 'eng'):
            print("Hello",name)
    elif(lang=='es'):
            print("Holla",name)
 
    elif(lang=='fr'):
        if(live =="France"):
            print("Bonjour",name)
    elif(lang=='fi'):
            print("Moi",name)
    elif(lang=='am'):
            print("Selam",name)
    else:
        print("Do you speak English?",name)
greet(lang,name)
```
### Built-in Functions

## Conditions
### One - way decision
```python
x = 10
if (x > 5):
        print x
```
### Two -way decision
```python
x = 10
if (x <5):
        print(x)
else:
        print(x)
```
### Multi -way decision
```python
name =input("What is your name: ").lower()
lang = input("What language do you speak: ").lower()
    if(lang == 'eng'):
            print("Hello",name)
    elif(lang=='es'):
            print("Holla",name)
 
    elif(lang=='fr'):
        if(live =="France"):
            print("Bonjour",name)
    elif(lang=='fi'):
            print("Moi",name)
    elif(lang=='am'):
            print("Selam",name)
    else:
        print("Do you speak English?",name)

```
## Loop
#### For in list
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
#### For number in range(a number)
```python
for num in range(15):
        if(num % 4 ==0):
                print(num,"is divisible by f.")
       
Print Result:
4 is divisible by 4.
8 is divisible by 4.
12 is divisible by 4.
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
['book', 'laptop',50, 1.5,'Mango', False, 'Venomous Snake\]
 
```
### List Methods
```python
lists = list()
dir(lists) # to get the list methods from console
```

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
### Dictionary Methods
## Tuples

