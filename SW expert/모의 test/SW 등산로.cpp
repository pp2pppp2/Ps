#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>

using namespace std;

struct Max_point {
	int x, y;
};

Max_point mp[5];
int mp_cnt,mp_tmp,result,result_tmp,tmp;
int tg = 0;
int park[8][8], visit[8][8] = { 0 };
int T, N, K;

int dx[4] = { 0, 0 ,1 ,-1 };
int dy[4] = { 1, -1, 0, 0 };

bool iswall(int i, int x, int y)
{
	int tx = x + dx[i];
	int ty = y + dy[i];
	if (tx == -1 || ty == -1 || tx == N || ty == N)
		return false;
	return true;
}

void solve(int x, int y)
{
	if (result < result_tmp)
		result = result_tmp;
	for (int i = 0; i < 4; i++) {
		if (iswall(i, x, y) && !visit[y + dy[i]][x + dx[i]]) {
			if (park[y][x] > park[y + dy[i]][x + dx[i]]) {
				visit[y][x]++;
				result_tmp++;
				solve(x + dx[i], y + dy[i]);
				visit[y][x]--;
				result_tmp--;
			}
			else if (!tg) {
				tg++;
				tmp = park[y + dy[i]][x + dx[i]];
				for (int n = 1; n < K+1; n++) {
					park[y + dy[i]][x + dx[i]]--;
					if (park[y][x] > park[y + dy[i]][x + dx[i]]) {
						visit[y][x]++;
						result_tmp++;
						solve(x + dx[i], y + dy[i]);
						visit[y][x]--;
						result_tmp--;
					}
				}
				park[y + dy[i]][x + dx[i]] = tmp;
				tg--;
			}
		}
	}		
}

int main()
{	
	//freopen("input.txt", "r", stdin);
	cin >> T;
	for (int tc = 0; tc < T; tc++) {
		cin >> N >> K;
		mp_tmp = 0;
		result = 0;
		for (int i = 0; i < N; i++)	{
			for (int j = 0; j < N; j++)	{
				cin >> park[i][j];
				if (park[i][j] > mp_tmp) {
					memset(mp, 0, sizeof(mp));
					mp_cnt = 0;
					mp_tmp = park[i][j];
					mp[mp_cnt].x = j;
					mp[mp_cnt].y = i;
				}
				else if (park[i][j] == mp_tmp)	{
					mp_cnt++;
					mp[mp_cnt].x = j;
					mp[mp_cnt].y = i;
				}
			}
		}
		for (int i = 0; i < mp_cnt + 1; i++){
			result_tmp = 1;
			solve(mp[i].x, mp[i].y);
		}
		cout << "#" << tc+1 << " "<< result << '\n';
	}
	return 0;
}