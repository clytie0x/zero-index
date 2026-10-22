#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(n + 1);
    vector<char> seen(n + 1);
    int first = 0, loops = 0;
    for (int i = 1; i <= m; i++) {
        int a, b;
        cin >> a >> b;
        fill(seen.begin(), seen.end(), 0);
        queue<int> q;
        q.push(a);
        seen[a] = 1;
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int to : adj[v]) {
                if (!seen[to]) {
                    seen[to] = 1;
                    q.push(to);
                }
            }
        }
        if (seen[b]) {
            loops++;
            if (first == 0) {
                first = i;
            }
        }
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    cout << first << '\n';
    cout << loops << '\n';
    return 0;
}
