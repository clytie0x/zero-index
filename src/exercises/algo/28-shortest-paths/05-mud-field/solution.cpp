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
    vector<int> cost(rows * cols);
    for (int i = 0; i < rows * cols; i++) {
        cin >> cost[i];
    }
    int last = rows * cols - 1;
    if (cost[0] == -1 || cost[last] == -1) {
        cout << -1 << '\n';
        return 0;
    }
    vector<long long> dist(rows * cols, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    dist[0] = cost[0];
    pq.push({dist[0], 0});
    while (!pq.empty()) {
        auto [d, id] = pq.top();
        pq.pop();
        if (d > dist[id]) {
            continue;
        }
        int r = id / cols, c = id % cols;
        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) {
                continue;
            }
            int next = nr * cols + nc;
            if (cost[next] == -1) {
                continue;
            }
            if (d + cost[next] < dist[next]) {
                dist[next] = d + cost[next];
                pq.push({dist[next], next});
            }
        }
    }
    cout << (dist[last] == INF ? -1 : dist[last]) << '\n';
    return 0;
}
