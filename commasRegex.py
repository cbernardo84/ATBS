#commasRegex returns the string of numbers properly formatted w/commmas (1,200)
#but will not return strings of numbers w/improperly formatted commas (12,00)
#nor will it return strings of numbers without commas (1200)

import re

commasRegex = re.compile(r'(^\d{1,3}$)|(^\d{1,3}(,\d{3})+$)')
