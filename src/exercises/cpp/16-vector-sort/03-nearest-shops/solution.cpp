#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> shops(n);
    for (int i = 0; i < n; i++) {
        cin >> shops[i].first;
        shops[i].second = i + 1;
    }
    sort(shops.begin(), shops.end());
    for (int i = 0; i < k; i++) {
        if (i > 0) {
            cout << ' ';
        }
        cout << shops[i].second;
    }
    cout << '\n';
    return 0;
}
