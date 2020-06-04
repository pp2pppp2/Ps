import sys
sys.stdin = open('5653.txt')

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def breed():
    global ACT, ACT_BREED, DEACT, ans

    ACT_BREED_TMP = []
    DEACT_TMP = []

    for deact in DEACT: # 비활성상태
        ty = deact[0]
        tx = deact[1]
        deact[2] -= 1
        if MAP[ty][tx] != deact[3]: continue # 동시에 번식하는경우 체크
        visit[ty][tx] = 1
        if deact[2]:    # 비활성시간이 남았다면
            DEACT_TMP.append(deact)
        else:       # 활성상태로 변하는 순간
            ACT_BREED_TMP.append([ty, tx, deact[3]])

    for act in ACT_BREED:
        for d in range(4): # 번식
            ty = act[0] + dy[d]
            tx = act[1] + dx[d]
            if visit[ty][tx] == 0 and MAP[ty][tx] < act[2]:
                MAP[ty][tx] = act[2]
                DEACT_TMP.append([ty, tx, act[2], act[2]])
        # 번식 후 활성상태로 남은 세포를 저장
        if act[2] - 1 > K:
            ans += 1
    # 1시간이 지난 애들 일괄적으로 처리하기 위해
    ACT_BREED = ACT_BREED_TMP[:]
    DEACT = DEACT_TMP[:]

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    TMP = [list(map(int, input().split())) for _ in range(N)]
    MAP = [[0 for _ in range(500)] for _ in range(500)] # 세포의 생명력 저장
    visit = [[0 for _ in range(500)] for _ in range(500)] # 세포 번식의 유무 판별

    ACT_BREED = [] # [y좌표, x좌표, 세포의 생명력]
    DEACT = [] # [y좌표, x좌표, 세포의 남은 생명력, 세포의 생명력]

    for y in range(N):
        for x in range(M):
            if TMP[y][x] > 0:
                MAP[y + 200][x + 200] = TMP[y][x]
                visit[y + 200][x + 200] = 1
                DEACT.append([y+200, x+200, TMP[y][x], TMP[y][x]])
    ans = 0
    while K:
        K -= 1
        breed()
    print("#{} {}".format(tc, ans + len(DEACT) + len(ACT_BREED)))