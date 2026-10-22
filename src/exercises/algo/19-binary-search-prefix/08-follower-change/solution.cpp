#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long k;
    cin >> n >> k;
    vector<long long> prefix(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        long long change;
        cin >> change;
        prefix[i] = prefix[i - 1] + change;
    }
    vector<pair<long long, int>> sorted_prefix(n + 1);
    for (int j = 0; j <= n; j++) {
        sorted_prefix[j] = make_pair(prefix[j], j);
    }
    sort(sorted_prefix.begin(), sorted_prefix.end());
    long long count = 0;
    for (int r = 1; r <= n; r++) {
        long long want = prefix[r] - k;
        auto from = lower_bound(sorted_prefix.begin(), sorted_prefix.end(), make_pair(want, 0));
        auto to = lower_bound(sorted_prefix.begin(), sorted_prefix.end(), make_pair(want, r));
        count += to - from;
    }
    cout << count << '\n';
    return 0;
}
