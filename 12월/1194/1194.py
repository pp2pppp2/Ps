import sys
sys.stdin = open("input.txt")

import collections
N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
visit = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(300)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for y in range(N):
    for x in range(M):
        if MAP[y][x] == '0':
            MAP[y][x] = '.'
            fy, fx = y, x

def solve(y, x, KEYS, move):
    global ans
    q = collections.deque()
    q.append((y, x, KEYS))
    while q:
        yy, xx, KEY = q.popleft()
        for i in range(4):
            ty, tx = yy + dy[i] , xx + dx[i]
            if 0 <= ty < N and 0 <= tx < M:
                if visit[KEY][ty][tx]: continue
                if MAP[ty][tx] == '#': continue
                if 'a' <= MAP[ty][tx] <= 'f':
                    if (KEY & (1 << (ord(MAP[ty][tx]) - ord('a')))) == 0:
                        tmp_KEY = KEY + (1 << (ord(MAP[ty][tx]) - ord('a')))
                        q.append((ty, tx, tmp_KEY))
                        visit[tmp_KEY][ty][tx] = visit[KEY][yy][xx] + 1
                    else:
                        q.append((ty, tx, KEY))
                        visit[KEY][ty][tx] = visit[KEY][yy][xx] + 1
                elif 'A' <= MAP[ty][tx] <= 'F':
                    if KEY & (1 << (ord(MAP[ty][tx]) - ord('A'))):
                        q.append((ty, tx, KEY))
                        visit[KEY][ty][tx] = visit[KEY][yy][xx] + 1
                elif MAP[ty][tx] == '.':
                    q.append((ty, tx, KEY))
                    visit[KEY][ty][tx] = visit[KEY][yy][xx] + 1
                elif MAP[ty][tx] == '1':
                    ans = visit[KEY][yy][xx] + 1
                    return
ans = 987654321
solve(fy, fx, 0, 0)
if ans == 987654321:
    ans = -1
print(ans)