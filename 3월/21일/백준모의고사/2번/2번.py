import sys
sys.stdin = open('2.txt')

N, M, G, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

F = []
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 2:
            F.append([y, x])

v = [0] * len(F)
seed = [G, R]

def solve():
    TMP = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
    TMPQ = []
    for i in range(len(F)):
        if v[i]:
            TMP[F[i][0]][F[i][1]][0] = v[i]
            TMP[F[i][0]][F[i][1]][1] = -1
            TMPQ.append([F[i][0], F[i][1], 0])
    q = TMPQ
    cnt = 0
    while q:
        y, x, c= q.pop(0)
        if TMP[y][x][0] == 999:
            continue
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < N and 0 <= tx < M and MAP[ty][tx] != 0 and TMP[ty][tx][0] != TMP[y][x][0]:
                if TMP[ty][tx][0] != 0 and TMP[ty][tx][0] != TMP[y][x][0] and TMP[ty][tx][1] == c:
                    if TMP[ty][tx][0] == 999:
                        continue
                    cnt += 1
                    TMP[ty][tx][0] = 999
                elif TMP[ty][tx][0] == TMP[y][x][0]:
                    continue
                elif TMP[ty][tx][0] == 0:
                    q.append((ty,tx,c+1))
                    TMP[ty][tx][0] = TMP[y][x][0]
                    TMP[ty][tx][1] = c
    return cnt

def d(n):
    global ans
    if n == len(F):
        if sum(seed):
            return
        ans = max(ans, solve())
        return
    for i in range(2):
        if seed[i]:
            seed[i] -= 1
            v[n] = 3 + i
            d(n+1)
            v[n] = 0
            seed[i] += 1
    if sum(seed) < len(F) - n:
        d(n+1)
ans = 0
d(0)
print(ans)