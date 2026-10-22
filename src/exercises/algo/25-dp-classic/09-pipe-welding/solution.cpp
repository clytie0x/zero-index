#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> prefix(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        long long length;
        cin >> length;
        prefix[i] = prefix[i - 1] + length;
    }
    vector<vector<long long>> cost(n + 2, vector<long long>(n + 2, 0));
    for (int span = 2; span <= n; span++) {
        for (int i = 1; i + span - 1 <= n; i++) {
            int j = i + span - 1;
            long long best = LLONG_MAX;
            for (int k = i; k < j; k++) {
                best = min(best, cost[i][k] + cost[k + 1][j]);
            }
            cost[i][j] = best + prefix[j] - prefix[i - 1];
        }
    }
    cout << cost[1][n] << '\n';
    return 0;
}
