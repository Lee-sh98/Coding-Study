def f(x):
    if not x:return 0
    if len(x)==len(S):return x==S
    a=b=0
    if x[-1]=='A':a=f(x[:-1])
    if x[0]=='B':b=f(x[1:][::-1])
    return a or b

S,T=input(),input()
print(int(f(T)))