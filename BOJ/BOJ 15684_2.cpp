#include <iostream>
#include <vector>

using namespace std;

int N, M, H;
vector<vector<int>> A(10);
vector<vector<int>> my_stack(10);
int min_set;
int tmp;
int even_tmp;
int conet[50][50];
int cnt2,cnt;

int search(int col);
int jug();
void jin(int i, int col);

int main()
{
	int c, d;
	int result;

	cin >> N >> M >> H;
	min_set = M;
	tmp = 0;

	for (int i = 0; i < M; i++)
	{
		cin >> c >> d;
		conet[d - 1][c - 1]++;
	}

	result = search(0);

	if (result > 3)
		cout << -1;
	else
		cout << result;
	return 0;
}

int search(int col)
{
	if (min_set < tmp)
		return min_set;
	if (jug() && min_set > tmp) {
		min_set = tmp;
		return min_set;
	}
	if (col - N + 1 == 0) {
		return min_set;
	}

	my_stack[col].clear();
	for (int i = 0; i < H; i++)
	{
		if (!A[col][i] && !A[col + 1][i])
		{
			my_stack[col].push_back(i);
		}
		jin(0, col);
	}

	return min_set;
}

int jug()
{
	cnt2 = 0;
	for (int a = 0; a < N; a++) {
		cnt = 0;
		for (int b = 0; b < H; b++) {
			if (a + cnt != 0 && conet[a + cnt - 1][b])
				cnt--;
			else if (a + cnt != N - 1 && conet[a + cnt][b])
				cnt++;
		}
		if (cnt != 0) {
			cnt2++;
			break;
		}
	}
	if (!cnt2)
		return 1;
	else
		return 0;
}

void jin(int i, int col)
{
	if (tmp > min_set)
		return;
	if (my_stack[col].size() == 0)
		return;
	int a;
	a = 0;
	if (i == my_stack[col].size() - 1) {
		min_set = search(col + 1);
		tmp++;
		conet[col][my_stack[col][i]]++;
		min_set = search(col + 1);
		conet[col][my_stack[col][i]]--;
		tmp--;
		return;
	}
	else {
		jin(i + 1, col);
		tmp++;
		conet[col][my_stack[col][i]]++;
		jin(i + 1, col);
		conet[col][my_stack[col][i]]--;
		tmp--;
	}

	return;
}