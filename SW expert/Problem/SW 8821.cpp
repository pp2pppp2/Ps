//#include <iostream>
//#include <string.h>
//using namespace std;
//int main() {
//	ios_base::sync_with_stdio(NULL);
//	cin.tie(NULL);
//	int T;
//	int x[10];
//	int ret, z;
//	cin >> T;
//	char in[10001];;
//	for (int i = 0; i < T; ++i) {
//		memset(x, 0, sizeof(x));
//		cin >> in;
//		z = 0;
//		ret = 0;
//		while (in[z] != 0) {
//			if (x[in[z] - '0'])
//				ret--;
//			else
//				ret++;
//			x[in[z] - '0'] ^= 1;
//			z++;
//		}
//		cout << "#" << i+1 << " " << ret << '\n';
//	}
//	return 0;
//}