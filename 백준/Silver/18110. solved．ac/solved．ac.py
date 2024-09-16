import sys
input = sys.stdin.readline

def new_round(n):
    q, r = divmod(n, 1)
    if r>=0.5:
        return int(q+1)
    else:
        return int(q)

n = int(input())
if n>0:
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    sep = new_round(n*0.15)
    target = arr[sep:-sep]

    if sep:
        print(new_round(sum(target)/len(target)))
    else:
        print(new_round(sum(arr)/n))
else:
    print(0)
