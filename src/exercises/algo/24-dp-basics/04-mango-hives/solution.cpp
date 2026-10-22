#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> fruits(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> fruits[i];
    }
    vector<long long> best(n + 1);
    best[0] = 0;
    best[1] = fruits[1];
    for (int i = 2; i <= n; i++) {
        best[i] = max(best[i - 1], best[i - 2] + fruits[i]);
    }
    cout << best[n] << '\n';
    return 0;
}
