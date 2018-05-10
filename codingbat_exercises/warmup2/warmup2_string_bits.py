
"""
Given a string, return a new string made of every other char starting with the
first, so "Hello" yields "Hlo"
"""

def string_bits(str):
    bits = str[::2]
    return bits

print(string_bits("Heeololeo"))
print(string_bits("Hello"))
print(string_bits("Hi"))
