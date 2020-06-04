import sys
sys.stdin = open('1107.txt')

def dfs(n, t):
    global ret
    if n == N_SIZE+1+t:
        return
    if n > max(0, N_SIZE-2):
        NN = len(str(int("".join(map(str, VISIT)))))
        ret = min(ret, NN + abs(N - int("".join(map(str, VISIT)))))
    for i in range(10):
        if BUTTON[i]:
            VISIT.append(i)
            dfs(n+1, t)
            VISIT.pop()

N = input()
N_SIZE = len(N)
N = int(N)
M = int(input())
BUTTON = [1 for _ in range(10)]
if M:
    K = list(map(int, input().split()))
    for k in K:
        BUTTON[k] = 0

VISIT = []
ret = abs(100 - N)

if M != 10:
    dfs(0, 0)
    for i in range(1, 10):
        if BUTTON[i] == 1:
            VISIT.append(i)
            dfs(1, 1)
            break
print(ret)