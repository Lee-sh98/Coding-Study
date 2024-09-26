import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    depth = 0
    tmp = 0
    for c in input().rstrip():
        if c=="[":
            tmp += 1
        else:
            depth = max(depth, tmp)
            tmp -= 1

    print(2**depth)
