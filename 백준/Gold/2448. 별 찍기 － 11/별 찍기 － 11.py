import sys

def solve(n):
    if n==3:
        return ["  *  ", " * * ", "*****"]

    half = n//2
    prev = solve(half)
    result = []

    for i in range(half):
        tmp = " "*half + prev[i] + " "*half
        result.append(tmp)

    for i in range(half):
        tmp = prev[i] + " " + prev[i]
        result.append(tmp)

    return result
    

N = int(sys.stdin.readline())
result = solve(N)
for r in result:
    print(r)
