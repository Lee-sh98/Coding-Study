def f(x):
    if not x:return 0
    if len(x)==len(S):return x==S
    a=x[-1]=='A'and f(x[:-1]);b=x[0]=='B'and f(x[1:][::-1])
    return a or b

S,T=input(),input()
print(int(f(T)))