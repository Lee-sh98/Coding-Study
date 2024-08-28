import sys
input = sys.stdin.readline

S = input().rstrip()
explosive = input().rstrip()
n = len(explosive)
stack = []
check = 0

for c in S:
    if not stack:
        if c == explosive[0]:
            stack.append((c, 1))
        else:
            stack.append((c, 0))
    else:
        if c == explosive[stack[-1][1]]:
            stack.append((c, stack[-1][1]+1))
        elif c == explosive[0]:
            stack.append((c, 1))
        else:
            stack.append((c, 0))

    if stack[-1][1] == len(explosive):
        for i in range(len(explosive)):
            stack.pop()

if stack:
    print("".join(map(lambda x: x[0], stack)))
else:
    print("FRULA")
        
