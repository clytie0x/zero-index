#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

vector<int> sizes;

long long count_ways(int index, int left)
{
    if (index == (int)sizes.size()) {
        return left == 0 ? 1 : 0;
    }
    long long total = 0;
    for (int used = 0; used * sizes[index] <= left; used++) {
        total += count_ways(index + 1, left - used * sizes[index]);
    }
    return total % MOD;
}

int main()
{
    int n, target;
    cin >> n >> target;
    sizes = vector<int>(n);
    for (int i = 0; i < n; i++) {
        cin >> sizes[i];
    }
    cout << count_ways(0, target) << '\n';
    return 0;
}
