# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = input().split()
a = list(map(int, a))
b = input().split()
b = list(map(int, b))
print(*list(product(a, b)))
