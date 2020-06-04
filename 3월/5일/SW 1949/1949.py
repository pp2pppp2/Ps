import sys
sys.stdin = open("1949.txt")

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def d(y, x, cnt, flag, val):
    global ret
    ret = max(ret, cnt)
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if 0 <= ty < N and 0 <= tx < N:
            if val > MAP[ty][tx] and visit[ty][tx] == 0:
                visit[ty][tx] = 1
                d(ty, tx, cnt+1, flag, MAP[ty][tx])
                visit[ty][tx] = 0
            elif flag and not visit[ty][tx] and val > MAP[ty][tx] - K:
                visit[ty][tx] = 1
                d(ty, tx, cnt+1, 0, val-1)
                visit[ty][tx] = 0

for tc in range(1, T+1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    M = 1
    q = []
    for y in range(N):
        for x in range(N):
            if M < MAP[y][x]:
                M = MAP[y][x]
                q = [(y, x)]
            elif M == MAP[y][x]:
                q.append((y, x))
    ret = 0
    for y, x in q:
        visit[y][x] = 1
        d(y, x, 1, 1, MAP[y][x])
        visit[y][x] = 0
    print("#{} {}".format(tc, ret))