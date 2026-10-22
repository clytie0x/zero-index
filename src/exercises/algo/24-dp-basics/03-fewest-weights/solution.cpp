#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000000;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, target;
    cin >> n >> target;
    vector<int> weights(n);
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
    }
    vector<int> fewest(target + 1, INF);
    fewest[0] = 0;
    for (int x = 1; x <= target; x++) {
        for (int w : weights) {
            if (w <= x) {
                fewest[x] = min(fewest[x], fewest[x - w] + 1);
            }
        }
    }
    if (fewest[target] == INF) {
        cout << -1 << '\n';
    } else {
        cout << fewest[target] << '\n';
    }
    return 0;
}
