#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<string.h>
#include<algorithm>

using namespace std;
int main(int argc, char** argv)
{
	int K;
	int i;
	int a;
	int cnt;
	char input[1020];
	vector<int> st;

	freopen("input.txt", "r", stdin);

	cin >> K;

	for (int tc = 1; tc <= K; tc++)
	{
		memset(input, '\0', sizeof(input));
		cin >> input;
		cnt = 0;
		i = 0;
		st.clear();
		
		while (input[i]) {
			st.push_back(input[i] - '0');
			i++;
		}
		
		while (!st.empty()){
			a = 0;
			a += st.back();
			st.pop_back();
			if (st.empty())
				break;
			a += st.back();
			st.pop_back();
			if (a > 9)
				st.push_back(a / 10);
			st.push_back(a % 10);
			cnt++;
		}

		if (cnt & 1)
			cout <<"#"<< tc <<" "<< "A";
		else
			cout <<"#"<< tc <<" "<< "B";
		cout << '\n';
	}
	return 0;
}
