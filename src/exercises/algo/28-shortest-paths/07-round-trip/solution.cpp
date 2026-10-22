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
    vector<vector<pair<int, int>>> forward(n + 1), backward(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        forward[u].push_back({v, w});
        backward[v].push_back({u, w});
    }
    vector<long long> go = dijkstra(forward, 1);
    vector<long long> back = dijkstra(backward, 1);
    long long total = 0;
    for (int v = 2; v <= n; v++) {
        if (go[v] == INF || back[v] == INF) {
            cout << -1 << '\n';
            return 0;
        }
        total += go[v] + back[v];
    }
    cout << total << '\n';
    return 0;
}
