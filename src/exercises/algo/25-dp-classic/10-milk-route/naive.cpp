#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    vector<vector<int>> dist(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> dist[i][j];
        }
    }
    vector<bool> urgent(n, false);
    for (int i = 0; i < k; i++) {
        int shop;
        cin >> shop;
        urgent[shop] = true;
    }
    vector<int> order;
    for (int i = 1; i < n; i++) {
        order.push_back(i);
    }
    long long answer = LLONG_MAX;
    do {
        bool ok = true;
        for (int i = 0; i < (int)order.size(); i++) {
            if (i < k && !urgent[order[i]]) {
                ok = false;
            }
        }
        if (!ok) {
            continue;
        }
        long long total = 0;
        int at = 0;
        for (int i = 0; i < (int)order.size(); i++) {
            total += dist[at][order[i]];
            at = order[i];
        }
        total += dist[at][0];
        answer = min(answer, total);
    } while (next_permutation(order.begin(), order.end()));
    cout << answer << '\n';
    return 0;
}
