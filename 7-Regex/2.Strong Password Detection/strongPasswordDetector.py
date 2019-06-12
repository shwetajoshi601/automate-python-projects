#! python3

import re

def isPasswordStrong(password):
    regex = re.compile(r'''
    (?=.{8,})(.*[a-z])(.*[A-Z])(.*[0-9])(.*)| #?=. is positive lookahead - matches the expression without considering it in the results - for enforcing length
    (?=.{8,})(.*[a-z])(.*[0-9])(.*[A-Z])(.*)|
    (?=.{8,})(.*[A-Z])(.*[a-z])(.*[0-9])(.*)|
    (?=.{8,})(.*[A-Z])(.*[0-9])(.*[a-z])(.*)|
    (?=.{8,})(.*[0-9])(.*[a-z])(.*[A-Z])(.*)|
    (?=.{8,})(.*[0-9])(.*[A-Z])(.*[a-z])(.*)
    ''', re.VERBOSE)
    match = regex.search(password)
    if match == None:
        return False
    else:
        return True

password = str(input('Enter Password: '))
if(isPasswordStrong(password)):
    print("Password is strong")
else:
    print("Password is not strong")