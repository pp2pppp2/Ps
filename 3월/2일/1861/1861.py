import sys
sys.stdin = open('1861.txt')

T = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def search(i,x,y):
    global temp_cnt

    for k in range(4):
        temp_x = x + dx[k]
        temp_y = y + dy[k]
        if 0<= temp_x <= N-1 and 0<= temp_y <= N-1:
            if square[temp_y][temp_x] == i+1:
                visited[i] = 1
                temp_cnt += 1
                search(i+1,temp_x,temp_y)

for tc in range(1,T+1):
    N = int(input()) # 정사각형 한 면의 길이
    min = 1 # 방 번호
    min_cnt = 1
    square = [list(map(int,input().split()))for _ in range(N)] #사각형
    visited =[0 for _ in range(N**2+1)]

    for i in range(1,N**2+1):
        if visited[i] == 0:
            for x in range(N):
                for y in range(N):
                    if square[y][x] == i:
                        temp_cnt = 1
                        search(i,x,y)
                        if min_cnt < temp_cnt:
                            min, min_cnt = i, temp_cnt

    print("#{} {} {}" .format(tc, min, min_cnt))