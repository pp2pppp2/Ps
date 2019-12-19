//#include <iostream>
//#define TIRENM 100001
//
//using namespace std;
//
//struct NODE {
//	int next[26];
//	void init() {
//		for (int i = 0; i < 26; ++i) {
//			next[i] = -1;
//		}
//	}
//}trie[TIRENM];
//
//int T;
//int start;
//int slen;
//char s[500001];
//char st[100001];
//int ret;
//
//void update(char *str, int strlen) {
//	if (!str[strlen]) return;
//	int ch = str[strlen] - 'a';
//	trie[start].init();
//	trie[start].next[ch] = start + 1;
//	start++;
//	slen++;
//	update(str, strlen + 1);
//}
//
//void s_find() {
//	ret = 0;
//	int i = 0;
//	int st = 0;
//	while (!s[i]) {
//		
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false); cin.tie(NULL);
//	cin >> T;
//	for (int tc = 1; tc <= T; ++tc) {
//		start = 0;
//		slen = 0;
//		cin >> s >> st;
//		update(st, 0);
//
//	}
//	return 0;
//}