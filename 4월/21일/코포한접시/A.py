import sys
sys.stdin = open('input.txt')

k = 1
kq = [1]
while k < 1000000001:
    k *= 2
    kq.append(k + kq[-1])

kq.pop(0)
T = int(input())
for tc in range(T):
    x = int(input())
    for i in kq:
        if x % i == 0:
            print(x // i)
            break