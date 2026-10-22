#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001;
vector<int> adj[MAXN];
int dist[MAXN];
int best_dist[MAXN];
int owner[MAXN];
int served[MAXN];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, k;
    cin >> n >> m >> k;
    vector<int> branches(k);
    for (int i = 0; i < k; i++) {
        cin >> branches[i];
    }
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    fill(best_dist, best_dist + n + 1, -1);
    for (int b : branches) {
        fill(dist, dist + n + 1, -1);
        queue<int> waiting;
        dist[b] = 0;
        waiting.push(b);
        while (!waiting.empty()) {
            int v = waiting.front();
            waiting.pop();
            for (int next : adj[v]) {
                if (dist[next] == -1) {
                    dist[next] = dist[v] + 1;
                    waiting.push(next);
                }
            }
        }
        for (int v = 1; v <= n; v++) {
            if (dist[v] == -1) {
                continue;
            }
            if (best_dist[v] == -1 || dist[v] < best_dist[v] || (dist[v] == best_dist[v] && b < owner[v])) {
                best_dist[v] = dist[v];
                owner[v] = b;
            }
        }
    }
    for (int v = 1; v <= n; v++) {
        if (best_dist[v] != -1) {
            served[owner[v]]++;
        }
    }
    for (int i = 0; i < k; i++) {
        cout << served[branches[i]] << (i + 1 == k ? '\n' : ' ');
    }
    return 0;
}
