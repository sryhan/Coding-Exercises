
# Given an int n, return the absolute difference between n and 21, except return
# double the absolute difference if n is over 21

def diff21(n):
    absDiff = 21 - n
    if n > 21:
        return (absDiff * 2)
    return absDiff

print(diff21(10))
print(diff21(32))
