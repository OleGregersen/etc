# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(input())):
    UID = input().strip()
    if UID.isalnum() and len(UID) == 10:
        if bool(re.search(r'(.*[A-Z]){2,}',UID)) and bool(re.search(r'(.*[0-9]){3,}',UID)):
            if re.search(r'.*(.).*\1+.*',UID):
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
