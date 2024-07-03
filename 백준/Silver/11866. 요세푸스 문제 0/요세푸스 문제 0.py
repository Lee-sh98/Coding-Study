import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

answer = []
q = deque(map(str, range(1, N+1)))

while q:
    q.rotate(-K)
    answer.append(q.pop())
    
print(f"<{', '.join(answer)}>")
