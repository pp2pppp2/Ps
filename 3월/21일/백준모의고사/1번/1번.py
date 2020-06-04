import sys
sys.stdin = open('1.txt')

N, M, K = map(int, input().split())
ANS = [[0 for _ in range(M)] for _ in range(N)]
S = []
SN = []

def rot(y, x, TMP):
    MAP = [[0 for _ in range(y)] for _ in range(x)]
    for Y in range(y):
        for X in range(x):
            MAP[X][y - Y - 1] = TMP[Y][X]
    return MAP

def isempty(y, x, ly, lx, TMP):
    for ty in range(ly):
        for tx in range(lx):
            if ANS[y+ty][x+tx] + TMP[ty][tx] == 2:
                return False
    for ty in range(ly):
        for tx in range(lx):
            ANS[y+ty][x+tx] += TMP[ty][tx]
    return True

def t(tN, tM, TMP):
    for a in range(4):
        for y in range(N - tN +1):
            for x in range(M - tM + 1):
                if isempty(y, x, tN, tM, TMP):
                    return
        TMP = rot(tN, tM, TMP)
        tN, tM = tM, tN

for k in range(K):
    tN, tM = map(int,input().split())
    TMP = [list(map(int, input().split())) for _ in range(tN)]
    t(tN,tM,TMP)

cnt = 0
for y in range(N):
    for x in range(M):
        if ANS[y][x]:
            cnt += 1
print(cnt)