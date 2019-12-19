//#include <iostream>
//#include <algorithm>
//#include <string.h>
//
//using namespace std;
//
//int arr[200001];
//int cnt[200001];
//int arr_len;
//int cnt_len;
//
//bool com(int a) {
//	int b = 0;
//	int cnt_idx = 0;
//	for (int i = 0; i < arr_len; ++i) {
//		if (arr[i] <= a)
//			b++;
//		else
//			b = 0;
//		if (b == cnt[cnt_idx]) {
//			cnt_idx++;
//			b = 0;
//			if (cnt_idx == cnt_len)
//				return true;
//		}
//	}
//	return false;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
//	int T;
//	int N, K, inum, xnum;
//	int tmp, ret, mid;
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		memset(arr, 0, sizeof(arr));
//		memset(cnt, 0, sizeof(cnt));
//		cin >> N >> K;
//		inum = 987654321;
//		xnum = 0;
//		arr_len = 0;
//		for (int i = 0; i < N; ++i) {
//			cin >> arr[i];
//			if (inum > arr[i])
//				inum = arr[i];
//			if (xnum < arr[i])
//				xnum = arr[i];
//			arr_len++;
//		}
//		ret = 0;
//		cnt_len = 0;
//		for (int i = 0; i < K; ++i) {
//			cin >> cnt[i];
//			cnt_len++;
//		}
//		while (inum != xnum) {
//			mid = (inum + xnum) / 2;
//			if (!com(mid)) {
//				inum = mid + 1;
//			}
//			else
//				xnum = mid;
//		}
//		cout << "#" << tc << " " << inum << '\n';
//	}
//	return 0;
//}