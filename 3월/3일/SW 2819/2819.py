import sys
sys.stdin = open('2819.txt')

T = int(input())
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def search(pos,k,t_res):
    if k == 8:
        results.append(t_res)
        return

    x,y = pos

    for dir in range(4):
        temp_x = x + dx[dir]
        temp_y = y + dy[dir]
        if (0<= temp_x < 4) and ( 0<=temp_y<4 ):
            search([temp_x,temp_y],k+1,t_res+str(board[temp_y][temp_x]))


for tc in range(1,T+1):
    board = [list(map(int,input().split()))for _ in range(4)]
    results = []
    for i in range(4):
        for j in range(4):
            search([i,j],1,'')

    print('#{} {}'.format(tc, len(set(results))))