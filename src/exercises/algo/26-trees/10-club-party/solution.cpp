#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> boss(n + 1);
    vector<vector<int>> team(n + 1);
    int root = 0;
    for (int v = 1; v <= n; v++) {
        cin >> boss[v];
        if (boss[v] == 0) {
            root = v;
        } else {
            team[boss[v]].push_back(v);
        }
    }
    vector<long long> take(n + 1), skip(n + 1, 0);
    for (int v = 1; v <= n; v++) {
        cin >> take[v];
    }
    vector<int> order;
    stack<int> waiting;
    waiting.push(root);
    while (!waiting.empty()) {
        int v = waiting.top();
        waiting.pop();
        order.push_back(v);
        for (int c : team[v]) {
            waiting.push(c);
        }
    }
    for (int i = n - 1; i >= 1; i--) {
        int v = order[i];
        take[boss[v]] += skip[v];
        skip[boss[v]] += max(take[v], skip[v]);
    }
    cout << max(take[root], skip[root]) << '\n';
    return 0;
}
