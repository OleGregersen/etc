# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

print(*[(len(list(c)), int(x)) for x, c in groupby(input())])
