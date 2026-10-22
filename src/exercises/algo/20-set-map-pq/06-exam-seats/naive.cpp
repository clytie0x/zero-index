#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<bool> taken(n + 1, false);
    for (int i = 0; i < q; i++) {
        char op;
        int x;
        cin >> op >> x;
        if (op == 'L') {
            taken[x] = false;
            continue;
        }
        int seat = x;
        while (seat <= n && taken[seat]) {
            seat++;
        }
        if (seat > n) {
            cout << 0 << '\n';
        } else {
            taken[seat] = true;
            cout << seat << '\n';
        }
    }
    return 0;
}
