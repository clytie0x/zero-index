#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001;
vector<int> adj[MAXN];
int to_goal[MAXN];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, start, goal;
    cin >> n >> m >> start >> goal;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    fill(to_goal, to_goal + n + 1, -1);
    queue<int> waiting;
    to_goal[goal] = 0;
    waiting.push(goal);
    while (!waiting.empty()) {
        int v = waiting.front();
        waiting.pop();
        for (int next : adj[v]) {
            if (to_goal[next] == -1) {
                to_goal[next] = to_goal[v] + 1;
                waiting.push(next);
            }
        }
    }
    if (to_goal[start] == -1) {
        cout << -1 << '\n';
        return 0;
    }
    cout << to_goal[start] << '\n';
    int v = start;
    cout << v;
    while (v != goal) {
        int best = -1;
        for (int next : adj[v]) {
            if (to_goal[next] == to_goal[v] - 1 && (best == -1 || next < best)) {
                best = next;
            }
        }
        v = best;
        cout << ' ' << v;
    }
    cout << '\n';
    return 0;
}
