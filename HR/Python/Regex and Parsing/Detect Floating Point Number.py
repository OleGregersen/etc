# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = re.compile('^[-+]?[0-9]*\.[0-9]+$')
for _ in range(int(input())):
    print(bool(N.match(input())))
