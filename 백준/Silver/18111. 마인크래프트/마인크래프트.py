import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, B = map(int, input().split())
blocks = {}
for _ in range(N):
    for height in map(int, input().split()):
        blocks[height] = blocks.get(height, 0) + 1

MIN, MAX = min(blocks), max(blocks)
MIN_TIME = INF
MAX_HEIGHT = 0

for target in range(MIN, MAX+1):
    time = 0
    inventory = B
    for height in blocks:
        if height > target:
            time += 2*(height - target)*blocks[height]
            inventory += (height-target)*blocks[height]
        elif height < target:
            time += (target - height)*blocks[height]
            inventory -= (target-height)*blocks[height]

    if inventory >= 0 and MIN_TIME >= time:
        MIN_TIME = min(MIN_TIME, time)
        MAX_HEIGHT = max(MAX_HEIGHT, target)

print(MIN_TIME, MAX_HEIGHT)
