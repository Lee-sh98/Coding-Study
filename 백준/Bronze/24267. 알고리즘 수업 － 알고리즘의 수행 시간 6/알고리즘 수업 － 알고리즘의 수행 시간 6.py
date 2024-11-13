n=int(input())
print(f'{(sum((i-1)*i//2 for i in range(2,n)), 0)[n<3]}\n3')
