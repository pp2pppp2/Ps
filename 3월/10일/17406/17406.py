import sys
sys.stdin = open('17406.txt')

from copy import deepcopy

N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
O = [list(map(int, input().split())) for _ in range(K)]
visit = [0] * K
A = []
def calMin(TMAP):
    ret = 99999999
    for y in range(N):
        tmp = 0
        for x in range(M):
            tmp += TMAP[y][x]
        ret = min(tmp, ret)
    return ret

def sw(y, x, C, TMAP):
    for c in range(1, C+1):
        tmp = TMAP[y-c][x-c]
        for ty in range(y-c, y+c):
            TMAP[ty][x-c] = TMAP[ty+1][x-c]
        for tx in range(x-c, x+c):
            TMAP[y+c][tx] = TMAP[y+c][tx+1]
        for ty in range(y+c, y-c, -1):
            TMAP[ty][x+c] = TMAP[ty-1][x+c]
        for tx in range(x+c, x-c, -1):
            TMAP[y-c][tx] = TMAP[y-c][tx-1]
        TMAP[y-c][x-c+1] = tmp

def rot(C, TMAP):
    y, x, c = C
    sw(y-1, x-1, c, TMAP)

def op():
    TMAP = deepcopy(MAP)
    for i in A:
        rot(O[i], TMAP)
    return calMin(TMAP)

def dfs(n):
    global ans
    if n == K:
        ans = min(ans, op())
        return
    for i in range(K):
        if visit[i] == 0:
            visit[i] = 1
            A.append(i)
            dfs(n+1)
            A.pop()
            visit[i] = 0
ans = 999999999
dfs(0)
print(ans)