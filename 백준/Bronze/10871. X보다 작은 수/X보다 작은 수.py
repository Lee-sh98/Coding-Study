#10871 number lesser than X

x = list(map(int, input().split()))[1]
print(' '.join(list(filter(lambda y: int(y)<x,input().split()))))