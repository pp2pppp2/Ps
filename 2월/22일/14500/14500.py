import sys
sys.stdin = open("14500.txt")

dx = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 1, 2], [-1, 0, 0, 0], [0, 1, 2, 2]]
dy = [[0, 1, 2, 3], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 2, 2], [0, 1, 0, 0], [0, 0, 1, 2], [0, 0, 0, -1]]
dx.append([0, 0, 1, 1])
dy.append([-1, 0, 0, 1])
dx.append([0, 1, 0, -1])
dy.append([0, 0, 1, 1])
dx.append([-1, 0, 1, 0])
dy.append([0, 0, 0, 1])
dx.append([-1, 0, 0, 0])
dy.append([0, -1, 0, 1])
dx.append([-1, 0, 1, 0])
dy.append([0, 0, 0, -1])
dx.append([0, 0, 0, 1])
dy.append([-1, 0, 1, 0])
dx.append([0, 0, 0, -1])
dy.append([0, 1, 2, 2])
dx.append([0, 0, 1, 2])
dy.append([-1, 0, 0, 0])
dx.append([0, 1, 0, 0])
dy.append([0, 0, 1, 2])
dx.append([0, 1, 2, 2])
dy.append([0, 0, 0, 1])
dx.append([0, 0, 1, 1])
dy.append([0, 1, 0, -1])
dx.append([-1, 0, 0, 1])
dy.append([0, 0, 1, 1])


N, M = map(int, input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]

ret = 0
for y in range(N):
    for x in range(M):
        for d in range(len(dx)):
            MAX = 0
            for i in range(4):
                ty = y + dy[d][i]
                tx = x + dx[d][i]
                if 0 <= tx < M and 0 <= ty < N:
                    MAX += MAP[ty][tx]
                else:
                    continue
            ret = max(MAX,ret)
print(ret)