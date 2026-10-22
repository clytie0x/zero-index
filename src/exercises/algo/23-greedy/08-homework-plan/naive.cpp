#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<long long> days(n), due(n);
    for (int i = 0; i < n; i++) {
        cin >> days[i] >> due[i];
    }
    vector<int> order(n);
    for (int i = 0; i < n; i++) {
        order[i] = i;
    }
    long long best = LLONG_MAX;
    do {
        long long today = 0, worst = 0;
        for (int i = 0; i < n; i++) {
            today += days[order[i]];
            worst = max(worst, today - due[order[i]]);
        }
        best = min(best, worst);
    } while (next_permutation(order.begin(), order.end()));
    cout << best << '\n';
    return 0;
}
