import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
MARS = [list(map(int, input().split())) for _ in range(n)]
