#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<long long, long long>> tasks(n);
    for (int i = 0; i < n; i++) {
        long long days, due;
        cin >> days >> due;
        tasks[i] = {due, days};
    }
    sort(tasks.begin(), tasks.end());
    long long today = 0, worst = 0;
    for (int i = 0; i < n; i++) {
        today += tasks[i].second;
        worst = max(worst, today - tasks[i].first);
    }
    cout << worst << '\n';
    return 0;
}
