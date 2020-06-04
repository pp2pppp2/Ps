import sys
sys.stdin = open('17135.txt')


from copy import deepcopy

N, M, D = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visit = [0 for _ in range(M)]
E = []
A = []

for y in range(N):
    for x in range(M):
        if MAP[y][x]:
            E.append([y, x])
def cal():
    Et = deepcopy(E)
    cnt = 0
    while Et:
        s = []
        for y, x in A:
            left = 100
            dist = 1000
            sel = -1
            for i in range(len(Et)):
                d = abs(Et[i][0] - y) + abs(Et[i][1] - x)
                if d <= D:
                    if dist > d:
                        sel = i
                        dist = d
                        left = Et[i][1]
                    elif dist == d and left > Et[i][1]:
                        sel = i
                        left = Et[i][1]
            if sel > -1:
                s.append(sel)
        for a in s:
            if Et[a][0] != 16:
                cnt += 1
            Et[a][0] = 16
        for i in range(len(Et)):
            Et[i][0] += 1
        Ett = []
        for y, x in Et:
            if 0 <= y < N:
                Ett.append([y, x])
        Et = deepcopy(Ett)
    return cnt

def dfs(x, r):
    global ret
    if r == 3:
        ret = max(ret, cal())
        return
    for i in range(x+1, M):
        A.append((N, i))
        dfs(i, r+1)
        A.pop()
ret =0
dfs(-1, 0)
print(ret)