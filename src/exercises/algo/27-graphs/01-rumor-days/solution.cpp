#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001;
vector<int> adj[MAXN];
int heard_on[MAXN];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, s;
    cin >> n >> m >> s;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    fill(heard_on, heard_on + n + 1, -1);
    queue<int> waiting;
    heard_on[s] = 0;
    waiting.push(s);
    int heard = 0, last_day = 0;
    while (!waiting.empty()) {
        int v = waiting.front();
        waiting.pop();
        heard++;
        last_day = heard_on[v];
        for (int next : adj[v]) {
            if (heard_on[next] == -1) {
                heard_on[next] = heard_on[v] + 1;
                waiting.push(next);
            }
        }
    }
    cout << heard << ' ' << last_day << '\n';
    return 0;
}
