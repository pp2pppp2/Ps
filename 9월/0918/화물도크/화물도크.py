import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    se = [[0, 30, 0] for _ in range(26)]
    for i in range(N):
        da = list(map(int, input().split()))
        if se[da[0]][1] > da[1]:
            se[da[0]] = da + [1]
    ret, tmp = 0, 30
    for i in range(25, -1, -1):
        if se[i][2] and tmp >= se[i][1]:
            tmp = se[i][0]
            ret += 1
    print("#{} {}".format(tc, ret))