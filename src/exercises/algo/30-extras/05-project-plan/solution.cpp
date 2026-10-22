#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<long long> days(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> days[i];
    }
    vector<vector<int>> next_tasks(n + 1);
    vector<int> waiting(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        next_tasks[a].push_back(b);
        waiting[b]++;
    }
    vector<long long> start(n + 1, 0);
    queue<int> ready;
    for (int task = 1; task <= n; task++) {
        if (waiting[task] == 0) {
            ready.push(task);
        }
    }
    long long answer = 0;
    while (!ready.empty()) {
        int task = ready.front();
        ready.pop();
        long long finish = start[task] + days[task];
        answer = max(answer, finish);
        for (int after : next_tasks[task]) {
            start[after] = max(start[after], finish);
            waiting[after]--;
            if (waiting[after] == 0) {
                ready.push(after);
            }
        }
    }
    cout << answer << '\n';
    return 0;
}
