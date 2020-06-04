import sys
sys.stdin = open('5656.txt')

from copy import deepcopy
T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def c(TMAP):
    for x in range(W):
        for y in range(H-1, -1, -1):
            if TMAP[y][x] == 0:
                flag = 1
                for ty in range(y-1, -1, -1):
                    if TMAP[ty][x]:
                        TMAP[ty][x], TMAP[y][x] = 0, TMAP[ty][x]
                        flag = 0
                        break
                if flag:
                    break

def b(i, v, TMAP):
    global cnt
    cnt += 1
    t = TMAP[i][v]
    TMAP[i][v] = 0
    for a in range(t):
        for dir in range(4):
            ty = i + dy[dir] * a
            tx = v + dx[dir] * a
            if 0 <= ty < H and 0 <= tx < W and TMAP[ty][tx]:
                b(ty, tx, TMAP)
    return t

def s(v, TMAP):
    for i in range(H):
        if TMAP[i][v]:
            return b(i, v, TMAP)
    return -1

def cal():
    global cnt
    TMAP = deepcopy(MAP)
    cnt = 0
    for v in V:
        if MAP[H-1][v]:
            if s(v, TMAP) > 1:
                c(TMAP)
    return cnt

def d(n):
    global ret
    if ret == ans:
        return
    if n == N:
        ret = max(ret, cal())
        return
    for i in range(W):
        V[n] = i
        d(n+1)

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(H)]
    V = [0] * N
    ans = 0
    for y in range(H):
        for x in range(W):
            if MAP[y][x]:
                ans += 1
    ret = 0
    d(0)
    print("#{} {}" .format(tc, ans-ret))