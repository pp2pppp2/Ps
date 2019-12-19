//#include <iostream>
//#include <string.h>
//
//using namespace std;
//
//int main() {
//	char S1[100001];
//	char S2[100001];
//	int alpha[30];
//	int T;
//	int ret;
//	int start, end;
//	int wcnt;
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		ret = 0;
//		cin >> S1;
//		int slen = 0;
//		memset(alpha, 0, sizeof(alpha));
//		wcnt = 0;
//		while (S1[slen]) {
//			alpha[S1[slen] - 'a']++;
//			if (alpha[S1[slen] - 'a'] == 1)
//				wcnt++;
//			slen++;
//		}
//		start = 0;
//		end = slen - 1;
//		cin >> S2;
//		int cnt = 0;
//		for (int i = 0; i <= end; ++i) {
//			alpha[S2[i] - 'a']--;
//			if (!alpha[S2[i] - 'a'])
//				wcnt--;
//			else if (alpha[S2[i] - 'a'] == -1)
//				wcnt++;
//		}
//		if (!wcnt)
//			ret++;
//		cnt = 0;
//		while (S2[cnt + end]) {
//			alpha[S2[cnt] - 'a']++;
//			if (alpha[S2[cnt] - 'a'] == 0)
//				wcnt--;
//			else if (alpha[S2[cnt] - 'a'] == 1)
//				wcnt++;
//			alpha[S2[cnt + end + 1] - 'a']--;
//			if (alpha[S2[cnt + end + 1] - 'a'] == 0)
//				wcnt--;
//			else if (alpha[S2[cnt + end + 1] - 'a'] == -1)
//				wcnt++;
//			cnt++;
//			if (wcnt == 0)
//				ret++;
//		}
//		cout << "#" << tc << " " << ret << '\n';
//	}
//	return 0;
//}