import sys
sys.stdin = open("input.txt")

from collections import deque

def cal_score(p,i):
    yard = deque()
    score = 0
    outcount = 0
    while 1:
        if outcount == 3:
            while len(yard) != 0 and yard[-1] <= 3:
                yard.pop()
            score += len(yard)
            p = (p + 1) % 9
            break
        if INNING[i][PLAYER[p]] != 0:
            for y in range(len(yard)-1,-1, -1):
                if yard[y] > 3:
                    break
                yard[y] += INNING[i][PLAYER[p]]
            yard.append(INNING[i][PLAYER[p]])
        else:
            outcount += 1
        p = (p + 1) % 9
    return p, score

def PLAY():
    global cnt
    score = 0
    i = 0
    p = 0
    while i < N:
        memoza = memo[INNING[i][PLAYER[p]]][INNING[i][PLAYER[(p+1)%9]]][INNING[i][PLAYER[(p+2)%9]]][INNING[i][PLAYER[(p+3)%9]]][INNING[i][PLAYER[(p+4)%9]]][INNING[i][PLAYER[(p+5)%9]]][INNING[i][PLAYER[(p+6)%9]]][INNING[i][PLAYER[(p+7)%9]]][INNING[i][PLAYER[(p+8)%9]]][0]
        if memoza == -1:
            p_tmp, score_tmp = cal_score(p, i)
            score += score_tmp
            pp = 0
            if p_tmp > p:
                pp = p_tmp + 8 - p
            elif p_tmp < p:
                pp = p - p_tmp
            memo[INNING[i][PLAYER[p]]][INNING[i][PLAYER[(p + 1) % 9]]][INNING[i][PLAYER[(p + 2) % 9]]][
                INNING[i][PLAYER[(p + 3) % 9]]][INNING[i][PLAYER[(p + 4) % 9]]][INNING[i][PLAYER[(p + 5) % 9]]][
                INNING[i][PLAYER[(p + 6) % 9]]][INNING[i][PLAYER[(p + 7) % 9]]][INNING[i][PLAYER[(p + 8) % 9]]][0] = score_tmp
            memo[INNING[i][PLAYER[p]]][INNING[i][PLAYER[(p + 1) % 9]]][INNING[i][PLAYER[(p + 2) % 9]]][
                INNING[i][PLAYER[(p + 3) % 9]]][INNING[i][PLAYER[(p + 4) % 9]]][INNING[i][PLAYER[(p + 5) % 9]]][
                INNING[i][PLAYER[(p + 6) % 9]]][INNING[i][PLAYER[(p + 7) % 9]]][INNING[i][PLAYER[(p + 8) % 9]]][1] = pp
            p = p_tmp
        else:
            score += memoza
            p = (p + memo[INNING[i][PLAYER[p]]][INNING[i][PLAYER[(p + 1) % 9]]][INNING[i][PLAYER[(p + 2) % 9]]][
                INNING[i][PLAYER[(p + 3) % 9]]][INNING[i][PLAYER[(p + 4) % 9]]][INNING[i][PLAYER[(p + 5) % 9]]][
                INNING[i][PLAYER[(p + 6) % 9]]][INNING[i][PLAYER[(p + 7) % 9]]][INNING[i][PLAYER[(p + 8) % 9]]][1]) % 9
        i += 1
    return score


def d(n):
    global ret
    if n == 3:
        d(n+1)
        return
    if n == 9:
        ret = max(ret, PLAY())
        return
    else:
        for i in range(1,9):
            if visit[i] == 0:
                visit[i] = 1
                PLAYER[n] = i
                d(n + 1)
                visit[i] = 0

N = int(input())
cnt = 0
INNING = [list(map(int, input().split())) for _ in range(N)]
memo = [[[[[[[[[[-1,0] for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)]
visit = [0] * 9
PLAYER = [0] * 9
ret = 0
d(0)

print(ret)