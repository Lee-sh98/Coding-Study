f=lambda:{*map(int, input().split())}
f()
C = f()-f()
print(len(C))
print(*sorted(C))
