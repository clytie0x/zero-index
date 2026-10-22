#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, start;
    cin >> n >> m >> start;
    vector<vector<pair<int, int>>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }
    vector<long long> dist(n + 1, INF);
    vector<bool> done(n + 1, false);
    dist[start] = 0;
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
            }
        }
    }
    for (int u = 1; u <= n; u++) {
        cout << (dist[u] == INF ? -1 : dist[u]) << (u == n ? '\n' : ' ');
    }
    return 0;
}
