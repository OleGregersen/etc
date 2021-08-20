# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = input()
s = Counter(map(int, input().split()))
n = int(input())
rev = 0
for _ in range(n):
    size, price = map(int, input().split())
    if s[size]:
        rev += price
        s[size] -= 1
print(rev)
