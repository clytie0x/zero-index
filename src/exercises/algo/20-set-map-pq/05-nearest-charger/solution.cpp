#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    multiset<int> chargers;
    for (int i = 0; i < q; i++) {
        char op;
        int x;
        cin >> op >> x;
        if (op == '+') {
            chargers.insert(x);
        } else if (op == '-') {
            chargers.erase(chargers.find(x));
        } else if (chargers.empty()) {
            cout << -1 << '\n';
        } else {
            int best = INT_MAX;
            auto it = chargers.lower_bound(x);
            if (it != chargers.end()) {
                best = min(best, *it - x);
            }
            if (it != chargers.begin()) {
                best = min(best, x - *prev(it));
            }
            cout << best << '\n';
        }
    }
    return 0;
}
