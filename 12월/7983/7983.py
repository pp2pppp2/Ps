import sys
sys.stdin = open("input.txt")

N = int(input())

WORK = [list(map(int, input().split())) for _ in range(N)]

WORK = sorted(WORK, key=lambda x: -x[1])
ret = 999999999999999999
for i in range(N):
    day = min(ret, WORK[i][1])
    ret = day - WORK[i][0]
print(ret)