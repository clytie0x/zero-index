#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<vector<int>> dist(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> dist[i][j];
        }
    }
    vector<int> order;
    for (int i = 1; i < n; i++) {
        order.push_back(i);
    }
    long long answer = LLONG_MAX;
    do {
        long long total = 0;
        int at = 0;
        for (int k = 0; k < (int)order.size(); k++) {
            total += dist[at][order[k]];
            at = order[k];
        }
        answer = min(answer, total);
    } while (next_permutation(order.begin(), order.end()));
    cout << answer << '\n';
    return 0;
}
