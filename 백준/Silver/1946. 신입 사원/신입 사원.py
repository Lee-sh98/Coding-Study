import sys
input = sys.stdin.readline



def solution():
    N = int(input())
    applicants = [list(map(int, input().split())) for _ in range(N)]
    applicants.sort(key = lambda x: (x[0], x[1]))
    acceptance = 0
    max_score = applicants[0][1]
    
    for _, interview in applicants:
        if interview<=max_score:
            acceptance+=1
            max_score = interview

    print(acceptance)

T = int(input())
for _ in range(T):
    solution()
