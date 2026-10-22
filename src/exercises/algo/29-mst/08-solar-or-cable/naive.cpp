#include <bits/stdc++.h>
using namespace std;

vector<int> parent;

int find_root(int x)
{
    int root = x;
    while (parent[root] != root) {
        root = parent[root];
    }
    while (parent[x] != root) {
        int next = parent[x];
        parent[x] = root;
        x = next;
    }
    return root;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long per_meter;
    cin >> n >> per_meter;
    vector<long long> x(n + 1), y(n + 1);
    vector<tuple<long long, int, int>> edges;
    for (int i = 1; i <= n; i++) {
        long long solar;
        cin >> x[i] >> y[i] >> solar;
        edges.push_back({solar, 0, i});
    }
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            long long cable = per_meter * (abs(x[i] - x[j]) + abs(y[i] - y[j]));
            edges.push_back({cable, i, j});
        }
    }
    sort(edges.begin(), edges.end());
    parent.resize(n + 1);
    for (int i = 0; i <= n; i++) {
        parent[i] = i;
    }
    long long total = 0;
    for (auto [cost, a, b] : edges) {
        int root_a = find_root(a);
        int root_b = find_root(b);
        if (root_a != root_b) {
            parent[root_a] = root_b;
            total += cost;
        }
    }
    cout << total << '\n';
    return 0;
}
