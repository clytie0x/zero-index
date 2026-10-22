#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<long long> sales(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> sales[i];
    }
    for (int k = 0; k < q; k++) {
        int type;
        cin >> type;
        if (type == 1) {
            int i;
            long long v;
            cin >> i >> v;
            sales[i] = v;
        } else {
            int l, r;
            cin >> l >> r;
            long long total = 0;
            for (int i = l; i <= r; i++) {
                total += sales[i];
            }
            cout << total << '\n';
        }
    }
    return 0;
}
