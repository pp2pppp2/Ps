import sys
sys.stdin = open("17779.txt")

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

def cal(ty, tx, d1, d2):
    P = [0] * 5
    for y in range(N):
        for x in range(N):
            if y < ty:
                if x <= tx:
                    P[0] += MAP[y][x]
                else:
                    P[1] += MAP[y][x]
            elif y < ty + d1 and x < tx - abs(y - ty):
                P[0] += MAP[y][x]
            elif y <= ty + d2 and x > tx + abs(y - ty):
                P[1] += MAP[y][x]
            elif y >= ty + d1 and y <= ty + d1 + d2 and x < tx - d1 + abs(y - ty) - d1:
                P[2] += MAP[y][x]
            elif y > ty + d2 and y <= ty + d1 + d2 and x > tx + d2 - abs(y - ty) + d2:
                P[3] += MAP[y][x]
            elif y > ty + d1 + d2:
                if x < tx - d1 + d2:
                    P[2] += MAP[y][x]
                else:
                    P[3] += MAP[y][x]
            else:
                P[4] += MAP[y][x]
    return abs(max(P) - min(P))
ret = 9999999
for y in range(N-1):
    for x in range(1, N-1):
        for d1 in range(1, x+1):
            for d2 in range(1, N-x):
                ret = min(ret, cal(y, x, d1, d2))
print(ret)