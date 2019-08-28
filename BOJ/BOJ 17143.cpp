#define fastio() ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0)

#include<iostream>
#include<string.h>

using namespace std;

struct Shark {
	int s, d, z = 0;
	bool alive = false;
};

int dx[] = { 0, 0, 0, 1, -1 };
int dy[] = { 0, -1, 1, 0, 0 };

int R, C, M, cnt = 0;
Shark m[101][101];


void fisher(int x) {
	for (int y = 0; y < R; y++) {
		if (m[y][x].alive) {
			m[y][x].alive = false;
			cnt += m[y][x].z;
			break;
		}
	}
}

void moveShark() {
	Shark n[101][101];
	memset(n, 0, sizeof(n));
	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < C; ++j) {
			if (m[i][j].alive) {
				int mx = (j + m[i][j].s * dx[m[i][j].d]) % (2 * (C - 1));
				if (mx < 0)
					m[i][j].d = 3;
				mx = abs(mx);
				if (mx > C - 1) {
					mx = 2 * C - mx - 2;
					m[i][j].d = 4;
				}
				int my = (i + m[i][j].s * dy[m[i][j].d]) % (2 * (R - 1));
				if (my < 0)
					m[i][j].d = 2;
				my = abs(my);
				if (my > R - 1) {
					my = 2 * R - my - 2;
					m[i][j].d = 1;
				}
				if (n[my][mx].z > m[i][j].z)
					continue;
				n[my][mx] = m[i][j];
			}
		}
	}
	memcpy(m, n, sizeof(n));
}

int main(int argc, char** argv) {
	fastio();
	cin >> R >> C >> M;

	for (int i = 0, r, c, s, d, z; i < M; ++i) {
		cin >> r >> c >> s >> d >> z;
		m[r - 1][c - 1] = { s, d, z, true };
	}

	for (int i = 0; i < C; ++i) {
		fisher(i);
		moveShark();
	}
	cout << cnt << '\n';

	return 0;
}