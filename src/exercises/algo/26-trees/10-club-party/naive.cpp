#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> boss(n + 1);
    for (int v = 1; v <= n; v++) {
        cin >> boss[v];
    }
    vector<long long> take(n + 1), skip(n + 1, 0);
    for (int v = 1; v <= n; v++) {
        cin >> take[v];
    }
    vector<pair<int, int>> by_depth;
    int root = 0;
    for (int v = 1; v <= n; v++) {
        int depth = 0;
        for (int u = v; boss[u] != 0; u = boss[u]) {
            depth++;
        }
        by_depth.push_back({-depth, v});
        if (boss[v] == 0) {
            root = v;
        }
    }
    sort(by_depth.begin(), by_depth.end());
    for (int i = 0; i < n; i++) {
        int v = by_depth[i].second;
        if (boss[v] != 0) {
            take[boss[v]] += skip[v];
            skip[boss[v]] += max(take[v], skip[v]);
        }
    }
    cout << max(take[root], skip[root]) << '\n';
    return 0;
}
