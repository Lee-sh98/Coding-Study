for s in[*open(0)][1:]:a,b=map(s.lower().count,'gb');print(s[:-1],'is',('NEUTRAL','GOOD','A BADDY')[(a>b)-(a<b)])