# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
s = set(map(int, input().split()))
n2 = int(input())
for i in range(n2):
    o = input().split()
    if o[0] == "intersection_update":
        tmp = set(map(int, input().split()))
        s.intersection_update(tmp)
    elif o[0] == "update":
        tmp = set(map(int, input().split()))
        s.update(tmp)
    elif o[0] == "symmetric_difference_update":
        tmp = set(map(int, input().split()))
        s.symmetric_difference_update(tmp)
    elif o[0] == "difference_update":
        tmp = set(map(int, input().split()))
        s.difference_update(tmp)
print(sum(s))
