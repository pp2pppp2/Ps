#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

int N, M, H;
vector<vector<int>> my_stack(10);
int min_set;
int tmp;
int conet[12][32];
int min_tmp;
int cnt;
int cnt2;
int a;
int cc;

int search(int col);// , int min);
int jug();
void jin(int i, int col);

int main()
{
	int c, d;
	int result;

	cin >> N >> M >> H;
	min_set = 0;
	tmp = 0;
	cc = 0;
	result = 0;
	memset(conet, 0, sizeof(conet));

	for (int i = 0; i < M; i++)	{
		cin >> c >> d;
		conet[d - 1][c - 1]++;
	}

	if (jug())
		result = 0;
	else{
		//while (result == 0) {
		//	min_tmp = cc;
		//	result = search(0, min_tmp);
		//	cc++;
		//	if (cc == 4){
		//		result = -1;
		//		break;
		//	}
		//}	
		min_tmp = 5;
		result = search(0);// , min_tmp);
	}
	cout << result;
	return 0;
}

int search(int col)//, int min_tmp)
{
	//if (min_set == min_tmp)
	//	return min_set;
	if (col - N + 1 == 0) {
		if (min_set > tmp && jug()) {
			min_set = tmp;
			return min_set;
		}
		return min_set;
	}
	/*if (tmp > min_tmp) {
		if (min_set < tmp && jug()) {
			min_set = tmp;
			return min_set;
		}
		return search(col + 1, min_tmp);
	}*/
	//even_tmp = 0;
	//for (int j = 0; j < H; j++)
	//{
	//	even_tmp += A[col][j];
	//}

	my_stack[col].clear();
	for (int i = 0; i < H; i++) {
		if (!conet[col][i] && !conet[col+1][i]){
			my_stack[col].push_back(i);
		}
		jin(0, col);
	}

	return min_set;
}

int jug()
{
	cnt2 = 0;
	for (int a = 0; a < N; a++)	{
		cnt = 0;
		for (int b = 0; b < H; b++)		{
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
	if (/*min_set > min_tmp ||*/ tmp  > min_tmp)
		return;
	if (tmp > 3)
		return;
	if (my_stack[col].size() == 0)
		return;

	a = 0;
	if (i == my_stack[col].size() - 1) {
		min_set = search(col + 1);// , min_tmp);
		tmp++;
		conet[col][my_stack[col][i]]++;
		min_set = search(col + 1);//, min_tmp);
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