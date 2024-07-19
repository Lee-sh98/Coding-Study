import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
T = list(sorted(map(int, input().split())))

result = last = T[-1]
i, j = 0, N-2

for count in range(1, K):
    if count%2:
        last = T[count//2]
    else:
        result += T[-(count//2)-1] - last
        last = T[-(count//2)-1]

sys.stdout.write(str(result)+"\n")
