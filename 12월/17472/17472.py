import sys
sys.stdin = open("17472.txt")

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def color(fy, fx, num):
    q = [(fy, fx)]
    MAP[fy][fx] = num
    while q:
        y, x = q.pop(0)
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < N and 0 <= tx < M and MAP[ty][tx] == 1:
                MAP[ty][tx] = num
                q.append((ty, tx))
def init():
    num = 1
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 1:
                land.append((y, x))
                num += 1
                color(y, x, num)

def cal(y, x, d, num):
    q = 0
    while MAP[y][x] == 0:
        q += 1
        y += dy[d]
        x += dx[d]
        if 0 > y or y >= N or 0 > x or x >= M or MAP[y][x] == num:
            return
        if MAP[y][x] and q > 1:
            con[num-2][MAP[y][x]-2] = min(q, con[num-2][MAP[y][x]-2])

def findroad():
    q = [land.pop(0)]
    while q:
        y, x = q.pop(0)
        visit[y][x] = 1
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < N and 0 <= tx < M and visit[ty][tx] == 0:
                if MAP[ty][tx] == 0:
                    cal(ty, tx, i, MAP[y][x])
                else:
                    q.append((ty,tx))

def connect(s):
    q = [s]
    zz[s] = 1
    while q:
        z = q.pop(0)
        for i in range(C):
            if zz[i]: continue
            if dvisit[z][i]:
                q.append(i)
                zz[i] = 1

def d(n, r, sum2, x):
    global ret, zz
    if x == C:
        return
    if n == C:
        connect(0)
        if sum(zz) == C:
            ret = min(sum2, ret)
        zz = [0] * C
        return
    for i in range(r, C+1):
        if con[x][i] == 98764321 or dvisit[x][i]: continue
        dvisit[x][i] = 1
        dvisit[i][x] = 1
        if i == C:
            d(n+1, 0, sum2+con[x][i], x+1)
        else:
            d(n+1, i+1, sum2+con[x][i], x)
        dvisit[x][i] = 0
        dvisit[i][x] = 0
    d(n, 0, sum2, x+1)

ret = 98675421
land = []
visit = [[0 for _ in range(M)] for _ in range(N)]
dvisit = [[0 for _ in range(8)] for _ in range(8)]
con = [[98764321 for _ in range(8)] for _ in range(8)]
init()
C = len(land)
zz = [0] * C
while land:
    findroad()
d(1, 0, 0, 0)
print(ret if ret != 98675421 else -1)

