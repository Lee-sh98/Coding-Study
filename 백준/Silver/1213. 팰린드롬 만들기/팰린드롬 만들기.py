import sys
from collections import Counter

count = Counter(sys.stdin.readline().rstrip())
if len(list(filter(int(2).__rmod__, count.values()))) > 1:
    print("I'm Sorry Hansoo")
else:
    side, mid = "", ""
    s = list(sorted(count))
    
    for ch in s:
        if count[ch]%2:
            mid = ch
        side += ch*(count[ch]//2)
    print(side+mid+side[::-1])
