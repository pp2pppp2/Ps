#define fastio() ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)
#include <iostream>
#include <string.h>

using namespace std;

int gear[1002][8];
int LR[1002][2];
int chk[1002];

void rotationgear(int N, int C) {
	LR[N][0] = (LR[N][0] + 8 - C) % 8;
	LR[N][1] = (LR[N][1] + 8 - C) % 8;
}

void chkrotation(int T) { // 1: 1 ~ 2 °°À¸¸é 0 ´Ù¸£¸é 1
	for (int i = 1; i <= T; ++i)
		chk[i] = gear[i][LR[i][1]] == gear[i + 1][LR[i + 1][0]] ? 0 : 1;
}

void solve(int N, int C) {
	if (chk[N]) {
		chk[N] = 0;
		rotationgear(N + 1, C);
		solve(N + 1, -C);
	}

	if (chk[N - 1]) {
		chk[N - 1] = 0;
		rotationgear(N - 1, C);
		solve(N - 1, -C);
	}
}

int main(int argc, char** argv) {
	memset(chk, 0, sizeof(chk));
	int T;
	int c;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		for (int j = 0; j < 8; ++j) { // Åé´Ï¹ÙÄû ±Ø¼º Á¤º¸ ÀÔ·Â
			char c;
			cin >> c;
			gear[i][j] = c - '0';
		}
	}

	for (int i = 1; i <= T; ++i) { // Åé´Ï¹ÙÄû ÀÎµ¦½º ¼³Á¤
		LR[i][0] = 6;
		LR[i][1] = 2;
	}

	int K, N, C;
	cin >> K;
	for (int i = 0; i < K; ++i) {
		cin >> N >> C;
		chkrotation(T);
		rotationgear(N, C);
		solve(N, -C);
		/*for (int a = 0; a < 4; a++)
		{
			cout << chk[a+1] << LR[a+1][0] << LR[a+1][1];
		}*/
	}

	int cnt = 0;
	for (int i = 1; i <= T; ++i) {
		//cout << gear[i][(LR[i][0] + 2) % 8];
		c = (LR[i][0] + 2) % 8;
		if (gear[i][c])
			cnt++;
	}
	cout << cnt << '\n';

	return 0;
}