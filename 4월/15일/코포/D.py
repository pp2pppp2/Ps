import sys
sys.stdin = open('input.txt')

def c(x, y, z):
    return (x - y) ** 2 + (y - z) ** 2 + (z - x) ** 2

T = int(input())

for tc in range(T):
    r,g,b = map(int,input().split())
    r = list(map(int, input().split()))
    g = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = []
    r = max(r), min(r)
    g = max(g), min(g)
    b = max(b), min(b)
    ans = 999999999999999999999999999999
    for i in r:
        for j in g:
            for k in b:
                ans = min(ans, c(i, j, k))
    print(ans)

