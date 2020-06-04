import sys
sys.stdin = open("14888.txt")

N = int(input())
NUM = list(map(int, input().split()))
OP = list(map(int, input().split()))
retMin = 198987654321
retMax = -19847586944

def cal(s, i, n):
    if i == 0:
        return s + NUM[n]
    elif i == 1:
        return s - NUM[n]
    elif i == 2:
        return s * NUM[n]
    elif i == 3:
        if s < 0:
            return - (-s // NUM[n])
        return s // NUM[n]

def D(n, s):
    global retMin, retMax
    if n == N:
        retMin = min(retMin, s)
        retMax = max(retMax, s)
    for i in range(4):
        if OP[i]:
            OP[i] -= 1
            D(n+1, cal(s, i, n))
            OP[i] += 1
D(1, NUM[0])
print(retMax)
print(retMin)