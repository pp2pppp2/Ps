import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ca = list(map(int, input().split()))
    tr = list(map(int, input().split()))
    ca.sort()
    tr.sort()
    cnt = 0
    ret = 0
    while cnt < M and len(ca):
        tmp = ca.pop()
        if tmp <= tr[-1]:
            tr.pop()
            ret += tmp
            cnt += 1
    print("#{} {}".format(tc, ret))