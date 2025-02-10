for s in [*open(0)][1:]:
    r,*s=s
    for c in s:r+=c*(c!=r[-1])
    print(end=r)