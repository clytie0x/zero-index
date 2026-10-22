#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> next_steps(n + 1);
    vector<int> waiting(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        next_steps[a].push_back(b);
        waiting[b]++;
    }
    priority_queue<int, vector<int>, greater<int>> ready;
    for (int step = 1; step <= n; step++) {
        if (waiting[step] == 0) {
            ready.push(step);
        }
    }
    vector<int> order;
    while (!ready.empty()) {
        int step = ready.top();
        ready.pop();
        order.push_back(step);
        for (int after : next_steps[step]) {
            waiting[after]--;
            if (waiting[after] == 0) {
                ready.push(after);
            }
        }
    }
    if ((int)order.size() < n) {
        cout << -1 << '\n';
        return 0;
    }
    for (int i = 0; i < n; i++) {
        cout << order[i] << (i + 1 == n ? '\n' : ' ');
    }
    return 0;
}
