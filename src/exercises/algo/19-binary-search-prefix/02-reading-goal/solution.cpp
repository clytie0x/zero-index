#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<long long> prefix(n + 1, 0);
    for (int day = 1; day <= n; day++) {
        int pages;
        cin >> pages;
        prefix[day] = prefix[day - 1] + pages;
    }
    for (int k = 0; k < q; k++) {
        int start;
        long long target;
        cin >> start >> target;
        long long need = prefix[start - 1] + target;
        int day = lower_bound(prefix.begin() + start, prefix.end(), need) - prefix.begin();
        if (day > n) {
            cout << -1 << '\n';
        } else {
            cout << day << '\n';
        }
    }
    return 0;
}
