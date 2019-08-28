#define _CRT_SECURE_NO_WARNINGS
#include<iostream>

using namespace std;
int map[12][12];
int visit[12][12];
int jong_scale;
int tmp;
int max_tmp;
int jong_cnt;
int jong[5];

int cal_js(int s, int x, int y)
{
	//int cnt = 0;
	for (int i = 0; i < s; i++)
	{
		if (!map[x +s -1][y + i] || !map[x + i][y + s -1])
		{
			return 0;
			//cnt++;
		}
	}
	//if (cnt == s)
	//	return cal_js(s + 1, x, y);
	//cnt = 0;
	//s--;
	for (int i = 0; i < s ; i++)
	{
		visit[x + s - 1][y + i] = 1;
		visit[x + i][y + s - 1] = 1;
	}

	return s;
}

void search(int x, int y, int q)
{
	visit[x][y] = 1;
	max_tmp = cal_js(q, x, y);
	if (max_tmp > 0)
	{
		jong_cnt++;
		jong[max_tmp - 1]--;
	}
	if (max_tmp == 0)
	{
		visit[x][y] = 0;
	}
	
}



int main()
{
	freopen("input.txt", "r", stdin);

	int b = 0;
	int a = 0;
	max_tmp = 0;
	jong_cnt = 0;

	for (int a = 0; a < 5; a++)
	{
		jong[a] = 5;
	}

	for (int i = 1; i <= 10; i++)
	{
		for (int j = 1; j <= 10; j++)
		{
			cin >> a;
			map[i][j] = a;
			visit[i][j] = 0;
		}
	}
	for (int k = 5; k > 0; k--)
	{
		for (int i = 1; i <= 10; i++)
		{
			for (int j = 1; j <= 10; j++)
			{
				if (map[i][j] && !visit[i][j])
				{
					search(i, j, k);
					if (max_tmp > 0) {
						if (jong[max_tmp - 1] < 0) {
							b = 1;
							break;
						}
					}
					max_tmp = 0;
				}
			}
			if (b == 1)
				break;
		}
	}
	if (b)
		cout << "-1";
	else
		cout << jong_cnt;
	return 0;
}