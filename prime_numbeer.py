z = [x for x in range(2,100) if all (x%y!=0 for y in range(2,int(x/2)))]
print(z)

import re

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print (re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher


ip = '1.255.255.9'

pattern = re.sub('\.','[..]',ip)

print(pattern)
