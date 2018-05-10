
#Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10


def makes10(a, b):
    sum = a + b
    if ((a == 10) or (b == 10) or (sum == 10)):
        return True
    return False

print(makes10(10, 20))
print(makes10(9,1))
print(makes10(4,5))


# return (a == 10 or b == 10 or a+b == 10)
