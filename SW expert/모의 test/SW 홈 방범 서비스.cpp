#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <string.h>

using namespace std;

struct xy {
	int x, y;
};

int T, N, M;
int max_K, result, tmp;
int map[20][20];
int visit[20][20];
int depth;
int dp_cnt;
int max_s, s, pp, max_pp;

int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };

bool iswall(xy tmp) {
	if (tmp.x < 0 || tmp.y <0 || tmp.x > N - 1 || tmp.y > N - 1 || visit[tmp.y][tmp.x])
		return false;
	return true;
}

void bfs(int x, int y) {
	xy tmp, tmp2;
	int cnt = 0;
	memset(visit, 0, sizeof(visit));
	tmp.x = x;
	tmp.y = y;
	queue<xy> q;
	q.push(tmp);
	depth = 1;
	visit[y][x] = 1;
	dp_cnt = 1;
	s = 0;
	pp = 0;
	if (map[tmp.y][tmp.x]) {
		pp++;
		if (result < pp)
			result = pp;
	}
		
	while (!q.empty())
	{
		if (max_pp*M - (depth*depth + (depth - 1)*(depth - 1)) < 0)
			break;
		if (dp_cnt == cnt) {
			depth++;
			dp_cnt = q.size();
			cnt = 0;
			s = pp * M - (depth*depth + (depth - 1)*(depth - 1));
			if (s >= 0 && result < pp) {
				result = pp;
			}
		}
		tmp = q.front();
		for (int i = 0; i < 4; i++)
		{
			tmp2.x = tmp.x + dx[i];
			tmp2.y = tmp.y + dy[i];
			if (iswall(tmp2)) {
				q.push(tmp2);
				visit[tmp2.y][tmp2.x]++;
				if (map[tmp2.y][tmp2.x])
					pp++;
			}
		}
		q.pop();
		cnt++;
	}
}

int main(){
	//freopen("input.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> T;
	for (int tc = 0; tc < T; tc++)
	{
		cin >> N >> M;
		max_s = 0;
		result = 0;
		max_pp = 0;
		for (int y = 0; y < N; y++) {
			for (int x = 0; x < N; x++) {
				cin >> map[y][x];
				if (map[y][x] == 1)
					max_pp++;
			}
		}
		for (int y = 0; y < N; y++) {
			for (int x = 0; x < N; x++) {
				bfs(x,y);
			}
		}
		cout <<"#" << tc+1 << " "<< result << '\n';
	}
	return 0;
}


