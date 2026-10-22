#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001;
vector<int> adj[MAXN];
bool seen[MAXN];

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
    int no_loop = 0, ring = 0;
    for (int start = 1; start <= n; start++) {
        if (seen[start]) {
            continue;
        }
        long long villages = 0, road_ends = 0;
        bool all_two = true;
        stack<int> waiting;
        seen[start] = true;
        waiting.push(start);
        while (!waiting.empty()) {
            int v = waiting.top();
            waiting.pop();
            villages++;
            road_ends += adj[v].size();
            if (adj[v].size() != 2) {
                all_two = false;
            }
            for (int next : adj[v]) {
                if (!seen[next]) {
                    seen[next] = true;
                    waiting.push(next);
                }
            }
        }
        if (road_ends / 2 == villages - 1) {
            no_loop++;
        } else if (all_two) {
            ring++;
        }
    }
    cout << no_loop << ' ' << ring << '\n';
    return 0;
}
