import sys
sys.stdin = open("input.txt")


def di(s):
    t = s
    visit[t] = 1
    tmp = 987654321
    for i in node[t]:
        if i[1] < tmp and visit[i[2]] == 0:
            tmp = i[1]
            j = i[2]
    visit[j] = 1
    for


n, m = int(input()), int(input())
node = [[] for _ in range(n+1)]
visit = [0] *(  n+1)
D = [987654321] * (n + 1)
for i in range(m):
    a, b, c = map(int, input().split())
    node[a].append([b, c])
s, e = map(int, input().split())


