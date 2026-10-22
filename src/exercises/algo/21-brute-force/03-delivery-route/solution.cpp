#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<vector<int>> dist(n + 1, vector<int>(n + 1));
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) {
            cin >> dist[i][j];
        }
    }
    vector<int> order(n);
    for (int i = 0; i < n; i++) {
        order[i] = i + 1;
    }
    int best = INT_MAX;
    do {
        int total = dist[0][order[0]];
        for (int i = 0; i + 1 < n; i++) {
            total += dist[order[i]][order[i + 1]];
        }
        best = min(best, total);
    } while (next_permutation(order.begin(), order.end()));
    cout << best << '\n';
    return 0;
}
