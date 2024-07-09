def move(start, end):
    print(start, end)

def hanoi(n, start, end, other):
    if n==1:
        move(start, end)
    else:
        hanoi(n-1, start,other, end)
        move(start, end)
        hanoi(n-1, other,end, start)

N = int(input())
print(2**N-1)
hanoi(N, 1, 3, 2)
