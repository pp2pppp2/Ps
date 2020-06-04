import sys
sys.stdin = open("원숭이.txt")

# K = int(input())
# W, H = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(H)]
# DIST = [[[987654421 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# hx = [1, 2, 2, 1, -1, -2, -2, -1]
# hy = [-2, -1, 1, 2, 2, 1, -1, -2]
# def bfs():
#     ret = 987654321
#     q = [[0, 0, 1, K]]
#     while q:
#         t = q.pop()
#         if t[1] == H-1 and t[0] == W-1:
#             ret = min(t[2], ret)
#             break
#         for i in range(4):
#             tx = t[0] + dx[i]
#             ty = t[1] + dy[i]
#             if 0 <= ty < H and 0 <= tx < W and MAP[ty][tx] == 0 and DIST[ty][tx][t[3]] > t[2]:
#                 DIST[ty][tx][t[3]] = t[2]
#                 q.append([tx, ty, t[2] + 1, t[3]])
#         if t[3] > 0:
#             for i in range(8):
#                 tx = t[0] + hx[i]
#                 ty = t[1] + hy[i]
#                 if 0 <= ty < H and 0 <= tx < W and MAP[ty][tx] == 0 and DIST[ty][tx][t[3] - 1] > t[2]:
#                     DIST[ty][tx][t[3]-1] = t[2]
#                     q.append([tx, ty, t[2]+1, t[3] - 1])
#     if ret == 987654321:
#         ret = 0
#     return ret - 1
# print(bfs())
#print(min(DIST[H-1][W-1])) if min(DIST[H-1][W-1]) != 987654421 else print(-1)

from collections import deque
K = int(input())
W, H = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(H)]
DIST = [[[987654321 for _ in range(K + 1)] for _ in range(W)] for _ in range(H)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
hx = [1, 2, 2, 1, -1, -2, -2, -1]
hy = [-2, -1, 1, 2, 2, 1, -1, -2]
DIST[0][0][K] = 987654321
def bfs():
    q = deque([[0, 0, 0, K]])
    while q:
        t = q.popleft()
        if t[1] == H-1 and t[0] == W-1:
            return t[2]
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if 0 <= ty < H and 0 <= tx < W and MAP[ty][tx] == 0 and DIST[ty][tx][t[3]] > t[2] + 1:
                DIST[ty][tx][t[3]] = t[2] + 1
                q.append([tx, ty, t[2] + 1, t[3]])
        if t[3] > 0:
            for i in range(8):
                tx = t[0] + hx[i]
                ty = t[1] + hy[i]
                if 0 <= ty < H and 0 <= tx < W and MAP[ty][tx] == 0 and DIST[ty][tx][t[3]-1] > t[2] + 1:
                    DIST[ty][tx][t[3]-1] = t[2] + 1
                    q.append([tx, ty, t[2] + 1, t[3] - 1])
    return -1
print(bfs())
