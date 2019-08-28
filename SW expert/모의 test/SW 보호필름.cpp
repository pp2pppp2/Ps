#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>

using namespace std;

int T, D, W, K;
int cell[13][20];
int cellcpy[13][20];
int B[20] = { 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 };
int A[20] = { 0 };
int result, cnt, recnt, real_result;

void solve(int cnt, int DW);

bool ss(int x, int c) {
	int tmp = 0;
	if (c == 1) {
		for (int i = 0; i < D - K + 1; i++) {
			tmp = 0;
			for (int j = 0; j < K; j++) {
				tmp += cellcpy[i + j][x];
			}
			if (tmp == 0 || tmp == K)
				return true;
		}
	}
	return false;
}


int ismatch() {
	for (int i = 0; i < W; i++) {
		if (!ss(i, 1)) {
			return 0;
		}
	}
	return 99;
}

void solve(int cnt, int DW) {
	if (cnt > D - 1 || recnt >= real_result)
		return;
	solve(cnt + 1, DW);
	if (DW)
		memcpy(cellcpy[cnt], A, sizeof(A));
	else
		memcpy(cellcpy[cnt], B, sizeof(B));
	recnt++;
	if (ismatch() && real_result > recnt)
		real_result = recnt;
	solve(cnt + 1, DW);
	if (DW)
		memcpy(cellcpy[cnt], cell[cnt], sizeof(A));
	else
		memcpy(cellcpy[cnt], cell[cnt], sizeof(B));
	recnt--;
}


int main()
{
	//freopen("input.txt", "r", stdin);
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> D >> W >> K;
		recnt = 0;
		real_result = K;
		for (int i = 0; i < D; i++) {
			for (int j = 0; j < W; j++) {
				cin >> cell[i][j];
			}
		}
		memcpy(cellcpy, cell, sizeof(cell));
		result = ismatch();
		if (result == 99)
			cout << "#" << tc << " " << 0 << "\n";
		else {
			solve(0, 1);
			solve(0, 0);
			cout << "#" << tc << " " << real_result << '\n';
		}
	}
}