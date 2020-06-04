dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]
D = [0, 0, 0, 0, 0, 0, 0]
def MOVE(d):
    if d==1:D[1],D[3],D[4],D[6]=D[4],D[1],D[6],D[3]
    elif d==2:D[1],D[3],D[4],D[6]=D[3],D[6],D[1],D[4]
    elif d==3:D[2],D[1],D[5],D[6]=D[1],D[5],D[6],D[2]
    else:D[2],D[1],D[5],D[6]=D[6],D[2],D[1],D[5]
N,M,y,x,K=map(int, input().split())
P=[list(map(int, input().split())) for _ in range(N)]
C=list(map(int, input().split()))
for d in C:
    ty = y + dy[d]
    tx = x + dx[d]
    if 0 <= ty < N and 0 <= tx < M:
        MOVE(d)
        if P[ty][tx]:
            D[6] = P[ty][tx]
            P[ty][tx] = 0
        else:P[ty][tx] = D[6]
        y, x = ty, tx
        print(D[1])