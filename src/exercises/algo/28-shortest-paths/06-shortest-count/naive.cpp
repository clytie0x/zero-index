#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;
const long long MOD = 1000000007;

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
    vector<long long> dist(n + 1, INF), ways(n + 1, 0);
    vector<bool> done(n + 1, false);
    dist[1] = 0;
    ways[1] = 1;
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
                ways[v] = ways[u];
            } else if (dist[u] + w == dist[v]) {
                ways[v] = (ways[v] + ways[u]) % MOD;
            }
        }
    }
    if (dist[n] == INF) {
        cout << -1 << '\n';
    } else {
        cout << dist[n] << ' ' << ways[n] << '\n';
    }
    return 0;
}
