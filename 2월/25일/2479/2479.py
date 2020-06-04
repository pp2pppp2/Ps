import sys
sys.stdin = open("2479.txt")

N, K = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
visit = [0] * (N + 1)
S, E = map(int, input().split())

def findham(i, j):
    cnt = 0
    for k in range(K):
        if MAP[i][k] != MAP[j][k]:
            cnt += 1
            if cnt == 2:
                return 0
    return cnt

def solve():
    q = [(S-1, 1)]
    visit[S] = -1
    while q:
        i, c = q.pop(0)
        for j in range(N):
            if findham(i, j) and visit[j+1] == 0:
                visit[j+1] = i+1
                if j == E - 1:
                    return True
                q.append((j, c+1))
    return False
if solve():
    a = E
    cnt = 0
    ans = []
    while visit[a] != -1:
        ans.append(a)
        a = visit[a]
    ans.append(S)
    print(" ".join(map(str, reversed(ans))))
else:
    print(-1)