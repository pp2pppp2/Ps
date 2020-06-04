import sys
sys.stdin = open("2115.txt")

def findHoney(y, x, c, n, r):
    global b
    if n == M - 1:
        return r
    if c - MAP[y][x+1] >= 0:
        b = max(b, findHoney(y, x + 1, c - MAP[y][x + 1], n + 1, r + MAP[y][x+1] ** 2))
    b = max(b, findHoney(y, x + 1, c, n + 1, r))
    return b

def solve(y, x, r):
    MAX = 0
    for ty in range(y, N):
        for tx in range(0, N-M+1):
            if y == ty and tx < x : continue
            MAX = max(MAX, r+H[ty][tx])
    return MAX
T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    H = [[0 for _ in range(N-M+1)] for _ in range(N)]
    MAP = [list(map(int, input().split())) for _ in range(N)]
    for y in range(N):
        for x in range(N-M+1):
            b = 0
            H[y][x] = max(findHoney(y, x, C-MAP[y][x], 0, MAP[y][x] ** 2), findHoney(y, x, C, 0, 0))
    ret = 0
    for y in range(N):
        for x in range(N-M+1):
            if x + M >= N - M + 1:
                ret = max(ret, solve(y+1, 0, H[y][x]))
            else:
                ret = max(ret, solve(y, x+M, H[y][x]))
    print("#{} {}" .format(tc, ret))
