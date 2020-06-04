import sys
sys.stdin = open("input.txt")
def s(a):
    return int(a)/ 100
def d(h, dep):
    global mt
    if mt >= h:
        return
    if dep == N:
        mt = max(mt, h)
        return
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            d(h * data[dep][i], dep+1)
            visit[i] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(s, input().split()))
    mt = 0
    visit = [0] * N
    d(100, 0)
    print("#%d" % tc , end=" ")
    print("%.6f" % mt)