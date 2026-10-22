#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<int>> cost;
vector<vector<int>> cheapest_first;
vector<bool> taken;
long long best = LLONG_MAX;

long long optimistic_rest(int teacher)
{
    long long sum = 0;
    for (int t = teacher; t < n; t++) {
        for (int duty : cheapest_first[t]) {
            if (!taken[duty]) {
                sum += cost[t][duty];
                break;
            }
        }
    }
    return sum;
}

void go(int teacher, long long total)
{
    if (teacher == n) {
        best = min(best, total);
        return;
    }
    if (total + optimistic_rest(teacher) >= best) {
        return;
    }
    for (int duty : cheapest_first[teacher]) {
        if (!taken[duty]) {
            taken[duty] = true;
            go(teacher + 1, total + cost[teacher][duty]);
            taken[duty] = false;
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    cost.assign(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> cost[i][j];
        }
    }
    cheapest_first.assign(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cheapest_first[i][j] = j;
        }
        sort(cheapest_first[i].begin(), cheapest_first[i].end(), [&](int a, int b) {
            return cost[i][a] < cost[i][b];
        });
    }
    taken.assign(n, false);
    go(0, 0);
    cout << best << '\n';
    return 0;
}
