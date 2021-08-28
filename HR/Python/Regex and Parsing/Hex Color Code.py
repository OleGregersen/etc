# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    hex = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if hex:
        print(*hex, sep='\n')
