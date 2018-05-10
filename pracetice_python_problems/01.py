
# 01 CHARACTER INPUT
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
#
#     1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#     2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

import datetime

name = input('Input your name: ')
age = input('Input your age: ')
repeat = int(input('How many times would you like to repeat this message? '))

rangeRepeat = range(repeat)

#print out a message that tells the year they will turn 100 years old

turnOnehundred = 100 - int(age)
now = datetime.datetime.now()
year = now.year

x = year + turnOnehundred

for i in rangeRepeat:
    print('You will turn 100 in the year: ' + str(x) + "\n")
