#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long n;
    cin >> n;
    long long count = 0;
    long long low = 1;
    for (int bits = 1; low <= n; bits++) {
        long long high = min(2 * low - 1, n);
        count += bits * (high - low + 1);
        low *= 2;
    }
    cout << count << '\n';
    return 0;
}
