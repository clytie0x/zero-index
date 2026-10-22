#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<int, int>> events;
    events.reserve(2 * n);
    for (int i = 0; i < n; i++) {
        int enter, leave;
        cin >> enter >> leave;
        events.push_back({enter, 1});
        events.push_back({leave, -1});
    }
    sort(events.begin(), events.end());
    int inside = 0;
    int best = 0;
    int best_time = 0;
    for (auto [time, change] : events) {
        inside += change;
        if (inside > best) {
            best = inside;
            best_time = time;
        }
    }
    cout << best << ' ' << best_time << '\n';
    return 0;
}
