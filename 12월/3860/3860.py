import sys
sys.stdin = open("input.txt")

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def cal():
    q = deque()
    q.append((0, 0, 0))
    visit[0][0] = 1
    ret = 987654321
    while q:
        y, x, T = q.popleft()
        if y == H - 1 and x == W - 1:
            ret = min(T, ret)
            continue
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < H and 0 <= tx < W and visit[ty][tx] == 0 and MAP[ty][tx] != 99999:
                visit[ty][tx] = 1
                q.append((ty, tx, T+1))
    return ret
while 1:
    W, H = map(int, input().split())
    if W == H == 0:
        break
    G = int(input())
    MAP = [[0 for _ in range(W)] for _ in range(H)]
    visit = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(G):
        y, x = map(int, input().split())
        MAP[y][x] = 99999
    cal()