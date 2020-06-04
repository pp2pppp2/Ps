import sys
sys.stdin = open('17070.txt')

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
memo = [[[-1 for _ in range(4)] for _ in range(N)] for _ in range(N)]
dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]

def wall(y, x, dir):
    for i in range(1, dir+1):
        if dir & i:
            ty = y + dy[i]
            tx = x + dx[i]
            if MAP[ty][tx]:
                return False
    return True

def d(y, x, dir):
    if y == x == N-1:
        return 1
    if memo[y][x][dir] == -1:
        memo[y][x][dir] = 0
    else: return memo[y][x][dir]
    for i in range(1,4):
        if dir & i:
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < N and 0 <= tx < N and wall(y,x,i):
                memo[y][x][dir] += d(ty, tx, i)
    return memo[y][x][dir]
print(d(0, 1, 1))
