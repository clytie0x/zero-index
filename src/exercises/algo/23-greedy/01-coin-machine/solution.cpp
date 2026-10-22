#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k, q;
    cin >> k >> q;
    vector<long long> coins(k);
    for (int i = 0; i < k; i++) {
        cin >> coins[i];
    }
    sort(coins.rbegin(), coins.rend());
    for (int j = 0; j < q; j++) {
        long long amount;
        cin >> amount;
        long long total = 0;
        for (int i = 0; i < k; i++) {
            total += amount / coins[i];
            amount %= coins[i];
        }
        cout << total << '\n';
    }
    return 0;
}
