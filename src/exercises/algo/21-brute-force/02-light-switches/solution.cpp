#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> effect(n, 0);
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        for (int t = 0; t < k; t++) {
            int lamp;
            cin >> lamp;
            effect[i] |= 1 << (lamp - 1);
        }
    }
    int all_on = (1 << m) - 1;
    int best = -1;
    for (int mask = 0; mask < (1 << n); mask++) {
        int lamps = 0;
        for (int i = 0; i < n; i++) {
            if ((mask >> i) & 1) {
                lamps ^= effect[i];
            }
        }
        if (lamps == all_on) {
            int presses = __builtin_popcount(mask);
            if (best == -1 || presses < best) {
                best = presses;
            }
        }
    }
    cout << best << '\n';
    return 0;
}
