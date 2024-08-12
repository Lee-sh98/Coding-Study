import sys
from collections import deque
input = sys.stdin.readline

def parse_list(listStr):
    replaced = listStr[1:-1]
    if not replaced:
        return []
    return replaced.split(",")

def format_list(arr):
    message = ",".join(arr)
    return f"[{message}]"

def solution():
    commend = input().rstrip()
    N = int(input())
    arr = parse_list(input().rstrip())
    direction = 1
    error = False
    q = deque(arr)
    

    for c in commend:
        if c == "R":
            direction *= -1
        elif c == "D":
            if not q:
                error = True
                continue
            if direction == 1:
                q.popleft()
            else:
                q.pop()
    if error:
        print("error")
    else:
        if direction == -1:
            q.reverse()
        result = format_list(q)
        print(result)

T = int(input())
for _ in range(T):
    solution()
