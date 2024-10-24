import sys
from heapq import *
input = sys.stdin.readline

while True:
    data = list(filter(int(0).__lt__, map(int, input().split())))
    if not any(data):
        break
    heapify(data)

    while len(data) > 1:
        cur = heappop(data)
        for i in range(len(data)):
            data[i] -= cur

        while data and data[0] <= 0:
            heappop(data)

        heappush(data, cur)

    print(data[0])
