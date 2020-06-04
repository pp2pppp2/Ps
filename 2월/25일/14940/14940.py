import sys
sys.stdin = open("14940.txt")

from collections import deque
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(fy, fx):
    q = deque()
    q.append((fy, fx))
    MAP[fy][fx] = 0
    visit[fy][fx] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < N and 0 <= tx < M:
                if visit[ty][tx] == 0 and MAP[ty][tx] == 1:
                    MAP[ty][tx] = MAP[y][x] + 1
                    visit[ty][tx] = 1
                    q.append((ty, tx))
def init():
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 2:
                bfs(y, x)
                return
init()

for y in range(N):
    for x in range(M):
        if visit[y][x]:
            pass
        elif MAP[y][x]:
            print(-1, end=" ")
            continue
        print(MAP[y][x], end=" ")
    print()