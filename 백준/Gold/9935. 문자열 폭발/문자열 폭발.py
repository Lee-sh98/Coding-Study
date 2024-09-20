import sys
input = sys.stdin.readline

S = input().rstrip()
explosive = input().rstrip()
n = len(explosive)
stack = []

for c in S:
    if not stack:
        stack.append((c, c==explosive[0]))
    else:
        if c == explosive[stack[-1][1]]:
            stack.append((c, stack[-1][1]+1))
        else:
            stack.append((c, c==explosive[0]))

    if stack[-1][1] == n:
        for i in range(n):
            stack.pop()

if stack:
    print("".join(map(lambda x: x[0], stack)))
else:
    print("FRULA")
        
