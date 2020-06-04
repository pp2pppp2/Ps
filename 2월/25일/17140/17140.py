import sys
sys.stdin = open("17140.txt")

r, c, k = map(int, input().split())
TMP = [list(map(int, input().split())) for _ in range(3)]
MAP = [[0 for _ in range(100)] for _ in range(100)]

for y in range(3):
    for x in range(3):
       MAP[y][x] = TMP[y][x]
Y = 3
X = 3

def A():
    Y_tmp, X_tmp = 0, 0
    for y in range(Y):
        q = []
        cnt = [0] * 101
        for x in range(X):
            if x != 0:
                cnt[x] += 1
                q.append(x)
        tq = []
        for a in q:
            tq.append((a, cnt[a]))

def B():
    pass