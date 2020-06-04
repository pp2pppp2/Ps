import sys
sys.stdin = open("input.txt")

def baby(tr):
    global flag
    if tr[0] == tr[1] == tr[2] or tr[0] == tr[1] - 1 == tr[2] - 2:
        flag = 1
def d(a, b, dep):
    global tr
    if dep == b:
        baby(tr)
        return
    if flag == 1:
        ret[a] = b
        return
    use = [0] * 10
    for i in range(b):
        if visit[i] == 0 and use[A[a][i]] == 0:
            visit[i] = 1
            use[A[a][i]] = 1
            tr += [A[a][i]]
            d(a, b, dep + 1)
            tr.pop()
            visit[i] = 0
def f(re):
    if re[0] == re[1] == 99:
        return 0
    if re[0] < re[1]:
        return 2
    return 1

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    A = [[], []]
    ret = [99] * 2
    for i in range(12):
        if i % 2:
            A[0] += [data[i]]
        else:
            A[1] += [data[i]]
    for a in range(2):
        flag = 0
        tr = []
        visit = [0] * 6
        for b in range(3, 7):
            d(a, b, 0)
            if ret[a] != 99:
                break
    print("#{} {}" .format(tc, f(ret)))
