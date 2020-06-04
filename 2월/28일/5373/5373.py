import sys
sys.stdin = open('5373.txt')

T = int(input())
CUBE = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(6)]
color = ['w', 'r', 'o', 'g', 'b', 'y']
def init():
    for c in range(6):
        for y in range(3):
            for x in range(3):
                CUBE[c][y][x] = color[c]

def R(c1, c2, c3, rt, r, cb):
    for i in range(r):
        t1, t2, t3 = CUBE[cb[0]][c1[0][0]][c1[0][1]], CUBE[cb[0]][c2[0][0]][c2[0][1]], CUBE[cb[0]][c3[0][0]][c3[0][1]]
        for c in range(3):
            CUBE[cb[c]][c1[c][0]][c1[c][1]], CUBE[cb[c]][c2[c][0]][c2[c][1]], CUBE[cb[c]][c3[c][0]][c3[c][1]] = CUBE[cb[c+1]][c1[c+1][0]][c1[c+1][1]], CUBE[cb[c+1]][c2[c+1][0]][c2[c+1][1]], CUBE[cb[c+1]][c3[c+1][0]][c3[c+1][1]]
        CUBE[cb[3]][c1[3][0]][c1[3][1]], CUBE[cb[3]][c2[3][0]][c2[3][1]], CUBE[cb[3]][c3[3][0]][c3[3][1]] = t1, t2, t3

        t1, t2, t3 = CUBE[rt][0][0], CUBE[rt][0][1], CUBE[rt][0][2]
        CUBE[rt][0][0], CUBE[rt][0][1], CUBE[rt][0][2] = CUBE[rt][0][2], CUBE[rt][1][2], CUBE[rt][2][2]
        CUBE[rt][0][2], CUBE[rt][1][2], CUBE[rt][2][2] = CUBE[rt][2][2], CUBE[rt][2][1], CUBE[rt][2][0]
        CUBE[rt][2][2], CUBE[rt][2][1], CUBE[rt][2][0] = CUBE[rt][2][0], CUBE[rt][1][0], CUBE[rt][0][0]
        CUBE[rt][2][0], CUBE[rt][1][0], CUBE[rt][0][0] = t1, t2, t3


def C(a):
    r = 1
    if a[1] == '+':
        r = 3
    if a[0] == 'U':
        cb = [1, 3, 2, 4]
        c1 = [(0, 0), (0, 0), (0, 0), (0, 0)]
        c2 = [(0, 1), (0, 1), (0, 1), (0, 1)]
        c3 = [(0, 2), (0, 2), (0, 2), (0, 2)]
        R(c1, c2, c3, 0, r, cb)
    elif a[0] == 'D':
        cb = [1, 4, 2, 3]
        c1 = [(2, 0), (2, 0), (2, 0), (2, 0)]
        c2 = [(2, 1), (2, 1), (2, 1), (2, 1)]
        c3 = [(2, 2), (2, 2), (2, 2), (2, 2)]
        R(c1, c2, c3, 5, r, cb)
    elif a[0] == 'F':
        cb = [0, 4, 5, 3]
        c1 = [(2, 0), (0, 0), (0, 2), (2, 2)]
        c2 = [(2, 1), (1, 0), (0, 1), (1, 2)]
        c3 = [(2, 2), (2, 0), (0, 0), (0, 2)]
        R(c1, c2, c3, 1, r, cb)
    elif a[0] == 'B':
        cb = [0, 3, 5, 4]
        c1 = [(0, 0), (2, 0), (2, 2), (0, 2)]
        c2 = [(0, 1), (1, 0), (2, 1), (1, 2)]
        c3 = [(0, 2), (0, 0), (2, 0), (2, 2)]
        R(c1, c2, c3, 2, r, cb)
    elif a[0] == 'L':
        cb = [0, 1, 5, 2]
        c1 = [(0, 0), (0, 0), (0, 0), (2, 2)]
        c2 = [(1, 0), (1, 0), (1, 0), (1, 2)]
        c3 = [(2, 0), (2, 0), (2, 0), (0, 2)]
        R(c1, c2, c3, 3, r, cb)
    elif a[0] == 'R':
        cb = [0, 2, 5, 1]
        c1 = [(2, 2), (0, 0), (2, 2), (2, 2)]
        c2 = [(1, 2), (1, 0), (1, 2), (1, 2)]
        c3 = [(0, 2), (2, 0), (0, 2), (0, 2)]
        R(c1, c2, c3, 4, r, cb)


for tc in range(T):
    K = input()
    A = input().split()
    init()
    for a in A:
        C(a)
    [print("".join(i)) for i in CUBE[0]]