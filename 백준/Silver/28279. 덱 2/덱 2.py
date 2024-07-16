import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dq = deque()
for _ in range(N):
    commend, *operand = map(int, input().split())

    match commend:
        case 1:
            dq.appendleft(*operand)
        case 2:
            dq.append(*operand)
        case 3:
            print(dq.popleft() if dq else -1)
        case 4:
            print(dq.pop() if dq else -1)
        case 5:
            print(len(dq))
        case 6:
            print(int(not dq))
        case 7:
            print(dq[0] if dq else -1)
        case 8:
            print(dq[-1] if dq else -1)
