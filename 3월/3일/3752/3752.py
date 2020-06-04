import sys
sys.stdin = open('3752.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = list(map(int,input().split()))
    ret = {0}
    for m in sorted(MAP):
        tmp = list(ret)
        for t in tmp:
            ret.add(m + t)
    print("#{} {}" .format(tc, len(ret)))