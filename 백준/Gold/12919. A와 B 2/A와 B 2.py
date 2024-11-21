def f(x):
    if not x or len(x)==len(S):return x==S
    return (x[-1]=='A'and f(x[:-1]))or(x[0]=='B'and f(x[1:][::-1]))
S=input()
print(int(f(input())))