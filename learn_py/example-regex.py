import re

phoneNumRegex = re.compile(r'\d{11}')
mo = phoneNumRegex.search('hello this is the number 171547887, what do you think?')
if mo != None:
    print(mo.group())