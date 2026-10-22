#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001;
vector<int> out_roads[MAXN];

vector<bool> reachable_from(int n, int start)
{
    vector<bool> seen(n + 1, false);
    queue<int> waiting;
    seen[start] = true;
    waiting.push(start);
    while (!waiting.empty()) {
        int v = waiting.front();
        waiting.pop();
        for (int next : out_roads[v]) {
            if (!seen[next]) {
                seen[next] = true;
                waiting.push(next);
            }
        }
    }
    return seen;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int from, to;
        cin >> from >> to;
        out_roads[from].push_back(to);
    }
    vector<bool> go = reachable_from(n, 1);
    int go_count = 0, back_count = 0, both = 0;
    for (int v = 2; v <= n; v++) {
        bool back = reachable_from(n, v)[1];
        go_count += go[v];
        back_count += back;
        both += go[v] && back;
    }
    cout << go_count << ' ' << back_count << ' ' << both << '\n';
    return 0;
}
