def solution(n):
    answer = [[0]*n for _ in range(n)]
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cur= 0
    if n==1:
        return [[1]]
    count = 1
    x, y = 0, 0
    
    while count < n*n:
        dx, dy = direction[cur]
        nx, ny = x+dx, y+dy
        answer[x][y] = count
        
        if 0<=nx<n and 0<=ny<n and answer[nx][ny] == 0:
            x, y = nx, ny
            answer[nx][ny] = count+1
            count += 1
        else:
            cur = (cur+1)%4
    return answer
