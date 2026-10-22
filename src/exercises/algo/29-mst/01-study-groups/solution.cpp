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

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    parent.resize(n + 1);
    group_size.assign(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    long long pairs = 0;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        int root_a = find_root(a);
        int root_b = find_root(b);
        if (root_a != root_b) {
            pairs += (long long)group_size[root_a] * group_size[root_b];
            if (group_size[root_a] < group_size[root_b]) {
                swap(root_a, root_b);
            }
            parent[root_b] = root_a;
            group_size[root_a] += group_size[root_b];
        }
        cout << pairs << '\n';
    }
    return 0;
}
