#include <bits/stdc++.h>
using namespace std;

long long best_total = LLONG_MAX;

void weld(vector<long long> &pipes, long long total)
{
    if (pipes.size() == 1) {
        best_total = min(best_total, total);
        return;
    }
    for (int k = 0; k + 1 < (int)pipes.size(); k++) {
        vector<long long> next;
        for (int i = 0; i < k; i++) {
            next.push_back(pipes[i]);
        }
        next.push_back(pipes[k] + pipes[k + 1]);
        for (int i = k + 2; i < (int)pipes.size(); i++) {
            next.push_back(pipes[i]);
        }
        weld(next, total + pipes[k] + pipes[k + 1]);
    }
}

int main()
{
    int n;
    cin >> n;
    vector<long long> pipes(n);
    for (int i = 0; i < n; i++) {
        cin >> pipes[i];
    }
    weld(pipes, 0);
    cout << best_total << '\n';
    return 0;
}
