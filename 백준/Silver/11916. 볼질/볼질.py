def push():
    global B,result
    result+=B[2]
    B=[0]+B[:2]

N=int(input())
A=[*map(int,input().split())]
B=[0]*3
count=0
result=0

for a in A:
    match a:
        case 1:
            count += 1
        case 2:
            count = 4
        case 3:
            count += 1
            push()
    if count == 4:
        if B[0]:
            push()
        B[0]=1
        count=0
print(result)