N = int(input())
A = set(map(int, input().split()))
M = int(input())

for num in map(int, input().split()):
    print(int(num in A))
