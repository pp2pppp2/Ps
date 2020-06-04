import sys
sys.stdin = open("15683.txt")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
CAM = []
MAP = [list(map(int, input().split())) for _ in range(N)]
VISIT = [[0 for _ in range(M)] for _ in range(N)]
ret = 0
CAMD = [0] * 8
visitnum = 0
zero = 0
zero_tmp = 0
ran = [(0, 1, 1), (0, 3, 2), (0, 2, 1), (0, 3, 1)]
def init():
    global C, zero, zero_tmp
    q = []
    for y in range(N):
        for x in range(M):
            if 0 < MAP[y][x] < 5:
                CAM.append((y, x, MAP[y][x]))
            elif MAP[y][x] == 5:
                q.append((y, x))

    for a in q:
        y, x = a[0], a[1]
        for d in range(4):
            ty = y + dy[d]
            tx = x + dx[d]
            while 0 <= ty < N and 0 <= tx < M and MAP[ty][tx] < 6:
                if MAP[ty][tx] == 0:
                    MAP[ty][tx] = 5
                    zero_tmp += 1
                ty = ty + dy[d]
                tx = tx + dx[d]
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 0:
                zero += 1
def cal():
    global visitnum
    cnt = 0
    visitnum -= 1
    for c in range(len(CAM)):
        for d in range(ran[CAM[c][2] - 1][0], ran[CAM[c][2] - 1][1], ran[CAM[c][2] - 1][2]):
            y, x = CAM[c][0], CAM[c][1]
            ty = y + dy[(CAMD[c]+d) % 4]
            tx = x + dx[(CAMD[c]+d) % 4]
            while 0 <= ty < N and 0 <= tx < M and MAP[ty][tx] < 6:
                if MAP[ty][tx] < 1:
                    if MAP[ty][tx] == 0 or MAP[ty][tx] > visitnum:
                        MAP[ty][tx] = visitnum
                        cnt += 1
                ty = ty + dy[(CAMD[c] + d) % 4]
                tx = tx + dx[(CAMD[c] + d) % 4]
    return cnt

def d(n):
    global ret
    if n == len(CAM):
        ret = max(ret, cal())
        return
    if CAM[n][2] == 2:
        for j in range(1, 3):
            CAMD[n] = j
            d(n + 1)
            CAMD[n] = 0
    else:
        for j in range(4):
            CAMD[n] = j
            d(n + 1)
            CAMD[n] = 0
init()
d(0)
print(zero - ret)