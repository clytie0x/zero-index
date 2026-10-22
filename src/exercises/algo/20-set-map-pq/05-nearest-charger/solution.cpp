#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    set<int> stations;
    for (int i = 0; i < q; i++) {
        char op;
        int x;
        cin >> op >> x;
        if (op == '+') {
            stations.insert(x);
        } else if (op == '-') {
            stations.erase(x);
        } else if (stations.empty()) {
            cout << -1 << '\n';
        } else {
            int best = INT_MAX;
            auto it = stations.lower_bound(x);
            if (it != stations.end()) {
                best = min(best, *it - x);
            }
            if (it != stations.begin()) {
                best = min(best, x - *prev(it));
            }
            cout << best << '\n';
        }
    }
    return 0;
}
