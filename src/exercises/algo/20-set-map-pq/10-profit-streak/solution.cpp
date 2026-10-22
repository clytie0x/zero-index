#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long target;
    cin >> n >> target;
    map<long long, int> first_day;
    first_day[0] = 0;
    long long prefix = 0;
    int best = 0;
    for (int i = 1; i <= n; i++) {
        long long profit;
        cin >> profit;
        prefix += profit;
        auto it = first_day.find(prefix - target);
        if (it != first_day.end()) {
            best = max(best, i - it->second);
        }
        if (first_day.count(prefix) == 0) {
            first_day[prefix] = i;
        }
    }
    cout << best << '\n';
    return 0;
}
