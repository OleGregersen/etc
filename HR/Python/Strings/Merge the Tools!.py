def merge_the_tools(string, k):
    # your code goes here
    subs = len(string) // k
    out = []
    output = []
    for i in range(0, len(string) - k + 1, k):
        out.append(string[i:i + k])
    for sub in out:
        for char in sub:
            count = sub.count(char)
            if count > 1:
                sub = sub[::-1]
                sub = sub.replace(char, '', count - 1)
                sub = sub[::-1]
        output.append(sub)
    print("\n".join(map(str, output)))

