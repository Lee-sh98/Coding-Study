import sys

class Equation:
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r
        
    def confirm(self, x, y):
        return self.p*x+self.q*y == self.r

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

e1, e2 = Equation(a,b,c), Equation(d,e,f)
flag = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if e1.confirm(x, y) and e2.confirm(x, y):
            print(x, y)
            flag = True
            break
    if flag:
        break
