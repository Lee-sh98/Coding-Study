import sys
from collections import deque
input = sys.stdin.readline

def solution(arr):
    stack = []
    last = 0
    while arr:
        cur = arr.popleft()
        while stack and stack[-1] == last+1:
            last = stack.pop()
        if cur == last + 1:
            last = cur
        else:
            stack.append(cur)

    while stack and stack[-1] == last+1:
        last = stack.pop()
        
    return not stack

N = int(input())
arr = deque(map(int, input().split()))

if solution(arr):
    print("Nice")
else:
    print("Sad")

