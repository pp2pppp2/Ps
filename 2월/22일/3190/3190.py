import sys
sys.stdin = open("3190.txt")

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
K = int(input())

MAP = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(K):
    y, x = map(int,input().split())
    MAP[y][x] = 1

L = int(input())

MOVE = [0] * 10001
for i in range(L):
    x, c = input().split()
    MOVE[int(x)] = c
T = 0
d = 0
MAP[1][1] = 2
q = [(1, 1)]
while 1:
    if MOVE[T] == "D":
        d = (d + 1) % 4
    if MOVE[T] == "L":
        d = (d + 3) % 4
    T += 1
    y, x = q[-1]
    ty = y + dy[d]
    tx = x + dx[d]
    if 1 <= ty < N+1 and 1 <= tx < N+1 and MAP[ty][tx] != 2:
        q.append((ty, tx))
        if MAP[ty][tx] == 0:
            ay, ax = q.pop(0)
            MAP[ay][ax] = 0
        MAP[ty][tx] = 2
    else:
        break
print(T)