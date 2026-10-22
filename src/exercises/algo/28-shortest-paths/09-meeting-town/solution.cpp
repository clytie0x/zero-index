#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<long long>> d(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; i++) {
        d[i][i] = 0;
    }
    for (int e = 0; e < m; e++) {
        int u, v, w;
        cin >> u >> v >> w;
        d[u][v] = min(d[u][v], (long long)w);
        d[v][u] = min(d[v][u], (long long)w);
    }
    for (int via = 1; via <= n; via++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (d[i][via] + d[via][j] < d[i][j]) {
                    d[i][j] = d[i][via] + d[via][j];
                }
            }
        }
    }
    vector<int> home(k);
    for (int i = 0; i < k; i++) {
        cin >> home[i];
    }
    int best_town = -1;
    long long best_total = INF;
    for (int town = 1; town <= n; town++) {
        long long total = 0;
        bool everyone = true;
        for (int i = 0; i < k; i++) {
            if (d[home[i]][town] == INF) {
                everyone = false;
                break;
            }
            total += d[home[i]][town];
        }
        if (everyone && total < best_total) {
            best_total = total;
            best_town = town;
        }
    }
    if (best_town == -1) {
        cout << -1 << '\n';
    } else {
        cout << best_town << ' ' << best_total << '\n';
    }
    return 0;
}
