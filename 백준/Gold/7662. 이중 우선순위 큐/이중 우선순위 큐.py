import sys
from heapq import *
from collections import Counter
input = sys.stdin.readline

def sync():
    while max_q and count[-max_q[0]] == 0:
        heappop(max_q)
    while min_q and count[min_q[0]] == 0:
        heappop(min_q)

T = int(input())
for _ in range(T):
    k = int(input())
    min_q, max_q = [], []
    
    count = Counter()
    for _ in range(k):
        commend, operand = input().split()
        num = int(operand)

        if commend == "I":
            heappush(min_q, num)
            heappush(max_q, -num)
            count[num] += 1
            
        elif num == 1:
            if max_q:
                count[-heappop(max_q)] -= 1
            sync()
            
        elif num == -1:
            if min_q:
                count[heappop(min_q)] -= 1
            sync()
    
    if any(count.values()):
        print(-max_q[0], min_q[0])
    else:
        print("EMPTY")
