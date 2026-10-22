#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> enter(n), leave(n);
    for (int i = 0; i < n; i++) {
        cin >> enter[i] >> leave[i];
    }
    int best = 0;
    int best_time = 0;
    for (int i = 0; i < n; i++) {
        int t = enter[i];
        int inside = 0;
        for (int j = 0; j < n; j++) {
            if (enter[j] <= t && t < leave[j]) {
                inside++;
            }
        }
        if (inside > best || (inside == best && t < best_time)) {
            best = inside;
            best_time = t;
        }
    }
    cout << best << ' ' << best_time << '\n';
    return 0;
}
