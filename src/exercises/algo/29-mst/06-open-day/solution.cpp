#include <bits/stdc++.h>
using namespace std;

vector<int> parent, group_size;

int find_root(int x)
{
    if (parent[x] == x) {
        return x;
    }
    parent[x] = find_root(parent[x]);
    return parent[x];
}

bool unite(int a, int b)
{
    int root_a = find_root(a);
    int root_b = find_root(b);
    if (root_a == root_b) {
        return false;
    }
    if (group_size[root_a] < group_size[root_b]) {
        swap(root_a, root_b);
    }
    parent[root_b] = root_a;
    group_size[root_a] += group_size[root_b];
    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<tuple<int, int, int>> roads(m);
    for (int i = 0; i < m; i++) {
        int a, b, day;
        cin >> a >> b >> day;
        roads[i] = {day, a, b};
    }
    sort(roads.begin(), roads.end());
    parent.resize(n + 1);
    group_size.assign(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    vector<vector<pair<int, int>>> tree(n + 1);
    for (auto [day, a, b] : roads) {
        if (unite(a, b)) {
            tree[a].push_back({b, day});
            tree[b].push_back({a, day});
        }
    }
    vector<int> first_day(n + 1, -1);
    first_day[1] = 0;
    queue<int> q;
    q.push(1);
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (auto [to, day] : tree[v]) {
            if (first_day[to] == -1) {
                first_day[to] = max(first_day[v], day);
                q.push(to);
            }
        }
    }
    for (int i = 2; i <= n; i++) {
        cout << first_day[i] << (i == n ? '\n' : ' ');
    }
    return 0;
}
