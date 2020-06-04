import sys
sys.stdin = open("text.txt")

def mst():
    u = 4
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
V = int(input())
E = int(input())
data = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    n1, n2, w = map(int, input().split())
    data[n1][n2] = w
    print(n1,n2,w)
D = [987654321] * (V + 1)
PI = [0] * (V + 1)
visit = [0] * (V + 1)
k = input()
print("#{} {}".format(1, mst()))
print(data)
print(D)
