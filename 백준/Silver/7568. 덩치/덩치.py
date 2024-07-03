import sys
input = sys.stdin.readline

def compare(me, another):
    return me[0]<another[0] and me[1]<another[1]

N = int(input())
body = [list(map(int, input().split())) for _ in range(N)]
result = [0]*N

for i in range(N):
    count = sum(compare(body[i], body[j]) for j in range(N))
    result[i]=count+1

print(*result, sep=" ")
