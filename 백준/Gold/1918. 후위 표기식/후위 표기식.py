import sys

s = sys.stdin.readline().rstrip()

stack = []
result = ""

for c in s:
    if c.isalpha():
        result+=c
    elif c == '(':
        stack.append(c)
    elif c in "*/":
        while stack and stack[-1] in "*/":
            result += stack.pop()
        stack.append(c)
    elif c in "+-":
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(c)
    elif c == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()

while stack:
    result += stack.pop()

print(result)
