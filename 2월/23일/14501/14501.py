import sys
sys.stdin = open("14501.txt")

N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]
def D(n, s):
    global ret
    if n > N:
        return
    ret = max(ret, s)
    for i in range(n, N):
        D(i + C[i][0], s + C[i][1])
ret = 0
D(0, 0)
print(ret)