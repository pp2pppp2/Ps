# pop(0) 해서 시간초과 남 ㅡㅡ 30분 날림 귀찮아도 deque 씁시다
N, K = map(int, input().split())
visit = [0] * 100001
from collections import deque
def bfs(n, k):
    q = deque()
    q.append((n, 0))
    while q:
        t, s = q.popleft()
        if visit[t] == 0:
            visit[t] = 1
            if t == k: return s
            if t > 0:
                q.append((t - 1, s+1))
            if t < 100000:
                q.append((t + 1, s + 1))
            if t <= 50000:
                q.append((t * 2, s + 1))
print(bfs(N, K))