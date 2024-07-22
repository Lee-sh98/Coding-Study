def solution(picture, k):
    answer = [""]*k*len(picture)
    for i, pic in zip(range(0, k*len(picture), k), picture):
        for j in range(k):
            answer[i+j] = "".join(map(lambda p: p*k, pic))
    return answer