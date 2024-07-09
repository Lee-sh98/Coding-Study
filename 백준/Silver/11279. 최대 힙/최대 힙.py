import sys
import heapq
input = sys.stdin.readline

def dp(func):
    mem = []
    heapq.heapify(mem)
    def helper(n):
        if n == 0:
            if mem:
                print(-1*heapq.heappop(mem))
            else:
                print(0)
        else:
            heapq.heappush(mem, -n)
    return helper

action = dp(lambda x: x)

N = int(input())
for _ in range(N):
    action(int(input()))
