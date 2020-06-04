import sys
sys.stdin = open('14502.txt')

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    global num, ans
    q = deque()
    tmp = 0
    for i in SELECT:
        q.append((VI[i][0], VI[i][1], 0))
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= tx < N and 0 <= ty < N and MAP[ty][tx] != 1 and VISIT[ty][tx] < num:
                q.append((ty, tx, cnt+1))
                VISIT[ty][tx] = num
                if MAP[ty][tx] == 0:
                    tmp += 1
                    if ZERO == tmp:
                        return cnt+1
    return ans

def dfs(n, r):
    global num, ans
    if n == C:
        num += 1
        ans = min(ans, bfs())
        return
    for d in range(r, len(VI)):
        if SEL[d] == 0:
            SEL[d] = 1
            SELECT.append(d)
            dfs(n+1, d+1)
            SELECT.pop()
            SEL[d] = 0

N, C= map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
VISIT = [[0 for _ in range(N)] for _ in range(N)]
SEL = [0] * 10
SELECT = []
VI = []
ZERO = 0
ONE = 0
num = 1

for y in range(N):
    for x in range(N):
        if MAP[y][x] == 2:
            VI.append((y, x))
        elif MAP[y][x] == 0:
            ZERO += 1
if ZERO == 0:
    print(0)
else:
    ans = 9999999
    dfs(0, 0)
    print(ans if ans !=9999999 else -1)