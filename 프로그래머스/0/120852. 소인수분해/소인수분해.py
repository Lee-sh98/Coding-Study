def solution(n):
    answer = set()
    for i in range(2, n+1):
        while n%i == 0:
            answer.add(i)
            n//=i
    answer = list(answer)
    return sorted(answer)