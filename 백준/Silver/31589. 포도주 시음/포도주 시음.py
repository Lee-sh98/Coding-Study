import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
T = list(sorted(map(int, input().split())))

result = last = T[-1]
count = 1
i, j = 0, N-2

while count < K:
    if count%2:
        last = T[i]
        i += 1
    else:
        result += T[j] - last
        last = T[j]
        j -= 1
    count += 1

sys.stdout.write(str(result)+"\n")
