#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000000;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<vector<int>> dist(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> dist[i][j];
        }
    }
    int urgent = 0;
    for (int i = 0; i < k; i++) {
        int shop;
        cin >> shop;
        urgent |= 1 << shop;
    }
    if (n == 1) {
        cout << 0 << '\n';
        return 0;
    }
    int full = (1 << n) - 1;
    vector<vector<int>> best(1 << n, vector<int>(n, INF));
    best[1][0] = 0;
    for (int mask = 1; mask <= full; mask++) {
        bool urgent_done = (mask & urgent) == urgent;
        for (int last = 0; last < n; last++) {
            if (best[mask][last] == INF) {
                continue;
            }
            for (int next = 0; next < n; next++) {
                if ((mask & (1 << next)) != 0) {
                    continue;
                }
                if ((urgent & (1 << next)) == 0 && !urgent_done) {
                    continue;
                }
                int grown = mask | (1 << next);
                best[grown][next] = min(best[grown][next], best[mask][last] + dist[last][next]);
            }
        }
    }
    int answer = INF;
    for (int last = 1; last < n; last++) {
        answer = min(answer, best[full][last] + dist[last][0]);
    }
    cout << answer << '\n';
    return 0;
}
