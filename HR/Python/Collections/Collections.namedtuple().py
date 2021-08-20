# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n, s = int(input()), namedtuple('s', input())
print("{:.2f}".format(sum([int(s(*input().split()).MARKS) for _ in range(n)]) / n))
