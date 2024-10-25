N = int(input())
a = b = 1

for _ in range(N//2):
    a += 2*b
    b += a
print((a, 0)[N%2])
