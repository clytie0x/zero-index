#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> next_steps(n + 1);
    vector<int> waiting(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        next_steps[a].push_back(b);
        waiting[b]++;
    }
    vector<bool> done(n + 1, false);
    vector<int> order;
    for (int round = 0; round < n; round++) {
        int chosen = -1;
        for (int step = 1; step <= n; step++) {
            if (!done[step] && waiting[step] == 0) {
                chosen = step;
                break;
            }
        }
        if (chosen == -1) {
            cout << -1 << '\n';
            return 0;
        }
        done[chosen] = true;
        order.push_back(chosen);
        for (int after : next_steps[chosen]) {
            waiting[after]--;
        }
    }
    for (int i = 0; i < n; i++) {
        cout << order[i] << (i + 1 == n ? '\n' : ' ');
    }
    return 0;
}
