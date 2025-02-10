for s in [*open(0)][1:]:
    r=""
    for c in s:print(end=c*(r!=c));r=c