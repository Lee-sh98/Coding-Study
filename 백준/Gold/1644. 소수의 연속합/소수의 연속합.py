import sys

def make_prime_array(N):
    result = list(range(N+1))
    M = int(N**0.5)
    for i in range(2, M+1):
        if result[i]:
            for j in range(i+i, N+1, i):
                result[j] = 0
    return list(filter(int, result[2:]))

N = int(sys.stdin.readline())
prime_arr = make_prime_array(N)
L = len(prime_arr)
acc = [0]*(L+1)
result = 0

for i in range(L):
    acc[i+1] = acc[i] + prime_arr[i]

i, j = 0, 0
while i<=j<=L:
    sum_ = acc[j] - acc[i]
    if sum_ >= N:
        if sum_ == N:
            result += 1
        i += 1
    else:
        j += 1
print(result)
        
