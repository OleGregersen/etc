# Enter your code here. Read input from STDIN. Print output to STDOUT
s1 = set(input().split())
n = int(input())
o = True
for i in range(n):
    s2 = set(input().split())
    if not s2.issubset(s1):
        o = False
    if len(s2) >= len(s1):
        o = False
print(o)
