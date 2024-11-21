def f(x):
    if not x:
        return 0
    if len(x)==len(S) and x==S:
        return 1
    a=b=0
    if x[-1]=='A':
        a=f(x[:-1])
    if x[0]=='B':
        b=f(x[1:][::-1])
    return max(a,b)

S,T=input(),input()
print(f(T))