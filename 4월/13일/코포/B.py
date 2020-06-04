import sys
sys.stdin =open('a.txt')

T = int(input())

for tc in range(T):
    a, b, c = map(int, input().split())
    ans = ''
    tmp = 'abcdefghijklmnopqrstuvwxyz'
    tmp = tmp[:c]
    for i in range(a):
        ans += tmp[i%c]
    print(ans)