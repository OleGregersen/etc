# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
a = input().split()
k = int(input())
cl = list(combinations(a, k))
al = [e for e in cl if 'a' in e]
print(len(al) / len(cl))
