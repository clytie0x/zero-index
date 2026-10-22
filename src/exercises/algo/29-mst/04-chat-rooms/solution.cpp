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
    int n, q;
    cin >> n >> q;
    parent.resize(n + 1);
    group_size.assign(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    for (int k = 0; k < q; k++) {
        int type, a;
        cin >> type >> a;
        if (type == 1) {
            int b;
            cin >> b;
            unite(a, b);
        } else if (type == 2) {
            int b;
            cin >> b;
            cout << (find_root(a) == find_root(b) ? "YES" : "NO") << '\n';
        } else {
            cout << group_size[find_root(a)] << '\n';
        }
    }
    return 0;
}
