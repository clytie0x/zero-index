#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001;
vector<int> adj[MAXN];
int team[MAXN];
char registered[MAXN];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, k;
    cin >> n >> m >> k;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    for (int i = 0; i < k; i++) {
        int v;
        char color;
        cin >> v >> color;
        registered[v] = color;
    }
    fill(team, team + n + 1, -1);
    int red = 0;
    for (int start = 1; start <= n; start++) {
        if (team[start] != -1) {
            continue;
        }
        int side_size[2] = {0, 0};
        int red_side = -1;
        queue<int> waiting;
        team[start] = 0;
        waiting.push(start);
        while (!waiting.empty()) {
            int v = waiting.front();
            waiting.pop();
            side_size[team[v]]++;
            if (registered[v] != 0) {
                int need = (registered[v] == 'R' ? team[v] : 1 - team[v]);
                if (red_side == -1) {
                    red_side = need;
                } else if (red_side != need) {
                    cout << -1 << '\n';
                    return 0;
                }
            }
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
        if (red_side == -1) {
            red += min(side_size[0], side_size[1]);
        } else {
            red += side_size[red_side];
        }
    }
    cout << red << '\n';
    return 0;
}
