#include <bits/stdc++.h>
using namespace std;

int n, k;
long long target;
vector<long long> weight;
vector<bool> used;

bool fill_bag(int bags_done, int start, long long load)
{
    if (bags_done == k - 1) {
        return true;
    }
    if (load == target) {
        return fill_bag(bags_done + 1, 0, 0);
    }
    long long last_failed = -1;
    for (int i = start; i < n; i++) {
        if (used[i] || weight[i] == last_failed || load + weight[i] > target) {
            continue;
        }
        used[i] = true;
        if (fill_bag(bags_done, i + 1, load + weight[i])) {
            return true;
        }
        used[i] = false;
        last_failed = weight[i];
        if (load == 0) {
            break;
        }
    }
    return false;
}

int main()
{
    cin >> n >> k;
    weight.resize(n);
    long long total = 0;
    for (int i = 0; i < n; i++) {
        cin >> weight[i];
        total += weight[i];
    }
    sort(weight.rbegin(), weight.rend());
    used.assign(n, false);
    target = total / k;
    bool ok = total % k == 0 && weight[0] <= target && fill_bag(0, 0, 0);
    cout << (ok ? "YES" : "NO") << '\n';
    return 0;
}
