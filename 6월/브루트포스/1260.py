# 기본 BFS, DFS 코멘트도 할게 없음
def i(): return map(int, input().split());
N, M, V = i();MAP=[[0 for _ in range(N+1)] for _ in range(N+1)];visit=[0]*(N+1);visit[V]=1;
for z in range(M):
    A, B = i()
    MAP[A][B] = 1;MAP[B][A] = 1
def dfs(n):
    print(n, end=" ")
    for next in range(1, N+1):
        if MAP[n][next] and not visit[next]:
            visit[next] = 1
            dfs(next)
def bfs(n):
    q = [n]
    while q:
        t = q.pop(0)
        print(t, end=" ")
        for next in range(1, N+1):
            if MAP[t][next] and not visit[next]:
                visit[next] = 1
                q.append(next)
dfs(V);print();visit = [0]*(N+1);visit[V] = 1;bfs(V)