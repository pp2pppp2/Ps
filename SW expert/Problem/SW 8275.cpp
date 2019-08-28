#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>

using namespace std;
int T, N, X, M;
vector<int> l(10), r(10), s(10);
vector<int> zip(6);
vector<int> result(6);
vector<int> tmp_vec(6);
int rt, tmp, cnt, tmp_sum, result_sum;

void solve()
{
	for (int a = 0; a <= X; a++){
		for (int b = 0; b <= X; b++){
			for (int c = 0; c <= X; c++){
				for (int d = 0; d <= X; d++){
					for (int e = 0; e <= X; e++)	{
						for (int f = 0; f <= X; f++){
							cnt = 0;
							for (int g = 0; g < M; g++)	{
								tmp = 0;
								for (int h = l[g] - 1; h < r[g]; h++)
									tmp += zip[h];
								if (tmp != s[g])
									break;
								else
									cnt++;
							}
							if (cnt == M) {
								rt++;
								if (rt == 1) {
									result_sum = 0;
									for (int loop = 0; loop < N; loop++) {
										result[loop] = zip[loop];
										result_sum += zip[loop];
									}
								}
								else {
									tmp_sum = 0;
									for (int loop = 0; loop < N; loop++) {
										tmp_sum += zip[loop];
									}
									if (tmp_sum > result_sum) {
										result_sum = tmp_sum;
										for (int loop = 0; loop < N; loop++) {
											result[loop] = zip[loop];
										}
									}
									if (tmp_sum == result_sum && tmp_vec > result) {
										result_sum = tmp_sum;
										for (int loop = 0; loop < N; loop++) {
											result[loop] = zip[loop];
										}
									}
								}
							}
							zip[0] -= 1;
						}
						if (N < 1)
							return;
						zip[0] = X;
						zip[1] -= 1;
					}
					if (N < 2)
						return;
					zip[1] = X;
					zip[2] -= 1;
				}
				if (N < 3)
					return;
				zip[2] = X;
				zip[3] -= 1;
			}
			if (N < 4)
				return;
			zip[3] = X;
			zip[4] -= 1;
		}
		if (N < 5)
			return;
		zip[4] = X;
		zip[5] -= 1;
	}
}

int main()
{
	//freopen("input.txt", "r", stdin);
	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++)
	{
		cin >> N >> X >> M;
		rt = 0;
		tmp_sum = 0;
		result_sum = 0;
		result.assign(6, 10);
		for (int i = 0; i < M; i++)	{
			cin >> l[i] >> r[i] >> s[i];
		}
		for (int i = 0; i < N; i++)	{
			zip[i] = X;
		}
		solve();
		if (rt)	{
			cout << "#" << test_case;
			for (int a = 0; a < N; a++)	{
				cout << " " << result[a];
			}
			cout << '\n';
		}
		else {
			cout << "#" << test_case;
			cout << " " << -1 << '\n';
		}
	}
	return 0;
}