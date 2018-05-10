"""
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

Extras:

    1. Write two different functions to do this - one using a loop and
    constructing a list, and another using sets.
    2. Go back and do Exercise 5 using sets, and write the solution for that in a
    different function.
"""
import random

randList1 = []
# randlist2 = []

# random list of values 
for i in range (0,20):
    randList1.append(random.randint(0,20))
    # randlist2.append(random.randint(0,20))

print(sorted(randList1))
# print(randlist2)

def thisList():
    listSet = set(randList1)
    newList = []
    for item in listSet:
        newList.append(item)
    return sorted(newList)

print(thisList())
