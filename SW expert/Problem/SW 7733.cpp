#include<iostream>
int chee_info[102][102][6];
int days;
int dung;
int Max_dung;
int K;

using namespace std;

void connet(int K){
	for (int xx = 0; xx < K; xx++) {
		for (int yy = 0; yy < K; yy++) {
			if (chee_info[xx][yy][0] > days) {
				if (yy != 0)
					if (chee_info[xx][yy - 1][0] > days)		// UP
						chee_info[xx][yy][2] = 1;
				if (xx != K)
					if (chee_info[xx + 1][yy][0] > days)		// RIGHT
						chee_info[xx][yy][3] = 1;
				if (yy != K)
					if (chee_info[xx][yy + 1][0] > days)		// DOWN
						chee_info[xx][yy][4] = 1;
				if (xx != 0)
					if (chee_info[xx - 1][yy][0] > days)		// left
						chee_info[xx][yy][5] = 1;
			}
		}
	}
}

void add_dung(int x, int y)
{
	chee_info[x][y][1] = dung;

	if (chee_info[x][y][2] == 1 ) {
		chee_info[x][y][2] = 0;
		chee_info[x][y-1][4] = 0;
		add_dung(x, y - 1);
	}
	if (chee_info[x][y][3] == 1) {
		chee_info[x][y][3] = 0;
		chee_info[x + 1][y][5] = 0;
		add_dung(x + 1, y);
	}
	if (chee_info[x][y][4] == 1) {
		chee_info[x][y][4] = 0;
		chee_info[x][y + 1][2] = 0;
		add_dung(x, y + 1);
	}
	if (chee_info[x][y][5] == 1) {
		chee_info[x][y][5] = 0;
		chee_info[x - 1][y][3] = 0;
		add_dung(x - 1, y);
	}
}

void chee_dung(int K) {
	for (int yy = 0; yy < K; yy++) {
		for (int xx = 0; xx < K; xx++) {
			if (chee_info[xx][yy][0] > days && chee_info[xx][yy][1] == 0) {
				dung += 1;
				add_dung(xx, yy);
			}
		}
	}
	if (Max_dung < dung)
		Max_dung = dung;
	dung = 0;
}


int main(int argc, char** argv)
{
	int test_case;
	int T;
	// 0 이면  - 맛있는 정도  1 - 덩어리 판별
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case) {
		Max_dung = 0;
		cin >> K;
		for (int x_x = 0; x_x < K; x_x++) {
			for (int y_y = 0; y_y < K; y_y++) {
				cin >> chee_info[x_x][y_y][0];
				for (int i = 1; i < 6; i++) {
					chee_info[x_x][y_y][i] = 0;
				}
			}
		}
		for (days = 0; days <= 100; days++) {
			connet(K);
			chee_dung(K);
			for (int x_x = 0; x_x < K; x_x++) {
				for (int y_y = 0; y_y < K; y_y++) {
					for (int i = 1; i < 6; i++) {
						chee_info[x_x][y_y][i] = 0;
					}
				}
			}
		}
		cout << Max_dung;
	}
	return 0;
}
