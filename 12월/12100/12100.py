import sys
sys.stdin = open('12100.txt')

from copy import deepcopy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def move(d):
    # up
    for y in range(sd[d % 2][0],sd[d % 2][1],sd[d % 2][2]):
        for x in range(sd[d % 2][0],sd[d % 2][1],sd[d % 2][2]):
            ty = y + dy[d]
            tx = x + dx[d]
            if 0 <= ty < N and 0 <= tx < N:
                if MAP[ty][tx] == 0:
                    qy, qx = ty, tx
                    while 0 <= qy < N and 0 <= qx < N and MAP[qy][qx]==0:
                        qy += dy[d]
                        qx += dx[d]
                    qx -= dx[d]
                    qy -= dy[d]
                    MAP[y][x], MAP[qy][qx] = MAP[qy][qx], MAP[y][x]
def mer(d):
    global ret
    flag = 0
    for y in range(sd[d % 2][0],sd[d % 2][1],sd[d % 2][2]):
        for x in range(sd[d % 2][0],sd[d % 2][1],sd[d % 2][2]):
            ty = y + dy[d]
            tx = x + dx[d]
            if 0 <= ty < N and 0 <= tx < N:
                if MAP[y][x] == MAP[ty][tx]:
                    MAP[y][x], MAP[ty][tx] = 0, 2*MAP[ty][tx]
                    ret = max(MAP[ty][tx], ret)
                    flag = 1
    if flag:
        return True
    return False

def cal():
    global ret, MAP
    MAP = deepcopy(MAP_T)
    for d in SEL:
        move(d)
        mer(d)
        move(d)
    return False
def dfs(n):
    global sum, ret
    if sum == ret:
        return
    if n == 5:
        cal()
        return
    for i in range(4):
        SEL.append(i)
        dfs(n+1)
        SEL.pop()

N = int(input())
sd = [(N-1, -1, -1),(0, N, 1)]
MAP_T = [list(map(int, input().split())) for _ in range(N)]
ret = 0
MAP = []
sum = 0
for y in range(N):
    for x in range(N):
        sum += MAP_T[y][x]
        ret = max(ret, MAP_T[y][x])
SEL = []

dfs(0)
print(ret)