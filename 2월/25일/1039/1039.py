import sys
sys.stdin = open("1039.txt")

N, K = input().split()
N = list(N)
K = int(K)
memo =[[-1 for _ in range(11)] for _ in range(1000001)]
MAX = int(''.join(sorted(N)[::-1]))
ret = -1
ans = 0
def D(n):
    global ret, ans
    if memo[int(''.join(N))][n] != -1:
        return
    memo[int(''.join(N))][n] = 1
    if n == K:
        ret = max(ret, int(''.join(N)))
        return
    for i in range(len(N)-1):
        for j in range(len(N)):
            if j == i: continue
            if i == 0 and N[j] == '0': continue
            N[i], N[j] = N[j], N[i]
            D(n+1)
            N[i], N[j] = N[j], N[i]
D(0)
print(ret)