import sys
sys.stdin = open('B.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    NUM = list(map(int, input().split()))
    a = dict()
    ret = 0
    for n in NUM:
        if not a.get(n):
            a[n] = 1
            ret += 1
    print(ret)