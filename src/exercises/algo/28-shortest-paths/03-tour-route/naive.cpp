#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<pair<int, int>>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    vector<long long> dist(n + 1, INF);
    vector<int> parent(n + 1, 0);
    vector<bool> done(n + 1, false);
    dist[1] = 0;
    for (int round = 0; round < n; round++) {
        int u = -1;
        for (int i = 1; i <= n; i++) {
            if (!done[i] && (u == -1 || dist[i] < dist[u])) {
                u = i;
            }
        }
        if (dist[u] == INF) {
            break;
        }
        done[u] = true;
        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                parent[v] = u;
            }
        }
    }
    if (dist[n] == INF) {
        cout << -1 << '\n';
        return 0;
    }
    vector<int> path;
    for (int u = n; u != 0; u = parent[u]) {
        path.push_back(u);
    }
    reverse(path.begin(), path.end());
    cout << dist[n] << '\n';
    for (int i = 0; i < (int)path.size(); i++) {
        cout << path[i] << (i + 1 == (int)path.size() ? '\n' : ' ');
    }
    return 0;
}
