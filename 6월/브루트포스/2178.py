# BFS COST visit == 0 이면 COST 제일 작은 녀석입니다. 헷갈리지 않도록합니다.
N,M =map(int, input().split())
MAP = [input()for _ in range(N)]
visit = [[0]*(M)for _ in range(N)]
from collections import deque
dx = [0,0,1,-1]; dy=[1,-1,0,0]
def bfs():
    q = deque()
    q.append((0,0,1))
    visit[0][0] = 1
    while q:
        y, x, c = q.popleft()
        for i in range(4):
            ty=y+dy[i];tx=x+dx[i]
            if 0<=ty<N and 0<=tx<M and visit[ty][tx] == 0 and MAP[ty][tx] == '1':
                q.append((ty,tx,c+1))
                visit[ty][tx] = c+1
    return visit[N-1][M-1]
print(bfs())