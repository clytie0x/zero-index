#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    long long k;
    cin >> n >> q >> k;
    vector<long long> diff(n + 2, 0);
    for (int j = 0; j < q; j++) {
        int l, r, layers;
        cin >> l >> r >> layers;
        diff[l] += layers;
        diff[r + 1] -= layers;
    }
    long long current = 0;
    int thin = 0;
    for (int board = 1; board <= n; board++) {
        current += diff[board];
        if (current < k) {
            thin++;
        }
    }
    cout << thin << '\n';
    return 0;
}
