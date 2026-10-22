#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    long long k;
    cin >> n >> q >> k;
    vector<long long> paint(n + 1, 0);
    for (int j = 0; j < q; j++) {
        int l, r, layers;
        cin >> l >> r >> layers;
        for (int board = l; board <= r; board++) {
            paint[board] += layers;
        }
    }
    int thin = 0;
    for (int board = 1; board <= n; board++) {
        if (paint[board] < k) {
            thin++;
        }
    }
    cout << thin << '\n';
    return 0;
}
