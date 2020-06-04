import sys
sys.stdin =open('input.txt')


from collections import deque

def dfs(n, r):
    for i in MAP[n]:
        if v[i] == 0:
            v[i] = 1
            visit[i] = r + 1
            dfs(i, r+1)
            vc[n] += vc[i]
    visit[n] += vc[n]
    vc[n] -= 1

a, b = map(int, input().split())
MAP = [[] for _ in range(a+1)]
q = []
visit = [0] * (a+1)
v = [0] * (a+1)
vc = [0] * (a + 1)
for i in range(a-1):
    c, d = map(int, input().split())
    MAP[c].append(d)
    MAP[d].append(c)
q = []
b = []
q.append((1, 0))
v[1] = 1
while q:
    n, r = q.pop()
    b.append(n)
    for i in MAP[n]:
        if v[i] == 0:
            v[i] = 1
            visit[i] = r + 1
            q.append((i, r+1))

for i in b[::-1]:
    vc[MAP[i]] += vc[i]

a = [visit[i] - vc[i] for i in range(len(visit))]
print(sum(sorted(a[2:])[-b:]))
print(sum(sorted(visit[2:])[-b:]))

# n, k = map(int, input().split())
# g = [[] for _ in range(n)]
#
# for _ in range(n - 1):
#     i, j = map(lambda i: int(i) - 1, input().split())
#     g[i].append(j)
#     g[j].append(i)
#
# q = [0]
# c = [0] * n
# p = [None] + [0] * (n - 1)
# d = [0] + [None] * (n - 1)
#
# while True:
#     i = q.pop()
#     if i == -1: break
#
#     j = -(i + 1)
#     if j > 0: c[p[j]] += c[j] + 1; continue
#     q.append(j)
#     for j in g[i]:
#         if d[j] is not None: continue
#         d[j] = d[i] + 1
#         p[j] = i
#         q.append(j)
# sr = sorted([d[i] - c[i] for i in range(n)], reverse=True)
# print(sr)
# print(sum(sr[:k]))