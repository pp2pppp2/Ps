import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    k = int(input())
    Q = list(map(int, input().split()))
    tmp = Q[0]
    if tmp > 0:
        t = 1
    else:
        t = 0
    ans = 0
    for i in Q:
        if t == 1 and i < 0:
            ans += tmp
            tmp = i
            t = 0
        elif t == 0 and i > 0:
            ans += tmp
            t = 1
        tmp = max(i, tmp)
    ans += tmp
    print(ans)