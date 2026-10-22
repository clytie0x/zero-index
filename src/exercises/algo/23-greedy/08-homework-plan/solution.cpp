#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<pair<long long, long long>> tasks(n);
    for (int i = 0; i < n; i++) {
        long long days, due;
        cin >> days >> due;
        tasks[i] = {due, days};
    }
    vector<long long> exams(k);
    for (int i = 0; i < k; i++) {
        cin >> exams[i];
    }
    sort(tasks.begin(), tasks.end());
    sort(exams.begin(), exams.end());
    long long worked = 0, worst = 0;
    int passed = 0;
    for (int i = 0; i < n; i++) {
        worked += tasks[i].second;
        while (passed < k && exams[passed] <= worked + passed) {
            passed++;
        }
        long long finish = worked + passed;
        worst = max(worst, finish - tasks[i].first);
    }
    cout << worst << '\n';
    return 0;
}
