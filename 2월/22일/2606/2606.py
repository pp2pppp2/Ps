import sys
sys.stdin = open("2606.txt")

N = int(input())
M = int(input())
MAP = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit = [0] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    MAP[a][b] = 1
    MAP[b][a] = 1
visit[1] = 1
q = [1]
ans = 0
while q:
    t = q.pop(0)
    for i in range(1, N+1):
        if visit[i]: continue
        if MAP[t][i]:
            q.append(i)
            visit[i] = 1
            ans += 1
print(ans)