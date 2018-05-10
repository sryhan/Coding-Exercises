
"""
Given a string and a non-negative int n, return a larger string that is n copies
of the original String
"""

def string_times(str, n):
    if n < 0:
        return False
    longer_string = str*n
    return longer_string

print(string_times("Bob", 3))
print(string_times("Bob", -1))
