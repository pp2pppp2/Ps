import sys
sys.stdin = open('123.txt')

# def find(x):
#     if x == p[x]:
#         return x
#     else:
#         p[x] = find(p[x])
#         return p[x]
#
# def solve():
#     global ret
#     A, B = -1, -1
#     Anum, Bnum = 0, 0
#     for idx, i in enumerate(visited):
#         if i:
#             Anum += po[idx]
#             if A == -1:
#                 A = find(idx)
#             elif A != find(idx):
#                 return
#         else:
#             Bnum += po[idx]
#             if B == -1:
#                 B = find(idx)
#             elif B != find(idx):
#                 return
#     if abs(Anum - Bnum) < ret:
#         ret = abs(Anum - Bnum)
#
# def dfs(x, t, a):
#     if x == N - a:
#         solve()
#         return
#     for i in range(t, N):
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(x + 1, i, a)
#             visited[i] = 0
#
# N = int(input())
# po = list(map(int, input().split()))
# arr = [list(map(int, input().split()[1:])) for _ in range(N)]
# p = [_ for _ in range(N)]
# visited = [0] * N
#
# for idx, A in enumerate(arr):
#     for B in A:
#         FB = find(B-1)
#         FA = find(idx)
#         if FB != FA:
#             p[FB] = FA
# print(p)
# ret = 987654321
# for i in range(1, N):
#     dfs(0, 0, i)
#
# if ret == 987654321: ret = -1
# print(ret)
N = int(input())
p = list(map(int, input().split()))
cities = [list(map(int, input().split()))[1:] for _ in range(N)]
T = [0 for _ in range(N)]
ans = 12341234132412345134123
print(cities)


# 연결되어있는지 아닌지
def link(city, k):
    q = []
    for i in range(N):
        if city[i] == k:  # 첫 뭐시기 저시기이면???
            city[i] += 2
            q.append(i)
            break

    while q:
        t = q.pop()  # 노드 번호
        # print(t)
        for c in cities[t]:
            if city[c - 1] == k:
                city[c - 1] += 2
                q.append(c - 1)
    print(city)
    for i in city:
        if k in city:
            return False
    return True


# 부분집합 만드는 함수
def powerset(x):
    a = 0
    b = 0
    if x == N:
        print(T)
        if sum(T) == N or sum(T) == 0:
            return
        # if link(T, 1) and link(T, 0):
        #     pass

    else:
        T[x] = 1
        powerset(x + 1)
        T[x] = 0
        powerset(x + 1)


temp_cnt = powerset(0)

# if temp_cnt > cnt: