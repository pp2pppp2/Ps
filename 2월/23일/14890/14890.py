import sys
sys.stdin = open("14890.txt")

N, L = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

dy = [[0, 0], [1, -1]]
dx = [[1, -1], [0, 0]]
b = [0] * N
c = [0] * N

def chk(i, a, v):
    global b, c
    if v:
        y, x = a, i
    else:
        y, x = i, a
    ty = y + dy[v][0]
    tx = x + dx[v][0]
    if 0 <= ty < N and 0 <= tx < N:
        if MAP[y][x] == MAP[ty][tx]:
            return True
        elif abs(MAP[y][x] - MAP[ty][tx]) == 1:
            if MAP[y][x] > MAP[ty][tx]:
                tmp = MAP[ty][tx]
                tty = ty
                ttx = tx
                if not v:
                    b[ttx] = 1
                else:
                    c[tty] = 1
                for a in range(1, L+1):
                    if 0 <= tty < N and 0 <= ttx < N:
                        if not v:
                            b[ttx] = 1
                        else:
                            c[tty] = 1
                        if tmp != MAP[tty][ttx]:
                            return False
                    else:
                        return False
                    tty = tty + dy[v][0]
                    ttx = ttx + dx[v][0]
            else:
                tty = y
                ttx = x
                tmp = MAP[y][x]
                if not v:
                    if b[ttx]:
                        return False
                else:
                    if c[tty]:
                        return False
                for a in range(1, L+1):
                    if 0 <= tty < N and 0 <= ttx < N:
                        if not v:
                            if b[ttx]:
                                return False
                        else:
                            if c[tty]:
                                return False
                        if tmp != MAP[tty][ttx]:
                            return False
                    else:
                        return False
                    tty = tty - dy[v][0]
                    ttx = ttx - dx[v][0]
            return True
    return False

def can(i, v):
    global b, c
    b = [0] * N
    c = [0] * N
    for a in range(N-1):
        if not chk(i, a, v):
            return False
    return True
ret = 0
for i in range(N):
    if can(i, 0):
        ret += 1
    if can(i, 1):
        ret += 1
print(ret)