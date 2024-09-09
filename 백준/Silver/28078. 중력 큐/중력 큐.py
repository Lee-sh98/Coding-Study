import sys
from collections import deque
input = sys.stdin.readline

class gravity_queue:
    def __init__(self):
        self.q = deque()
        self.d = 0
        self.count = {"b":0, "w":0}

    def action(self, commend, *operand):
        match commend:
            case "push":
                self.q.appendleft(operand[0])
                self.count[operand[0]] += 1
            case "count":
                print(self.count[operand[0]])
            case "pop":
                if self.q:
                    self.count[self.q.pop()] -= 1
            case "rotate":
                if operand[0] == "l":
                    self.d = (self.d-1)%4
                else:
                    self.d = (self.d+1)%4
        self.drop()
            
    def drop(self):
        if self.d == 1:
            while self.q and self.q[-1] == "b":
                self.count[self.q.pop()] -= 1
        if self.d == 3:
            while self.q and self.q[0] == "b":
                self.count[self.q.popleft()] -= 1
        
Q = int(input())
gq = gravity_queue()

for _ in range(Q):
    commend, *operand = input().split()
    gq.action(commend, *operand)
