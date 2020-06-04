import sys
sys.stdin = open('17822.txt')

N, M, T = map(int, input().split())
CIRClE = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1]
dy = [0, 1, 0]
def search():
    q = []
    sum = 0
    cnt = 0
    for y in range(N):
        for x in range(M):
            if CIRClE[y][x]:
                sum += CIRClE[y][x]
                cnt += 1
                flag = 0
                for i in range(3):
                    ty = y + dy[i]
                    tx = (x + dx[i] + M ) % M
                    if 0 <= ty < N and 0 <= tx < M and CIRClE[y][x] == CIRClE[ty][tx]:
                        flag = 1
                        q.append((ty,tx))
                if flag:
                    q.append((y, x))
    if q:
        for i in q:
            CIRClE[i[0]][i[1]] = 0
    else:
        if cnt == 0:
            return
        avg = sum / cnt
        for y in range(N):
            for x in range(M):
                if CIRClE[y][x]:
                    if CIRClE[y][x] > avg:
                        CIRClE[y][x] -= 1
                    elif CIRClE[y][x] < avg:
                        CIRClE[y][x] += 1
def rot(x, d, k):
    if d == 0:
        k = M - (k % M)
    else:
        k = k % M
    for i in range(x - 1, N, x):
        for _ in range(k):
            q = CIRClE[i].pop(0)
            CIRClE[i].append(q)
for i in range(T):
    x, d, k = map(int, input().split())
    rot(x, d, k)
    search()

ret = 0
for y in range(N):
    for x in range(M):
        ret += CIRClE[y][x]
print(ret)