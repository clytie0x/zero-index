#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    vector<int> stones(q);
    int farthest = 0;
    for (int j = 0; j < q; j++) {
        cin >> stones[j];
        farthest = max(farthest, stones[j]);
    }
    vector<int> ways(farthest + 1, 0);
    ways[0] = 1;
    for (int i = 1; i <= farthest; i++) {
        long long total = 0;
        for (int jump = 1; jump <= 3 && jump <= i; jump++) {
            total += ways[i - jump];
        }
        ways[i] = total % MOD;
    }
    for (int j = 0; j < q; j++) {
        cout << ways[stones[j]] << '\n';
    }
    return 0;
}
