import sys
sys.stdin = open('a.txt')

def calv(MAP):
    d = dict()
    for M in MAP:
        if d.get(M):
            d[M] += 1
        else:
            d[M] = 1
    q = []
    for i in range(1, 27):
        if d.get(i):
            q.append(i)
    return q, d
T = int(input())

for tc in range(T):
    n = int(input())
    MAP = list(map(int, input().split()))
    v, vd = calv(MAP)
    print(v, vd)