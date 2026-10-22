#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

long long count_ways(int stone)
{
    if (stone == 0) {
        return 1;
    }
    long long total = 0;
    for (int jump = 1; jump <= 3 && jump <= stone; jump++) {
        total += count_ways(stone - jump);
    }
    return total % MOD;
}

int main()
{
    int n;
    cin >> n;
    cout << count_ways(n) << '\n';
    return 0;
}
