#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

long long count_ways(int left, int last)
{
    if (left == 0) {
        return 1;
    }
    long long total = 0;
    for (int jump = 1; jump <= 3 && jump <= left; jump++) {
        if (jump != last) {
            total += count_ways(left - jump, jump);
        }
    }
    return total % MOD;
}

int main()
{
    int n;
    cin >> n;
    cout << count_ways(n, 0) << '\n';
    return 0;
}
