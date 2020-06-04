import sys
sys.stdin = open('1865.txt')

T = int(input())

def perm(n,k):
    global success
    if k == 0:
        return
    else:
        for i in range(N-1,k,-1):
            wp[k], wp[i] = wp[i], wp[k]
            temp_success = 1
            for i in range(N):
                temp_success *= table[wp[i] - 1][i]
                if temp_success <= success:
                    return
            if k == 1:
                print(wp)
                success = max(success, temp_success)
            perm(n,k-1)
            wp[k], wp[i] = wp[i], wp[k]

for tc in range(1,T+1):
    N = int(input()) #일의 수, 사람의 수
    table = [list(map(int,input().split()))for _ in range(N)]
    success = 0  # 모든 일이 성공할 확률
    wp = [_ for _ in range(1, N + 1)]

    for i in range(N):
        for j in range(N):
            table[i][j] *= 0.01

    perm(N,N-2)

    print( '#{} {}'.format(tc,"%0.6f" % round(success*100,7)))