import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    x, a, b = map(int, input().split())
    for i in range(a):
        x = min(x, x//2 + 10)
    for i in range(b):
        x -= 10
    if x <= 0:
        print('YES')
    else:
        print('NO')