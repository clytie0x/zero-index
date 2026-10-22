#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<pair<int, int>>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    vector<long long> best(n + 1, INF);
    for (int i = 0; i < k; i++) {
        int shelter;
        cin >> shelter;
        vector<long long> dist(n + 1, INF);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        dist[shelter] = 0;
        pq.push({0, shelter});
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (d > dist[u]) {
                continue;
            }
            for (auto [v, w] : adj[u]) {
                if (d + w < dist[v]) {
                    dist[v] = d + w;
                    pq.push({dist[v], v});
                }
            }
        }
        for (int u = 1; u <= n; u++) {
            best[u] = min(best[u], dist[u]);
        }
    }
    long long longest = 0;
    int stranded = 0;
    for (int u = 1; u <= n; u++) {
        if (best[u] == INF) {
            stranded++;
        } else {
            longest = max(longest, best[u]);
        }
    }
    cout << longest << ' ' << stranded << '\n';
    return 0;
}
