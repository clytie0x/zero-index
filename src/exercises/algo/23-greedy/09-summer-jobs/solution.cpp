#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long per_day;
    cin >> n >> per_day;
    vector<pair<long long, long long>> jobs(n);
    for (int i = 0; i < n; i++) {
        cin >> jobs[i].first >> jobs[i].second;
    }
    sort(jobs.begin(), jobs.end());
    priority_queue<long long, vector<long long>, greater<long long>> kept;
    long long total = 0;
    for (int i = 0; i < n; i++) {
        kept.push(jobs[i].second);
        total += jobs[i].second;
        if ((long long)kept.size() > per_day * jobs[i].first) {
            total -= kept.top();
            kept.pop();
        }
    }
    cout << total << '\n';
    return 0;
}
