#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> profit(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> profit[i];
    }
    vector<long long> ending(n + 1);
    vector<int> start(n + 1);
    ending[1] = profit[1];
    start[1] = 1;
    int best_start = 1, best_end = 1;
    for (int i = 2; i <= n; i++) {
        if (ending[i - 1] >= 0) {
            ending[i] = ending[i - 1] + profit[i];
            start[i] = start[i - 1];
        } else {
            ending[i] = profit[i];
            start[i] = i;
        }
        long long best = ending[best_end];
        if (ending[i] > best || (ending[i] == best && start[i] < best_start)) {
            best_start = start[i];
            best_end = i;
        }
    }
    cout << ending[best_end] << '\n';
    cout << best_start << ' ' << best_end << '\n';
    return 0;
}
