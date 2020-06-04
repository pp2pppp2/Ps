import sys
sys.stdin = open("16637.txt")

N = int(input())
MAP = list(input())
NUM =[]
OP = []
ret = -0xffffffff
for i in range(N):
    if i % 2:
        OP.append(MAP[i])
    else:
        NUM.append(int(MAP[i]))

def cal(ln, rn, l):
    if OP[l] == '+':
        return ln + rn
    elif OP[l] == '-':
        return ln - rn
    elif OP[l] == '*':
        return ln * rn

def d(l, r, ln, rn, tn, f):
    global ret
    if r == len(OP)-1:
        ret = max(ret, cal(cal(ln,rn,l), tn, r))
        if not f:
            ret = max(ret, cal(ln, cal(rn,tn,r), l))
        return
    d(r, r+1, cal(ln,rn,l), tn, NUM[r+2], 0)
    if f == 0:
        d(l, r+1, ln, cal(rn, tn, r), NUM[r+2], 1)
if N == 1:
    print(NUM[0])
elif N == 3:
    print(cal(NUM[0], NUM[1], 0))
else:
    d(0, 1, NUM[0], NUM[1], NUM[2], 0)
    print(ret)
