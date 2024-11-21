f=lambda x:(x[-1]=='A'and f(x[:-1]))or(x[0]=='B'and f(x[1:][::-1]))if x and len(x)!=len(S)else x==S
S=input()
print(int(f(input())))