import sys
sys.stdin = open('17825.txt')

H = list(map(int, input().split()))
N = [0] * 10
C = [(0, 1) for _ in range(4)]
def MOVE(i, cnt):
    global C
    n = C[i][0]
    t = C[i][1]
    while cnt:
        if t == 1:
            n += 2
        elif t == 2:
            n += 3
            if n > 19:
                n, t = 25, 5
        elif t == 3:
            n += 2
            if n > 24:
                n, t = 25, 5
        elif t == 4:
            if n == 30:
                n -= 1
            n -= 1
            if n < 26:
                n, t = 25, 5
        elif t == 5:
            n += 5
        cnt -= 1
    if t == 1:
        if n == 10:
            t = 2
        elif n == 20:
            t = 3
        elif n == 30:
            t = 4
    for a in range(4):
        if n == 40:
            if C[a][0] == n:
                return -1
        else:
            if C[a][0] == n and C[a][1] == t:
                return -1
    if n > 40:
        C[i] = (999, 0)
        return 0
    C[i] = (n, t)
    return n

def cal():
    global C
    sm = 0
    C = [(0, 1) for _ in range(4)]
    for id, i in enumerate(N):
        if C[i][0] <= 40:
            s = MOVE(i, H[id])
            if s == -1:
                return 0
            sm += s
        else:
            return 0
    return sm
def d(n):
    global ret
    if n == 10:
        ret = max(ret, cal())
        return
    else:
        for i in range(4):
            N[n] = i
            d(n+1)
ret = 0
d(0)
print(ret)