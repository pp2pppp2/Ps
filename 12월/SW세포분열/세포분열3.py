import sys
sys.stdin = open('5653.txt')

def set_status():
    for n in range(N):  # 세로
        for m in range(M):  # 가로
            if type(status[n][m]) == int and status[n][m] > -cells[n][m]:
                status[n][m] -= 1

def breed():
    for n in range(N):  # 세로
        for m in range(M):  # 가로
            if status[n][m] == 0:
                for d in range(4):
                    temp_m = m + dx[d]
                    temp_n = n + dy[d]

                    # if temp_m < 0 or temp_m >= M or temp_n < 0 or temp_n >=N:
                    #     continue

                    if cells[temp_n][temp_m] == 0:
                        status[temp_n][temp_m] = cells[n][m] + 1
                        cells[temp_n][temp_m] = cells[n][m]

                    elif cells[temp_n][temp_m] + 1 == status[temp_n][temp_m] and cells[temp_n][temp_m] < cells[n][m]:  # cell에 이미 세포가잇을때
                        status[temp_n][temp_m] = cells[n][m] + 1
                        cells[temp_n][temp_m] = cells[n][m]

T = int(input())
dx = [1, 0, -1, 0]  # 오 밑 왼 위
dy = [0, 1, 0, -1]

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # 세로크기, 가로크기, 시간 후
    cells = [[0 for _ in range(2 * K + M)] for _ in range(K)]  # 세포
    status = []
    ans = 0
    for i in range(N):
        cells.append([0 for _ in range(K)] + list(map(int, input().split())) + [0 for _ in range(K)])

    cells += [[0 for _ in range(2 * K + M)] for _ in range(K)]

    N += 2 * K
    M += 2 * K

    for i in range(N):
        temp = []
        for j in range(M):
            if cells[i][j] == 0:
                temp.append('')
            else:
                temp.append(cells[i][j])
        status.append(temp)

    for k in range(K):  # k 시간 후
        breed()
        set_status()  # 시간 check

        # print(cells)
        # break

    for n in range(N):
        for m in range(M):
            if type(status[n][m]) == int and status[n][m] > -cells[n][m]:
                ans += 1

    # [print(cells[i]) for i in range(len(cells))]
    # [print(status[i]) for i in range(len(status))]
    print(ans)