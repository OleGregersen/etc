# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

v = 'aeiou'
c = 'qwrtypsdfghjklzxcvbnm'
s = re.findall(r'(?<=[' + c + '])([' + v + ']{2,})(?=[' + c + '])', input(), flags=re.I)
print('\n'.join(s or ['-1']))
