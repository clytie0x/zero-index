#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000000;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, target;
    cin >> n >> target;
    vector<int> prices(n);
    for (int i = 0; i < n; i++) {
        cin >> prices[i];
    }
    sort(prices.rbegin(), prices.rend());
    vector<int> fewest(target + 1, INF);
    fewest[0] = 0;
    for (int x = 1; x <= target; x++) {
        for (int p : prices) {
            if (p <= x) {
                fewest[x] = min(fewest[x], fewest[x - p] + 1);
            }
        }
    }
    if (fewest[target] == INF) {
        cout << -1 << '\n';
        return 0;
    }
    cout << fewest[target] << '\n';
    int x = target;
    bool first = true;
    while (x > 0) {
        for (int p : prices) {
            if (p <= x && fewest[x - p] == fewest[x] - 1) {
                cout << (first ? "" : " ") << p;
                first = false;
                x -= p;
                break;
            }
        }
    }
    cout << '\n';
    return 0;
}
