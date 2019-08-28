#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int q;
	int K;
	int cnt;
	int Max_cnt;
	int bss;
	vector<char> in;
	vector<char> out;
	vector<int> result_tmp;
	vector<int> result;

	freopen("input.txt", "r", stdin);

	cin >> K;
	cnt = 0;
	q = 3;
	Max_cnt = 1000001;
	bss = 0;

	in.assign(K, 0);
	out.assign(K, 0);
	result.assign(K+2, 0);
	result_tmp.assign(K+2, 0);

	for (int i = 0; i < K; i++)	{
		cin >> in[i];
	}

	for (int i = 0; i < K; i++)	{
		cin >> out[i];
		result[i] = in[i] ^ out[i];
		bss += in[i] ^ out[i];
	}

	if (bss){
		result_tmp = result;
		result_tmp[0] ^= 1;
		result_tmp[1] ^= 1;
		cnt++;

		for (int i = 0; i < K - 1; i++)	{
			if (result_tmp[i])	{
				for (int j = 0; j < 3; j++)
					result_tmp[i + j] ^= 1;
				cnt++;
			}
		}

		if (!result_tmp[K - 1])
			Max_cnt = cnt;
		result_tmp = result;
		cnt = 0;

		for (int i = 0; i < K - 1; i++)	{
			if (result_tmp[i])	{
				for (int j = 0; j < 3; j++)
					result_tmp[i + j] ^= 1;
				cnt++;
			}
		}

		if (!result_tmp[K - 1] && Max_cnt > cnt)
			Max_cnt = cnt;
		if (Max_cnt==1000001)
			Max_cnt = -1;

		if (Max_cnt != -1)	{
			cnt = 0;
			result_tmp = result;
			result_tmp[K - 1] ^= 1;
			result_tmp[K - 2] ^= 1;
			cnt++;

			for (int i = K - 1; i > 0; i--)	{
				if (result_tmp[i])	{
					if (i == 1)
						q = 2;
					else
						q = 3;
					for (int j = 0; j < q; j++)
						result_tmp[i - j] ^= 1;
					cnt++;
				}
			}

			if (!result_tmp[0] && Max_cnt > cnt)
				Max_cnt = cnt;
			result_tmp = result;
			cnt = 0;

			for (int i = K - 1; i > 0; i--)	{
				if (result_tmp[i])	{
					if (i == 1)
						q = 2;
					else
						q = 3;
					for (int j = 0; j < q; j++)	{
						result_tmp[i - j] ^= 1;
					}
					cnt++;
				}
			}
			if (!result_tmp[0] && Max_cnt > cnt)
				Max_cnt = cnt;
		}
	}
	else
		Max_cnt = 0;
	cout << Max_cnt;

	return 0;

}