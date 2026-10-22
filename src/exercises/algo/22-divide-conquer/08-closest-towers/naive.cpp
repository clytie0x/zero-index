#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> x(n), y(n);
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i];
    }
    long long best = LLONG_MAX;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            long long dx = x[i] - x[j];
            long long dy = y[i] - y[j];
            best = min(best, dx * dx + dy * dy);
        }
    }
    cout << best << '\n';
    return 0;
}
