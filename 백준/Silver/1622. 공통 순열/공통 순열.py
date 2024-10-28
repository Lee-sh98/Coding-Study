from collections import Counter

while True:
    try:
        a = Counter(input())
        b = Counter(input())
        
        print("".join(sorted((a&b).elements())))
    except:
        break
