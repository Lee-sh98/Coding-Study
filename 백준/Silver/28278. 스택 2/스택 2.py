import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.s = []
        op = [self.s.append, self.s.pop, self.s.__len__,
              self.empty, self.top]
        self.operation = dict(zip(range(1, 6), op))

    def action(self, commend, *operand):
        func = self.operation[commend]

        if commend == 1:
            func(*operand)
        elif commend in [3, 4]:
            print(func())
        else:
            print(self.prepare(func)())

    def prepare(self, func):
        if self.s:
            return func
        else:
            return lambda: -1
    
    def empty(self):
        return int(not self.s)

    def top(self):
        return self.s[-1]
    

N = int(input())
st = Stack()

for _ in range(N):
    st.action(*map(int, input().split()))
