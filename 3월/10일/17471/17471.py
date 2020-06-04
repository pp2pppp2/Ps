import sys
sys.stdin = open('17471.txt')

N = int(input())
MAP = list(map(int, input().split()))
po = sum(MAP)
co = [[0 for _ in range(N)] for _ in range(N)]
visit = [0] * N

for n in range(N):
    TMP = list(map(int, input().split()))
    for t in range(1, TMP[0]+1):
        co[n][TMP[t]-1] = 1

def isco(val):
    q = []
    v = [-1] * N
    for i in range(N):
        if visit[i] == val:
            q.append(i)
            v[i] = val
            break
    while q:
        t = q.pop(0)
        for i in range(N):
            if co[t][i] == 1 and v[i] == -1 and visit[i] == val:
                q.append(i)
                v[i] = val
    for i in range(N):
        if visit[i] == val and v[i] != val:
            return False
    return True

def cal():
    if isco(0) and isco(1):
        tmp = 0
        for i in range(N):
            if visit[i]:
                tmp += MAP[i]
        return abs(tmp - (po - tmp))
    return 9999999

def dfs(n, k):
    global ret
    if n == k:
        return cal()
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            ret = min(ret, dfs(n+1, k))
            visit[i] = 0
    return ret
ret = 9999999
for i in range(N//2+1, 0, -1):
    dfs(0, i)
print(ret if ret != 9999999 else -1)