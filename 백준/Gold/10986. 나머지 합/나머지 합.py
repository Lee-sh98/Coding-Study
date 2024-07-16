import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
acc = [0]*(N+1)
mcc = [0]*(M)

for i in range(N):
    acc[i+1] = acc[i] + arr[i]
    mcc[acc[i+1]%M] += 1

result = mcc[0]    

for m in mcc:
    result += m*(m-1)//2

print(result)
