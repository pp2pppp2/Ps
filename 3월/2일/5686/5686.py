import sys
sys.stdin = open('5686.txt')

def cal(a):
    s, i = 0, 0
    while len(a) != i:
        s *= 16
        s += int(a[i], 16)
        i += 1
    return s

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    NUM = input()
    n = N // 4
    NUM += NUM[:n]
    s = set()
    for i in range(N):
        s.add(NUM[i:i+n])
    print("#{} {}" .format(tc, cal(sorted(list(s), reverse=True)[K-1])))

