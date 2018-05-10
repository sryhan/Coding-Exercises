
"""
Given a non-empty string like "Code", return a string like "CCoCodCode"
"""

def string_splosion(str):
    parts = ""
    for n in range(len(str)):
        parts = parts + str[:n+1]
    return parts


#original attempt
# def string_splosion(str):
#     part1 = str[:1]
#     part2 = str[:2]
#     part3 = str[:3]
#     part4 = str[:4]
#
#     parts = part1 + part2 + part3 + part4
#     return parts

print(string_splosion("Phone"))
print(string_splosion("Burger"))
