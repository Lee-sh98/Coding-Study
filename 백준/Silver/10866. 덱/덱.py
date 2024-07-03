import sys
from collections import deque
input = sys.stdin.readline

printable = ["pop_front", "pop_back", "size", "empty", "front", "back"]

action = {
    "push_front":deque.appendleft,
    "push_back": deque.append,
    "pop_front": lambda x: x.popleft() if x else -1,
    "pop_back": lambda x: x.pop() if x else -1,
    "size": deque.__len__,
    "empty": lambda x: int(len(x)==0),
    "front": lambda x: x[0] if x else -1,
    "back": lambda x: x[-1] if x else -1
    }

N = int(input())
dq = deque()

for _ in range(N):
    commend, *operand = input().split()
    if commend in printable:
        print(action[commend](dq, *operand))
    else:
        action[commend](dq, *operand)
 