from collections import Counter

def solution(k, tan):
    counts = Counter(tan)
    classified = []
    for size, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        classified += [size]*count
    
    return len(set(classified[:k]))