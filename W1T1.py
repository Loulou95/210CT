import random
list = [20, 16, 10, 5];
x = []
for i in range (0, len(list), 1):
    randomnumber = random.randint(0, len(list)-1)
    minus = list.pop(randomnumber)
    x.append(minus)

print (x) 
