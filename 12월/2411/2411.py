import sys
sys.stdin = open('2411.txt')

N, M, A, B = map(int, input().split())
DP = [[[0, 0] for _ in range(M+1)] for _ in range(N+1)]
VISIT = [[0 for _ in range(M+1)] for _ in range(N+1)]

for a in range(A):
    y, x = map(int, input().split())
    VISIT[y][x] = 1

for b in range(B):
    y, x = map(int, input().split())
    VISIT[y][x] = 2

flag = 0
flag2 = 0
for y in range(1, N+1):
    if VISIT[y][1] == 2:
        break
    if VISIT[y][1] == 1:
        flag += 1
        DP[y][1] = [1, flag]
    else:
        if flag:
            DP[y][1] = [1, flag]
        else:
            DP[y][1] = [1, 0]
if M >= 2:
    for x in range(2, M+1):
        for y in range(1, N+1):
            U = DP[y - 1][x]
            L = DP[y][x - 1]
            if VISIT[y][x] == 2:
                DP[y][x] = [0, -1]
            elif U[1] == L[1]:
                DP[y][x] = [U[0] + L[0], U[1]]
            elif U[1] == -1 or L[1] == -1:
                DP[y][x] = [U[0] + L[0], max(U[1], L[1])]
            else:
                if U[1] > L[1]:
                    DP[y][x] = [U[0], U[1]]
                else:
                    DP[y][x] = [L[0], L[1]]
            if VISIT[y][x] == 1:
                DP[y][x][1] += 1

if DP[N][M][1] == A:
    print(DP[N][M][0])
else:
    print(0)