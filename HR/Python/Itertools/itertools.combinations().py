# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s = input().split()
for i in range(1, int(s[1]) + 1):
    for j in combinations(sorted(s[0]), i):
        print(''.join(j))
