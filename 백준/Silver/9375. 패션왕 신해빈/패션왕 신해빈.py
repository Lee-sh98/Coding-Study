import sys
input = sys.stdin.readline

T  = int(input())
for _ in range(T):
    fashion = {}
    n = int(input())

    for _ in range(n):
        name, kind = input().split()
        if kind not in fashion:
            fashion[kind] = 1
        fashion[kind] += 1

    result = 1
    for i in fashion:
        result *= fashion[i]

    print(result - 1)
