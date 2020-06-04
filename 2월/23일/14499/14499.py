import sys
sys.stdin = open("14499.txt")

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

DICE = [0, 0, 0, 0, 0, 0, 0]

def MOVE(dir):
    if dir == 1:
        DICE[1], DICE[3], DICE[4], DICE[6] = DICE[4], DICE[1], DICE[6], DICE[3]
    elif dir == 2:
        DICE[1], DICE[3], DICE[4], DICE[6] = DICE[3], DICE[6], DICE[1], DICE[4]
    elif dir == 3:
        DICE[2], DICE[1], DICE[5], DICE[6] = DICE[1], DICE[5], DICE[6], DICE[2]
    elif dir == 4:
        DICE[2], DICE[1], DICE[5], DICE[6] = DICE[6], DICE[2], DICE[1], DICE[5]

N, M, y, x, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
C = list(map(int, input().split()))

for d in C:
    ty = y + dy[d]
    tx = x + dx[d]
    if 0 <= ty < N and 0 <= tx < M:
        MOVE(d)
        if MAP[ty][tx]:
            DICE[6] = MAP[ty][tx]
            MAP[ty][tx] = 0
        else:
            MAP[ty][tx] = DICE[6]
        y, x = ty, tx
        print(DICE[1])