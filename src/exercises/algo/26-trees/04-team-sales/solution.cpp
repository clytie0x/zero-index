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
    vector<long long> total(n + 1);
    for (int v = 1; v <= n; v++) {
        cin >> total[v];
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
        total[boss[v]] += total[v];
    }
    for (int v = 1; v <= n; v++) {
        if (v > 1) {
            cout << ' ';
        }
        cout << total[v];
    }
    cout << '\n';
    return 0;
}
