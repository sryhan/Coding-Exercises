# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return true if we sleep in.


def sleep_in(weekday, vacation):
    if weekday == False or vacation:
        return True
    else:
        return False

print(sleep_in(False, False))
