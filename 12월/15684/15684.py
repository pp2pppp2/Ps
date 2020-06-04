import sys

sys.stdin = open('15684.txt')

import copy
def comb(y, x, t, k):
    global flag # 1-1 2-2... 다 되면 1
    if flag == 1:
        return
    if t == k:
        temp_ans = 0
        for i in range(1,N+1): # 각 가로줄에서 출발
            temp_x = i
            for temp_y in range(0, H):
                for dir in range(-1,1):
                    t_temp_x = temp_x + dir
                    if t_temp_x <= 0 or t_temp_x >= N+1:
                        continue
                    if temp_checked[temp_y+1][t_temp_x] == 1:
                        if dir == -1:
                            temp_x = t_temp_x
                            break
                        if dir == 0:
                            temp_x += 1

            if temp_x == i:
                temp_ans += 1
            else:
                break
        if temp_ans == N:
            flag = 1
            return
    else:
        for i in range(x, N):
            for j in range(y, H):
                if temp_checked[j][i]:
                    continue
                temp_checked[j][i] = 1
                if i >= 2:
                    if not temp_checked[j][i-1]:
                        temp_checked[j][i - 1] = 3
                if i <= N - 1:
                    if not temp_checked[j][i+1]:
                        temp_checked[j][i + 1] = 3
                comb(y+1, x, t+1, k)
                temp_checked[j][i] = 0
                if i >= 2 and temp_checked[j][i-1]==3:
                    temp_checked[j][i - 1] = 0
                if i <= N-1 and temp_checked[j][i+1]==3:
                    temp_checked[j][i + 1] = 0


## 만들어지면 할 일


N, M, H = map(int, input().split()) #가로, 다리 수, 세로
if M ==0:
    print(0)
else:
    checked = [[0 for _ in range(N+1)] for _ in range(H+1)]
    ladder = [] # 기존 사다리
    flag = 0 # 안되면 0
    ans = -1
    for _ in range(M):
        y, x = map(int, input().split())
        ladder.append([x,y])
        checked[y][x] = 1

        if x >= 2:
            checked[y][x-1] = 2
        if x <= N-1:
            checked[y][x+1] = 2

    for k in range(0,4):
        flag = 0
        temp_checked = copy.deepcopy(checked)
        comb(1, 1, 0, k)
        if flag == 1:# 됫으면 거서 멈추세용
            ans = k
            break
    print(ans)