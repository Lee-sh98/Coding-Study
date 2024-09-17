import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0]*w)

time = 0
total = 0

while total or trucks:
    total -= bridge.popleft()

    if trucks and total+trucks[0] <= L:
        bridge.append(trucks.popleft())
        total += bridge[-1]
    else:
        bridge.append(0)
    
    time += 1

print(time)
