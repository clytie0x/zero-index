#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, q;
    cin >> n >> m >> q;
    vector<vector<pair<int, int>>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b, limit;
        cin >> a >> b >> limit;
        adj[a].push_back(make_pair(b, limit));
        adj[b].push_back(make_pair(a, limit));
    }
    vector<bool> seen(n + 1);
    for (int j = 0; j < q; j++) {
        int x, y, weight;
        cin >> x >> y >> weight;
        fill(seen.begin(), seen.end(), false);
        queue<int> bfs;
        bfs.push(x);
        seen[x] = true;
        while (!bfs.empty()) {
            int v = bfs.front();
            bfs.pop();
            for (auto [next, limit] : adj[v]) {
                if (limit >= weight && !seen[next]) {
                    seen[next] = true;
                    bfs.push(next);
                }
            }
        }
        cout << (seen[y] ? "YES" : "NO") << '\n';
    }
    return 0;
}
