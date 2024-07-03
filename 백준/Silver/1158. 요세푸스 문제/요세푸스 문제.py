import sys
input = sys.stdin.readline

class Person:
    def __init__(self, n):
        self.number = n+1
    def __repr__(self):
        return str(self.number)

N, K = map(int, input().split())

answer = []
people = list(range(1, N+1))
cur = 0

while people:
    count = K
    while count:
        count -= 1
        if count == 0:
            who = people.pop(cur)
            answer.append(str(who))
            break
        cur = (cur+1)%len(people)
        
print(f"<{', '.join(answer)}>")
