#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include<string.h>
#include <stdio.h>


int N;
int X;
int search[22];
int search2[22];
int search3[22];
int NOPE;
using namespace std;

int jud(int search[], int a) {
	if (a > X && search[a] - search[a - 1] == 1) {
		for (int b = 1; b < X + 1; b++) {
			if (search[a] - search[a - b] != 1)
				return 1;
			else
				search3[a - b]++;
		}
	}
	if (a > 0 && a < X && search[a] - search[a - 1] == 1) 
		return 1;
	if (a > 0 && search[a] - search[a - 1] > 1)
		return 1;
	return 0;
}
int jud2(int search[], int a) {
	
	if (a < N - X && search[a] - search[a + 1] == 1) {
		for (int b = 1; b < X + 1; b++) {
			if (search[a] - search[a + b] != 1 || search3[a + b])
				return 1;
		}
	}
	if (a < N - 1 && a > N - X - 1 && search[a] - search[a + 1] == 1) 
		return 1;
	if (a < N - 1 && search[a] - search[a + 1] > 1) 
		return 1;
	return 0;
}

using namespace std;

int main(int argc, char** argv)
{
	int map[20][20];
	freopen("input.txt" , "r" , stdin);
	int test_case;
	int T;
	int ret;
	int ret2;
	int cnt;


	cin >> T;



	for (test_case = 1; test_case <= T; ++test_case)
	{
		memset(search3, 0, sizeof(search3));
		ret = 0;
		ret2 = 0;
		cnt = 0;
		NOPE = 0;

		cin >> N;
		cin >> X;
		
		for (int a = 0; a < N; a++)	{
			for (int b = 0; b < N; b++)	{
				cin >> map[a][b];
			}
		}

		for (int row = 0; row < N; row++)
		{
			for (int col = 0; col < N; col++){
				search[col] = map[row][col];
				search2[col] = map[col][row];
			}
			//ÆÇº°
			for (int c = 0; c < N; c++) {
				ret += jud(search, c);
			}
			for (int d = 0; d < N; d++)	{
				ret += jud2(search, d);
			}
			memset(search3, 0, sizeof(search3));
			for (int e = 0; e < N; e++) {
				ret2 += jud(search2, e);
			}
			for (int f = 0; f < N; f++) {
				ret2 += jud2(search2, f);
			}
			memset(search3, 0, sizeof(search3));

			if (ret)
				cnt++;
			if (ret2)
				cnt++;

			ret = 0;
			ret2 = 0;
		}
		cnt = N * 2 - cnt;
		cout << "#" << test_case << " " << cnt << "\n";
	}
	return 0;
}