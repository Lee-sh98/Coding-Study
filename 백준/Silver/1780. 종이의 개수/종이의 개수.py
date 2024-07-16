import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(arr):
    n = len(arr)
    total = set()

    for line in arr:
        total |= set(line)

    if len(total) == 1:
        count[list(total)[0]+1] += 1
        return

    for i in range(0, n, n//3):
        for j in range(0, n, n//3):
            tmp = []
            for k in range(i, i+n//3):
                tmp.append(arr[k][j:j+n//3])
            solution(tmp)

N = int(input())
count = [0, 0, 0]
paper = [list(map(int, input().split())) for _ in range(N)]

solution(paper)

print(*count, sep="\n")
