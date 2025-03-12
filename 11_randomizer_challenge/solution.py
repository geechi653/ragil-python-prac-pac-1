import random

list = ["red", "blue", "green", "black", "yellow"]
list2 = ["apple", "banana", "plum", "orange"] 
print(random.random())
print(random.randint(1,50))

print(random.choice(list))

random.shuffle(list2)

print(list2)