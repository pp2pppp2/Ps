import sys
sys.stdin = open("15686.txt")

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
CH = []
HOME = []
visit = [0] * 14

for y in range(N):
    for x in range(N):
        if MAP[y][x] == 1:
            HOME.append((y, x))
        elif MAP[y][x] == 2:
            CH.append((y, x))

def cal():
    global ans
    ret = 0
    for j in HOME:
        MIN = 99999999
        for i in range(len(CH)):
            if visit[i] == 1:
                MIN = min(MIN, abs(CH[i][0]-j[0]) + abs(CH[i][1]-j[1]))
        ret += MIN
        if ret > ans:
            return -1
    return ret
def ch(n, r):
    global ans
    if n > len(CH):
        return
    if r == M:
        tmp = cal()
        if tmp == -1:
            return
        ans = tmp
        return
    visit[n] = 1
    ch(n+1, r+1)
    visit[n] = 0
    ch(n+1, r)
ans = 999999999
ch(0, 0)
print(ans)