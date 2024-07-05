word = input()

for i in range(len(word)):
    print(word[i], end=("", "\n")[(i+1)%10==0])
