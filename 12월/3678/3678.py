import sys
sys.stdin = open('3678.txt')

CATAN = [1, 2, 3, 4, 5, 2, 3, 1, 4]
COUNT = [0, 2, 2, 2, 2, 1]

F, S, A, B, T = 1, 1, 1, 1, 2
AC, BC = 0, 0
for i in range(8, 10002):
    if T == 6:
        T = 0
        if A == B == 1:
            A += 1
            AC = 0
        else:
            A += 1
            B += 1
            AC = 0
            BC = 0
    if T < 3:
        if T % 2:
            if BC == 0:
                F += 1
            elif BC == B:
                S += 1
                T += 1
                BC = -1
            else:
                F += 1
                S += 1
            BC += 1
        else:
            if AC == 0:
                F += 1
            elif AC == A:
                S += 1
                T += 1
                AC = -1
            else:
                F += 1
                S += 1
            AC += 1
    else:
        if T % 2:
            if AC == 0:
                F += 1
            elif AC == A:
                S += 1
                T += 1
                AC = -1
            else:
                F += 1
                S += 1
            AC += 1
        else:
            if BC == 0:
                F += 1
            elif BC == B:
                S += 1
                T += 1
                BC = -1
            else:
                F += 1
                S += 1
            BC += 1
    MAX = 99999
    SEL = 0
    for num in range(1, 6):
        if num == CATAN[F] or num == CATAN[S] or num == CATAN[-1]: continue
        if MAX > COUNT[num]:
            MAX = COUNT[num]
            SEL = num
    COUNT[SEL] += 1
    CATAN.append(SEL)
print(COUNT)
print(CATAN)
C = int(input())
for c in range(C):
    tmp = int(input())
    print(CATAN[tmp-1])