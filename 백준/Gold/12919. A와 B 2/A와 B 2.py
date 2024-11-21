f=lambda x:(x[-1]=='A'and f(x[:-1]))|(x[0]=='B'and f(x[1:][::-1]))if len(x)!=len(S)else x==S
S=input()
print(int(f(input())))