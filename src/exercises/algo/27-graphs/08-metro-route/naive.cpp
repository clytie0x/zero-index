#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001;
vector<int> adj[MAXN];
int dist[MAXN];
int n;

int rides(int from, int to)
{
    fill(dist, dist + n + 1, -1);
    queue<int> waiting;
    dist[from] = 0;
    waiting.push(from);
    while (!waiting.empty()) {
        int v = waiting.front();
        waiting.pop();
        if (v == to) {
            return dist[v];
        }
        for (int next : adj[v]) {
            if (dist[next] == -1) {
                dist[next] = dist[v] + 1;
                waiting.push(next);
            }
        }
    }
    return -1;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m, start, goal;
    cin >> n >> m >> start >> goal;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    for (int v = 1; v <= n; v++) {
        sort(adj[v].begin(), adj[v].end());
    }
    int total = rides(start, goal);
    if (total == -1) {
        cout << -1 << '\n';
        return 0;
    }
    cout << total << '\n';
    int v = start;
    cout << v;
    for (int left = total; left > 0; left--) {
        for (int next : adj[v]) {
            if (rides(next, goal) == left - 1) {
                v = next;
                break;
            }
        }
        cout << ' ' << v;
    }
    cout << '\n';
    return 0;
}
