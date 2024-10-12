import sys

S = sys.stdin.readline().rstrip()
parenthesis = "()"
stack = []
result = 0

for i in range(len(S)):
    if S[i].isdecimal():
        stack.append(S[i])
    elif S[i] == '(':
        stack.append('(')
    else:
        count = 0
        while stack and stack[-1] != '(':
            c = stack.pop()
            if type(c) == int:
                count += c
            else:
                count += 1

        stack.pop()
        stack.append(int(stack.pop())*count)

for c in stack:
    if type(c) == int:
        result += c
    else:
        result += 1

print(result)
