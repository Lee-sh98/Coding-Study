import sys
input = sys.stdin.readline

def solution(arr):
    stack = []
    target = 1
    
    for cur in arr:
        stack.append(cur)
        while stack and stack[-1] == target:
            target = stack.pop() + 1

    return not stack

N = int(input())
arr = map(int, input().split())

print(("Sad", "Nice")[solution(arr)])
