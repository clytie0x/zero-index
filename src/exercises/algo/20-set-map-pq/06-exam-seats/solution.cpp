#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    set<int> empty_seats;
    for (int seat = 1; seat <= n; seat++) {
        empty_seats.insert(seat);
    }
    for (int i = 0; i < q; i++) {
        char op;
        int x;
        cin >> op >> x;
        if (op == 'L') {
            empty_seats.insert(x);
            continue;
        }
        auto it = empty_seats.lower_bound(x);
        if (it == empty_seats.end()) {
            cout << 0 << '\n';
        } else {
            cout << *it << '\n';
            empty_seats.erase(it);
        }
    }
    return 0;
}
