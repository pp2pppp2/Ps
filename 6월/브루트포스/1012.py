dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
def bfs(y, x):
    q = [(y, x)]
    while q:
        y, x = q.pop(0)
        for i in range(4):
            ty = y + dy[i]; tx = x + dx[i]
            if 0 <= ty < N and 0 <= tx < M and not visit[ty][tx] and MAP[ty][tx] == 1:
                visit[ty][tx] = 1; q.append((ty, tx))
for tc in range(int(input())):
    M, N, K = map(int, input().split())
    MAP = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for k in range(K):
        X, Y = map(int, input().split())
        MAP[Y][X] = 1
    ans = 0
    for y in range(N):
        for x in range(M):
            if MAP[y][x] and visit[y][x] == 0: bfs(y, x); ans += 1
    print(ans)