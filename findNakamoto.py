#findNakamoto is a regex that matches the full name of someone whose last name is Nakamoto
#it will not match names where the first name is not capitalized (satoshi) or
#if the preceding word has a nonletter character (Mr.) or
#where Nakamoto is not capitalized (nakamoto)

import re

#look for a capitalized character, then one or more \w chars, a space and then Nakamoto
findNakamoto = re.compile(r'[A-Z]\w+ Nakamoto')

#this worked on the first try!  
