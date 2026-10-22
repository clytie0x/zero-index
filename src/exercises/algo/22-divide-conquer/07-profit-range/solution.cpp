#include <bits/stdc++.h>
using namespace std;

long long low, high;

long long count_ranges(vector<long long> &prefix, vector<long long> &temp, int lo, int hi)
{
    if (hi - lo <= 1) {
        return 0;
    }
    int mid = (lo + hi) / 2;
    long long count = count_ranges(prefix, temp, lo, mid) + count_ranges(prefix, temp, mid, hi);
    int from = lo, to = lo;
    for (int j = mid; j < hi; j++) {
        while (from < mid && prefix[from] < prefix[j] - high) {
            from++;
        }
        while (to < mid && prefix[to] <= prefix[j] - low) {
            to++;
        }
        count += to - from;
    }
    int i = lo, j = mid, k = lo;
    while (i < mid && j < hi) {
        if (prefix[i] <= prefix[j]) {
            temp[k] = prefix[i];
            i++;
        } else {
            temp[k] = prefix[j];
            j++;
        }
        k++;
    }
    while (i < mid) {
        temp[k] = prefix[i];
        i++;
        k++;
    }
    while (j < hi) {
        temp[k] = prefix[j];
        j++;
        k++;
    }
    for (int t = lo; t < hi; t++) {
        prefix[t] = temp[t];
    }
    return count;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n >> low >> high;
    vector<long long> prefix(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        long long profit;
        cin >> profit;
        prefix[i] = prefix[i - 1] + profit;
    }
    vector<long long> temp(n + 1);
    cout << count_ranges(prefix, temp, 0, n + 1) << '\n';
    return 0;
}
