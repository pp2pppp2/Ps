import sys
sys.stdin = open('A.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    print(1, N-1)