//#define _CRT_SECURE_NO_WARNINGS
//#include <iostream>
//#include <vector>
//#include <string.h>
//
//using namespace std;
//struct xy {
//	int x, y;
//};
//char ma;
//vector<xy> p;
//int visit[5][5] = { 0, };
//int dx[4] = { 0, 0, 1, -1 };
//int dy[4] = { 1,-1, 0, 0 };
//int m[5][5];
//int mv[5];
//int rret, ret;
//
//void sol2(int cnt) {
//	if (cnt == p.size()) {
//		if (ret > rret) {
//			ret = rret;
//		}
//		return;
//	}
//	if (ret < rret)
//		return;
//	for (int i = 0; i < p.size(); ++i) {
//		if (mv[i] == 0) {
//			mv[i] = 1;
//			rret += m[cnt][i];
//			sol2(cnt + 1);
//			rret -= m[cnt][i];
//			mv[i] = 0;
//		}
//	}
//}
//bool is_wall(int y, int x, int cnt) {
//	int tx, ty;
//	int flag = 0;
//	for (int i = 0; i < 4; ++i) {
//		ty = y + dy[i];
//		tx = x + dx[i];
//		if (tx >= 0 && tx < 5 && ty >= 0 && ty < 5 && visit[ty][tx] || !cnt)
//			flag = 1;
//	}
//	if (flag)
//		return true;
//	else
//		return false;
//}
//void solve(int y, int x, int cnt) {
//	if (cnt == p.size()) {
//		rret = 0;
//		memset(mv, 0, sizeof(mv));
//		sol2(0);
//		return;
//	}
//	for (int i = 0; i < 5; ++i) {
//		for (int j = 0; j < 5; ++j) {
//			if (is_wall(i, j, cnt) && !visit[i][j]) {
//				visit[i][j] = 1;
//				for (int a = 0; a < p.size(); ++a) {
//					m[cnt][a] = abs(j - p[a].x) + abs(i - p[a].y);
//				}
//				solve(i, j, cnt + 1);
//				visit[i][j] = 0;
//			}
//		}
//	}
//}
//int main() {
//	ios_base::sync_with_stdio(NULL);
//	cin.tie(NULL);
//	for (int y = 0; y < 5; ++y) {
//		for (int x = 0; x < 5; ++x) {
//			cin >> ma;
//			if (ma == '*') {
//				xy tp;
//				tp.x = x;
//				tp.y = y;
//				p.push_back(tp);
//			}
//		}
//	}
//	ret = 98765432;
//	solve(0, 0, 0);
//	cout << ret;
//	return 0;
//}