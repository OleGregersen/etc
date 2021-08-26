# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())
a = []
for _ in range(x):
    a.append(map(float, input().split()))
for i in zip(*a):
    print(sum(i) / len(i))
