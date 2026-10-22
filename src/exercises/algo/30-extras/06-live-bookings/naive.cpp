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
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            long long guests;
            cin >> l >> r >> guests;
            for (int night = l; night <= r; night++) {
                guests_on[night] += guests;
            }
        } else {
            int night;
            cin >> night;
            cout << guests_on[night] << '\n';
        }
    }
    return 0;
}
