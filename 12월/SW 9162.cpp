//#include <iostream>
//
//using namespace std;
//int T, N, M;
//int bo[10][10] = { 0, };
//int visit[10][10] = { 0, };
//int dy[4] = { 0, 0, 1, -1 };
//int dx[4] = { 1, -1, 0, 0 };
//int sx, sy, ret;
//void sol(int x, int y, int mx, int my, int tmp) {
//	if (tmp > ret) return;
//	if (bo[y][x] == 3) {
//		if (my == 0 && mx == 0 || ( my == 2 && mx == 2) || (my == -2 && mx == -2) || (my == 2 && mx == -2) || (my == -2 && mx == 2)) ret = ret < tmp ? ret : tmp;
//		return;
//	}
//	for (int i = 0; i < 4; ++i) {
//		int tx = x + dx[i];
//		int ty = y + dy[i];
//		if (bo[ty][tx] && !visit[ty][tx]) {
//			visit[ty][tx] = 1;
//			int mmx = my % 2 ? mx : ( mx + dx[i] ) % 4;
//			int mmy = mx % 2 ? my : ( my + dy[i] ) % 4;
//			sol(tx, ty, mmx , mmy, tmp + 1);
//			visit[ty][tx] = 0;
//		}
//	}
//}
//int main() {
//	ios_base::sync_with_stdio(false); cin.tie(NULL);
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		cin >> N >> M;
//		for (int y = 1; y <= M; ++y) {
//			for (int x = 1; x <= N; ++x) {
//				cin >> bo[y][x];
//				if (bo[y][x] == 2){
//					sx = x;
//					sy = y;
//				}
//			}
//		}
//		ret = 987654321;
//		sol(sx, sy, 0, 0, 0);
//		if (ret == 987654321)
//			ret = -1;
//		cout << "#" << tc << " " << ret << '\n';
//	}
//	return 0;
//}