import sys
sys.stdin = open("input.txt")

from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dt = [1, -1]

def findS():
    for f in range(L):
        for y in range(R):
            for x in range(C):
                if b[f][y][x] == 'S':
                    return f, y, x
def ise(f, y, x, ret):
    if b[f][y][x] == 'E':
        print("Escaped in {} minute(s).".format(ret))
        return True
def bfs(f):
    q = deque()
    q.append([f[0], f[1], f[2], 1])
    while q:
        t = q.popleft()
        for i in range(4):
            ty = t[1] + dy[i]
            tx = t[2] + dx[i]
            if 0 <= tx < C and 0 <= ty < R and b[t[0]][ty][tx] != '#':
                if ise(t[0], ty, tx, t[3]):
                    return
                b[t[0]][ty][tx] = '#'
                q.append([t[0], ty, tx, t[3]+1])
        for i in range(2):
            tf = t[0] + dt[i]
            if 0 <= tf < L and b[tf][t[1]][t[2]] != '#':
                if ise(tf, t[1], t[2], t[3]):
                    return
                b[tf][t[1]][t[2]] = '#'
                q.append([tf, t[1], t[2], t[3] + 1])
    print("Trapped!")

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break
    b = [[list(input()) for _ in range(R+1)] for _ in range(L)]
    visit = [0] * L
    bfs(findS())