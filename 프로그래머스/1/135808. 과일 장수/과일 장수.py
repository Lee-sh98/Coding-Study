def solution(k, m, score):
    answer = 0
    counts = [0]*(k+1)
    result = []
    
    for apple in score:
        counts[apple]+=1
    
    for s, count in enumerate(counts):
        result += [s]*count
    
    result.reverse()
    N = len(result)
    
    for i in range(0, N, m):
        if len(result[i:i+m])==m:
            answer += result[i+m-1]*m
            
    
    return answer