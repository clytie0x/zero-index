#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> parent(n + 1);
    for (int v = 1; v <= n; v++) {
        cin >> parent[v];
    }
    vector<int> count_at(n, 0);
    int height = 0;
    for (int v = 1; v <= n; v++) {
        int depth = 0;
        for (int u = v; parent[u] != 0; u = parent[u]) {
            depth++;
        }
        count_at[depth]++;
        height = max(height, depth);
    }
    for (int k = 0; k <= height; k++) {
        if (k > 0) {
            cout << ' ';
        }
        cout << count_at[k];
    }
    cout << '\n';
    return 0;
}
