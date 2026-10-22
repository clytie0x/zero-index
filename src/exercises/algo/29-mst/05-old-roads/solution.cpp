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
    int n, k, m;
    cin >> n >> k >> m;
    parent.resize(n + 1);
    group_size.assign(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    int groups = n;
    for (int i = 0; i < k; i++) {
        int a, b;
        cin >> a >> b;
        if (unite(a, b)) {
            groups--;
        }
    }
    vector<tuple<int, int, int>> roads(m);
    for (int i = 0; i < m; i++) {
        int a, b, cost;
        cin >> a >> b >> cost;
        roads[i] = make_tuple(cost, a, b);
    }
    sort(roads.begin(), roads.end());
    long long total = 0;
    int built = 0;
    for (auto [cost, a, b] : roads) {
        if (unite(a, b)) {
            groups--;
            total += cost;
            built++;
        }
    }
    if (groups == 1) {
        cout << total << '\n';
        cout << built << '\n';
    } else {
        cout << -1 << '\n';
    }
    return 0;
}
