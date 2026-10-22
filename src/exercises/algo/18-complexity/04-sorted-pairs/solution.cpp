#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long k;
    cin >> n >> k;
    vector<long long> price(n);
    for (int i = 0; i < n; i++) {
        cin >> price[i];
    }
    int ways = 0;
    int i = 0, j = n - 1;
    while (i < j) {
        long long total = price[i] + price[j];
        if (total == k) {
            ways++;
            i++;
            j--;
        } else if (total < k) {
            i++;
        } else {
            j--;
        }
    }
    cout << ways << '\n';
    return 0;
}
