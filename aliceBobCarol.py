#! python3

#aliceBobCarol is a regex that matches a sentence where the first word is either Alice, Bob,
#or Carol, the second word is either eats, pets or throws; the third word is apples, cats, or
#baseballs; and the sentence ends with a period.  The regex is case-insensitive and will match:

#'Alice eats apples.'

# but not:

#'Robocop eats apples.'

import re

aliceBobCarol = re.compile(r'''(
    (^Alice|^Bob|^Carol)                               #sentence starts with Alice Bob or Carol
    (\seats|\spets|\sthrows)                           #space eats pets or throws
    (\sapples|\scats|\sbaseballs)                      #space apples cats or baseballs
    .                                                  #ends with a period
    )''', re.VERBOSE)
