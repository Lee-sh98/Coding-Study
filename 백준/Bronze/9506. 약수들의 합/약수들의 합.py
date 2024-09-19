import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    s = set([1])
    for i in range(2, int(n**0.5)+1):
        q, r = divmod(n, i)
        if not r:
            s |= set([i, q])

    if sum(s) == n:
        text = " + ".join(map(str, sorted(s)))
        print(f"{n} = {text}")
    else:
        print(f"{n} is NOT perfect.")
