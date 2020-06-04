import sys
sys.stdin = open('a.txt')

T = int(input())

for tc in range(T):
    n = int(input())
    ans = n // 2
    if not n % 2:
        ans -= 1
    print(ans)