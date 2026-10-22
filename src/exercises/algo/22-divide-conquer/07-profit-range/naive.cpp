#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long low, high;
    cin >> n >> low >> high;
    vector<long long> prefix(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        long long profit;
        cin >> profit;
        prefix[i] = prefix[i - 1] + profit;
    }
    long long count = 0;
    for (int l = 1; l <= n; l++) {
        for (int r = l; r <= n; r++) {
            long long total = prefix[r] - prefix[l - 1];
            if (low <= total && total <= high) {
                count++;
            }
        }
    }
    cout << count << '\n';
    return 0;
}
