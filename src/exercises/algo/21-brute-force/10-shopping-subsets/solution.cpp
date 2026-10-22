#include <bits/stdc++.h>
using namespace std;

vector<long long> all_sums(const vector<long long>& items)
{
    int m = items.size();
    vector<long long> sums(1 << m);
    for (int mask = 0; mask < (1 << m); mask++) {
        long long total = 0;
        for (int i = 0; i < m; i++) {
            if ((mask >> i) & 1) {
                total += items[i];
            }
        }
        sums[mask] = total;
    }
    return sums;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long budget;
    cin >> n >> budget;
    vector<long long> first_half, second_half;
    for (int i = 0; i < n; i++) {
        long long price;
        cin >> price;
        if (i < n / 2) {
            first_half.push_back(price);
        } else {
            second_half.push_back(price);
        }
    }
    vector<long long> left = all_sums(first_half);
    vector<long long> right = all_sums(second_half);
    sort(right.begin(), right.end());
    long long ways = 0;
    for (long long x : left) {
        if (x <= budget) {
            ways += upper_bound(right.begin(), right.end(), budget - x) - right.begin();
        }
    }
    cout << ways << '\n';
    return 0;
}
