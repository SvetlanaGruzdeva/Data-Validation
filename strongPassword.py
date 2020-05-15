#! python3 
# strongPassword.py - validates password. 

import re

password = input()

def checkPassword(password):
    # Check lenght
    if len(password) < 8:
        return False
    else:
        length =  True

    # Check if contains at least 1 digit
    digitRegex = re.compile(r'\d')
    digit = digitRegex.search(password)
    if not digit:
        return False

    # Check if has both upper case and lower case
    letterRegex = re.compile(r'[a-z]')
    lowerCase = letterRegex.search(password)
    if not lowerCase:
        return False

    letterRegex = re.compile(r'[A-Z]')
    upperCase = letterRegex.search(password)
    if not upperCase:
        return False
    
    return(length and digit and lowerCase and upperCase is not None)

print(checkPassword(password))


