#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<vector<int>> cost(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> cost[i][j];
        }
    }
    vector<int> duty(n);
    for (int i = 0; i < n; i++) {
        duty[i] = i;
    }
    long long best = LLONG_MAX;
    do {
        long long total = 0;
        for (int i = 0; i < n; i++) {
            total += cost[i][duty[i]];
        }
        best = min(best, total);
    } while (next_permutation(duty.begin(), duty.end()));
    cout << best << '\n';
    return 0;
}
