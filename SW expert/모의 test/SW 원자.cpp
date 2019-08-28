#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>
#include <vector>

using namespace std;
struct elec {
	int x, y, d, k, e;
};
struct xy {
	int x, y;
};
int T, K;
elec e[1000];
vector<xy> t,p;
xy tmp;
int m[2002][2002][5];
int tx, ty , ecnt , result, ecnt_f;
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { 1, -1, 0, 0 };
int ti;

bool wa(int x , int y) {
	if (x < 0 || y < 0 || x > 2001 || y > 2001)
		return false;
	return true;
}

void cal() {
	if (t.size()) {
		for (int j = 0; j < t.size(); j++) {
			for (int i = 0; i < 4; i++) {
				if (m[t[j].y][t[j].x][i]) {
					result += e[m[t[j].y][t[j].x][i] - 1].k;
					e[m[t[j].y][t[j].x][i] - 1].e = 0;
					ecnt--;
					m[t[j].y][t[j].x][i] = 0;
				}
			}
		}
	}
	if (p.size()) {
		for (int j = 0; j < p.size(); j++) {
			int n = m[p[j].y][p[j].x][0] - 1;
			tx = e[n].x + dx[e[n].d - 1];
			ty = e[n].y + dy[e[n].d - 1];
			if (tx > 0 && ty > 0 && tx < 2001 && ty < 2001 && e[m[ty][tx][0] - 1].e) {
				if (e[m[p[j].y][p[j].x][0] - 1].d % 2) {
					if (e[n].d + 1 == e[m[ty][tx][0] - 1].d) {
						result += e[n].k;
						e[n].e = 0;
						ecnt--;
						m[p[j].y][p[j].x][0] = 0;
						result += e[m[ty][tx][0] - 1].k;
						e[m[ty][tx][0] - 1].e = 0;
						ecnt--;
						m[ty][tx][0] = 0;
					}
				}
				else {
					if (e[n].d - 1 == e[m[ty][tx][0] - 1].d) {
						result += e[n].k;
						e[n].e = 0;
						ecnt--;
						m[p[j].y][p[j].x][0] = 0;
						result += e[m[ty][tx][0] - 1].k;
						e[m[ty][tx][0] - 1].e = 0;
						ecnt--;
						m[ty][tx][0] = 0;
					}
				}
			}
			m[p[j].y][p[j].x][0] = 0;
		}	
	}
}

void move() {
	for (int i = 0; i < ecnt_f; i++) {
		if (e[i].e) {
			tx = e[i].x + dx[e[i].d - 1];
			ty = e[i].y + dy[e[i].d - 1];
			if (wa(tx, ty)) {
				int c = 0;
				for (int a = 0; a < 4; a++) {
					if (m[ty][tx][a] == 0 ) {
						m[ty][tx][a] = i+1;
						c = a+1;
						break;
					}
				}
				e[i].x = tx;
				e[i].y = ty;
				if (c == 2) {
					tmp.x = tx;
					tmp.y = ty;
					t.push_back(tmp);
				}
				if (c == 1) {
					tmp.x = tx;
					tmp.y = ty;
					p.push_back(tmp);
				}
			}
			else {
				e[i].e = 0;
				ecnt--;
			}
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	cin >> T;
	for (int tc = 0; tc < T; tc++) {
		cin >> K;
		ecnt = 0;
		result = 0;
		for (int i = 0; i < K; i++) {
			cin >> tx >> ty;
			e[i].x = tx + 1000;
			e[i].y = ty + 1000;
			int td;
			cin >> td >> e[i].k;
			e[i].d = td + 1;
			e[i].e = 1;
			ecnt++;
			tmp.x = e[i].x;
			tmp.y = e[i].y;
			p.push_back(tmp);
			m[e[i].y][e[i].x][0] = i+1;
		}
		ecnt_f = ecnt;
		cal();
		p.clear();
		while (ecnt > 0) {
			move();
			cal();
			t.clear();
			p.clear();
		}
		cout << "#" << tc + 1 << " " << result << '\n';
	}
	return 0;
}