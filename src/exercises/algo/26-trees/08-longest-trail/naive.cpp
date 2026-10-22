#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> parent(n + 1);
    for (int v = 1; v <= n; v++) {
        cin >> parent[v];
    }
    vector<vector<pair<int, long long>>> next_to(n + 1);
    for (int v = 1; v <= n; v++) {
        long long length;
        cin >> length;
        if (parent[v] != 0) {
            next_to[v].push_back({parent[v], length});
            next_to[parent[v]].push_back({v, length});
        }
    }
    long long answer = 0;
    vector<long long> dist(n + 1);
    vector<int> came_from(n + 1);
    for (int start = 1; start <= n; start++) {
        stack<int> waiting;
        waiting.push(start);
        dist[start] = 0;
        came_from[start] = 0;
        while (!waiting.empty()) {
            int v = waiting.top();
            waiting.pop();
            answer = max(answer, dist[v]);
            for (auto [u, length] : next_to[v]) {
                if (u != came_from[v]) {
                    came_from[u] = v;
                    dist[u] = dist[v] + length;
                    waiting.push(u);
                }
            }
        }
    }
    cout << answer << '\n';
    return 0;
}
