import sys
sys.stdin = open('1953.txt')

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
m = [0, 15, 5, 10, 3, 6, 12, 9]
for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    q = [(R, C, 1)]
    MAP[R][C] += 16
    ret = 1
    while q:
        y, x, t = q.pop(0)
        if t == L: break
        for i in range(4):
            if m[MAP[y][x] - 16] & 1 << i:
                ty = y + dy[i]
                tx = x + dx[i]
                if 0 <= ty < N and 0 <= tx < M and MAP[ty][tx] < 16 and m[MAP[ty][tx]] & 1 << (i+2) % 4:
                    q.append((ty, tx, t+1))
                    MAP[ty][tx] ^= 16
                    ret += 1
    print("#{} {}" .format(tc, ret))