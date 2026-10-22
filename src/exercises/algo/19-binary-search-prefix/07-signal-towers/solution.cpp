#include <bits/stdc++.h>
using namespace std;

bool can_place(const vector<int> &spots, int towers, int gap)
{
    int placed = 1;
    int last = spots[0];
    for (int i = 1; i < (int)spots.size(); i++) {
        if (spots[i] - last >= gap) {
            placed++;
            last = spots[i];
            if (placed >= towers) {
                return true;
            }
        }
    }
    return placed >= towers;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, towers;
    cin >> n >> towers;
    vector<int> spots(n);
    for (int i = 0; i < n; i++) {
        cin >> spots[i];
    }
    sort(spots.begin(), spots.end());
    int lo = 0, hi = spots[n - 1] - spots[0];
    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2;
        if (can_place(spots, towers, mid)) {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    cout << lo << '\n';
    return 0;
}
