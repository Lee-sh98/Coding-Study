import sys
input = sys.stdin.readline

def push(a):
    stack.append(a)
    result.append("+")

def pop():
    stack.pop()
    result.append("-")

n = int(input())
arr = [int(input()) for _ in range(n)]
cur = 0
stack = []
result = []

for i in range(1, n+1):
    push(i)
    while stack and stack[-1] == arr[cur]:
        pop()
        cur += 1

print(("\n".join(result), "NO")[bool(stack)])
