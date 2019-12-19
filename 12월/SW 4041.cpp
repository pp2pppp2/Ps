//#include <iostream>
//#include <queue>
//
//using namespace std;
//
//int CCW(int ax, int ay, int bx, int by, int cx, int cy) {
//	int t = (bx - ax) * (cy - ay) - (cx - ax) * (by - ay);
//	if (t > 0) return 1;
//	if (t < 0) return -1;
//	return 0;
//}
//struct xy{
//	int x, y;
//};
//
//struct com {
//	bool operator()(xy a, xy b) {
//		if (a.y > b.y)
//			return true;
//		else if (a.x > b.y)
//			return true;
//		return false;
//	}
//};
//
//priority_queue<xy, vector<xy>, com> pq;
//
//int main() {
//	int T, N;
//	cin >> T;
//	for (int tc = 1; tc < T; ++tc) {
//		cin >> N;
//		
//	}
//	return 0;
//}