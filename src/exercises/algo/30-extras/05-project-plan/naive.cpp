#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<long long> days(n + 1), finish(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> days[i];
        finish[i] = days[i];
    }
    vector<int> from(m), to(m);
    for (int i = 0; i < m; i++) {
        cin >> from[i] >> to[i];
    }
    bool changed = true;
    while (changed) {
        changed = false;
        for (int i = 0; i < m; i++) {
            if (finish[from[i]] + days[to[i]] > finish[to[i]]) {
                finish[to[i]] = finish[from[i]] + days[to[i]];
                changed = true;
            }
        }
    }
    long long answer = 0;
    for (int i = 1; i <= n; i++) {
        answer = max(answer, finish[i]);
    }
    cout << answer << '\n';
    return 0;
}
