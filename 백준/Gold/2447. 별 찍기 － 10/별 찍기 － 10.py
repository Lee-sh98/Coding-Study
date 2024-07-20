import sys

print = sys.stdout.write

def makeStar(size):
    if size==1:
        return ["*"]

    result = [""]*size
    scale = size//3
    prevStar = makeStar(scale)
    blank = " "*scale

    for i, star in enumerate(prevStar):
        result[i] = star*3
        result[i+scale] = star+blank+star
        result[i+2*scale] = star*3

    return result
           

# N : length of a side
N = int(sys.stdin.readline())

for line in makeStar(N):
    print(line+"\n")
   
