#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    vector<long long> days(n), due(n);
    for (int i = 0; i < n; i++) {
        cin >> days[i] >> due[i];
    }
    vector<long long> exams(k);
    for (int i = 0; i < k; i++) {
        cin >> exams[i];
    }
    sort(exams.begin(), exams.end());
    vector<int> order(n);
    for (int i = 0; i < n; i++) {
        order[i] = i;
    }
    long long best = LLONG_MAX;
    do {
        long long worked = 0, worst = 0;
        for (int i = 0; i < n; i++) {
            worked += days[order[i]];
            long long low = worked, high = worked + k;
            while (low < high) {
                long long mid = (low + high) / 2;
                long long exam_days = upper_bound(exams.begin(), exams.end(), mid) - exams.begin();
                if (mid - exam_days >= worked) {
                    high = mid;
                } else {
                    low = mid + 1;
                }
            }
            worst = max(worst, low - due[order[i]]);
        }
        best = min(best, worst);
    } while (next_permutation(order.begin(), order.end()));
    cout << best << '\n';
    return 0;
}
