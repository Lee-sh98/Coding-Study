N = int(input())
a = b = 1

for _ in range(N//2):
    b += (a := a + 2*b)
print((a, 0)[N%2])
