import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_dict, num_dict = {}, {}

for i in map(str, range(1, N+1)):
    pokemon = input().rstrip()
    name_dict[pokemon] = i
    num_dict[i] = pokemon

for _ in range(M):
    if (question:=input().rstrip()).isdigit():
        print(num_dict[question])
    else:
        print(name_dict[question])
