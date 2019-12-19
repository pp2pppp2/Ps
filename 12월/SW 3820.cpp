//#include <iostream>
//#include <queue>
//
//using namespace std;
//
//struct r {
//	long long a, b;
//};
//
//struct com {
//	bool operator()(r a, r b) {
//		if ((a.a - 1) * b.b >= (b.a - 1) * a.b)
//			return false;
//		else
//			return true;
//	}
//};
//
//
//priority_queue<r, vector<r>, com> pq;
//vector<r> qq;
//r q;
//long long ret;
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
//	//freopen("input.txt", "r", stdin);
//	int T, N;
//	int a, b;
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		cin >> N;
//		for (int n = 0; n < N; ++n) {
//			cin >> a >> b;
//			q.a = a;
//			q.b = b;
//			pq.push(q);
//		}
//		ret = 1;
//		//sort(qq.begin(), qq.end(), compare);
//		while (!pq.empty()) {
//			q = pq.top();
//			pq.pop();
//			ret = (q.a * ret) % 1000000007 + q.b;
//		}
//		cout << "#" << tc << " " << ret << '\n';
//	}
//
//	return 0;
//}