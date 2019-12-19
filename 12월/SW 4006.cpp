//#include <iostream>
//#include <queue>
//
//using namespace std;
//
//struct m {
//	int a, b, val;
//};
//struct com {
//	bool operator()(m a, m b){ return a.val > b.val; }
//};
//
//int T, N, M;
//int p[50001];
//priority_queue<m, vector<m>, com> pq;
//m tmp;
//int find(int x) {
//	if (p[x] == x)
//		return x;
//	p[x] = find(p[x]);
//	return p[x];
//}
//
//void merge(int a, int b) {
//	p[p[a]] = b;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false); cin.tie(NULL);
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		cin >> N >> M;
//		for (int n = 1; n <= N; ++n) p[n] = n;
//		for (int m = 0; m < M; ++m) {
//			cin >> tmp.a >> tmp.b >> tmp.val;
//			pq.push(tmp);
//		}
//		long long ret = 0;
//		while (!pq.empty()) {
//			tmp = pq.top();
//			pq.pop();
//			if (find(tmp.a) != find(tmp.b)) {
//				ret += tmp.val;
//				--N;
//				merge(tmp.a, tmp.b);
//			}
//			if (N == 1) break;
//		}
//		cout << "#" << tc << " " << ret << '\n';
//	}
//	return 0;
//}