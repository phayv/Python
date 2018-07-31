import re

datestr = '2-11-2002\n23/9/2002\n3/8/02\n9/3/2002\n2 May 2002\n23 September 2002\nJan 2, 2002\nOctober 23, 2002\n'

"""
Potential Digit(s) in the beginning (up to 2)
Return more than just the abbreviation of months
[a-z]* because May doesn't necesarrily have anything after
2 - 4 digits for the year
"""
part1 = r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}'
part2 = r'(?:\d{1,2} )?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (?:\d{1,2}, )?\d{2,4}'

# working on combining
"""
potential digit(s) in the beginning with ' ', '/', and '-'
potential digit(s) after, but we only have '/' and '-'
potential Month spelled out or abbreviated followed by a space.
potential digit(s) with comma after potential Month spelled out
2 - 4 digits for the year
"""
combine = r'(?:\d{1,2}[ /-])?(?:\d{1,2}[/-])?(?:(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* )?(?:\d{1,2}[,/-](?: )?)?\d{2,4}'

# Adding more variations
datestr2 = '2002-2-11\n2002-11-2\n2-2002-11\n11-2002-2\n2002 Jan 2\n2002 October 23\n'
datestr = datestr + datestr2

combine = r'(?:\d{1,4}[ /-])?(?:\d{1,4}[ /-])?(?:(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z ]*)?(?:\d{1,4}[,/-](?: )?)?\d{1,4}'

print(re.findall(combine, datestr))

# there are more obscure variations we haven't tested