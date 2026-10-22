#include <bits/stdc++.h>
using namespace std;

vector<int> parent;

int find_root(int x)
{
    while (parent[x] != x) {
        x = parent[x];
    }
    return x;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    parent.resize(n + 1);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        int root_a = find_root(a);
        int root_b = find_root(b);
        if (root_a != root_b) {
            parent[root_a] = root_b;
        }
    }
    vector<int> count(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        count[find_root(i)]++;
    }
    int groups = 0, largest = 0;
    for (int i = 1; i <= n; i++) {
        if (count[i] > 0) {
            groups++;
            largest = max(largest, count[i]);
        }
    }
    cout << groups << '\n';
    cout << largest << '\n';
    return 0;
}
