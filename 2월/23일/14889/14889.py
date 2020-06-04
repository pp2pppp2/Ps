import sys
sys.stdin = open("14889.txt")

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
TEAM = [0] * 20
ret = 982374123
def cal():
    T = [0, 0]
    for i in range(N):
        for j in range(N):
            if TEAM[j] == TEAM[i]:
                T[TEAM[i]] += MAP[i][j]
    return abs(T[0] - T[1])

def d(n, r):
    global ret
    if r > N:
        return
    if n == N // 2:
        ret = min(ret, cal())
        return
    for i in range(r, N):
        TEAM[i] = 1
        d(n+1, i+1)
        TEAM[i] = 0
d(0, 0)
print(ret)