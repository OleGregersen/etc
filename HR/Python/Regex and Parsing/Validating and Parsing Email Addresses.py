# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pat = r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$'
for _ in range(int(input())):
    name, email = input().split(' ')
    if re.match(pat, email):
        print(name, email)
