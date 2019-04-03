#! python3

#strongPass.py uses regex to make sure the password string it is passed is strong.  A strong
#password is defined as:
    #eight characters long
    #both uppercase and lowercase chars
    #at least one digit

import re

password = input('enter password:  ')

eightChars = re.compile(r'\w{8,}')

mo1 = eightChars.search(password).group()
print('At least 8 characters')

#this version works...i think
##upLowNum = re.compile(r'[a-z][A-Z]\d+.*|[A-Z][a-z]\d+.*|\d+.*[A-Za-z]')

#trying to factor the code, I think that's what you call making it shorter...
#better, but I still think I can remove the pipe.  Revisit later.
upLowNum = re.compile(r'\d+[A-Za-z]+.*|[A-Za-z]+\d+.*')

result = upLowNum.search(mo1).group()
print(result)

