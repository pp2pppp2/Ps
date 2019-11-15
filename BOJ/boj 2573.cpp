//#include<iostream>
//#include<queue>
//
//using namespace std;
//struct xy {
//	int x, y;
//};
//int N, M;
//int fx, fy;
//int tx, ty;
//int mcnt, ret;
//int m[301][301];
//int visit[301][301];
//int dx[4] = { 0,0,1,-1 };
//int dy[4] = { 1,-1,0,0 };
//int rrcnt;
//int flag;
//xy t;
//xy f;
//queue<xy> q;
//
//void d() {
//	int asd = 0;
//	rrcnt = 1;
//	f.x = fx;
//	f.y = fy;
//	q.push(f);
//	visit[f.y][f.x] = ret;
//	while (!q.empty()) {
//		t = q.front();
//		q.pop();
//		for (int i = 0; i < 4; ++i) {
//			tx = t.x + dx[i];
//			ty = t.y + dy[i];
//			if (tx >= 0 && tx < M && ty >= 0 && ty < N && visit[ty][tx] < ret) {
//				if (m[ty][tx] <= 0) {
//					m[t.y][t.x]--;
//					if (m[t.y][t.x] == 0) {
//						asd++;
//					}
//				}
//				else {
//					f.x = tx;
//					f.y = ty;
//					rrcnt++;
//					visit[ty][tx] = ret;
//					q.push(f);
//				}
//			}
//		}
//	}
//	if (rrcnt != mcnt) {
//		flag = 0;
//	}
//	mcnt -= asd;
//	for (int y = 0; y < N; ++y) {
//		for (int x = 0; x < M; ++x) {
//			if (m[y][x] > 0) {
//				fx = x;
//				fy = y;
//			}
//		}
//	}
//}
//
//
//int main() {
//	ios_base::sync_with_stdio(NULL);
//	cin.tie(NULL);
//	cin >> N >> M;
//	mcnt = 0;
//	ret = 1;
//	fx = -1;
//	for (int y = 0; y < N; ++y) {
//		for (int x = 0; x < M; ++x) {
//			cin >> m[y][x];
//			if (m[y][x] != 0) {
//				mcnt++;
//				if (fx == -1) {
//					fx = x;
//					fy = y;
//				}
//			}
//		}
//	}
//	if (fx == -1) {
//		fx = 1;
//		fy = 1;
//	}
//	flag = 1;
//	while (flag) {
//		ret++;
//		d();
//	}
//	int fd = 0;
//	for (int y = 0; y < N; ++y) {
//		for (int x = 0; x < M; ++x) {
//			if (m[y][x] > 0 && visit[y][x] < ret)
//				fd++;
//		}
//	}
//	if (fd == 0)
//		cout << 0;
//	else
//		cout << ret - 2;
//	return 0;
//}