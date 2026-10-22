#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    for (int j = 0; j < q; j++) {
        int n;
        cin >> n;
        vector<int> ways(n + 1, 0);
        ways[0] = 1;
        for (int i = 1; i <= n; i++) {
            long long total = 0;
            for (int jump = 1; jump <= 3 && jump <= i; jump++) {
                total += ways[i - jump];
            }
            ways[i] = total % MOD;
        }
        cout << ways[n] << '\n';
    }
    return 0;
}
