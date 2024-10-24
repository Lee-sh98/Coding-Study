import sys
sys.setrecursionlimit(10**5)

def factorial(n):
    if n <= 1:
        return 1
    if n not in fact:
        fact[n] = n*factorial(n-1)
    return fact[n]

def solve(target):
    initial = list(sorted(target))
    if initial == target:
        return -1
    
    sequence = 0
    copy = initial[:]
    for i in range(N):
        idx = copy.index(target[i])
        copy.remove(target[i])
        f = factorial(N-i-1)
        sequence += f*idx

    sequence -= 1
    
    answer = [0]*N
    for i in range(N):
        f = factorial(N-i-1)
        q, sequence = divmod(sequence, f)

        answer[i] = str(initial.pop(q))
    return " ".join(answer)
    

fact = {}

N = int(input())
target = list(map(int, input().split()))

result = solve(target)
print(result)
