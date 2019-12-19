//#include <iostream>
//#include <vector>
//#include <queue>
//
//using namespace std;
//
//struct ma {
//	int idx, val;
//};
//
//int visit[50001];
//int visit2[50001];
//long long dist[50001];
//long long dist2[50001];
//int vertex;
//int edge;
//int start;
//int ret;
//
//struct com {
//	bool operator()(ma a, ma b) {
//		if (a.val > b.val)
//			return true;
//		return false;
//	}
//};
//
//vector<vector<ma>> mav;
//vector<vector<ma>> mav2;
//priority_queue<ma, vector<ma>, com> pq;
//
//void dijkstra(void)
//{
//	int i;
//	int j;
//	int v;
//	ma tmp;
//	tmp.idx = start;
//	tmp.val = 0;
//	pq.push(tmp);
//	dist[start] = 0;
//
//	while (!pq.empty())
//	{
//		tmp = pq.top();
//		pq.pop();
//		v = tmp.idx;
//		if (visit[v]) continue;
//		visit[v] = 1;
//
//		for (j = 0; j < mav[v].size(); j++)
//		{
//			if (dist[mav[v][j].idx] > dist[v] + mav[v][j].val) {
//				dist[mav[v][j].idx] = dist[v] + mav[v][j].val;
//				tmp.idx = mav[v][j].idx;
//				tmp.val = dist[mav[v][j].idx];
//				pq.push(tmp);
//			}
//		}
//	}
//
//	tmp.idx = start;
//	tmp.val = 0;
//	pq.push(tmp);
//	dist[start] = 0;
//
//	while (!pq.empty())
//	{
//		tmp = pq.top();
//		pq.pop();
//		v = tmp.idx;
//		if (visit2[v]) continue;
//		visit2[v] = 1;
//
//		for (j = 0; j < mav2[v].size(); j++)
//		{
//			if (dist2[mav2[v][j].idx] > dist2[v] + mav2[v][j].val) {
//				dist2[mav2[v][j].idx] = dist2[v] + mav2[v][j].val;
//				tmp.idx = mav2[v][j].idx;
//				tmp.val = dist2[mav2[v][j].idx];
//				pq.push(tmp);
//			}
//		}
//	}
//}
//
//int main(void)
//{
//	int test_case;
//	int T;
//	int i;
//	int j;
//	int from;
//	int to;
//	int value;
//	int end;
//
//	scanf("%d", &T);
//
//	for (test_case = 1; test_case <= T; test_case++)
//	{
//		scanf("%d %d %d", &vertex, &edge, &start);
//		mav.clear();
//		mav.resize(vertex + 1);
//		mav2.clear();
//		mav2.resize(vertex + 1);
//
//		for (i = 1; i <= edge; i++)
//		{
//			scanf("%d %d %d", &from, &to, &value);
//			ma mp;
//			mp.idx = to;
//			mp.val = value;
//			mav[from].push_back(mp);
//			mp.idx = from;
//			mav2[to].push_back(mp);
//		}
//		memset(visit, 0, sizeof(visit));
//		memset(dist, 284, sizeof(dist));
//		memset(dist2, 284, sizeof(dist2));
//
//		printf("#%d ", test_case);
//		dijkstra();
//		ret = 0;
//		for (int i = 1; i <= vertex; ++i) {
//			int tmp = dist[i] + dist2[i];
//			ret = max(ret, tmp);
//		}
//		printf("%d \n", ret);
//	}
//	return 0;
//}