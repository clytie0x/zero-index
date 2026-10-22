#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long per_meter;
    cin >> n >> per_meter;
    vector<long long> x(n), y(n), best(n);
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i] >> best[i];
    }
    vector<bool> in_tree(n, false);
    long long total = 0;
    for (int step = 0; step < n; step++) {
        int v = -1;
        for (int i = 0; i < n; i++) {
            if (!in_tree[i] && (v == -1 || best[i] < best[v])) {
                v = i;
            }
        }
        in_tree[v] = true;
        total += best[v];
        for (int i = 0; i < n; i++) {
            if (!in_tree[i]) {
                long long cable = per_meter * (abs(x[v] - x[i]) + abs(y[v] - y[i]));
                best[i] = min(best[i], cable);
            }
        }
    }
    cout << total << '\n';
    return 0;
}
