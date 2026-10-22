#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

vector<long long> dijkstra(const vector<vector<pair<int, int>>> &adj, int start)
{
    int n = (int)adj.size() - 1;
    vector<long long> dist(n + 1, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    dist[start] = 0;
    pq.push({0, start});
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
    return dist;
}

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
    }
    vector<long long> go = dijkstra(adj, 1);
    long long total = 0;
    bool possible = true;
    for (int v = 2; v <= n; v++) {
        long long back = dijkstra(adj, v)[1];
        if (go[v] == INF || back == INF) {
            possible = false;
        } else {
            total += go[v] + back;
        }
    }
    cout << (possible ? total : -1) << '\n';
    return 0;
}
