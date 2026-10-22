#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> profit(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> profit[i];
    }
    long long best = LLONG_MIN;
    int best_start = 0, best_end = 0;
    for (int l = 1; l <= n; l++) {
        long long sum = 0;
        for (int r = l; r <= n; r++) {
            sum += profit[r];
            if (sum > best) {
                best = sum;
                best_start = l;
                best_end = r;
            }
        }
    }
    cout << best << '\n';
    cout << best_start << ' ' << best_end << '\n';
    return 0;
}
