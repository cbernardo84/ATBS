#! python3

#regexStrip takes a string and does the same thing as the strip() string
#method.  If no other arguments  are passed other than the string to strip,
#then whitespace characters will be removed from the beginning and end of
#the string. Otherwise, the characters specified in the second argument to
#the function will be removed from the string.

import re

#After remembering what .strip() does, I think we'll need to save initial
#.strips in variables for further processing, so whitespace removal then
#specific character removal.<--this was my initial thought, ended up doing
#character removal first, I don't remember why.

userInput = input('input a string with spaces: ')
userInput2 = input('which character should I remove ?: ')

def regex_strip(userInput, userInput2):
    removeChars = re.compile(r'[^' + userInput2 + ']') ##remove user input chars

    mo1 = removeChars.findall(userInput) ## .findall regex in 'string'

    noChars = ''.join(mo1) ##turns list returned by .findall into a str
    print(noChars) ##Just to make sure this step was working
    
    removeSpaces = re.compile(r'[^\s]') ##regex removing spaces

    mo2 = removeSpaces.findall(noChars) ## .findall regex in 'noChars', the first mo

    final = ''.join(mo2) ##turn list returned by .findall into a str
    print('You\'re left with: '+ final)
    return(final) ##somewhere in the tutorial it said you needed to return so, here it is
    

regex_strip(userInput, userInput2)
    
            
    
