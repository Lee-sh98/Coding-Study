from collections import Counter
from itertools import combinations as t, chain

*W, k = (input() for _ in range(4))

c = Counter(chain(*map(lambda w: t(w, int(k)), W)))

if (r:=sorted(filter(lambda d: c[d]>=2, c))):
    print("\n".join(map("".join, r)))
else:
    print(-1)
