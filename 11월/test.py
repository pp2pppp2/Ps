for _ in range(int(input())):
    n=int(input())
    l=set()
    l.add(0)
    for i in range(1,int(pow(n,0.5))+10):
        t=n//i
        l.add(t)
        if t!=0:
            l.add(n//t)
    l=sorted(list(l))
    print(len(l))
    print(*l)