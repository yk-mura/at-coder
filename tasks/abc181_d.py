import sys
from collections import Counter

S = input()

if len(S) <= 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    sys.exit(0)
    
s_cnt = Counter(S)
for i in range(112, 1000, 8):
    i_cnt = Counter(str(i))
    if len(i_cnt - s_cnt) == 0:
        print('Yes')
        sys.exit(0)

print('No')