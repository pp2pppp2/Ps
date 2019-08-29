// FAIL //
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
int Max;
int map[752][752];
int N;
int M;
int a;
int temp;
int Max_temp;
using namespace std;

int mine(int mine , int x , int y){
	for (int a = 1; a <= mine; a++)
	{
		if (!map[x + a][y + a] || !map[x - a][y + a])
			return 0;
		if (!map[x + a][y + mine * 2 - a] || !map[x - a][y + mine * 2 - a])
			return 0;
	}
	return mine;
}

int search(int Max_sea, int x , int y){
	for (int i = Max_temp; i <= Max; i++)
	{
		temp = mine(i, x, y);
		if (Max_temp < temp)
			Max_temp = temp;
	}
	return Max_temp;
}

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int test_case;
	int T;
	int result;
	int result_tem;
	char x;
	int mine_cnt;
	int c;

	memset(map, 0, sizeof(map));



	freopen("input.txt", "r", stdin);

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> N;
		cin >> M;
		c = 0;
		temp = 0;
		result = 0;
		mine_cnt = 0;

		if (N > M){	
			if (M % 2)
				Max = M / 2;
			else
				Max = M / 2 - 1;
		}
		else{
			if (N % 2)
				Max = N / 2;
			else
				Max = N / 2 - 1;
		}
		
		for (int n = 1; n <= N; n++)	{
			for (int m = 1; m <= M; m++) {
				cin >> x;
				map[m][n] = x - '0';
				mine_cnt += x - '0';
			}
		}
		if (mine_cnt == 1)
			c = 1;
		else if (mine_cnt == 0)
			c = 2;
		else if (Max > mine_cnt / 4)
		{
			c = 3;
			Max = mine_cnt;
		}

		Max_temp = 0;
		if (!c || c==3)
		{
			for (int a = 1; a <= N; a++)
			{
				for (int b = 1; b <= M; b++)
				{
					if (map[a][b] || !(N + 1 - a < 2 * Max_temp + 1 || b - Max_temp < 0 || b + Max_temp > N))
					{
						result_tem = search(Max, b, a);
						if (result < result_tem)
							result = result_tem;
						if (result == Max)
							break;
					}
				}
				if (result == Max)
					break;
			}
			cout << "#" << test_case << " " << result + 1 << '\n';
		}
		else if (c == 1)
			cout << "#" << test_case << " " << 1 << '\n';
		else if (c == 2)
			cout << "#" << test_case << " " << 0 << '\n';
		
		
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
