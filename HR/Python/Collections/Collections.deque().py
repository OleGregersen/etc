# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n = int(input())
d = deque()
for i in range(n):
    a = input().split()
    if a[0] == 'append':
        d.append(a[1])
    elif a[0] == 'pop':
        d.pop()
    elif a[0] == 'popleft':
        d.popleft()
    elif a[0] == 'appendleft':
        d.appendleft(a[1])
print(*d)
