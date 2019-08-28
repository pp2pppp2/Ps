#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>

using namespace std;
int tunel[50][50];
int visit[50][50];
int v_cnt[50][50];
int result;
int T, N, M, R, C, L;

int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

bool iswall(int x, int y, int i)
{
	int tx = x + dx[i];
	int ty = y + dy[i];
	if (i == 0 && tx != -1 && (tunel[y][x] == 1 || tunel[y][x] == 3 || tunel[y][x] == 6 || tunel[y][x] == 7) && (tunel[ty][tx] == 1 || tunel[ty][tx] == 3 || tunel[ty][tx] == 4 || tunel[ty][tx] == 5))
		return true;
	if (i == 1 && tx != M && (tunel[y][x] == 1 || tunel[y][x] == 3 || tunel[y][x] == 4 || tunel[y][x] == 5) && (tunel[ty][tx] == 1 || tunel[ty][tx] == 3 || tunel[ty][tx] == 6 || tunel[ty][tx] == 7))
		return true;
	if (i == 2 && ty != -1 && (tunel[y][x] == 1 || tunel[y][x] == 2 || tunel[y][x] == 4 || tunel[y][x] == 7) && (tunel[ty][tx] == 1 || tunel[ty][tx] == 2 || tunel[ty][tx] == 5 || tunel[ty][tx] == 6))
		return true;
	if (i == 3 && ty != N && (tunel[y][x] == 1 || tunel[y][x] == 2 || tunel[y][x] == 5 || tunel[y][x] == 6) && (tunel[ty][tx] == 1 || tunel[ty][tx] == 2 || tunel[ty][tx] == 4 || tunel[ty][tx] == 7))
		return true;

	return false;
}

void solve(int x, int y, int time) {
	if (!v_cnt[y][x]) {
		result++;
		v_cnt[y][x]++;
	}
	for (int i = 0; i < 4; i++)	{
		if (iswall(x, y, i) && !visit[y + dy[i]][x + dx[i]] && time + 1 < L){
			visit[y + dy[i]][x + dx[i]]++;
			solve(x + dx[i], y + dy[i], time + 1);
			visit[y + dy[i]][x + dx[i]]--;
		}
	}

}

int main()
{
	//freopen("input.txt", "r", stdin);
	cin >> T;
	for (int tc = 0; tc < T; tc++){
		cin >> N >> M >> R >> C >> L;
		memset(tunel, 0, sizeof(tunel));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				cin >> tunel[i][j];
			}
		}
		memset(visit, 0, sizeof(visit));
		memset(v_cnt, 0, sizeof(v_cnt));
		result = 0;
		visit[R][C]++;
		solve(C, R, 0);

		cout << "#" << tc + 1 << " " << result << '\n';
	}

	return 0;
}