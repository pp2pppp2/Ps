import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n = int(input())
    if n % 4:
        print("NO")
        continue
    else:
        print("YES")
        tmp = 0
        s = 0
        for i in range(n//2):
            tmp += 2
            s += tmp
            print(tmp, end=" ")
        tmp = -1
        d = 0
        for i in range(n//2 - 1):
            tmp += 2
            d += tmp
            print(tmp, end=" ")
        print(s - d)
