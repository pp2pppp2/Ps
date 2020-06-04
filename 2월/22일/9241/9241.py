import sys
sys.stdin = open("9241.txt")

B = list(input())
A = list(input())
chk = 0
ans = 987654321
while B and B[-1] == A[len(A) - 1 - chk]:
    if chk >= len(A):
        ans = 0
        break
    chk += 1
    B.pop()
chks = -987654321
if ans:
    chks = 0
    while B and chks < len(A) and chks < len(B) and B[chks] == A[chks]:
        chks += 1
    if len(A) - chk - chks < 0:
        chks = -987654321
        ans = 0
print(min(len(A) - chk - chks, ans))