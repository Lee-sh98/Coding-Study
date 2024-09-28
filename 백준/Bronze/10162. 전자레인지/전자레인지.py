import sys

T = int(sys.stdin.readline())
button = [300, 60, 10]
result = [0]*3
for i in range(3):
    result[i], T = divmod(T, button[i])

if not T:
    print(*result)
else:
    print(-1)
