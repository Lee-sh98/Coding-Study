import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(10)]
result = 0
dif = 100

for a in arr:
    if dif>=abs(100-(result+a)):
        dif = 100 - (result + a)
        result += a
    else:
        break
print(result)
