import sys
input = sys.stdin.readline

class Comparator:
    def __init__(self, phrase, rule):
        self.phrase = phrase
        self.rule = rule
        
    def compare(self, x, y, z):
        return self.phrase.get(self.rule(x, y, z), "Error")

def rule(x, y, z):
    return sum([x==y, y==z, z==x]) if sum([x, y, z]) == 180 else -1
    
word = ["Scalene", "Isosceles", "Equilateral"]
phrase = dict(zip([0, 1, 3], word))

cmp = Comparator(phrase, rule)
result = cmp.compare(*(int(input()) for _ in range(3)))
print(result)
