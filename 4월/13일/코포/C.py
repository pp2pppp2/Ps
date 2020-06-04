import sys
sys.stdin = open('a.txt')

T = int(input())
for tc in range(T):
    n = int(input())
    MAP = list(map(int, input().split()))
    d = dict()
    ma = 1
    ln = 0
    qq = n // 2
    for m in MAP:
        if d.get(m):
            d[m] += 1
            ma = max(ma, d[m])
        else:
            d[m] = 1
            ln += 1
    if ln == ma:
        ans = ma - 1
    else:
        ans = min(ma, ln)
    print(ans)