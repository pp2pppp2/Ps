import sys
sys.stdin = open("13458.txt")

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ret = N
for a in A:
    TMP = a
    TMP -= B
    if TMP < 0:
        continue
    ret += TMP // C
    if TMP % C:
        ret += 1
print(ret)