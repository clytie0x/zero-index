#include <bits/stdc++.h>
using namespace std;

vector<pair<long long, long long>> towers;

long long dist2(pair<long long, long long> p, pair<long long, long long> q)
{
    long long dx = p.first - q.first;
    long long dy = p.second - q.second;
    return dx * dx + dy * dy;
}

long long closest(int lo, int hi)
{
    long long best = LLONG_MAX;
    if (hi - lo <= 3) {
        for (int i = lo; i < hi; i++) {
            for (int j = i + 1; j < hi; j++) {
                best = min(best, dist2(towers[i], towers[j]));
            }
        }
        return best;
    }
    int mid = (lo + hi) / 2;
    long long mid_x = towers[mid].first;
    best = min(closest(lo, mid), closest(mid, hi));
    vector<pair<long long, long long>> strip;
    for (int i = lo; i < hi; i++) {
        long long dx = towers[i].first - mid_x;
        if (dx * dx < best) {
            strip.push_back(towers[i]);
        }
    }
    sort(strip.begin(), strip.end(), [](pair<long long, long long> p, pair<long long, long long> q) {
        return p.second < q.second;
    });
    for (int i = 0; i < (int)strip.size(); i++) {
        for (int j = i + 1; j < (int)strip.size(); j++) {
            long long dy = strip[j].second - strip[i].second;
            if (dy * dy >= best) {
                break;
            }
            best = min(best, dist2(strip[i], strip[j]));
        }
    }
    return best;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    towers.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> towers[i].first >> towers[i].second;
    }
    sort(towers.begin(), towers.end());
    cout << closest(0, n) << '\n';
    return 0;
}
