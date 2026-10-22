#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<long long, long long>> jobs(n);
    for (int i = 0; i < n; i++) {
        long long deadline, pay;
        cin >> deadline >> pay;
        jobs[i] = {pay, min(deadline, (long long)n)};
    }
    sort(jobs.rbegin(), jobs.rend());
    vector<bool> busy(n + 1, false);
    long long total = 0;
    for (int i = 0; i < n; i++) {
        for (int day = jobs[i].second; day >= 1; day--) {
            if (!busy[day]) {
                busy[day] = true;
                total += jobs[i].first;
                break;
            }
        }
    }
    cout << total << '\n';
    return 0;
}
