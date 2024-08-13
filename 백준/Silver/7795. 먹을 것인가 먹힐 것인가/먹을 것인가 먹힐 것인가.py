import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    result = 0
    A = list(sorted(map(int, input().split())))
    B = list(sorted(map(int, input().split())))

    j = 0
    
    for i in range(N):
        while j<M and A[i]>B[j]:
            j += 1
        result += j
    print(result)

T = int(input())

for _ in range(T):
    solution()
