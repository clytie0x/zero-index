#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<long long> guests_on(n + 1, 0);
    for (int k = 0; k < q; k++) {
        int type, l, r;
        cin >> type >> l >> r;
        if (type == 1) {
            long long guests;
            cin >> guests;
            for (int night = l; night <= r; night++) {
                guests_on[night] += guests;
            }
        } else {
            long long total = 0;
            for (int night = l; night <= r; night++) {
                total += guests_on[night];
            }
            cout << total << '\n';
        }
    }
    return 0;
}
