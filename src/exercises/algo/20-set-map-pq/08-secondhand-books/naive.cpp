#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> price(n);
    vector<bool> sold(n, false);
    for (int i = 0; i < n; i++) {
        cin >> price[i];
    }
    for (int j = 0; j < m; j++) {
        int budget;
        cin >> budget;
        int best = -1;
        for (int i = 0; i < n; i++) {
            if (!sold[i] && price[i] <= budget && (best == -1 || price[i] > price[best])) {
                best = i;
            }
        }
        if (best == -1) {
            cout << -1 << '\n';
        } else {
            sold[best] = true;
            cout << price[best] << '\n';
        }
    }
    return 0;
}
