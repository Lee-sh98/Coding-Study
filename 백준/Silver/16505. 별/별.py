import sys

def solution(n):
    if n==0:
        return ["*"]
    prev = solution(n-1)
    result = []
    for i, line in enumerate(prev):
        result.append(line+" "*i+line)
    for line in prev:
        result.append(line)
    return result

N = int(sys.stdin.readline())

for line in solution(N):
    print(line)
