#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, target;
    cin >> n >> target;
    vector<int> sizes(n);
    for (int i = 0; i < n; i++) {
        cin >> sizes[i];
    }
    vector<int> ways(target + 1, 0);
    ways[0] = 1;
    for (int s : sizes) {
        for (int x = s; x <= target; x++) {
            ways[x] = (ways[x] + ways[x - s]) % MOD;
        }
    }
    cout << ways[target] << '\n';
    return 0;
}
