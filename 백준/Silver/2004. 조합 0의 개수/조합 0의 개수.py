import sys

n, m = map(int, sys.stdin.readline().split())

def count_prime(n, t):
    count = 0
    while n:
        n //= t
        count += n
    return count

result = []
for i in [2, 5]:
    tmp = count_prime(n, i) - count_prime(m, i) - count_prime(n-m, i)
    result.append(tmp)

print(min(result))
