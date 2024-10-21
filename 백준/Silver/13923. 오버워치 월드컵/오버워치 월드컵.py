import sys
from collections import defaultdict
input = sys.stdin.readline

def solve(N):
    people = [""]*N
    
    for i in range(N):
        people[i] = "".join(input().split())

    joined = "".join(people)
    count = defaultdict(int)
    for person in joined:
        count[person] += 1
    
    M = list(filter(lambda x: count[x] in [1, N+1], count))[0]
    V = list(filter(lambda y: count[y] == N-1, count))[0]
    
    if count[M] == 1:
        Q, R = divmod(joined.find(M), N)
        return Q+1, R+1, V
    else:
        row, col = 0, 0
        transpose = list(map(list, zip(*people)))
        
        for i in range(N):
            if people[i].count(M) == 2:
                row = i
            if transpose[i].count(M) == 2:
                col = i

        return row+1, col+1, V

while True:
    try:
        N = int(input())
        R, C, V = solve(N)
        print(R, C, V)
    except Exception as e:
        break
