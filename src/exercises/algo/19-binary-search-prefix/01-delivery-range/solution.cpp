#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<long long> houses(n);
    for (int i = 0; i < n; i++) {
        cin >> houses[i];
    }
    sort(houses.begin(), houses.end());
    for (int k = 0; k < q; k++) {
        long long p, d;
        cin >> p >> d;
        int from = lower_bound(houses.begin(), houses.end(), p - d) - houses.begin();
        int to = upper_bound(houses.begin(), houses.end(), p + d) - houses.begin();
        cout << to - from << '\n';
    }
    return 0;
}
