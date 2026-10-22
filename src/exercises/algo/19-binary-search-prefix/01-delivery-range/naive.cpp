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
    for (int k = 0; k < q; k++) {
        long long p, d;
        cin >> p >> d;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (houses[i] >= p - d && houses[i] <= p + d) {
                count++;
            }
        }
        cout << count << '\n';
    }
    return 0;
}
