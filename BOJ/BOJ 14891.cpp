#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<int> G_pos(1000);
vector<int> G_index(1000);
vector<int> G_visit(1000);
vector<vector<int>> A(1000);
int c, d;
int T;

void G_poss()
{
	G_pos.assign(1000, 0);
	for (int i = 0; i < T-1; i++)	{
		c = (G_index[i]+2) %8;
		d = (G_index[i+1]+6) %8;
		if (A[i][c] != A[i + 1][d])
			G_pos[i] = 1;
	}
}

void G_rott(int G_num, int G_rot)
{
	if (G_num == 1 && !G_visit[0])
	{
		G_visit[0] = 1;
		G_index[0] += G_rot;
		if (G_index[0] == -1)
			G_index[0] = 7;
		G_index[0] %= 8;
		if (G_pos[0]){
			G_rott(2, -G_rot);
		}
	}
	else if (G_num == T && !G_visit[T-1])
	{
		G_visit[T-1] = 1;
		G_index[T-1] += G_rot;
		if (G_index[T-1] == -1)
			G_index[T-1] = 7;
		G_index[T-1] %= 8;
		if (G_pos[T-2]) {
			G_rott(T-1, -G_rot);
		}
	}
	else if (!G_visit[G_num-1])
	{
		G_visit[G_num-1] = 1;
		G_index[G_num - 1] += G_rot;
		if (G_index[G_num - 1] == -1)
			G_index[G_num - 1] = 7;
		G_index[G_num - 1] %= 8;
		if (G_pos[G_num - 2]) {
			G_rott(G_num - 1, -G_rot);
		}
		if (G_pos[G_num - 1]) {
			G_rott(G_num + 1, -G_rot);
		}
	}
}

int main()
{
	int result;
	char IP[9];
	int K;
	int G_num, G_rot;


	cin >> T;
	for (int j = 0; j < T; j++) {
		cin >> IP;
		A[j].assign(8, 0);
		for (int i = 0; i < 8; i++) {
			A[j][i] += IP[i] - '0';
		}
	}

	cin >> K;
	G_index.assign(T, 0);
	for (int i = 0; i < K; i++) {
		cin >> G_num >> G_rot;
		G_poss();
		//for (int a = 0; a < 4; a++)
		//{
		//	cout << G_index[a];
		//}
		G_visit.assign(1000, 0);
		G_rott(G_num, -G_rot);
	}

	result = 0;

	for (int i = 0; i < T; i++) {
		result += A[i][G_index[i]];
	}

	cout << result;

	return 0;
}