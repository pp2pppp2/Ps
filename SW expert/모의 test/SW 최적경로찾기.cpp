#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;

struct xy {
	int x, y;
};
int T, N, C;
int visit[11];
vector<xy> cl, st;
vector<int> cli;
xy com, home, tmp;
int sum1, sum2, result, sum_tmp, sum;
int hs[22][22];

int abs(int a) {
	if (a < 0)
		return -a;
	return a;
}

bool compare(xy a, xy b) {
	return abs(com.x - a.x) + abs(com.y - a.y) < abs(com.x - b.x) + abs(com.y - b.y);
}

void test() {
	if (!hs[0][cli[0]])
		hs[0][cli[0]] = abs(com.x - st[cli[0]-1].x) + abs(com.y - st[cli[0]-1].y);
	sum = hs[0][cli[0]];
		
	for (int i = 0; i < cli.size()-1; i++) {
		sum += hs[cli[i]][cli[i + 1]];
	}
	if (!hs[cli.back()][N + 1])
		hs[cli.back()][N + 1] = abs(home.x - st[cli.back() - 1].x) + abs(home.y - st[cli.back() - 1].y);
	sum += hs[cli.back()][N + 1];


}

void solve(int x) {
	if (!cli.empty()) {
		test();
		if (result < sum)
			return;
	}
	if (cli.size() == N && result > sum) {
		result = sum;
		return;
	}
	for (int i = 1; i < st.size()+1; i++) {
		if (!visit[i]) {
			visit[i]++;
			cli.push_back(i);
			solve(i);
			cli.pop_back();
			visit[i]--;
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> T;
	for (int tc = 0; tc < T; tc++) {
		result = 99999;
		cin >> N;
		cin >> com.x >> com.y >> home.x >> home.y;
		memset(visit, 0, sizeof(visit));
		memset(hs, 0, sizeof(hs));
		st.clear();
		for (int i = 0; i < N; i++) {
			cin >> tmp.x;
			cin >> tmp.y;
			st.push_back(tmp);
		}
		sort(st.begin(), st.end(), compare);
		C = N % 2 ? N / 2 + 1 : N / 2;
		for (int i = 1; i < N+1; i++) {
			for (int j = i + 1; j < N+1; j++) {
				hs[i][j] = abs(st[i - 1].x - st[j - 1].x) + abs(st[i - 1].y - st[j - 1].y);
				hs[j][i] = hs[i][j];
			}
		}
		for (int i = 1; i < N; i++)
		{
			visit[i]++;
			cli.push_back(i);
			solve(i);
			cli.pop_back();
			visit[i]--;
		}

		cout << "#" << tc + 1 << " " << result << '\n';
	}
	return 0;
}