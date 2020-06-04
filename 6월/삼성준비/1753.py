import heapq as h
def i():return map(int,input().split())
N,E=i();y=[[]for _ in range(N+1)]
t=[[10**9]*(N+1) for _ in range(3)]
while E:E-=1;u,v,w=i();y[u]+=[(v,w)];y[v]+=[(u,w)]
A,B=i();f=[1,A,B];
for i in range(3):
    p=[]
    h.heappush(p,(0,f[i]))
    t[i][f[i]]=0
    while p:
        d,a = h.heappop(p)
        for q in y[a]:
            n,w=q
            if t[i][n]>d+w:t[i][n]=d+w;h.heappush(p,(t[i][n],n))
ans=min(t[0][f[1]]+t[1][f[2]]+t[2][N],t[0][f[2]]+t[2][f[1]]+t[1][N])
print(-1if ans>=10**9 else ans)