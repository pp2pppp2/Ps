#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<math.h>
#include<cmath>

long long sult;
long long rere;
int re;
int M;
long long result2;

long long sum[1000000];


//long long mul(int N, long long sult)
//{
//	long long ssr = 0;
//	for (int i = 0; i < N ; i++)
//	{
//		ssr += sult;
//		if (ssr > 1000000007)
//			ssr %= 1000000007;
//		
//	}
//	return ssr;
//}
//
//long long cal(int N)
//{
//	if (N == 1)
//	{
//		return 1;
//	}
//	else if (N == 2)
//		return 4;
//	else
//	{
//		sult = 0;
//		for (int a = 0; a < N; a++)
//		{
//			sult += N;
//		}
//		for (int b = 0; b < N-2; b++)
//		{
//			sult = mul(N, sult);
//		}
//		return sult;
//	}
//}

long long cal2(long long rere, int N)
{
	long long tmp = 1;
	while (N)
	{
		if (N & 1) {
			tmp *= rere;
			tmp %= 1000000007;
		}
		N >>= 1;
		rere *= rere;
		rere %= 1000000007;

	}
	return tmp;
}


using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	int N;
	int result;
	//freopen("input.txt", "r", stdin);
	cin >> T;
	sum[0] = 1;
	for (int i = 1; i < 1000000; i++)
	{
		sum[i] = (sum[i - 1] + cal2(i + 1, i + 1))%1000000007;
	}

	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> N;
		cout << "# " << test_case << sum[N-1] << '\n';
		
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}