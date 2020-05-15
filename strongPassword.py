#! python3 
# strongPassword.py - validates password. 

import re

password = input()

def checkPassword(password):
    # Check lenght
    if len(password) < 8:
        # print('Invalid password: password should contain at least 8 characters')
        return False
    else:
        # print('Valid password check1')
        length =  True

    # Check if contains at least 1 digit
    digitRegex = re.compile(r'\d')
    digit = digitRegex.search(password)
    if not digit:
        # print('Invalid password: password should contain at least 1 digit')
        return False
    # else:
        # print('Valid password check2')

    # Check if has both upper case and lower case
    letterRegex = re.compile(r'[a-z]')
    lowerCase = letterRegex.search(password)
    if not lowerCase:
        # print('Invalid password: password should contain at least 1 lower case character')
        return False
    # else:
    #     print('Valid password check3')

    letterRegex = re.compile(r'[A-Z]')
    upperCase = letterRegex.search(password)
    if not upperCase:
        # print('Invalid password: password should contain at least 1 upper case character')
        return False
    # else:
    #     print('Valid password check4')
    
    return(length and digit and lowerCase and upperCase is not None)

print(checkPassword(password))


