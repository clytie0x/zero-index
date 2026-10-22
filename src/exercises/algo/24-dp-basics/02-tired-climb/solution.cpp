#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> cost(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> cost[i];
    }
    vector<long long> tired(n + 1);
    tired[0] = 0;
    tired[1] = cost[1];
    for (int i = 2; i <= n; i++) {
        tired[i] = cost[i] + min(tired[i - 1], tired[i - 2]);
    }
    cout << tired[n] << '\n';
    return 0;
}
