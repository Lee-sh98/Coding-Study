import sys
input = lambda: map(int, sys.stdin.readline().split())

def find_repeated(arr):
    return sum(len(set(a))!=N for a in arr)

T, = input()
for i in range(1, T+1):
    N, =input()
    mat = [list(input()) for _ in range(N)]

    k = sum(mat[i][i] for i in range(N))
    r = find_repeated(mat)
    c = find_repeated(list(map(list, zip(*mat))))

    print(f"Case #{i}: {k} {r} {c}")
