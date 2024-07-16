import sys
input = sys.stdin.readline


def solution(line):
    stack = []
    for c in filter("()[]".__contains__, line):
        if c in open_bracket:
            stack.append(c)
        elif c in close_bracket:
            if not stack:
                return False
            if stack and stack[-1] == bracket[c]:
                stack.pop()
            elif stack and stack[-1] != bracket[c]:
                return False
    return not stack

open_bracket = "(["
close_bracket = ")]"
bracket = dict(zip(close_bracket, open_bracket))

while True:
    if (line:=input().rstrip()) == ".":
        break
    print("yes" if solution(line) else "no")
