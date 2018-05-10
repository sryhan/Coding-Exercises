
# Given a string, return a new string where "not" has been added to the front.
# However, if the string already begins with "not", return the string unchanged

def not_string(str):
    if "not" in str[:4]:
        return str
    else:
        return "not " + str


print(not_string("not string"))
print(not_string("dole"))
