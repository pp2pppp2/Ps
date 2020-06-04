import sys
sys.stdin = open("input.txt")

def mst():
    u = 0
    D[u] = 0
    for i in range(V+1):
        print(visit)
        m = 987654321
        for j in range(V+1):
            if visit[j] == 0 and m > D[j]:
                m = D[j]
                u = j
        visit[u] = 1
        for v in range(V+1):
            if data[u][v] != 0 and visit[v] == 0 and D[u] + data[u][v] < D[v]:
                D[v] = D[u] + data[u][v]
                PI[v] = u
    return D[-1]
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        data[n1][n2] = w
    D = [987654321] * (V + 1)
    PI = [0] * (V + 1)
    visit = [0] * (V + 1)
    print("#{} {}".format(tc, mst()))
    print(D)
