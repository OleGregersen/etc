# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = sorted(map(int, input().split()))
for i in range(len(s)):
    if(i != len(s) - 1):
        if(s[i] != s[i-1] and s[i] != s[i + 1]):
            print(s[i])
            break;
    else:
        print(s[i])
