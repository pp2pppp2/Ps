#include <iostream>
#include <string.h>
#include <vector>

using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int T, Y, X, P;
	int ret[2001] = { 0, };
	int tmp;
	int a, b;
	vector<int> s[2001];
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		cin >> Y >> X >> P;
		memset(ret, 0, sizeof(ret));
		for (int y = 0; y < Y; ++y) {
			for (int x = 0; x < X; ++x) {
				cin >> tmp;
				if (!tmp)
					ret[x]++;
				else
					s[y].push_back(x);
			}
		}
		b = 0;

		for (int p = 0; p < s[P-1].size(); ++p) {
			b += ret[s[P-1][p]];
		}
		a = 1;
		for (int y = 0; y < Y; ++y) {
			tmp = 0;
			for (int p = 0; p < s[y].size(); ++p) {
				tmp += ret[s[y][p]];
			}
			if (y < P - 1) {
				if (tmp >= b)
					a++;
			}
			else {
				if (tmp > b)
					a++;
			}
		}
		for (int p = 0; p < Y; ++p) {
			s[p].clear();
		}
		cout << "#" << tc << " " << b << " " << a;
	}
	return 0;
}