"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""

num = int(input("Enter a number: "))
numRange = range(1, num+1)

numList = []

for number in numRange:
    if num % number == 0:
        numList.append(number)

if len(numList) < 3:
    print(str(num) + " is prime")
else:
    print(str(num) + " is not prime")

print(numList)
