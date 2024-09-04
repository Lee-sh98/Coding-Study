import sys
from collections import deque
input = sys.stdin.readline
    
def solution():
    left, right = [], []

    enter = input().rstrip()

    for e in enter:
        match e:
            case "<":
                if left:
                    right.append(left.pop())
            case ">":
                if right:
                    left.append(right.pop())
            case "-":
                if left:
                    left.pop()
            case _:
                left.append(e)
    while right:
        left.append(right.pop())
    return "".join(left)
    


T = int(input())
for _ in range(T):
    result = solution()
    print(result)
