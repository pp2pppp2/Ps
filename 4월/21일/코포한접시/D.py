import sys
sys.stdin = open('input.txt')

def calsum(tq):
    cnt = 0
    for i in range(n // 2):
        tmp = Q[i] + Q[-(i + 1)]
        if tmp != tq:
            if tmp < tq:
                mt = max(Q[i], Q[-(i + 1)])
                if tq > mt + k:
                    cnt += 2
                else:
                    cnt += 1
            elif tmp > tq:
                st = min(Q[i], Q[-(i + 1)])
                if tq < st + 1:
                    cnt += 2
                else:
                    cnt += 1
        if cnt > ans:
            return ans
    return cnt
T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    Q = list(map(int, input().split()))
    d = dict()
    q = []
    min_tmp = 9999999999
    max_tmp = 0
    for i in range(n//2):
        tmp = Q[i] + Q[-(i+1)]
        if d.get(tmp):
            d[tmp] += 1
        else:
            d[tmp] = 1
            q.append(tmp)
            min_tmp = min(tmp, min_tmp)
            max_tmp = max(tmp, max_tmp)
    q = sorted(q, key=lambda x:-d.get(x))
    ans = n // 2
    tq = q[0]
    tmp = d.get(tq)

    if d.get(tq) == 1:
        ans = calsum(min_tmp)
        ans = calsum(max_tmp)
    else:
        for i in range(len(q)):
            ans = calsum(q[i])
    print(ans)