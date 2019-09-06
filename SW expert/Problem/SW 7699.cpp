#include<iostream>
#include<string.h>
#define _CRT_SECURE_NO_WARNINGS
int visit[21][21];
char land[21][21];
bool landmark['Z' - 'A' + 1];
int landmark_num;
int R, C, Max, limit;

using namespace std;
void search(int x, int y)
{
	if (landmark[land[x][y] - 'A'])	{
		return;
	}
	landmark[land[x][y] - 'A'] = true;
	landmark_num++;

	if (Max < landmark_num)
		Max = landmark_num;
	if (Max == limit)
		return;
	
	visit[x][y] = 1;
	if (y != 0 && visit[x][y - 1] == 0) {
		search(x, y - 1);
	}
	if (x != R - 1 && visit[x + 1][y] == 0) {
		search(x + 1, y);
	}
	if (y != C - 1 && visit[x][y + 1] == 0) {
		search(x, y + 1);
	}
	if (x != 0 && visit[x - 1][y] == 0) {
		search(x - 1, y);
	}
	visit[x][y] = 0;
	landmark_num--;
	landmark[land[x][y] - 'A'] = false;
}
int main(int argc, char** argv)
{
	int test_case;
	int T;
	//freopen("input.txt", "r", stdin);
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		memset(landmark, 0, sizeof(landmark));			
		cin >> R >> C;
		landmark_num = 0;
		limit = 0;
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				cin >> land[r][c];
				if (!landmark[land[r][c]-'A'])	{
					landmark[land[r][c]-'A'] = true;
					limit++;
				}
			}
		}
		memset(landmark, 0, sizeof(landmark));
		Max = 0;
		search(0, 0);
		cout << "#" << test_case << " " << Max << '\n';
	}
	return 0;
}
