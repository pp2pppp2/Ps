//#include <iostream>
//#define NM 1000005
//
//using namespace std;
//
//
//struct NODE {
//	int next[26];
//	int cnt;
//	void init() {
//		for (int i = 0; i < 26; ++i) {
//			next[i] = -1;
//		}
//	}
//}trie[NM];
//int root = 0, trieN;
//
//void init() {
//	root = 0;
//	trieN = 0;
//	trie[0].init();
//}
//
//void myinsert(int idx, int bufs, int strlen, char *str) {
//	trie[idx].cnt++;
//	if (bufs == strlen) return;
//	int ch = str[bufs] - 'a';
//	
//	if (trie[idx].next[ch] == -1) {
//		trie[idx].next[ch] = ++trieN;
//		trie[trieN].init;
//	}
//
//	myinsert(trieN, bufs + 1, strlen, str);
//}
//void insert(int strlen, char *str) {
//	myinsert(root, 0, strlen, str);
//}
//
//int query(int strlen, char *str) {
//	int idx = root;
//	for (int i = 0; i < strlen; ++i) {
//		int ch = str[i] - 'a';
//		idx = trie[idx].next[ch];
//		if (idx == -1) return 0;
//	}
//	return trie[idx].cnt;
//}
//
//
//int main() {
//	
//	return 0;
//}