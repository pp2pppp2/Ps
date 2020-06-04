import sys
sys.stdin = open('1952.txt')

T = int(input())
def d(n, s):
    global ret
    if n >= 12:
        ret = min(ret, s)
        return
    if MON[n]:
        d(n+1, s + MON[n] * PRICE[0])
        d(n+1, s + PRICE[1])
        d(n+3, s + PRICE[2])
    else:
        d(n+1, s)

for tc in range(1, T+1):
    ret = 99999999
    PRICE = list(map(int, input().split()))
    MON = list(map(int, input().split()))
    d(0, 0)
    print("#{} {}" .format(tc, min(ret, PRICE[3])))