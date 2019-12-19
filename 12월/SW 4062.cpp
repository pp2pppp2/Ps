//#include <iostream>
//#include <algorithm>
//using namespace std;
//
//char arr[1001][1001];
//int xsum[1001][1001] = { 0, };
//int T, N;
//int ret;
//int main() {
//	ios_base::sync_with_stdio(false); cin.tie(NULL);
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		cin >> N;
//		ret = 0;
//		for (int y = 1; y <= N; ++y) {
//			for (int x = 1; x <= N; ++x) {
//				cin >> arr[y][x];
//				if (arr[y][x] - '0')
//					xsum[y][x] = 0;
//				else {
//					xsum[y][x] = min(min(xsum[y - 1][x], xsum[y][x - 1]), xsum[y - 1][x - 1]) + 1;
//					ret = max(xsum[y][x], ret);
//				}
//			}
//		}
//		cout << "#" << tc << " " << ret << '\n';
//	}
//	return 0;
//}