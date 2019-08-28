#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main()
{
	int K;
	int N;
	int A;
	int B;
	int c;
	int time;
	int limit_n;
	int tmp;
	queue<int> table;
	queue<int> all_table;
	vector<int> result;

	freopen("input.txt", "r", stdin);

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> K;

	for (int test_kace = 1; test_kace <= K; test_kace++)
	{

		cin >> N >> A >> B;
		time = 0;
		limit_n = A / 2 + A % 2;

		for (int i = 0; i < N; i++)
		{
			cin >> tmp;
			all_table.push(tmp);
		}

		while (!table.empty() || !all_table.empty())
		{
			time++;
			if (!all_table.empty() && all_table.front() == time)
			{
				table.push(all_table.front());
				all_table.pop();
			}
			
			if (table.size() >= A)
			{
				for (int a = 0; a < limit_n; a++)
				{
					result.push_back(time);
					table.pop();
				}
			}
			
			if (!table.empty() && time - table.front() == B)
			{
				c = table.size() / 2 + table.size() % 2;
				for (int a = 0; a < c ; a++)
				{
					result.push_back(time);
					table.pop();
				}
			}	
		}
		cout << "#" << test_kace;
		
		for (int i = 0; i < result.size(); i++)
		{
			cout << " " << result[i];
		}
		result.clear();
		cout << '\n';
	}
	return 0;
}