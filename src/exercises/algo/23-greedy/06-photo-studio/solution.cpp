#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<long long> minutes(n);
    for (int i = 0; i < n; i++) {
        cin >> minutes[i];
    }
    sort(minutes.begin(), minutes.end(), greater<long long>());
    long long total = 0;
    for (int j = 0; j < n; j++) {
        total += minutes[j] * (j / k);
    }
    cout << total << '\n';
    return 0;
}
