#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long k;
    cin >> n >> k;
    vector<long long> change(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> change[i];
    }
    long long count = 0;
    for (int l = 1; l <= n; l++) {
        long long total = 0;
        for (int r = l; r <= n; r++) {
            total += change[r];
            if (total == k) {
                count++;
            }
        }
    }
    cout << count << '\n';
    return 0;
}
