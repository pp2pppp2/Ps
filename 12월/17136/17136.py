import sys
sys.stdin = open("17136.txt")

MAP = [list(map(int, input().split())) for _ in range(10)]
visit = [5 for _ in range(6)]
def istrue(y, x, i):
    if i == 1:
        return True
    for ay in range(i):
        for ax in range(i):
            if y + ay > 9 or x + ax > 9 or MAP[y+ay][x+ax] == 0:
                return False
    return True
def zero():
    for y in range(10):
        for x in range(10):
            if y == x == 9:
                break
            if MAP[y][x] == 1:
                return False
    return True
def dfs(y, x, n):
    global ret
    if ret <= n:
        return
    if y == x == 9:
        if MAP[y][x] == 1:
            if visit[1]:
                ret = min(ret, n + 1)
        else:
            ret = min(ret, n)
        return
    if MAP[y][x] == 0:
        if x  == 9:
            dfs(y+1, 0, n)
            return
        else:
            dfs(y, x+1, n)
            return
    for i in range(5, 0, -1):
        if visit[i] == 0: continue
        if istrue(y, x, i):
            for ay in range(i):
                for ax in range(i):
                    MAP[y+ay][x+ax] = 0
            visit[i] -= 1
            if x == 9:
                dfs(y + 1, 0, n+1)
            else:
                dfs(y, x + 1, n+1)
            visit[i] += 1
            for ay in range(i):
                for ax in range(i):
                    MAP[y+ay][x+ax] = 1
ret = 9999999
dfs(0, 0, 0)
print(ret if ret != 9999999 else -1)