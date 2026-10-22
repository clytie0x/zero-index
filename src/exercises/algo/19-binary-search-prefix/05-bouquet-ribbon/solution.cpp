#include <bits/stdc++.h>
using namespace std;

long long pieces(const vector<int> &lengths, int cut)
{
    long long total = 0;
    for (int i = 0; i < (int)lengths.size(); i++) {
        total += lengths[i] / cut;
    }
    return total;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long k;
    cin >> n >> k;
    vector<int> lengths(n);
    int lo = 0, hi = 0;
    for (int i = 0; i < n; i++) {
        cin >> lengths[i];
        hi = max(hi, lengths[i]);
    }
    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2;
        if (pieces(lengths, mid) >= k) {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    cout << lo << '\n';
    return 0;
}
