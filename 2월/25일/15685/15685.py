import sys
sys.stdin = open("15685.txt")

def asd(y, x):
    pass
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
MAP = [[0 for _ in range(101)] for _ in range(101)]
for n in range(int(input())):
    x, y, d, g = map(int, input().split())
    q = [d]
    q_tmp = [d]
    for i in range(g):
        q = q_tmp
        for j in reversed(q):
            q_tmp.append((j+1) % 4)
    for a in q:
        MAP[y][x] = 1
        y = y + dy[a]
        x = x + dx[a]
        MAP[y][x] = 1
ret = 0
for y in range(100):
    for x in range(100):
        if MAP[y][x+1] and MAP[y+1][x] and MAP[y+1][x+1] and MAP[y][x]:
            ret += 1
print(ret)
