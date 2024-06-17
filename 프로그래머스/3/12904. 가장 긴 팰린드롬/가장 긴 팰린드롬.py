def solution(s):
    answer = 0
    
    n = len(s)
    for i in range(n):
        end = i
        while end<=n:
            if is_palindrome(s[i:end]):
                answer = max(end-i, answer)
            end+=1
        
    return answer

def is_palindrome(word):
    n = len(word)
    return word[:n//2] == word[::-1][:n//2]