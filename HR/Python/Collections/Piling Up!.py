# Enter your code here. Read input from STDIN. Print output to STDOUT
for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    i = 0
    while i < n - 1 and s[i] >= s[i + 1]:
        i += 1
    while i < n - 1 and s[i] <= s[i + 1]:
        i += 1
    print('Yes' if i == n - 1 else 'No')
