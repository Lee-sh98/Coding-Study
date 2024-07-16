import sys
from collections import deque
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.q = deque([])
        self.operation = {"push": self.q.append,
                          "pop": self.pop,
                          "size": self.size,
                          "empty": self.empty,
                          "front": self.front,
                          "back": self.back}

    def action(self, commend, *operand):
        self.operation[commend](*operand)

    def print(self, func, otherwise=-1):
        if self.q:
            print(func())
        else:
            print(otherwise)

    def pop(self):
        self.print(lambda: self.q.popleft())

    def size(self):
        self.print(self.q.__len__, 0)

    def empty(self):
        self.print(lambda: 0, 1)

    def front(self):
        self.print(lambda: self.q[0])

    def back(self):
        self.print(lambda: self.q[-1])

N = int(input())
q = Queue()

for _ in range(N):
    commend, *operand = input().split()
    q.action(commend, *operand)
    
