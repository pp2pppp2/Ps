import sys
sys.stdin = open("input.txt")

dx = [[0, 0, 1, -2], [0, 0, 2, -1], [0, 0, 1, -1]]
dy = [[1, -2, 0, 0], [1, -1, 0, 0], [2, -1, 0, 0]]

next_status = [[2, 2, 1, 1], [1, 1, 0, 0], [0, 0, 2, 2]]

def dfs(y, x, s, n, sum):
    global num, ret, flag
    if n >= ret:
        return
    if sum == vbvb:
        ret = n
        if n == 9:
            aisdjfijasdf= 1
        return
    for i in range(4):
        ty = y + dy[s][i]
        tx = x + dx[s][i]
        if 0 > tx or M <= tx or 0 > ty or N <= ty: continue
        if MAP[ty][tx] == 0: continue
        if next_status[s][i] == 0:
            if visit[ty][tx] == 0:
                sum += 1
            visit[ty][tx] += 1
            dfs(ty, tx, 0, n+1, sum)
            visit[ty][tx] -= 1
            if visit[ty][tx] == 0:
                sum -= 1
        elif next_status[s][i] == 1:
            if tx + 1 >= M or MAP[ty][tx + 1] == 0: continue
            if visit[ty][tx] == 0:
                sum += 1
            if visit[ty][tx+1] == 0:
                sum += 1
            visit[ty][tx] += 1
            visit[ty][tx + 1] += 1
            dfs(ty, tx, 1, n+1, sum)
            visit[ty][tx] -= 1
            visit[ty][tx + 1] -= 1
            if visit[ty][tx] == 0:
                sum -= 1
            if visit[ty][tx+1] == 0:
                sum -= 1
        elif next_status[s][i] == 2:
            if ty + 1 >= N or MAP[ty + 1][tx] == 0: continue
            if visit[ty][tx] == 0:
                sum += 1
            if visit[ty + 1][tx] == 0:
                sum += 1
            visit[ty][tx] += 1
            visit[ty+1][tx] += 1
            dfs(ty, tx, 2, n+1, sum)
            visit[ty][tx] -= 1
            visit[ty+1][tx] -= 1
            if visit[ty][tx] == 0:
                sum -= 1
            if visit[ty+1][tx] == 0:
                sum -= 1

def solve(status):
    global flag, ret
    if status == 0:
        for p in initPosition:
            visit[p[0]][p[1]] = 1
            dfs(p[0], p[1], 0, 1, 1)
            visit[p[0]][p[1]] = 0
    elif status == 1:
        for p in initPosition:
            if p[1] + 1 >= M or MAP[p[0]][p[1] + 1] == 0: continue
            visit[p[0]][p[1]] = 1
            visit[p[0]][p[1] + 1] = 1
            dfs(p[0], p[1], 1, 1, 2)
            visit[p[0]][p[1]] = 0
            visit[p[0]][p[1] + 1] = 0
    elif status == 2:
        for p in initPosition:
            if p[0] + 1 >= N or MAP[p[0] + 1][p[1]] == 0: continue
            visit[p[0]][p[1]] = 1
            visit[p[0]+1][p[1]] = 1
            dfs(p[0], p[1], 2, 1, 2)
            visit[p[0]][p[1]] = 0
            visit[p[0] + 1][p[1]] = 0

T = int(input())
num = 2
for tc in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    initPosition = []
    ret = 11
    vbvb = 0
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 1:
                initPosition.append([y, x])
                vbvb += 1
    for s in range(3):
        solve(s)
    print("#{} {}".format(tc, -1 if ret == 11 else ret))
