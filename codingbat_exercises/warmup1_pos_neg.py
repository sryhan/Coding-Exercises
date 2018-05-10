# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative


def pos_neg(a, b, negative):
    if negative:
        if (a < 0 and b < 0):
            return True
        return False
    if (a < 0 or b < 0) and (a > 0 or b > 0):
        return True
    return False

print(pos_neg(4, -4, False))
print(pos_neg(-6, -7, True))
print(pos_neg(4, 4, False))
