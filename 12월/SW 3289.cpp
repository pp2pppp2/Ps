//#include <iostream>
//
//using namespace std;
//
//int p[1000002];
//int fc, fb;
//int T, N, M;
//int a, b, c;
//
//int fd(int x) {
//	if (p[x] == x)
//		return x;
//	p[x] = fd(p[x]);
//	return p[x];
//}
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
//	cout.tie(NULL);
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		cout << "#" << tc << " ";
//		cin >> N >> M;
//		for (int n = 0; n <= N; ++n)
//			p[n] = n;
//		for (int m = 0; m < M; ++m) {
//			cin >> a >> b >> c;
//			if (a) {
//				fb = fd(b);
//				fc = fd(c);
//				if (fb == fc)
//					cout << 1;
//				else
//					cout << 0;
//			}
//			else
//				p[fb] = fc;
//		}
//		cout << '\n';
//	}
//	
//}