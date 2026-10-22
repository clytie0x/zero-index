#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    vector<int> stations;
    for (int i = 0; i < q; i++) {
        char op;
        int x;
        cin >> op >> x;
        if (op == '+') {
            stations.push_back(x);
        } else if (op == '-') {
            for (int j = 0; j < (int)stations.size(); j++) {
                if (stations[j] == x) {
                    stations[j] = stations.back();
                    stations.pop_back();
                    break;
                }
            }
        } else if (stations.empty()) {
            cout << -1 << '\n';
        } else {
            int best = INT_MAX;
            for (int s : stations) {
                best = min(best, abs(s - x));
            }
            cout << best << '\n';
        }
    }
    return 0;
}
