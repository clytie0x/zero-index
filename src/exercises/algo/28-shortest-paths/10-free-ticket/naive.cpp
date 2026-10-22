#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> from(m), to(m), cost(m);
    for (int i = 0; i < m; i++) {
        cin >> from[i] >> to[i] >> cost[i];
    }
    long long best = INF;
    for (int free_road = 0; free_road < m; free_road++) {
        vector<vector<pair<int, int>>> adj(n + 1);
        for (int i = 0; i < m; i++) {
            int w = (i == free_road ? 0 : cost[i]);
            adj[from[i]].push_back({to[i], w});
            adj[to[i]].push_back({from[i], w});
        }
        vector<long long> dist(n + 1, INF);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        dist[1] = 0;
        pq.push({0, 1});
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
        best = min(best, dist[n]);
    }
    cout << (best == INF ? -1 : best) << '\n';
    return 0;
}
