def iseq(a, b):
    if len(b) != len(a):
        return False
    for s in range(len(b)):
        if b[s] == '*':
            continue
        if a[s] != b[s]:
            return False
    return True


def d(n):
    global N, ad
    if n == N:
        ad.add("".join(map(str, sorted(gg))))
        return
    for i in range(M):
        print(i)
        if i == 3:
            print(n, v, gg)
        if bi[n][i] and v[i] == 0:
            v[i] = 1
            gg.append(i)
            print(n, i)
            d(n + 1)
            gg.pop()
            v[i] = 0


def solution(user_id, banned_id):
    global N, bi, v, ad, gg, M
    answer = 0
    N = len(banned_id)
    M = len(user_id)
    bi = [[0 for _ in range(M)] for _ in range(N)]
    v = [0] * M
    ad = set()
    gg = []
    for i in range(N):
        for j in range(len(user_id)):
            if iseq(user_id[j], banned_id[i]):
                bi[i][j] = 1
    print(bi)
    d(0)
    print(ad)
    print(len(ad))
    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
ban_id = ["fr*d*", "*rodo", "******", "******"]

solution(user_id, ban_id)