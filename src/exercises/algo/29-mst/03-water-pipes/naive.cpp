#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<tuple<int, int, int>> pipes(m);
    for (int i = 0; i < m; i++) {
        int a, b, cost;
        cin >> a >> b >> cost;
        pipes[i] = {cost, a, b};
    }
    sort(pipes.begin(), pipes.end());
    vector<vector<int>> chosen(n + 1);
    vector<bool> seen(n + 1);
    long long total = 0;
    int used = 0;
    for (auto [cost, a, b] : pipes) {
        fill(seen.begin(), seen.end(), false);
        queue<int> q;
        q.push(a);
        seen[a] = true;
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int to : chosen[v]) {
                if (!seen[to]) {
                    seen[to] = true;
                    q.push(to);
                }
            }
        }
        if (!seen[b]) {
            chosen[a].push_back(b);
            chosen[b].push_back(a);
            total += cost;
            used++;
        }
    }
    if (used == n - 1) {
        cout << total << '\n';
    } else {
        cout << -1 << '\n';
    }
    return 0;
}
