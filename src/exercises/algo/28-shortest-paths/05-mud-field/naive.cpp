#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int rows, cols;
    cin >> rows >> cols;
    int total = rows * cols;
    vector<int> cost(total);
    for (int i = 0; i < total; i++) {
        cin >> cost[i];
    }
    if (cost[0] == -1 || cost[total - 1] == -1) {
        cout << -1 << '\n';
        return 0;
    }
    vector<long long> dist(total, INF);
    vector<bool> done(total, false);
    dist[0] = cost[0];
    for (int round = 0; round < total; round++) {
        int u = -1;
        for (int i = 0; i < total; i++) {
            if (!done[i] && (u == -1 || dist[i] < dist[u])) {
                u = i;
            }
        }
        if (dist[u] == INF) {
            break;
        }
        done[u] = true;
        int r = u / cols, c = u % cols;
        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) {
                continue;
            }
            int next = nr * cols + nc;
            if (cost[next] != -1 && dist[u] + cost[next] < dist[next]) {
                dist[next] = dist[u] + cost[next];
            }
        }
    }
    cout << (dist[total - 1] == INF ? -1 : dist[total - 1]) << '\n';
    return 0;
}
