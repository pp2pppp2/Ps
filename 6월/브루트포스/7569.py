# 너무 삽질 많이 했어요.. 생각을 충분히 더 하고 하시길 바랄게요..

M, N, H, = map(int, input().split())
MAP = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visit = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

dy = [0, 0, 0, 0, 1, -1]
dx = [0, 0, 1, -1, 0, 0]
dh = [1, -1, 0, 0, 0, 0]
ans = 0

from collections import deque

def bfs():
    global ans
    while q:
        y, x, h, t = q.popleft()
        for i in range(6):
            ty = y+ dy[i]; tx = x+dx[i]; th = h + dh[i]
            if 0 <= ty < N and 0 <= tx < M and 0 <= th < H and visit[th][ty][tx] == 0:
                if MAP[th][ty][tx] == -1: continue
                elif MAP[th][ty][tx] == 0:
                    MAP[th][ty][tx] = 1
                    q.append((ty,tx,th,t+1))
                    visit[th][ty][tx] = t + 1

def answer():
    global ans
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if MAP[h][y][x] == 0:
                    ans = -1
                    return
                if visit[h][y][x] != 0 and visit[h][y][x] != 999999999:
                    ans = max(ans, visit[h][y][x])
    if ans == 999999999: ans = 0
q = deque()
for h in range(H):
    for y in range(N):
        for x in range(M):
            if MAP[h][y][x] == 1 and visit[h][y][x] == 0:
                q.append((y,x,h,0))
                visit[h][y][x] = 999999999
bfs()
answer()
print(ans)