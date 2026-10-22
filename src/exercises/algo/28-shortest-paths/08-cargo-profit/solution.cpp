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
    vector<long long> dist(n + 1, INF);
    dist[1] = 0;
    for (int round = 1; round <= n - 1; round++) {
        bool changed = false;
        for (int i = 0; i < m; i++) {
            int u = from[i], v = to[i];
            if (dist[u] != INF && dist[u] + cost[i] < dist[v]) {
                dist[v] = dist[u] + cost[i];
                changed = true;
            }
        }
        if (!changed) {
            break;
        }
    }
    vector<bool> endless(n + 1, false);
    for (int round = 1; round <= n; round++) {
        for (int i = 0; i < m; i++) {
            int u = from[i], v = to[i];
            if (dist[u] == INF) {
                continue;
            }
            if (endless[u] || dist[u] + cost[i] < dist[v]) {
                endless[v] = true;
                dist[v] = min(dist[v], dist[u] + cost[i]);
            }
        }
    }
    if (dist[n] == INF) {
        cout << "unreachable" << '\n';
    } else if (endless[n]) {
        cout << "-inf" << '\n';
    } else {
        cout << dist[n] << '\n';
    }
    return 0;
}
