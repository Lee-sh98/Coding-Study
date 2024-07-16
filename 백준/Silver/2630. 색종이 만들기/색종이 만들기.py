import sys
from collections import defaultdict
input = sys.stdin.readline

def check(arr):
    total = set()
    for line in arr:
        total |= set(line)
    if len(total) == 1:
        count[arr[0][0]] += 1
    else:
        half = len(arr)//2

        check([i[:half] for i in arr[:half]])
        check([i[half:] for i in arr[:half]])
        check([i[:half] for i in arr[half:]])
        check([i[half:] for i in arr[half:]])

N = int(input())
paper = [list(input().split()) for _ in range(N)]
count = defaultdict(int)

check(paper)

print(count['0'])
print(count['1'])
