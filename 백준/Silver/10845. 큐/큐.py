import sys
from collections import deque
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.q = deque()
        self.operation = {"push": self.q.append,
                          "pop": self.q.popleft,
                          "size": self.q.__len__,
                          "empty": lambda: int(not self.q),
                          "front": lambda: self.q[0],
                          "back": lambda: self.q[-1]}
    def action(self, commend, *operand):
        func = self.operation[commend]

        match commend:
            case "push":
                func(*operand)
            case "size"|"empty":
                print(func())
            case _:
                print(self.prepare(func)())

    def prepare(self, func):
        return (func, lambda: -1)[not self.q]


N = int(input())
q = Queue()

for _ in range(N):
    q.action(*input().split())
