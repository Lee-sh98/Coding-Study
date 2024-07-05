import sys
input = sys.stdin.readline

class Paper:
    def __init__(self, x, y):
        self.x = range(x, x+10)
        self.y = range(y, y+10)

class Drawing_paper:
    def __init__(self, width, height):
        self.drawing_paper = [[0]*width for _ in range(height)]
        self.drawn = 0

    def draw(self, paper:Paper):
        for i in paper.x:
            for j in paper.y:
                self.drawn += self.drawing_paper[i][j] == 0
                self.drawing_paper[i][j] = 1
                
N = int(input())
dp = Drawing_paper(100, 100)

for _ in range(N):
    paper = Paper(*map(int, input().split()))
    dp.draw(paper)

print(dp.drawn)
