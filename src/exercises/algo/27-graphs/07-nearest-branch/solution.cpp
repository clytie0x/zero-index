#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001;
vector<int> adj[MAXN];
int dist[MAXN];
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
    fill(dist, dist + n + 1, -1);
    queue<int> waiting;
    for (int b : branches) {
        dist[b] = 0;
        owner[b] = b;
        waiting.push(b);
    }
    while (!waiting.empty()) {
        int v = waiting.front();
        waiting.pop();
        served[owner[v]]++;
        for (int next : adj[v]) {
            if (dist[next] == -1) {
                dist[next] = dist[v] + 1;
                owner[next] = owner[v];
                waiting.push(next);
            } else if (dist[next] == dist[v] + 1 && owner[v] < owner[next]) {
                owner[next] = owner[v];
            }
        }
    }
    for (int i = 0; i < k; i++) {
        cout << served[branches[i]] << (i + 1 == k ? '\n' : ' ');
    }
    return 0;
}
