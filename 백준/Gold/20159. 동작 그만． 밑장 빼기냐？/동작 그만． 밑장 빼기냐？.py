import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

odd_sum = [0]*(N//2+1)
even_sum = [0]*(N//2+1)

for i in range(N//2):
    odd_sum[i+1] = odd_sum[i] + arr[2*i]
    even_sum[i+1] = even_sum[i] + arr[2*i+1]

result = odd_sum[-1]

for i in range(N):
    mid = i//2
    if i%2:
        cur = odd_sum[mid+1] + (even_sum[-2] - even_sum[mid])
    else:
        cur = odd_sum[mid] + (even_sum[-1] - even_sum[mid])

    result = max(result, cur)

print(result)
