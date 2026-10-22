#include <bits/stdc++.h>
using namespace std;

int n, q;
vector<long long> need;
vector<int> from_tree, to_tree, water;

bool enough_after(int rounds)
{
    vector<long long> diff(n + 2, 0);
    for (int j = 0; j < rounds; j++) {
        diff[from_tree[j]] += water[j];
        diff[to_tree[j] + 1] -= water[j];
    }
    long long current = 0;
    for (int tree = 1; tree <= n; tree++) {
        current += diff[tree];
        if (current < need[tree]) {
            return false;
        }
    }
    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n >> q;
    need.assign(n + 1, 0);
    for (int tree = 1; tree <= n; tree++) {
        cin >> need[tree];
    }
    from_tree.resize(q);
    to_tree.resize(q);
    water.resize(q);
    for (int j = 0; j < q; j++) {
        cin >> from_tree[j] >> to_tree[j] >> water[j];
    }
    if (!enough_after(q)) {
        cout << -1 << '\n';
        return 0;
    }
    int lo = 0, hi = q;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (enough_after(mid)) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    cout << lo << '\n';
    return 0;
}
