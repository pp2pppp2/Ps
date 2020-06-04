import sys
sys.stdin = open("14503.txt")

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ret = 0

def clean(y, x):
    global ret
    MAP[y][x] = 2
    ret += 1

def seach(y, x, d):
    for i in range(4):
        td = (d - i - 1 + 4) % 4
        tx = x + dx[td]
        ty = y + dy[td]
        if 0 <= tx < M and 0 <= ty < N and MAP[ty][tx] == 0:
            act(ty, tx, td)
            return
    tx = x - dx[d]
    ty = y - dy[d]
    if 0 <= tx < M and 0 <= ty < N and MAP[ty][tx] != 1:
        seach(ty, tx, d)
        return

def act(y, x, d):
    clean(y, x)
    seach(y, x, d)

act(r, c, d)
print(ret)