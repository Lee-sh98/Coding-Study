import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
T = deque(sorted(map(int, input().split())))

result = last = T.pop()
count = 1
while count < K:
    if count%2:
        last = T.popleft()
    else:
        result += (picked:=T.pop()) - last
        last = picked
    count += 1
sys.stdout.write(str(result)+"\n")
