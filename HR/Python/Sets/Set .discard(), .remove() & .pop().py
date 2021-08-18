n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    inp = input().split()
    if inp[0] == "remove":
        s.remove(int(inp[1]))
    elif inp[0] == "discard":
        s.discard(int(inp[1]))
    else:
        s.pop()
print(sum(list(s)))
