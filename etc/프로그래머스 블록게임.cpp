//#include <string>
//#include <vector>
//#include <iostream>
//
//using namespace std;
//int dx[5] = { 1, -1, 0, 0, 1 };    // ㄴ  ㄴ반대 ㄴ긴거반대 ㄴ긴거 ㅗ모양
//int dy[5] = { 1, 1, 2, 2, 1 };
//int ddx[5] = { 2, -2, -1, 1, -1 };
//int ddy[5] = { 1, 1, 2, 2, 1 };
//int dxd[5] = { 1, -1, -1, 1 , 1};
//int dyd[5] = { 0, 0, 0 , 0, 0};
//int ddxd[5] = { 2, -2 , -1, 1, -1};
//int ddyd[5] = { 0, 0, 1, 1, 0};
//int visit[51] = { 0, };
//int N;
//int answer = 0;
//int board[51][51];
//
//bool iswall(int x) {
//	if (0 <= x && x < N)
//		return true;
//	else
//		return false;
//}
//
//
//void sol(int y, int x, int bn) {
//	board[y][x] = 0;
//	board[y + 1][x] = 0;
//	board[y + dy[bn]][x + dx[bn]] = 0;
//	board[y + ddy[bn]][x + ddx[bn]] = 0;
//	answer++;
//}
//
//int main() {
//	freopen("Text.txt", "r", stdin);
//	cin >> N;
//	for (int y = 0; y < N; ++y) {
//		for (int x = 0; x < N; ++x) {
//			cin >> board[y][x];
//		}
//	}
//
//	int flag = 0;
//	for (int y = 0; y < N - 1; ++y) {
//		for (int x = 0; x < N; ++x) {
//			if (board[y][x] != 0) {
//				int fg = 1;
//				for (int i = 0; i < 5; ++i) {
//					int tx = x + dx[i];
//					int ttx = x + ddx[i];
//					int ty = y + dy[i];
//					int tty = y + ddy[i];
//					int tttx = x + dxd[i];
//					int ttty = y + dyd[i];
//					int ttttx = x + ddxd[i];
//					int tttty = y + ddyd[i];
//					if (iswall(tttty) && iswall(ttttx) && iswall(ttty) && iswall(tttx) && iswall(tx) && iswall(ty) && iswall(ttx) && iswall(tty) && board[y][x] == board[ty][tx] && board[ty][tx] == board[tty][ttx] && board[ttty][tttx] == 0 && board[tttty][ttttx] == 0 && visit[tttx] == 0 && visit[ttttx] == 0) {
//						sol(y, x, i);
//						fg = 0;
//						break;
//					}
//				}
//				if (fg) {
//					visit[x] = 1;
//				}
//			}
//		}
//	}
//	cout << answer;
//	return 0;
//}