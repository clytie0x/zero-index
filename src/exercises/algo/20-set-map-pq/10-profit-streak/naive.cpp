#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long target;
    cin >> n >> target;
    vector<long long> profit(n);
    for (int i = 0; i < n; i++) {
        cin >> profit[i];
    }
    int best = 0;
    for (int l = 0; l < n; l++) {
        long long sum = 0;
        for (int r = l; r < n; r++) {
            sum += profit[r];
            if (sum == target) {
                best = max(best, r - l + 1);
            }
        }
    }
    cout << best << '\n';
    return 0;
}
