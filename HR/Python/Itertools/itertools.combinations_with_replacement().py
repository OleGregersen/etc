# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s = input().split()
c, n = sorted(s[0]), int(s[1])
print(*list(map(''.join, combinations_with_replacement(c, n))), sep='\n')
