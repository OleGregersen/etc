# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, k = input().split()
r = list(permutations(s, int(k)))
for i in sorted(r):
    print("".join(i))
