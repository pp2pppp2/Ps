//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//int sum_arr[200001];
//int min_sum[200001];
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
//	
//	int T;
//	int ret;
//	int tmp;
//	int N;
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		cin >> N;
//		sum_arr[0] = 0;
//		min_sum[0] = 0;
//		ret = -97462342;
//		for (int n = 1; n <= N; ++n) {
//			cin >> tmp;
//			sum_arr[n] = tmp + sum_arr[n - 1];
//			min_sum[n] = min(sum_arr[n], min_sum[n-1]);
//			ret = max(ret, sum_arr[n] - min_sum[n-1]);
//		}
//		cout << "#" << tc << " " << ret << "\n";
//	}
//	return 0;
//}