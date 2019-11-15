//#include <stdio.h>
//
//int main() {
//	int T, N;
//	long long A, B;
//	long long ret;
//	scanf("%d", &T);
//	for (int tc = 1; tc <= T; ++tc){
//		scanf("%d %d %d", &N, &A, &B);
//		if (A > B) {
//			printf("#%d 0\n", tc);
//		}
//		else if (A == B) {
//			printf("#%d 1\n", tc);
//		}
//		else {
//			if (N == 1) {
//				printf("#%d 0\n", tc);
//			}
//			else {
//				ret = (B - A)*(N - 2) + 1;
//				printf("#%d %llu\n", tc, ret);
//			}
//		}
//	}
//	return 0;
//}