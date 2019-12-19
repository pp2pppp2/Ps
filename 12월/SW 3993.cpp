//#include <iostream>
//
//using namespace std;
//int T, N, L, R;
//long long dp[21][21][21] = { 0, };
//
//int main() {
//	dp[1][1][1] = 1;
//	for (int n = 2; n <= 20; ++n) 
//		for (int l = 1; l <= n; ++l) 
//			for (int r = 1; r <= n; ++r) 
//				dp[n][l][r] = dp[n - 1][l - 1][r] + dp[n - 1][l][r - 1] + (n - 2) * dp[n - 1][l][r];
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		cin >> N >> L >> R;
//		cout << "#" << tc <<" " << dp[N][L][R] << '\n';
//	}
//	return 0;
//}