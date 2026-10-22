#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int rows, cols;
    cin >> rows >> cols;
    vector<long long> ways(cols, 0);
    ways[0] = 1;
    for (int r = 0; r < rows; r++) {
        string line;
        cin >> line;
        for (int c = 0; c < cols; c++) {
            if (line[c] == '#') {
                ways[c] = 0;
            } else if (c > 0) {
                ways[c] = (ways[c] + ways[c - 1]) % MOD;
            }
        }
    }
    cout << ways[cols - 1] << '\n';
    return 0;
}
