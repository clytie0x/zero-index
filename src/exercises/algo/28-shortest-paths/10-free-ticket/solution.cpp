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
    vector<long long> dist(2 * n + 1, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    dist[1] = 0;
    pq.push({0, 1});
    while (!pq.empty()) {
        auto [d, state] = pq.top();
        pq.pop();
        if (d > dist[state]) {
            continue;
        }
        bool used = state > n;
        int u = used ? state - n : state;
        for (auto [v, w] : adj[u]) {
            int next = used ? n + v : v;
            if (d + w < dist[next]) {
                dist[next] = d + w;
                pq.push({dist[next], next});
            }
            if (!used && d < dist[n + v]) {
                dist[n + v] = d;
                pq.push({d, n + v});
            }
        }
    }
    long long answer = min(dist[n], dist[2 * n]);
    cout << (answer == INF ? -1 : answer) << '\n';
    return 0;
}
