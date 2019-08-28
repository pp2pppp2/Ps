#include<iostream>

int visit[21][21];
char land[21][21];
char landmark[26];
int landmark_num;
int R;
int C;
int Max;
int limit;

using namespace std;

void search(int x, int y)
{
	for (int a = 0; a < landmark_num; a++)
	{
		if (land[x][y] == landmark[a])

			return;
	}
	landmark[landmark_num] = land[x][y];
	landmark_num++;
	if (Max < landmark_num)
	{
		Max = landmark_num;
	}
	if (Max == limit)
	{
		return;
	}
	if (y != 0)
	{
		if (visit[x][y - 1] == 0)
		{
			visit[x][y] = 1;
			search(x, y - 1);

		}
	}
	if (x != R)
	{
		if (visit[x + 1][y] == 0)
		{
			visit[x][y] = 1;
			search(x + 1, y);


		}
	}
	if (y != C)
	{
		if (visit[x][y + 1] == 0)
		{
			visit[x][y] = 1;
			search(x, y + 1);


		}
	}
	if (x != 0)
	{
		if (visit[x - 1][y] == 0)
		{
			visit[x][y] = 1;
			search(x - 1, y);


		}
	}
	visit[x][y] = 0;
	landmark_num--;
}
int main(int argc, char** argv)
{
	int test_case;
	int T;
	int limit_num;




	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		for (int i = 0; i < 21; i++)
		{
			for (int j = 0; j < 21; j++)
			{
				visit[i][j] = 0;
				land[i][j] = ' ';
			}
		}
		for (int a = 0; a < 26; a++)
		{
			landmark[a] = ' ';
		}
		landmark_num = 0;
		cin >> R >> C;

		limit_num = 0;
		limit = 0;



		for (int r = 0; r < R; r++)
		{
			for (int c = 0; c < C; c++)
			{
				cin >> land[r][c];
			}
		}

		for (int i = 0; i < 21; i++)
		{
			for (int j = 0; j < 21; j++)
			{
				for (int a = 0; a < limit; a++)
				{
					if (land[i][j] == landmark[a])
					{
						limit_num = 1;
					}
				}

				if (limit_num == 0)
				{
					landmark[limit] = land[i][j];
					limit++;
				}

				limit_num = 0;
			}
		}

		Max = 0;
		for (int a = 0; a < 26; a++)
		{
			landmark[a] = ' ';
		}

		search(0, 0);
		if (Max == 1)
		{
			Max = 2;
		}
		cout << "#" << test_case << " " << Max - 1 << '\n';
	}
	return 0;
}