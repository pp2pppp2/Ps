import sys
sys.stdin = open("17140.txt")

from operator import itemgetter

r, c, k = map(int, input().split())
TMP = [list(map(int, input().split())) for _ in range(3)]
MAP = [[0 for _ in range(101)] for _ in range(101)]

def cal():
    global rx, ry
    if rx <= ry:
        for y in range(ry):
            t = []
            tn = []
            count = [0] * 101
            for x in range(rx):
                if MAP[y][x]:
                    count[MAP[y][x]] += 1
                    if count[MAP[y][x]] == 1:
                        tn.append(MAP[y][x])
            for n in tn:
                t.append((n, count[n]))
            cnt = 0
            for s in sorted(sorted(t, key=itemgetter(0)), key=itemgetter(1)):
                MAP[y][cnt] = s[0]
                if cnt == 100:
                    break
                cnt += 1
                MAP[y][cnt] = s[1]
                cnt += 1
            if rx > cnt:
                for i in range(cnt, rx):
                    MAP[y][i] = 0
            else:
                rx = cnt
    else:
        for x in range(rx):
            t = []
            tn = []
            count = [0] * 101
            for y in range(ry):
                if MAP[y][x]:
                    count[MAP[y][x]] += 1
                    if count[MAP[y][x]] == 1:
                        tn.append(MAP[y][x])
            for n in tn:
                t.append((n, count[n]))
            cnt = 0
            for s in sorted(sorted(t, key=itemgetter(0)), key=itemgetter(1)):
                MAP[cnt][x] = s[0]
                if cnt == 100:
                    break
                cnt += 1
                MAP[cnt][x] = s[1]
                cnt += 1
            if ry > cnt:
                for i in range(cnt, rx):
                    MAP[i][x] = 0
            else:
                ry = cnt

for y in range(3):
    for x in range(3):
        MAP[y][x] = TMP[y][x]
rx = 3
ry = 3
t = 0
while MAP[r-1][c-1] != k:
    cal()
    t += 1
    if t > 100:
        t = -1
        break
print(t)