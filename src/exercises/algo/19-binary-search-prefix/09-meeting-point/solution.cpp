#include <bits/stdc++.h>
using namespace std;

bool can_meet(const vector<int> &place, const vector<int> &speed, double time)
{
    double left = -1e30, right = 1e30;
    for (int i = 0; i < (int)place.size(); i++) {
        left = max(left, place[i] - speed[i] * time);
        right = min(right, place[i] + speed[i] * time);
    }
    return left <= right;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> place(n), speed(n);
    for (int i = 0; i < n; i++) {
        cin >> place[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> speed[i];
    }
    double lo = 0, hi = 1e9;
    for (int step = 0; step < 100; step++) {
        double mid = (lo + hi) / 2;
        if (can_meet(place, speed, mid)) {
            hi = mid;
        } else {
            lo = mid;
        }
    }
    cout << fixed << setprecision(4) << hi << '\n';
    return 0;
}
