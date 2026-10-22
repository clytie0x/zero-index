#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string code;
    cin >> code;
    int n = code.size();
    vector<int> ways(n + 1, 0);
    ways[0] = 1;
    for (int i = 1; i <= n; i++) {
        if (code[i - 1] != '0') {
            ways[i] = ways[i - 1];
        }
        if (i >= 2) {
            int two = (code[i - 2] - '0') * 10 + (code[i - 1] - '0');
            if (two >= 10 && two <= 26) {
                ways[i] = (ways[i] + ways[i - 2]) % MOD;
            }
        }
    }
    cout << ways[n] << '\n';
    return 0;
}
