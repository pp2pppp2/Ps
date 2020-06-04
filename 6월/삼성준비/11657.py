
def sol():
    N, M = map(int, input().split())

    dist = [[] for _ in range(N + 1)]
    MAP = [9999999999999] * (N + 1)
    visit = [0] * (N + 1)
    qq = [0] * (N + 1)

    for m in range(M):
        A, B, C = map(int, input().split())
        dist[A].append((B, C))

    MAP[1] = 0
    qq[1] = 1

    q = [1]
    visit[1] = 1

    while q:
        t = q.pop(0)
        qq[t] = 0

        for d in dist[t]:
            n = d[0]
            c = d[1]

            if MAP[n] > MAP[t] + c:
                MAP[n] = MAP[t] + c

                if not qq[n]:
                    visit[n] += 1
                    if visit[n] >= N:
                        print('-1')
                        return
                q.append(n)
                qq[n] = 1

    for i in range(2, N+1):
        if MAP[i] != 9999999999999: print(MAP[i])
        else: print(-1)

sol()