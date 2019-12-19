//#include <iostream>
//#include <string.h>
//
//using namespace std;
//int T, N, K;
//int M, tmp;
//int cnt[10030];
//int ret = 0;
//int result;
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		cin >> N >> K;
//		M = 0;
//		memset(cnt, 0, sizeof(cnt));
//		for (int i = 0; i < N; ++i) {
//			cin >> tmp;
//			cnt[tmp]++;
//			if (M < tmp)
//				M = tmp;
//		}
//		ret = 0;
//		for (int i = 1; i <= K + 1; ++i) {
//			ret += cnt[i];
//		}
//		result = ret;
//		for (int i = 1; i <= M - K - 1; ++i) {
//			ret -= cnt[i];
//			ret += cnt[i + K + 1];
//			if (result < ret)
//				result = ret;
//		}
//		cout << "#" << tc << " " << result << '\n';
//	}
//	return 0;
//}