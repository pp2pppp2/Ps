import sys
sys.stdin = open("7575.txt")

N, K = map(int,input().split())

IN = [[0] for _ in range(N)]
VI = [0] * 1000

def chkcode(index):
    codelen = 0
    for chk in IN[index]:
        if VI[codelen] == chk:
            codelen += 1
            if codelen == K:
                return True
        else:
            codelen = 0
    codelen = 0
    for chk in reversed(IN[index]):
        if VI[codelen] == chk:
            codelen += 1
            if codelen == K:
                return True
        else:
            codelen = 0
    return False

def isvirus():
    for i in range(1, N):
        if chkcode(i): continue
        return False
    return True

def createCode(index, dir):
    for i in range(K):
        VI[i] = IN[0][index + (i*dir)]

def solve():
    for i in range(len(IN[0])):
        if i <= len(IN[0]) - K:
            createCode(i, 1)
            if isvirus():
                print('YES')
                return
        elif K - 1 <= i:
            createCode(i, -1)
            if isvirus():
                print('YES')
                return
    print('NO')

for n in range(N):
    M = int(input())
    IN[n] = list(map(int, input().split()))

solve()