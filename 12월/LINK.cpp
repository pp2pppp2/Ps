//#include <iostream>
//
//using namespace std;
//
//struct NODE {
//	int x, y;
//	int next;
//	int prev;
//};
//
//struct MY_LIST {
//	int HEAD = 502;
//	int TAIL = 503;
//	int pos;
//	NODE node[502];
//
//	MY_LIST() {
//		pos = 0;
//		node[HEAD].next = TAIL;
//		node[TAIL].prev = HEAD;
//	}
//
//	void push_back(int x, int y) {
//		int prev = node[TAIL].prev;
//		int next = node[prev].next; // TAIL
//
//		node[pos].x = x;
//		node[pos].y = y;
//
//		node[pos].prev = prev;
//		node[prev].next = pos;
//
//		node[pos].next = next;
//		node[next].prev = pos;
//		++pos;
//	}
//
//	void push_front(int x, int y) {
//		int next = node[HEAD].next;
//		int prev = node[next].prev; // HEAD
//
//		node[pos].x = x;
//		node[pos].y = y;
//
//		node[pos].prev = prev;
//		node[prev].next = pos;
//
//		node[pos].next = next;
//		node[next].prev = pos;
//		++pos;
//	}
//
//	void insert(int p, int x, int y) {
//		int next = node[HEAD].next;
//		for (int i = 0; i < p; ++i) {
//			next = node[next].next;
//		}
//		int prev = node[next].prev;
//
//		node[pos].x = x;
//		node[pos].y = y;
//
//		node[pos].prev = prev;
//		node[prev].next = pos;
//
//		node[pos].next = next;
//		node[next].prev = pos;
//		++pos;
//	}
//
//	void pop_back() {
//		int target = node[TAIL].prev;
//
//		int prev = node[target].prev;
//		int next = node[target].next;
//
//		node[prev].next = next;
//		node[next].prev = prev;
//	}
//
//	void pop_front() {
//		int target = node[HEAD].prev;
//
//		int prev = node[target].prev;
//		int next = node[target].next;
//
//		node[prev].next = next;
//		node[next].prev = prev;
//	}
//
//	void erase(int p) {
//		int target = node[HEAD].next;
//		for (int i = 0; i < p; ++i) {
//			target = node[target].next;
//		}
//		int prev = node[target].prev;
//		int next = node[target].next;
//
//		node[prev].next = next;
//		node[next].prev = prev;
//	}
//
//	void select_max() {
//		int target = node[HEAD].next;
//	}
//
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
//	int T, N, K;
//	int x, y;
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		MY_LIST my_list;
//		cin >> N >> K;
//		for (int n = 0; n < N; ++n) {
//			cin >> x >> y;
//			my_list.push_back(x, y);
//		}
//		for (int k = 0; k < K; ++k) {
//			my_list.select_max();
//		}
//	}
//	
//	return 0;
//}