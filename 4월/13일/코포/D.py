import sys
sys.stdin = open('a.txt')

T = int(input())
for tc in range(T):
    MAP = [list(input()) for _ in range(9)]
    MAP[0][6] = MAP[0][5]
    MAP[1][1] = MAP[1][0]
    MAP[2][5] = MAP[2][8]
    MAP[3][8] = MAP[3][5]
    MAP[4][2] = MAP[4][0]
    MAP[5][4] = MAP[5][7]
    MAP[6][7] = MAP[6][6]
    MAP[7][0] = MAP[7][1]
    MAP[8][3] = MAP[8][2]
    [print(''.join(M)) for M in MAP]