#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> parent(n + 1), child_count(n + 1, 0);
    for (int v = 1; v <= n; v++) {
        cin >> parent[v];
        if (parent[v] != 0) {
            child_count[parent[v]]++;
        }
    }
    int leaves = 0, height = 0;
    for (int v = 1; v <= n; v++) {
        if (child_count[v] == 0) {
            leaves++;
        }
        int depth = 0;
        for (int u = v; parent[u] != 0; u = parent[u]) {
            depth++;
        }
        height = max(height, depth);
    }
    cout << leaves << '\n' << height << '\n';
    return 0;
}
