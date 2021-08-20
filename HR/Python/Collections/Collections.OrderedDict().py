# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
d = OrderedDict()
for i in range(n):
    item = input().split()
    price = int(item[-1])
    name = " ".join(item[:-1])
    if d.get(name):
        d[name] += price
    else:
        d[name] = price
for i in d.keys():
    print(i, d[i])
