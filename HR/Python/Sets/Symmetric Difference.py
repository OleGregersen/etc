# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
s1 = set(map(int, input().split()))
n = int(input())
s2 = set(map(int, input().split()))
mdif = s1.difference(s2)
ndif = s2.difference(s1)
o = mdif.union(ndif)
for i in sorted(list(o)):
    print(i)
