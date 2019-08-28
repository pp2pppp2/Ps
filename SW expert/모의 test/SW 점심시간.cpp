#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>

using namespace std;

struct st {
	int x, y, n;
};
struct pe {
	int x, y, d[2];
};
int T, N;
st s[2];
pe p[10];
int times , sc , pc , tmp ,cnt , min_t;
int st_d[10];
int stb[2][3][2];
int stc[2];
int stdd[2][10];
int abs(int a) {
	if (a > 0)
		return a;
	return -a;
}

void rs() {
	stc[0] = 0;
	stc[1] = 0;
	cnt = 0;
	times = 0;
	while (cnt < pc) {
		times++;
		for (int a = 0; a < 3; a++) {
			for (int b = 0; b < 2; b++)	{
				if (stb[b][a][0]) {
					stb[b][a][0]--;
					if (stb[b][a][0] == 0) {
						cnt++;
						stc[b]--;
					}
				}
			}
		}
		for (int a = 0; a < 2; a++) {
			if (stc[a] <= 3) {
				for (int c = 0; c < 10; c++) {
					if (stdd[a][c]) {
						for (int b = 0; b < 3; b++) {
							if (stb[a][b][0] == 0) {
								stb[a][b][0] = s[st_d[stdd[a][c] - 1]].n;
								stb[a][b][1] = stdd[a][c];
								stc[a]++;
								stdd[a][c] = 0;
								break;
							}
						}
					}
				}
			}
		}
		
		for (int i = 0; i < pc; i++) {
			if (times == p[i].d[st_d[i]]) {
				if (stc[st_d[i]] >= 3) {
					for (int a = 0; a < 10; a++) {
						if (stdd[st_d[i]][a] == 0) {
							stdd[st_d[i]][a] = i+1;
							break;
						}
					}
				}
				else {
					for (int b = 0; b < 3; b++) {
						if (stb[st_d[i]][b][0] == 0) {
							stb[st_d[i]][b][0] = s[st_d[i]].n;
							stb[st_d[i]][b][1] = i;
							stc[st_d[i]]++;
							break;
						}	
					}					
				}
			}
		}

	}
	if (min_t > times) {
		min_t = times;
	}
}

void solve(int p_c) {
	if (p_c > pc)
		return;
	if (p_c == pc)
		rs();
	st_d[p_c] = 1;
	solve(p_c + 1);
	st_d[p_c] = 0;
	solve(p_c + 1);
}

int main() {
	freopen("input.txt", "r", stdin);
	cin >> T;
	for (int tc = 0; tc < T; tc++) {
		cin >> N;
		sc = 0;
		pc = 0;
		for (int y = 0; y < N; y++) {
			for (int x = 0; x < N; x++) {
				cin >> tmp;
				if (tmp == 1) {
					p[pc].x = x;
					p[pc].y = y;
					pc++;
				}
				else if (tmp >= 2) {
					s[sc].x = x;
					s[sc].y = y;
					s[sc].n = tmp;
					sc++;
				}
			}
		}
		for (int i = 0; i < pc; i++) {
			p[i].d[0] = abs(p[i].x - s[0].x) + abs(p[i].y - s[0].y);
			p[i].d[1] = abs(p[i].x - s[1].x) + abs(p[i].y - s[1].y);
		}
		min_t = 987654321;
		solve(0);

		cout <<"#" <<tc+1 << " "<< min_t+1 << '\n';
	}
	return 0;
}
//#define fastio() ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0)
//#define _CRT_SECURE_NO_WARNINGS
//#include <iostream>
//#include <string.h>
//#include <vector>
//#include <algorithm>
//using namespace std;
//
//struct pos {
//	int x = 0, y = 0, z = 0;
//};
//struct le {
//	int len;
//	bool ent;
//};
//pos m[10];
//pos s[2];
//vector<le> p;
//le tmp;
//int mcnt,scnt;
//int t[2][100] = { 0 };
//int mmlen = 0;
//
//bool compare(le a , le b) {
//	return a.len < b.len;
//}
//
//void dfs(int idx, int mask) {
//	if (idx == mcnt) {
//		memset(t, 0, sizeof(t));
//		p.clear();
//		int mlen = 0;
//		for (int i = 0; i < mcnt; ++i) {
//			tmp.ent = mask & (1 << i);
//			tmp.len = abs(s[tmp.ent].x - m[i].x) + abs(s[tmp.ent].y - m[i].y);
//			p.push_back(tmp);
//		}
//		sort(p.begin(), p.end(), compare);
//		for (int i = 0; i < p.size(); i++) {
//			int k = 0;
//			for (int j = p[i].len + 1; j <= p[i].len + s[p[i].ent].z + k; ++j) {
//				mlen = mlen > j ? mlen : j;
//				if (t[p[i].ent][j] >= 3) {
//					k++;
//					continue;
//				}
//				t[p[i].ent][j] += 1;
//			}
//		}
//		mmlen = mmlen < mlen ? mmlen : mlen;
//		return;
//	}
//	dfs(idx + 1, mask);
//	dfs(idx + 1, mask | (1 << idx));
//}
//
//int main(int argc, char** argv) {
//	fastio();
//	freopen("input.txt", "r", stdin);
//	int T;
//	cin >> T;
//	for (int testcase = 1, N; testcase <= T; ++testcase) {
//		mcnt = scnt = 0;
//		cin >> N;
//		for (int i = 0, tmp; i < N; ++i) {
//			for (int j = 0; j < N; ++j) {
//				cin >> tmp;
//				if (tmp > 1)
//					s[scnt++] = { j, i, tmp };
//				else if (tmp)
//					m[mcnt++] = { j, i };
//			}
//		}
//		mmlen = 1000;
//		dfs(0, 0);
//		cout << mmlen + 1 << '\n';
//
//	}
//	return 0;
////}
//#define fastio() ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0)
//#define _CRT_SECURE_NO_WARNINGS
//#include <iostream>
//#include <string.h>
//
//using namespace std;
//
//struct pos {
//	int x = 0, y = 0, z = 0;
//};
//
//pos m[10];
//pos s[2];
//
//int mcnt;
//int scnt;
//
//int mmlen = 0;
//
//void dfs(int idx, int mask) {
//	if (idx == mcnt) {
//		int t[2][100] = { 0 };
//		int mlen = 0;
//
//		for (int f =1; f < 25; ++f) {
//			for (int i = 0; i < mcnt; ++i) {
//				bool ent = mask & (1 << i);
//				int len = abs(s[ent].x - m[i].x) + abs(s[ent].y - m[i].y);
//
//				if (len == f) {
//					int k = 0;
//					for (int j = len + 1; j <= len + s[ent].z + k; ++j) {
//						mlen = mlen > j ? mlen : j;
//						if (t[ent][j] >= 3) {
//							k++;
//							continue;
//						}
//						t[ent][j] += 1;
//					}
//				}
//			}
//		}
//
//		mmlen = mmlen < mlen ? mmlen : mlen;
//		return;
//	}
//
//	dfs(idx + 1, mask);
//	dfs(idx + 1, mask | (1 << idx));
//}
//
//int main(int argc, char** argv) {
//	fastio();
//	freopen("input.txt", "r", stdin);
//	int T;
//	cin >> T;
//	for (int testcase = 1, N; testcase <= T; ++testcase) {
//		mcnt = scnt = 0;
//		cin >> N;
//		for (int i = 0, tmp; i < N; ++i) {
//			for (int j = 0; j < N; ++j) {
//				cin >> tmp;
//				if (tmp > 1)
//					s[scnt++] = { j, i, tmp };
//				else if (tmp)
//					m[mcnt++] = { j, i };
//			}
//		}
//		mmlen = 1000;
//		dfs(0, 0);
//		cout << mmlen + 1 << '\n';
//
//	}
//	return 0;
//}