#Strings are like lists but they are immutable, they can not be modified
fruit = 'Tomato'
#do't try to change
# fruit[0] ="P"
# fruit[2]="t"
T = fruit[0]
m = fruit[2]
print(T)
print(m)
lower = fruit.lower()
print(lower)
upper = fruit.upper()
print(upper)
print(fruit)
#Lists are mutable, they can be modified at any time

lotto = [2,16,19,23,25,27]
print(lotto)
lotto[0] = 4
print(len(lotto))
print(lotto[len(lotto)-1])
print(lotto[0] * lotto[len(lotto)-1])

lotto[len(lotto)-1] = lotto[0] * lotto[len(lotto)-1]
print(lotto)
