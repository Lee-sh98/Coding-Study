import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mem = {}
cumulative = [0]

for number in map(int, input().split()):
    cumulative.append(cumulative[-1] + number)
    
for _ in range(M):
    start, end = map(int, input().split())
    if (start, end) not in mem:
        mem[start, end] = cumulative[end] - cumulative[start-1]
    print(mem[start, end])
