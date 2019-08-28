#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>

using namespace std;

struct xy {
	int x, y;
};

xy first;
int T, N, result, cnt;
int cafe[20][20];
int de[101];
int dx[4] = { 1, -1, -1, 1 };
int dy[4] = { 1, 1, -1, -1 };

void solve(int x, int y, int s) {
	int tx = x + dx[s];
	int ty = y + dy[s];
	if (first.x == tx && first.y == ty && result < cnt){
		result = cnt+1;
		return;
	}
	if (tx != -1&& ty != -1 && tx != N && ty != N && de[cafe[ty][tx]] == 0) {
		de[cafe[ty][tx]]++;
		cnt++;
		solve(tx, ty, s);
		cnt--;
		de[cafe[ty][tx]]--;
	}
	if (s + 1 == 4)
		return;
	solve(x, y, ++s);	
}

int main() {
	freopen("input.txt", "r", stdin);
	cin >> T;
	for (int tc = 0; tc < T; tc++)
	{
		memset(de, 0, sizeof(de));
		result = 2;
		cin >> N;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> cafe[i][j];
			}
		}
		for (int i = 0; i < N - 2; i++) {
			for (int j = 1; j < N - 1; j++) {
				cnt = 0;
				first.x = j;
				first.y = i;
				de[cafe[i][j]]++;
				solve(j, i, 0);
				de[cafe[i][j]]--;
			}
		}
		if (result == 2)
			cout <<"#" << tc+1 <<" " << -1 <<"\n";
		else
			cout <<"#" << tc+1 << " " << result << "\n";
	}
	return 0;
}