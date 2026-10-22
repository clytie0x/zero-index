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
    vector<tuple<int, int, int>> pipes(m);
    for (int i = 0; i < m; i++) {
        int a, b, cost;
        cin >> a >> b >> cost;
        pipes[i] = make_tuple(cost, a, b);
    }
    sort(pipes.begin(), pipes.end());
    parent.resize(n + 1);
    group_size.assign(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    long long total = 0;
    int used = 0;
    for (auto [cost, a, b] : pipes) {
        if (unite(a, b)) {
            total += cost;
            used++;
        }
    }
    if (used == n - 1) {
        cout << total << '\n';
    } else {
        cout << -1 << '\n';
    }
    return 0;
}
