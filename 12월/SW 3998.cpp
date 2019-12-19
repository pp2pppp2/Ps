#include <iostream>
#include <string.h>
using namespace std;

long long arr[1000001];
long long fw[1000001];
int N;

int f_sum(long long fw[], int a) {
	int b = 0;
	while (a > 0) {
		b += fw[a];
		a -= (a & -a);
	}
	return b;
}

void f_upd(long long fw[], int me, int i, int diff) {
	while (i <= me) {
		fw[i] += diff;
		i += (i & -i);
	}
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int T;
	int tmp;
	int me , M, KK;
	cin >> N >> M >> KK;
	long long ret = 0;
	me = 0;
	for (int n = 1; n <= N; ++n) {
		cin >> arr[n];
		f_upd(fw, 1000000, n, arr[n]);
		if (me < arr[n]) me = arr[n];
	}
	for (int m = 0; m < M + KK; ++m) {
		long long a, b, c;
		cin >> a >> b >> c;
		if (a == 1) {
			int diff = c - fw[b];
			f_upd(fw, me, b, diff);
		}
		else {
			ret = f_sum(fw, c) - f_sum(fw, b - 1);
			cout << ret << '\n';
		}
	}
	return 0;
}


