a,*b=input()
print(dict(zip("ABCDF",[4,3,2,1,0.0]))[a]+(dict(zip("+0-",[0.3,0.0,-0.3]))[b[0]] if b else 0))