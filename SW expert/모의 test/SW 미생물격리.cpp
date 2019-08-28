#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>

using namespace std;
struct cel {
	int n, d, cn;
};
int T, N, M, K, x, y, tx, ty;
int dx[5] = { 0, 0, 0, -1, 1 };
int dy[5] = { 0, -1, 1, 0, 0 };
cel cell[100][100];
cel cell_tmp[100][100];

void cd() {
	if (ty == 0 || tx == 0 || ty == N - 1 || tx == N - 1) {
		cell_tmp[ty][tx].n /= 2;
		if (cell_tmp[ty][tx].d % 2)
			cell_tmp[ty][tx].d += 1;
		else
			cell_tmp[ty][tx].d -= 1;
	}
}

void move() {
	memset(cell_tmp, 0, sizeof(cell_tmp));
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < N; x++) {
			if (cell[y][x].n != 0) {
				cell[y][x].cn = cell[y][x].n;
				tx = x + dx[cell[y][x].d];
				ty = y + dy[cell[y][x].d];
				if (cell_tmp[ty][tx].n == 0) {
					cell_tmp[ty][tx] = cell[y][x];
					cd();
				}
				else if(cell_tmp[ty][tx].cn > cell[y][x].n) {
					cell_tmp[ty][tx].n += cell[y][x].n;
				}
				else {
					cell_tmp[ty][tx].n += cell[y][x].n;
					cell_tmp[ty][tx].cn = cell[y][x].n;
					cell_tmp[ty][tx].d = cell[y][x].d;
				}
			}
		}
	}
	memcpy(cell, cell_tmp, sizeof(cell));
}

int main() {
	freopen("input.txt", "r", stdin);
	cin >> T;

	for (int tc = 0; tc < T; tc++) {
		cin >> N >> M >> K;
		memset(cell, 0, sizeof(cell));
		for (int k = 0; k < K; k++) {
			cin >> y >> x;
			cin >> cell[y][x].n >> cell[y][x].d;
			cell[y][x].cn = cell[y][x].n;
		}

		for (int m = 0; m < M; m++) {
			move();
		}

		int result = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (cell[i][j].n)
					result += cell[i][j].n;
			}
		}

		cout << result << '\n';
	}
	return 0;
}