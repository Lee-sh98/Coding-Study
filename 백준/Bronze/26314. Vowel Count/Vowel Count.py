for _ in range(int(input())):
    print(s:=input())
    print(int(2*sum(map(s.count,'aeiou'))>len(s)))
