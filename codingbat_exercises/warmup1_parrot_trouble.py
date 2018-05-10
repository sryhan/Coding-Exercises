# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20.
# Return true if we are in trouble


def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False

print(parrot_trouble(True, 4))
print(parrot_trouble(False, 3))

# return (talking and (hour < 7 or hour > 20))
