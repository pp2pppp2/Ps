//#include <iostream>
//#include <vector>
//#include <algorithm>
//#include <utility>
//#include <string.h>
//using namespace std;
//pair<int, int> board[500002];
//pair<int, int> board_index[250001];
//int visit[250001];
//int W, H, N;
//int cnt;
//int start, now, before;
//int flag;
//int com1, com2;
//long long ret;
//bool compare(pair<int, int> a, pair<int, int> b) {
//	if (a.first > b.first)
//		return true;
//	else
//		return false;
//}
//int t_min(int a, int b) {
//	if (a < b)
//		return a;
//	return b;
//}
//int ano(pair<int, int> a) {
//	if (a.first == board_index[a.second].first)
//		return board_index[a.second].second;
//	return board_index[a.second].first;
//}
//
//void set_start() {
//	for (int i = 2 * N - 1; i >= 0; --i) {
//		if (i != 0) {
//			if (board[i].first == board[i - 1].first) {
//				if (com2 == -1)
//					com2 = i;
//			}
//			if (board[i].first != board[i - 1].first) {
//				if (com1 == -1)
//					com1 = i;
//			}
//		}
//		else {
//			if (com1 == -1)
//				com1 = i;
//			if (com2 == -1)
//				com2 = i;
//		}
//		int tmp = 0;
//		int sel = 0;
//		if (com1 != -1 && com2 != -1) {
//			for (int k = com1; k <= com2; ++k) {
//				if (!visit[board[k].second]) {
//					int b = ano(board[k]);
//					if (tmp < b) {
//						tmp = b;
//						sel = k;
//					}
//				}
//			}
//			ret += tmp;
//			visit[sel]++;
//			com1 = -1;
//			com2 = -1;
//		}
//		
//	}
//}
//int ttmp(int a) {
//	//if (now == board_index[a].first)
//	//	return board_index[a].second;
//	//return board_index[a].first;
//	if (board_index[a].first > board_index[a].second) {
//		if (now == board_index[a].first)
//			return board_index[a].second;
//		return board_index[a].first;
//	}
//	if (now == board_index[a].second)
//		return board_index[a].first;
//	return board_index[a].second;
//}
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
//	int T;
//	freopen("input.txt", "r", stdin);
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		cin >> N;
//		memset(visit, 0, sizeof(visit));
//		for (int n = 1; n <= N; n++) {
//			cin >> W >> H;
//			board_index[n].first = W;
//			board_index[n].second = H;
//			board[n * 2].first = W;
//			board[n * 2].second = n;
//			board[n * 2 - 1].first = H;
//			board[n * 2 - 1].second = n;
//		}
//		sort(board, board + 2 * N + 1, compare);
//		cnt = 0;
//		before = 9876543211;
//		flag = 0;
//		com1 = -1;
//		com2 = 2 * N - 1;
//		ret = 0;
//		set_start();
//		//now = board[start].first;
//		//before = 9876543211;
//		//com1 = -1;
//		//com2 = -1;
//		//for (int i = start; i < 2 * N; ++i) {
//		//	if (before == board[i].first && i != 2 * N - 1) {
//		//		if (com1 == -1) {
//		//			com1 = i;
//		//		}
//		//		else if (com2 == -1) {
//		//		}
//		//	}
//		//	else if (i == 2 * N - 1 || before != board[i].first && i != start) {
//		//		if (i == 2 * N - 1)
//		//			com2 = 2 * N - 1;
//		//		else
//		//			com2 = i;
//		//		int tmp = 9876544321;
//		//		int sel = 0;
//		//		for (int k = com1; k <= com2; ++k) {
//		//			int b = board[k].second;
//		//			if (visit[b] != 2 && tmp > -t_min(-board_index[b].first, -board_index[b].second)) {
//		//				tmp = -t_min(-board_index[b].first, -board_index[b].second);
//		//				sel = b;
//		//			}
//		//		}
//		//		ret += ttmp(board[sel].second);
//		//		visit[sel] = 2;
//		//		com1 = -1;
//		//		com2 = -1;
//		//	}
//		//	before = board[i].first;
//		//}
//		cout << ret << "\n";
//	}
//	return 0;
//}