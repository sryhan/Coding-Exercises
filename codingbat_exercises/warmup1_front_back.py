
# Given a string, return a new string where the first and last chars have been
# exchanged

def front_back(str):
    if str == "":
        return "Empty String"
    first_letter = str[0]
    last_letter = str[len(str)-1]
    body = str[1:-1]
    return last_letter + body + first_letter

print(front_back("Homer"))
