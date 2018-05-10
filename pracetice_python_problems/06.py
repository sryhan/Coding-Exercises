"""
Ask the user for a string and print out whether this string is a palindrome or
not. (A palindrome is a string that reads the same forwards and backwards.)
"""

def palindrome(str):
    pal1 = str[:]
    pal2 = str[::-1]

    if pal1 == pal2:
        return "Your word is a palindrome"
    else:
        return "Not a palindrome"

print(palindrome("racecar"))
print(palindrome("Homer"))
