#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> parent(n + 1), height(n + 1);
    for (int v = 1; v <= n; v++) {
        cin >> parent[v];
    }
    for (int v = 1; v <= n; v++) {
        cin >> height[v];
    }
    int peaks = 0;
    for (int v = 1; v <= n; v++) {
        bool highest = true;
        for (int u = parent[v]; u != 0; u = parent[u]) {
            if (height[u] >= height[v]) {
                highest = false;
                break;
            }
        }
        if (highest) {
            peaks++;
        }
    }
    cout << peaks << '\n';
    return 0;
}
