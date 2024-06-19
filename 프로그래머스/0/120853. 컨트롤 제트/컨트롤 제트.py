def solution(s):
    stack = []
    for c in s.split():
        if c.lstrip("-").isdigit():
            stack.append(int(c))
        else:
            if stack:
                stack.pop()
    return sum(stack)