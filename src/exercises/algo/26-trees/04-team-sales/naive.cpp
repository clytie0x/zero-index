#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> boss(n + 1);
    for (int v = 1; v <= n; v++) {
        cin >> boss[v];
    }
    vector<long long> total(n + 1, 0);
    for (int v = 1; v <= n; v++) {
        long long sales;
        cin >> sales;
        for (int u = v; u != 0; u = boss[u]) {
            total[u] += sales;
        }
    }
    for (int v = 1; v <= n; v++) {
        if (v > 1) {
            cout << ' ';
        }
        cout << total[v];
    }
    cout << '\n';
    return 0;
}
