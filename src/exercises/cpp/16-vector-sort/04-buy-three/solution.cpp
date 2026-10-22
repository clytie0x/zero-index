#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> price(n);
    for (int &p : price) {
        cin >> p;
    }
    sort(price.begin(), price.end(), greater<int>());
    long long total = 0;
    for (int i = 0; i < n; i++) {
        if (i % 3 != 2) {
            total += price[i];
        }
    }
    cout << total << '\n';
    return 0;
}
