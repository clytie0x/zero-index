#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<int> price(n);
    for (int i = 0; i < n; i++) {
        cin >> price[i];
    }
    vector<bool> bought(n, false);
    long long total = 0;
    for (int round = 0; round < k; round++) {
        int cheapest = -1;
        for (int i = 0; i < n; i++) {
            if (!bought[i] && (cheapest == -1 || price[i] < price[cheapest])) {
                cheapest = i;
            }
        }
        bought[cheapest] = true;
        total += price[cheapest];
    }
    cout << total << '\n';
    return 0;
}
