#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    vector<int> chargers;
    for (int i = 0; i < q; i++) {
        char op;
        int x;
        cin >> op >> x;
        if (op == '+') {
            chargers.push_back(x);
        } else if (op == '-') {
            for (int j = 0; j < (int)chargers.size(); j++) {
                if (chargers[j] == x) {
                    chargers[j] = chargers.back();
                    chargers.pop_back();
                    break;
                }
            }
        } else if (chargers.empty()) {
            cout << -1 << '\n';
        } else {
            int best = INT_MAX;
            for (int s : chargers) {
                best = min(best, abs(s - x));
            }
            cout << best << '\n';
        }
    }
    return 0;
}
