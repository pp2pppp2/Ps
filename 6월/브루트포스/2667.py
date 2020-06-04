N = int(input())
MAP = [input() for _ in range(N)]
visit =[[0 for _ in range(N)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
m = []
def bfs(y, x):
    q = [(y, x)]
    visit[y][x] = 1
    cnt = 1
    while q:
        y, x = q.pop(0)
        for i in range(4):
            ty = y + dy[i]; tx = x + dx[i]
            if 0 <= ty < N and 0 <= tx < N and visit[ty][tx] == 0 and MAP[ty][tx] == '1':
                visit[ty][tx] = 1
                cnt += 1
                q.append((ty, tx))
    m.append(cnt)
ans = 0
for y in range(N):
    for x in range(N):
        if MAP[y][x] == '1' and visit[y][x] == 0:bfs(y, x); ans += 1
print(ans)
for k in sorted(m):print(k)