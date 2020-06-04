import sys
sys.stdin = open("16234.txt")

N, L, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(fy, fx, T):
    global flag
    visit[fy][fx] = T
    q = [(fy, fx)]
    t = [(fy, fx)]
    s = MAP[fy][fx]
    while q:
        y, x = q.pop(0)
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < N and 0 <= tx < N:
                if L <= abs(MAP[y][x] - MAP[ty][tx]) <= R and visit[ty][tx] < T:
                    visit[ty][tx] = T
                    t.append((ty, tx))
                    q.append((ty, tx))
                    s += MAP[ty][tx]
    if len(t) >= 2:
        flag = 1
        for a in t:
            MAP[a[0]][a[1]] = s // len(t)

T = 1
while 1:
    flag = 0
    for y in range(N):
        for x in range(N):
            if visit[y][x] < T:
                bfs(y, x, T)
    if flag:
        T += 1
        continue
    break

print(T-1)