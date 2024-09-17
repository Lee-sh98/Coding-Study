import sys

def compare(a, b):
    return priority[a]>=priority[b]

s = sys.stdin.readline().rstrip()
priority = {'*': 3, '/': 3,
            '+': 2, '-': 2,
            '(': 1}
stack = []
result = []
for c in s:
    match c:
        case '(':
            stack.append(c)

        case '+'|'-'|'*'|'/':
            while stack and compare(stack[-1], c):
                result.append(stack.pop())
            stack.append(c)

        case ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        case _:
            result.append(c)

while stack:
    result.append(stack.pop())

print("".join(result))
