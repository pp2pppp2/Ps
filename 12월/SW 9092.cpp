//#include <iostream>
//#include <queue>
//
//using namespace std;
//
//struct xy {
//	int x, y;
//};
//int T, N, K;
//int mem[501][501];
//xy da[501];
//xy tmp;
//queue<int> q;
//
//int dist(xy a, xy b) { return abs(a.x - b.x) + abs(a.y - b.y); }
//
//void solve(int a, int m, int k) {
//	for (int i = 1; i <= K + 1 - k; ++i) {
//
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false); cin.tie(NULL);
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		cin >> N >> K;
//		for (int n = 0; n < N; ++n) {
//			cin >> tmp.x >> tmp.y;
//			da[n] = tmp;
//			if (n) mem[n][0] = dist(da[n - 1], da[n]);
//		}
//		solve(0, 0, 0);
//	}
//
//	return 0;
//}