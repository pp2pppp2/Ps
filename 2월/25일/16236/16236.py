import sys
sys.stdin = open("16236.txt")

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
T = 1
Sh = 2
def finds():
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == 9:
                MAP[y][x] = 0
                return y, x

def findf(ay, ax):
    global T
    flag = 0
    visit[ay][ax] = T
    q = [(ay, ax, 0)]
    ry, rx, rs = 999, 0, 0
    while q:
        y, x, s = q.pop(0)
        if flag:
            if s > rs:
                MAP[ry][rx] = 0
                return ry, rx, rs + 1
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < N and 0 <= tx < N and visit[ty][tx] < T:
                if 0 < MAP[ty][tx] < Sh:
                    flag = 1
                    if ry > ty:
                        ry, rx, rs = ty, tx, s
                    elif ry == ty and rx > tx:
                        ry, rx, rs = ty, tx, s
                elif MAP[ty][tx] == Sh or MAP[ty][tx] == 0:
                    q.append((ty, tx, s+1))
                    visit[ty][tx] = T
        if flag:
            if not q:
                MAP[ry][rx] = 0
                return ry, rx, rs + 1
    return -1, -1, 0
fy, fx = finds()
ret = 0
tmp = 0
while fy != -1 and fx != -1:
    fy, fx, s = findf(fy, fx)
    ret += s
    tmp += 1
    T += 1
    if tmp == Sh:
        Sh += 1
        tmp = 0
print(ret)
