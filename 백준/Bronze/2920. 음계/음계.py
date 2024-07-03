scale = dict(zip([" ".join(map(str, i)) for i in [range(1, 9), range(8, 0, -1)]],
             ["ascending", "descending"]))
print(scale.get(input(), "mixed"))
