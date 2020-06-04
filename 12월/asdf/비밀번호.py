import sys
sys.stdin = open("비밀번호.txt")

T = int(input())

def solve(r):  # 회차별 나오는 결과
    for i in range(r, N + r, M):
        temp_16num = numbers[i:i + M]
        # print(temp_16num)
        # print(temp_16num)
        temp_num = 0
        for j in range(M):
            t = ord(temp_16num[j])
            # print(f'이건 t다 {t}')
            if 48 <= t <= 57:
                temp_num += (ord(temp_16num[j]) - 48) * (16 ** (M - 1 - j))
                # print(f'이{j} 와{temp_16num} {temp_num}')
            else:
                temp_num += (ord(temp_16num[j]) - 55) * (16 ** (M - 1 - j))
                # print(f'이{j} 와{temp_16num} {temp_num}')
        # print(temp_num)
        result.append(temp_num)
    # print('끝')

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    M = N // 4

    numbers = 2 * input()
    result = []

    for i in range(M):
        solve(i)
        # print(i)
    # print(sorted(set(result)))
    print(sorted(set(result))[-K])

    # print(numbers)