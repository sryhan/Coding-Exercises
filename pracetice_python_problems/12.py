"""
Write a program that takes a list of numbers (for example,
a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last
elements of the given list. For practice, write this code inside a function.
"""

def firstAndLast():

    numberList = []
    while True:
        numbers = input("Enter number, press quit to close: ")
        if numbers == "quit":
            break
        numberList.append(numbers)
    #print(numberList[0])
    newNumberList = [numberList[0], numberList[-1]]
    print(newNumberList)

    #print("The first number is " + numberList.index[0] + " and the last number is " + numberList.index[-1])

firstAndLast()
