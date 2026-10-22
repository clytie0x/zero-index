#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    for (int c = 0; c < t; c++) {
        long long a, n, m;
        cin >> a >> n >> m;
        long long total = 0, coin = 1 % m;
        for (long long day = 0; day < n; day++) {
            total = (total + coin) % m;
            coin = coin * (a % m) % m;
        }
        cout << total << '\n';
    }
    return 0;
}
