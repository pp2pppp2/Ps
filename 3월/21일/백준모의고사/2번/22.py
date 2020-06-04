import sys

sys.stdin = open("2.txt")

N,M,G,R = map(int, input().split())

garden = [list(map(int, input().split())) for _ in range(N) ]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

candi = []
for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            candi.append([j,i])

# print(candi)
# print(spread)
# print(garden)

green =[0] *len(candi)
red = [0] * len(candi)
n = len(candi)

def bfs(q,spread):
    global result
    cnt = 0
    while q:
        t = q.pop(0)
        tx,ty,tc,tt = t

        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]
            if 0<=ny< N and 0 <= nx < M:
                if garden[ny][nx] != 0:
                    if spread[ny][nx] == -1 :
                        spread[ny][nx] = [tc,tt+1]
                        q.append([nx,ny,tc,tt+1])

                    elif spread[ny][nx] == 5:
                        pass
                    elif spread[ny][nx][0] == tc:
                        pass
                    else:
                        if spread[ny][nx][1] == tt+1:
                            cnt += 1
                            spread[ny][nx] = 5
    [print(s) for s in spread]

    if result < cnt :
        result = cnt


def rcomb(k,q):
    if n - q < R - k:
        return
    if k == R:
        print(green)
        print(red)
        print()
        spread = [[-1 for _ in range(M)] for _ in range(N)]
        q =[]
        for i in range(n):
            if green[i] == 1:
                spread[candi[i][1]][candi[i][0]] =[1,0]
                q.append(candi[i]+[1,0])
            if red[i] == 1:
                spread[candi[i][1]][candi[i][0]] =[2,0]
                q.append(candi[i] + [2,0])
        bfs(q,spread)
        return

    else:
        if green[q] == 0:
            red[q] = 1
            rcomb(k + 1, q + 1)
            red[q] = 0
            rcomb(k, q + 1)

        else:
            rcomb(k,q+1)

def gcomb(k,q):
    if n-q < G-k:
        return
    if k == G:
        rcomb(0,0)
        return

    else:
        green[q] = 1
        gcomb(k+1,q+1)
        green[q] = 0
        gcomb(k,q+1)

result = 0
gcomb(0,0)
print(result)