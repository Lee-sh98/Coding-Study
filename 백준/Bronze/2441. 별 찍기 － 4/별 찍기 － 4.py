print(*map(lambda x: " "*x[0]+x[1], enumerate("*"*i for i in range(int(input()), 0, -1))), sep="\n")
