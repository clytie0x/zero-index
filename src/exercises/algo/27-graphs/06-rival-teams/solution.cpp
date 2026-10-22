#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001;
vector<int> adj[MAXN];
int team[MAXN];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    fill(team, team + n + 1, -1);
    int red = 0;
    for (int start = 1; start <= n; start++) {
        if (team[start] != -1) {
            continue;
        }
        int count[2] = {0, 0};
        queue<int> waiting;
        team[start] = 0;
        waiting.push(start);
        while (!waiting.empty()) {
            int v = waiting.front();
            waiting.pop();
            count[team[v]]++;
            for (int next : adj[v]) {
                if (team[next] == -1) {
                    team[next] = 1 - team[v];
                    waiting.push(next);
                } else if (team[next] == team[v]) {
                    cout << -1 << '\n';
                    return 0;
                }
            }
        }
        red += min(count[0], count[1]);
    }
    cout << red << '\n';
    return 0;
}
