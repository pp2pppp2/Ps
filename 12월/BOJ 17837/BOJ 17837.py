# import sys
# sys.stdin = open("input.txt")
#
# dx = [0, 1, -1, 0, 0]
# dy = [0, 0, 0, -1, 1]
# p = 0
#
# def move(idx, t, flag):
#     global p
#     ty = t[0] - 1 + dy[t[2]]
#     tx = t[1] - 1 + dx[t[2]]
#     tmp = []
#     if 0 > tx or tx >= N or 0 > ty or ty >= N or board[ty][tx] == 2:
#         if flag:
#             return
#         else:
#             if ho[idx - 1][2] % 2:
#                 ho[idx - 1][2] += 1
#             else:
#                 ho[idx - 1][2] -= 1
#             move(idx, t, 1)
#     else:
#         for d, i in enumerate(ma[t[0]-1][t[1]-1]):
#             if i == idx:
#                 sel = d
#         if board[ty][tx] == 1:
#             tmp = list(reversed(ma[t[0]-1][t[1]-1][sel:]))
#         else:
#             tmp = list(ma[t[0]-1][t[1]-1][sel:])
#         ma[t[0]-1][t[1]-1] = list(ma[t[0]-1][t[1]-1][:sel])
#         ma[ty][tx] += tmp
#         for b in tmp:
#             ho[b-1][0] = ty + 1
#             ho[b-1][1] = tx + 1
#         if len(ma[ty][tx]) >= 4:
#             p = 1
#
# N, K = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# ma = [[[] for _ in range(N)] for _ in range(N)]
# ho = [list(map(int, input().split())) for _ in range(K)]
#
# ret = 1
#
# for i in range(1, K+1):
#     ma[ho[i-1][0]-1][ho[i-1][1]-1] += [i]
#     if len(ma[ho[i-1][0]-1][ho[i-1][1]-1]) >= 4:
#         p = 1
# while ret < 1001:
#     for idx, i in enumerate(ho):
#         move(idx + 1, i, 0)
#     if p: break
#     ret += 1
#
# if ret == 1001:
#     ret = -1
# print(ret)
import sys

sys.stdin = open('input.txt')

dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]
N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
board_on = [[[] for _ in range(N)] for _ in range(N) ]

mal = [0]+[list(map(int, input().split())) for _ in range(K)]
mal_on = list(range(K+1))

for i in range(1,K+1):
    mal[i][0] -= 1
    mal[i][1] -= 1

for z in range(1,1+K):
    board_on[mal[z][0]][mal[z][1]] += [z]

result = 987654321

def reverse(x, k, rev, bef):
    rev[k] = x
    if mal_on[x] == x:
        mal_on[x] = bef
        return
    else:
        reverse(mal_on[x], k+1, rev, x)
    mal_on[x] = bef

def white(x,y, nx, ny, num):

    rest = []
    bye = []
    flag = 0
    for a in board_on[y][x]:
        if a == num:
            if board_on[ny][nx]:
                mal_on[a] = board_on[ny][nx][-1]
            else:
                mal_on[a] = a
            flag = 1
        if flag == 1:
            bye += [a]
            mal[a][0] = ny
            mal[a][1] = nx
        else:
            rest += [a]
    board_on[ny][nx] += bye
    board_on[y][x] = rest



def red(x,y,nx,ny,mal_num):
    rest = []
    bye = []
    flag = 0
    for a in board_on[y][x]:
        if a == mal_num:
            mal_on[a] = a
            flag = 1
        if flag == 1:
            bye += [a]
            mal[a][0] = ny
            mal[a][1] = nx
        else:
            rest += [a]
    reverse(bye[-1], 0, bye, bye[-1])

    # if board_on[ny][nx]:
    #     mal_on[bye[0]] = board_on[ny][nx][-1]
    # else:
    #     mal_on[a] = a

    board_on[ny][nx] += bye
    board_on[y][x] = rest


def blue(x,y,nx,ny,num):
    if mal[num][2] == 1 or mal[num][2] ==3:
        mal[num][2] += 1
    else:
        mal[num][2] -= 1
    nx = x +dx[mal[num][2]]
    ny = y +dy[mal[num][2]]
    if 0 <= nx < N and 0 <= ny < N:
        if board[ny][nx] == 0:  # 하얀
            white(x, y, nx, ny, num)
        elif board[ny][nx] == 1:
            red(x, y, nx, ny, num)

def game():
    turn = 0
    while turn < 1000:
        turn += 1
        for a in range(1,K+1):
            x = mal[a][1]
            y = mal[a][0]
            d = mal[a][2]

            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if board[ny][nx] == 0: #하얀
                    white(x,y,nx, ny, a)
                elif board[ny][nx] == 1:
                    red(x,y,nx,ny, a)
                else :
                    blue(x,y,nx,ny, a)
                if len(board_on[ny][nx]) >= 4:
                    return turn
            else:
                blue(x,y,nx,ny, a)
    return -1

print(game())