#include <bits/stdc++.h>
using namespace std;

bool enough(const vector<long long> &minutes, long long time, long long trays)
{
    long long baked = 0;
    for (int i = 0; i < (int)minutes.size(); i++) {
        baked += time / minutes[i];
        if (baked >= trays) {
            return true;
        }
    }
    return false;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long trays;
    cin >> n >> trays;
    vector<long long> minutes(n);
    long long fastest = LLONG_MAX;
    for (int i = 0; i < n; i++) {
        cin >> minutes[i];
        fastest = min(fastest, minutes[i]);
    }
    long long lo = 1, hi = fastest * trays;
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        if (enough(minutes, mid, trays)) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    cout << lo << '\n';
    return 0;
}
