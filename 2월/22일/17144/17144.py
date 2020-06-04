import sys
sys.stdin = open("17144.txt")

dx = [[0, 1, 0, -1], [0, 1, 0, -1]]
dy = [[-1, 0, 1, 0], [1, 0, -1, 0]]

R, C, T = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]

def diffusion():
    DUST = []
    for y in range(R):
        for x in range(C):
            if MAP[y][x] > 0:
                DUST.append((MAP[y][x], y, x))
    for d in DUST:
        cnt = 0
        for i in range(4):
            ty = d[1] + dy[0][i]
            tx = d[2] + dx[0][i]
            if 0 <= ty < R and 0 <= tx < C and MAP[ty][tx] != -1:
                cnt += 1
                MAP[ty][tx] += d[0] // 5
        MAP[d[1]][d[2]] -= (d[0] // 5) * cnt

def findair():
    for i in range(R):
        if MAP[i][0] == -1:
            return i

def actair():
    MAP[fa-1][0] = 0
    MAP[fa+2][0] = 0
    init = [-1, 2]
    it = [1, 0]
    for i in range(2):
        y = fa + init[i]
        x = 0
        d = 0
        while d < 4:
            ty = y + dy[i][d]
            tx = x + dx[i][d]
            if d == 3 and tx == 0:
                MAP[ty][1] = 0
                break
            if ty == fa + it[i]:
                d += 1
                continue
            if 0 <= ty < R and 0 <= tx < C:
                MAP[y][x] = MAP[ty][tx]
                y, x = ty, tx
            else:
                d += 1
fa = findair()

while T:
    T -= 1
    diffusion()
    actair()
ret = 0
for y in range(R):
    for x in range(C):
        if MAP[y][x] > 0:
            ret += MAP[y][x]
print(ret)