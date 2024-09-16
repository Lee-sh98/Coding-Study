import sys
input = sys.stdin.readline

backward, forward = [], []
N, Q = map(int, input().split())
cur = None
for _ in range(Q):
    c, *v = input().split()

    if c=="B":
        if backward:
            forward.append(cur)
            cur = backward.pop()
    elif c=="F":
        if forward:
            backward.append(cur)
            cur = forward.pop()
    elif c == "A":
        forward.clear()
        if cur:
            backward.append(cur)
        cur = v[0]
    elif c == "C":
        if backward:
            tmp = [backward[0]]
            for b in backward[1:]:
                if tmp[-1] != b:
                    tmp.append(b)
            backward = tmp

print(cur)
print(" ".join(backward[::-1]) if backward else -1)
print(" ".join(forward[::-1]) if forward else -1)
