import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = 0
for _ in range(N):
    c, *d = map(int, input().split())
    if c==1:
        A, T = d
        stack.append([A, T-1])
    else:
        if stack:
            stack[-1][1] -= 1

    if stack and stack[-1][1] == 0:
        result += stack.pop()[0]

print(result)
