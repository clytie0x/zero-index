#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<long long> minutes(n);
    for (int i = 0; i < n; i++) {
        cin >> minutes[i];
    }
    vector<bool> done(n, false);
    vector<long long> free_at(k, 0);
    long long total = 0;
    for (int round = 0; round < n; round++) {
        int next = -1;
        for (int i = 0; i < n; i++) {
            if (!done[i] && (next == -1 || minutes[i] < minutes[next])) {
                next = i;
            }
        }
        int camera = 0;
        for (int c = 1; c < k; c++) {
            if (free_at[c] < free_at[camera]) {
                camera = c;
            }
        }
        done[next] = true;
        total += free_at[camera];
        free_at[camera] += minutes[next];
    }
    cout << total << '\n';
    return 0;
}
