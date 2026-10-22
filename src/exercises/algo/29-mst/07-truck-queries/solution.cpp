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

void unite(int a, int b)
{
    int root_a = find_root(a);
    int root_b = find_root(b);
    if (root_a == root_b) {
        return;
    }
    if (group_size[root_a] < group_size[root_b]) {
        swap(root_a, root_b);
    }
    parent[root_b] = root_a;
    group_size[root_a] += group_size[root_b];
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, q;
    cin >> n >> m >> q;
    vector<tuple<int, int, int>> roads(m);
    for (int i = 0; i < m; i++) {
        int a, b, limit;
        cin >> a >> b >> limit;
        roads[i] = make_tuple(limit, a, b);
    }
    sort(roads.begin(), roads.end(), greater<tuple<int, int, int>>());
    vector<int> from(q), to(q), weight(q), order(q);
    for (int j = 0; j < q; j++) {
        cin >> from[j] >> to[j] >> weight[j];
        order[j] = j;
    }
    sort(order.begin(), order.end(), [&](int x, int y) {
        return weight[x] > weight[y];
    });
    parent.resize(n + 1);
    group_size.assign(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    vector<bool> answer(q);
    int next_road = 0;
    for (int j : order) {
        while (next_road < m && get<0>(roads[next_road]) >= weight[j]) {
            unite(get<1>(roads[next_road]), get<2>(roads[next_road]));
            next_road++;
        }
        answer[j] = find_root(from[j]) == find_root(to[j]);
    }
    for (int j = 0; j < q; j++) {
        cout << (answer[j] ? "YES" : "NO") << '\n';
    }
    return 0;
}
